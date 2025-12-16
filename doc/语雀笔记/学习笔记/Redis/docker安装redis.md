# docker安装redis

## 1.拉取镜像

`docker pull redis:4.0.6`

## 2.本机编写redis配置文件

下载[redis配置文件](https://raw.githubusercontent.com/antirez/redis/4.0.6/redis.conf)，注意和redis版本对应，修改一下内容

```plain
bind 127.0.0.1 #注释掉这部分，这是限制redis只能本地访问

protected-mode no #默认yes，开启保护模式，限制为本地访问

daemonize no#默认no，改为yes意为以守护进程方式启动，可后台运行，除非kill进程，改为yes会使配置文件方式启动redis失败

databases 16 #数据库个数（可选），我修改了这个只是查看是否生效。。

dir  ./ #输入本地redis数据库存放文件夹（可选）

appendonly yes #redis持久化（可选）
```

注意需要将`daemonize no`这个配置注释掉，因为这会和redis的-d（后台启动） 参数冲突，导致直接失败

## 3.启动redis

```plain
docker run -d -p 6379:6379 -v /data/docker_redis/redis.conf:/etc/redis/redis.conf -v /data/docker_redis/data:/data --name redis 1e70071f4af4 redis-server /etc/redis/redis.conf
```

可能会启动失败，`docker ps -a`查看启动失败的redis容器id

`docker logs 容器id`查看启动日志

可能会遇到`**启动redis chown: cannot read directory '.': Permission denied**`这样的错误

```plain
容器中没有执行权限 //挂载外部数据卷时,无法启动容器, 报 chown: cannot read directory '/var/lib/mysql/': Permission denied 由$ docker logs [name] 查看得知 该原因为centOs7默认开启selinux安全模块,需要临时关闭该安全模块,或者添加目录到白名单 临时关闭selinux：su -c "setenforce 0" 重新开启selinux：su -c "setenforce 1" 添加selinux规则，将要挂载的目录添加到白名单： 示例：chcon -Rt svirt_sandbox_file_t   /data/mysql/db/
```

**解决方式：** 临时关闭selinux：`su -c "setenforce 0" `
