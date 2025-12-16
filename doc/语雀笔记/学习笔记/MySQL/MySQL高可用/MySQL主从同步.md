# MySQL主从同步

## 1. 准备

开放主数据库和从数据库的远程连接权限。

```sql
grant all privileges on *.* to 'root' @'%' identified by 'root';
```

## 2. 修改主从数据库配置文件

**Windows下MySQL配置文件的位置可以查看系统服务下的MySQL服务的启动参数，一般修改完之后建议复制一份到C:\Windows\下。**

**Linux下MySQL配置文件一般在/etc/my.cnf**

### 1.修改主数据库配置文件

**添加以下配置，如果本来就存在看情况修改**

```plain
# Binary Logging.
# log-bin 记录 主数据库的所有操作，方便从数据库同步
log-bin="C:/ProgramData/MySQL/MySQL Server 5.7/mysql-bin"

# Error Logging.
log-error="C:/ProgramData/MySQL/MySQL Server 5.7/mysql-error"

# Server Id. 主从数据库不能相同
server-id=1

# 指定需要同步哪些数据库（默认全部数据库）
# binlog-do-bo=mydb01

# 指定需要 不同步哪些数据库（排除）
binlog-ignore-db=mysql
```

### 2.修改从数据库配置文件

**添加以下配置，如果存在看情况修改，一定注意配置的server-id不能喝主数据库相同**

```plain
# 从数据库配置
server-id=2
log-bin=mysql-bin
# 表示只同步以下数据库
replicate-do-db=mydb01
replicate-do-db=mydb02
```

## 3. 重启主从数据库

注意：从本次重启开始，主数据库的所有操作都会被记录到log-bin的配置中，从数据库会同步执行。

## 4. 设置主从关系

主数据库下执行`show master status;`

```plain
mysql> show master status;
+------------------+----------+--------------+------------------+-------------------+
| File             | Position | Binlog_Do_DB | Binlog_Ignore_DB | Executed_Gtid_Set |
+------------------+----------+--------------+------------------+-------------------+
| mysql-bin.000004 |      154 |              | mysql            |                   |
+------------------+----------+--------------+------------------+-------------------+
```

从数据库下执行，其中master_log_file来自主数据库的File，master_log_pos来自主数据库的Position

```sql
change master to
master_host='192.168.2.130',
master_user='root',
master_password='root',
master_port=3306,
master_log_file='mysql-bin.000004',
master_log_pos=154;
```

然后在从数据库下执行start slave --> 查看从数据库状态：show slave status \G

```plain
mysql> show slave status \G
*************************** 1. row ***************************
               Slave_IO_State: Waiting for master to send event
                  Master_Host: 192.168.2.130
                  Master_User: root
                  Master_Port: 3306
                Connect_Retry: 60
              Master_Log_File: mysql-bin.000004
          Read_Master_Log_Pos: 154
               Relay_Log_File: bigdata01-relay-bin.000002
                Relay_Log_Pos: 320
        Relay_Master_Log_File: mysql-bin.000004
             Slave_IO_Running: Yes
            Slave_SQL_Running: Yes
              Replicate_Do_DB: mydb01,mydb02
          Replicate_Ignore_DB: 
           Replicate_Do_Table: 
       Replicate_Ignore_Table: 
      Replicate_Wild_Do_Table: 
  Replicate_Wild_Ignore_Table: 
                   Last_Errno: 0
                   Last_Error: 
                 Skip_Counter: 0
          Exec_Master_Log_Pos: 154
              Relay_Log_Space: 531
              Until_Condition: None
               Until_Log_File: 
                Until_Log_Pos: 0
           Master_SSL_Allowed: No
           Master_SSL_CA_File: 
           Master_SSL_CA_Path: 
              Master_SSL_Cert: 
            Master_SSL_Cipher: 
               Master_SSL_Key: 
        Seconds_Behind_Master: 0
Master_SSL_Verify_Server_Cert: No
                Last_IO_Errno: 0
                Last_IO_Error: 
               Last_SQL_Errno: 0
               Last_SQL_Error: 
  Replicate_Ignore_Server_Ids: 
             Master_Server_Id: 1
                  Master_UUID: 47fa5645-fb89-11e9-a89d-e454e8b6c044
             Master_Info_File: /var/lib/mysql/master.info
                    SQL_Delay: 0
          SQL_Remaining_Delay: NULL
      Slave_SQL_Running_State: Slave has read all relay log; waiting for more updates
           Master_Retry_Count: 86400
                  Master_Bind: 
      Last_IO_Error_Timestamp: 
     Last_SQL_Error_Timestamp: 
               Master_SSL_Crl: 
           Master_SSL_Crlpath: 
           Retrieved_Gtid_Set: 
            Executed_Gtid_Set: 
                Auto_Position: 0
         Replicate_Rewrite_DB: 
                 Channel_Name: 
           Master_TLS_Version: 
```

Slave_IO_Running和Slave_SQL_Running都为Yes表示一切正常，否则查看下方的Last_IO_Error和Last_SQL_Error日志信息。

## 5. 注意

主从数据库的字符设置应当相同，否则在同步数据表时会因为字符集不同而造成同步失败、中断。

**Window下设置字符集，分别在以下三个节点下设置字符集**

```plain
[client]
default-character-set=utf8

[mysql]
default-character-set=utf8

[mysqld]
character_set_server=utf8
```

**Linux下设置字符集，只需要在mysqld下设置即可**

```plain
[mysqld]
character_set_server=utf8
```
