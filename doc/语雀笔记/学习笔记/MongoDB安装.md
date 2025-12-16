# MongoDB安装

## 1.创建.repo文件，生成mongodb的源

```shell
vim /etc/yum.repos.d/mongodb-org-4.0.repo
# 添加以下内容
[mongodb-org-4.0]
name=MongoDB Repository
baseurl=https://repo.mongodb.org/yum/redhat/#releasever/mongodb-org/4.0/x86_64/
gpgcheck=1
enabled=1
gpgkey=https://www.mongodb.org/static/pgp/server-4.0.asc
```

## 2.通过yum安装

`yum install -y mongodb-org`

## 3.启动MongoDB并连接

启动：`systemctl start mongod`

连接：`mongo`

## 4.MongoDB相关操作

```plain
use person  # 使用person数据库，如果不存在则创建
db.person.insert({id: "1", name: "zhangsan", age: NumberInt(25)}) 
# db 相当于当前数据库 person，person相当于表person，这句话的含义相当于给数据库person中的person表
# 添加一条记录
# 其他操作
db.person.insert({id: "1", name: "zhangsan", age: NumberInt(25)})
db.person.insert({id: "2", name: "张三", age: NumberInt(24)})
db.person.insert({id: "3", name: "李四", age: NumberInt(28)})
db.person.insert({id: "4", name: "fdsf", age: NumberInt(434)})
db.person.findOne({id: "1"})
db.person.update({id: "2"}, {$set: {name: "王五"}})
db.person.remove(条件)
db.person.remove({id: "4"})
db.person.find({name: /^z/}) # 查询name以z开头的数据
查询条件
>: $gt
>=: $gte
<: $lt
<=: $lte
!=: $ne

db.person.find({age: {$lte: 25}})
db.person.find({age: {$in: [24, 28]}})
```

## 5.Java操作MongoDB

1. 引入依赖

```xml
<dependency>
  <groupId>org.mongodb</groupId>
  <artifactId>mongo-java-driver</artifactId>
  <version>3.4.2</version>
</dependency>
```

2. 创建客户端并使用

```java
// 创建客户端
MongoClient mongoClient = new MongoClient("192.168.2.128", 27017);
// 获取数据库
MongoDatabase database = mongoClient.getDatabase("crawler");
// 获取集合（表）
MongoCollection<org.bson.Document> course = database.getCollection("course");
// 向表中插入一条记录
course.insertOne(document);
document可以通过org.bson.Document.parse(jsonStr)来创建
```
