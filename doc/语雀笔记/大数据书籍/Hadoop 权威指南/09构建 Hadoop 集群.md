# 09构建 Hadoop 集群

# 1.Hadoop集群配置

- 在`etc/hadoop`​目录下，存在很多的配置文件和bash脚本
- 其中 map-env.sh 和 yarn-env.sh 可以覆盖 hadoop-env.sh 中对 MR 或 yarn 的配置
- 具体的 xml 配置，可以查看官网的 configuration 主题

Hadoop 的安装步骤：

1. 安装 Java
2. 创建 Unix 用户
3. 安装 Hadoop
4. SSH 配置（配置集群免密登录）
5. 配置 Hadoop
6. 格式化 HDFS 文件系统
7. 启动和停止守护进程
8. 创建用户

# 2.Hadoop 配置

## 2.1配置管理

Hadoop 并没有将所有的配置信息放在一个独立的全局位置中，相反每个 Hadoop 节点都有各自保存一系列配置文件，并由管理员完成这一系列文件的同步工作。

Hadoop 也支持将所有 master 和 slave 机器采用同一配置。这个做法最大的优势在于简单，不仅体现在理论上（仅需处理一套配置文件），也体现在可操作性上（使用 Hadoop 脚本就能进行管理）。

## 2.2环境配置

1. Java 配置：需要配置 JAVA_HOME 环境变量
2. 内存堆大小：默认情况下 Hadoop 为各个守护进程分配 1G 内存。该内存值由 hadoop-env.sh 文件的 HADOOP_HEAPSIZE 参数控制
3. 系统日志文件：默认情况下 Hadoop 生成的系统日志文件放在 $HADOOP_HOME/logs  目录之下，也可以通过 hadoop-env.sh 的 HADOOP_LOG_DIR 参数配置
4. SSH 设置

## 2.3Hadoop守护进程的关键属性

1. HDFS：运行 HDFS 需要将一台机器指定为 namenode。
2. YARN：运行 YARN 需要将一台机器指定为资源管理器。
3. YARN 和 MapReduce 的内存配置
4. YARN 和 MapReduce 中的 CPU 配置

## 2.4Hadoop守护进程的地址和端口

- RPC端口，用于守护进程间相互通信
- HTTP端口，用于提供守护进程与用户交互的web页面
- 端口号，一方面决定了守护进程绑定的网络接口；另一方面决定了用户或其他守护进程与之交互的网络接口。

# 3.安全性

从安全角度分析，Hadoop 缺乏一个安全的认证机制，以确保正在操作集群的用户恰是所声称的安全组用户。Hadoop 的文件许可模块只提供一种简单的认证机制来决定各个用户对也定文件的访问权限。

- 为了避免Hadoop文件系统的数据，被伪装的恶意用户删除，需要进行安全认证
- 雅虎工程师，基于kerberos（一种成熟的开源网络认证协议）实现了基于kerberos的安全认证
- kerberos认证只负责鉴定登陆账号是否为声称的用户，而用户的访问权限则是由Hadoop自己负责管理
