# Redis实现分布式锁

# 1.使用场景

对于一台机器面对并发请求我们的处理方式通常是加锁，但是加锁后会导致机器性能下降，此时的做法是扩展多台机器，但是JDK提供的锁只适用于同一个JVM，两台不同的机器对应不同的JVM，此时的锁就不会生效了；所以只要保证多台机器加的“锁”是同一把锁即可解决该问题。

分布式锁的思路是：**在整个系统提供一个全局、唯一的获取锁的“东西”，然后每个系统在需要加锁时，都去问这个“东西”拿到一把锁，这样不同的系统拿到的就可以认为是同一把锁。**

# 2.高效的分布式锁

在设计分布式锁的时候，应该考虑分布式锁至少要满足的一些条件，同时考虑如何高效的设计分布式锁，以下几点是必须要考虑的：

 **(1)**   **互斥**

在分布式高并发的条件下，最需要保证在同一时刻只能有一个线程获得锁，这是最基本的一点。

 **(2)**   **防止死锁**

在分布式高并发的条件下，比如有个线程获得锁的同时，还没有来得及去释放锁，就因为系统故障或者其它原因使它无法执行释放锁的命令,导致其它线程都无法获得锁，造成**死锁**。所以分布式非常有必要设置锁的有效时间，确保系统出现故障后，在一定时间内能够主动去释放锁，避免造成死锁的情况。

 **(3)**   **性能**

对于访问量大的共享资源，需要考虑减少锁等待的时间，避免导致大量线程阻塞。

所以在锁的设计时，需要考虑两点。

1、 锁的颗粒度要尽量小。比如你要通过锁来减库存，那这个锁的名称你可以设置成是商品的ID,而不是任取名称。这样这个锁只对当前商品有效,锁的颗粒度小。

2、 锁的范围尽量要小。比如只要锁2行代码就可以解决问题的，那就不要去锁10行代码了。

 **(4)**   **重入**

我们知道ReentrantLock是可重入锁，那它的特点就是：同一个线程可以重复拿到同一个资源的锁。重入锁非常有利于资源的高效利用。关于这点之后会做演示。

# 3.基于redis的分布式锁

 **（1）加锁**

`**SET lock_key random_value NX PX 10000**`

lock_key：锁的名称

random_value：每台机器独有的标识码

NX：当lock_key不存在时才能设置成功

PX：后面接过期时间

 **（2）解锁**

`**del lock_key**`

删除lock_key即可，但是删除前需要判断lock_key对应的value是否为本台机器的标识码，即不能删除其他人设置的锁

# 4.Java代码实现

```java
/**
 * @Author WJH
 * @Description
 * @date 2020/10/19 16:46
 * @Email ibytecode2020@gmail.com
 */
@RestController
@RequestMapping
public class IndexController {
    private static final String KEY = "stock";
    private static final String LOCK = "lock";
    private static final Integer TIMEOUT = 10;
    @Autowired
    StringRedisTemplate stringRedisTemplate;
    @GetMapping("/deduct_stock")
    public String deductStock() throws Exception {

        // 给自己的锁添加唯一标识
        String clientId = UUID.randomUUID().toString();
        try {
            // 尝试加锁
            Boolean isGetLock = stringRedisTemplate.opsForValue().setIfAbsent(LOCK, clientId, TIMEOUT, TimeUnit.SECONDS);
            // 加锁失败的逻辑
            if (!isGetLock) {
                return "is lock";
            }
            /*
            * 加锁成功后为了防止业务处理时间大于锁生效时间一般可以在此处添加一个子线程作为定时任务每隔 1/3 TIMEOUT
            * 查看锁是否还存在 （表示业务没有走完，没有手动释放锁），若存在则将锁的过期时间重置为TIMEOUT
            * stringRedisTemplate.expire(LOCK, TIMEOUT, TimeUnit.SECONDS);
             * */
            int stock = Integer.parseInt(Objects.requireNonNull(stringRedisTemplate.opsForValue().get(KEY)));

            if (stock > 0) {
                int realStock = stock - 1;
                stringRedisTemplate.opsForValue().set(KEY, String.valueOf(realStock));
                System.out.println("扣减成功，剩余商品：" + realStock);
            } else {
                System.out.println("库存不足。");
            }
        } finally {
            /*
            * 是自己的锁 则释放
            * 这里释放锁是非原子性的
            * */
            if (clientId.equals(stringRedisTemplate.opsForValue().get(LOCK))) {
                stringRedisTemplate.delete(LOCK);
            }
        }
        return "end";
    }
}
```

# 5.Redisson使用

 **（1）依赖**

```xml
<dependency>
  <groupId>org.redisson</groupId>
  <artifactId>redisson</artifactId>
  <version>3.11.4</version>
</dependency>
```

 **（2）配置类**

```java
@Configuration
public class RedissonConfig {

    @Value("${spring.redis.host}")
    private String redisHost;
    @Value("${spring.redis.port}")
    private String redisPort;
    private final String redisAddress = redisHost + ":" + redisPort;

    @Bean
    public RedissonClient redissonClient() {
        Config config = new Config();
        config.setCodec(new org.redisson.client.codec.StringCodec())
                .useSingleServer()
                .setAddress("redis://192.168.2.128:6379");
        return Redisson.create(config);
    }

}
```

 **（3）简单使用**

```java
@SpringBootTest
class DistributedLockApplicationTests {
	@Autowired
	RedissonClient redissonClient;
	@Test
	void contextLoads() {
		RKeys keys = redissonClient.getKeys();
		Iterable<String> keysByPattern = keys.getKeysByPattern("*");
		keysByPattern.forEach(System.out::println);
	}
	@Test
	void contextLoads1() {
		RBucket<Object> k1 = redissonClient.getBucket("k1");
		System.out.println(k1.get());
		k1.set("kk1");
		System.out.println(k1.get());
	}
	@Test
	void contextLoads2() {
		RList<String> list = redissonClient.getList("list");
//		list.add("hello");
//		list.add("world");
//		list.add("java");
//		list.add("redis");
//		list.remove(-1);
		list.forEach(System.out::println);
	}
}
```

 **（4）分布式锁**

```java
/**
 * @Author WJH
 * @Description
 * @date 2020/10/19 16:46
 * @Email ibytecode2020@gmail.com
 */
@RestController
@RequestMapping
public class IndexController {
    private static final String KEY = "stock";
    private static final String LOCK = "lock";
    private static final Integer TIMEOUT = 10;
    @Autowired
    StringRedisTemplate stringRedisTemplate;
    @Autowired
    RedissonClient redissonClient;
    @GetMapping("/deduct_stock")
    public String deductStock() throws Exception {
        // 获取锁
        RLock lock = redissonClient.getLock(LOCK);
        try {
            // 加锁
            lock.lock(TIMEOUT, TimeUnit.SECONDS);
            // 业务
            int stock = Integer.parseInt(Objects.requireNonNull(stringRedisTemplate.opsForValue().get(KEY)));
            if (stock > 0) {
                int realStock = stock - 1;
                stringRedisTemplate.opsForValue().set(KEY, String.valueOf(realStock));
                System.out.println("扣减成功，剩余商品：" + realStock);
            } else {
                System.out.println("库存不足。");
            }
        } finally {
            // 释放锁
            lock.unlock();
        }
        return "end";
    }
}
```

 **（5）说明**

在使用Redisson做分布式锁时，不需要手动添加子线程来维持当前客户端的锁，它会自带一个WatchDog来维持锁
