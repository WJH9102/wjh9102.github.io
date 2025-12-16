# Java 基础

## 1.BigDecimal 的比较

对于 BigDecimal 的比较，《阿里巴巴开发手册》建议的是使用`compareTo()`方法进行比较，而不是使用`equals()`方法。这是因为`equals()`除了比较值之外，还会比较标度。

BigDecimal 共有 4 类构造方法：

- ​`BigDecimal(int)`​
- ​`BigDecimal(double)`​
- ​`BigDecimal(long)`​
- ​`BigDecimal(String)`​

```java
public static void main(String[] args) {
    BigDecimal b1 = new BigDecimal(1);
    BigDecimal b2 = new BigDecimal(1.0);
    BigDecimal b3 = new BigDecimal("1.0");
    BigDecimal b4 = new BigDecimal(0.1);
    System.out.println(b1.scale()); // 0
    System.out.println(b2.scale()); // 0
    System.out.println(b3.scale()); // 1
    System.out.println(b4.scale()); // 55
}
```

因为 double 类型的 0.1 实际上是一个近似值：0.1000000000000000055511151231257827021181583404541015625

equals 方法的源码如下：

```java
public boolean equals(Object x) {
    if (!(x instanceof BigDecimal))
        return false;
    BigDecimal xDec = (BigDecimal) x;
    if (x == this)
        return true;
	// 比较标度
    if (scale != xDec.scale)
        return false;
    long s = this.intCompact;
    long xs = xDec.intCompact;
    if (s != INFLATED) {
        if (xs == INFLATED)
            xs = compactValFor(xDec.intVal);
        return xs == s;
    } else if (xs != INFLATED)
        return xs == compactValFor(this.intVal);

    return this.inflated().equals(xDec.inflated());
}
```

compareTo 的源码如下：

```java
public int compareTo(BigDecimal val) {
    // Quick path for equal scale and non-inflated case.
    if (scale == val.scale) {
        long xs = intCompact;
        long ys = val.intCompact;
        if (xs != INFLATED && ys != INFLATED)
            return xs != ys ? ((xs > ys) ? 1 : -1) : 0;
    }
    int xsign = this.signum();
    int ysign = val.signum();
    if (xsign != ysign)
        return (xsign > ysign) ? 1 : -1;
    if (xsign == 0)
        return 0;
    int cmp = compareMagnitude(val);
    return (xsign > 0) ? cmp : -cmp;
}
```

## 2.String 相关

### 2.1 避免在循环中使用“+”拼接字符串

```java
String wechat = "Hollis";
String introduce = "Chuang";
String hollis = wechat + "," + introduce;
```

将以上内容反编译后得到：

```java
String wechat = "Hollis";
String introduce = "Chuang";
String hollis = (new StringBuilder()).append(wechat).append(",").append(introduce).toString();
```

由此可以知道每次拼接字符串的时候都会创建一个新的 StringBuilder 对象。

### 2.2 intern 作用

intern 的作用是将编译期间无法确定的字符串存放的字符串常量池中。当一个字符串实例调用 intern 方法时，会首先在常量池中寻找是否存在与它相同的 Unicode 字符串常量，如果存在则直接返回其引用，否则在字符串常量池中新增一个与之相同的 Unicode 字符串，并返回其引用。

### 2.3 intern 的正确用法

```java
String str = new String("hello").intern();
```

编译期的**字面量**和**符号引用**是常量池的重要来源。由此可见，上面的 intern 方法似乎是多此一举的。但是对于下面的例子：

```java
String s1 = "Hollis";
String s2 = "Chuang";
String s3 = s1 + s2;
String s4 = "Hollis" + "Chuang";
```

反编译后：

```java
String s1 = "Hollis";
String s2 = "Chuang";
String s3 = (new StringBuilder()).append(s1).append(s2).toString();
String s4 = "HollisChuang";
```

可以看到 s3 和 s4 是完全不用的两种处理方案，这是因为在编译期间，s1 和 s2 是无法确定的字面量，所以无法使用常量池中的数据，因此会被编译成 StringBuilder 的形式。

有了这个特性，我们可以使用 intern 将在编译期无法确定的字符串加入到常量池中，避免字符串对象的重复创建：

```java
static final int MAX = 1000 * 10000;
static final String[] arr = new String[MAX];

public static void main(String[] args) throws Exception {
    Integer[] DB_DATA = new Integer[10];
    Random random = new Random(10 * 10000);
    for (int i = 0; i < DB_DATA.length; i++) {
        DB_DATA[i] = random.nextInt();
    }
    long t = System.currentTimeMillis();
    for (int i = 0; i < MAX; i++) {
         arr[i] = new String(String.valueOf(DB_DATA[i % DB_DATA.length])).intern();
    }

    System.out.println((System.currentTimeMillis() - t) + "ms");
    System.gc();
}
```

### 2.4 String a = "ab" 和 String b = "a" + "b" 相等吗

```java
public static void main(String[] args) {
    String a = "ab";
    String b = "a" + "b";
    System.out.println(a == b); // true
}
```

### 2.5 字符串进入字符串常量池的时机

除了在编译期的字面量会进入字符串常量池外，使用 intern() 方法也会将字符串添加到常量池中，并返回其引用：

```java
public class Test03 {
    public static void main(String[] args) {
        String s1 = new String("a") + new String("a"); // 1
        s1.intern(); // 2
        String s2 = "aa"; // 3
        System.out.println(s1 == s2); // 4
    }
}
```

上述代码在编译完成后，字符串常量池中会有“a”和“aa”两个字符串，“a”在第 1 行就会进入，“aa”在第 3 行才会进入常量池。但是在第 2 行，s1 执行 intern 方法，常量池中没有字符串“aa”，所以会把字符串“aa”添加到常量池中，并将其引用指向 s1。在第 3 行，给 s2 赋值的时候，常量池中已经有“aa”了，所以直接返回其引用，指向 s1。所以第 4 行打印 true。

接着看第二段代码：

```java
public class Test03 {
    public static void main(String[] args) {
        String s2 = "aa";
        String s1 = new String("a") + new String("a");
        s1.intern();
        System.out.println(s1 == s2); // 4
    }
}
```

经过上述分析，由于先定义了 s2 ，所以在 s1 执行 intern 方法时，并不会将“aa”添加到常量池中，也不会将 s1 的引用指向“aa”，所以第 4 行打印 false。

### 2.6 String 是如何保证其不可变性的

1. String 类由 final 修饰，导致其不可被集成
2. String 类内部没有提供用于修改字符串的公共方法，对于追加、删除和修改字符的方法都是通过返回一个新的 String 来实现的
3. 字符串内容 char[] 也由 final 修饰，导致其一旦被初始化就不能指向其他数组
