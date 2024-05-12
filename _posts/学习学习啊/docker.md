# Centos7安装docker

1.  为了防止安装失败先执行`yum install epel-release`
2.  执行`yum install docker`
3.  更改docker镜像`vim /etc/docker/daemon.json`，输入以下内容

~~~json
{
    "registry-mirrors": ["https://uyah70su.mirror.aliyuncs.com"]
}
~~~

4.  启动docker

~~~shell
systemctl enable docker
systemctl start docker
systemctl daemon-reload
systemctl restart docker
~~~

4.  测试拉取mysql5.7`docker pull mysql:5.7`
5.  启动docker镜像中的mysql`docker run -d -p 53306:3306 -e MYSQL_ROOT_PASSWORD=root--name docker_mysql mysql:5.7`
    -   启动失败执行`yum update`
6.  查看启动镜像`docker ps`
7.  开放53306端口`firewall-cmd --zone=public --add-port=53306/tcp --permanent `
8.  重启防火墙`firewall-cmd --reload`
9.  使用本地客户端连接测试

![img](http://tc.junhaox.cn/img/20200519143625.png)

```

List<xt_gate_queue> xt_gate_queues
page.getRecords
List<gw_mttask_202005> gw_mttask_202005s
for xt_gate_queues
map:{
"8888,21","电信测试"
}

for gw_mttask_202005s
{
map.get("8888,21")
}
gatename
page.setRecords
```





