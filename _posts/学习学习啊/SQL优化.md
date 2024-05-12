---
typora-copy-images-to: ..\upload
---

# MySQL SQL优化

## 1.创建百万条数据

1.  创建内存表

~~~mysql
CREATE TABLE `vote_record_memory` (
    `id` INT (11) NOT NULL AUTO_INCREMENT,
    `user_id` VARCHAR (20) NOT NULL,
    `vote_id` INT (11) NOT NULL,
    `group_id` INT (11) NOT NULL,
    `create_time` datetime NOT NULL,
    PRIMARY KEY (`id`),
    KEY `index_id` (`user_id`) USING HASH
) ENGINE = MEMORY AUTO_INCREMENT = 1 DEFAULT CHARSET = utf8
~~~

2.  创建普通表

~~~mysql
CREATE TABLE `vote_record` (
    `id` INT (11) NOT NULL AUTO_INCREMENT,
    `user_id` VARCHAR (20) NOT NULL,
    `vote_id` INT (11) NOT NULL,
    `group_id` INT (11) NOT NULL,
    `create_time` datetime NOT NULL,
    PRIMARY KEY (`id`),
    KEY `index_user_id` (`user_id`) USING HASH
) ENGINE = INNODB AUTO_INCREMENT = 1 DEFAULT CHARSET = utf8
~~~

3.  创建存储过程及函数

~~~mysql
CREATE FUNCTION `rand_string`(n INT) RETURNS varchar(255) CHARSET latin1
BEGIN 
DECLARE chars_str varchar(100) DEFAULT 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'; 
DECLARE return_str varchar(255) DEFAULT '' ;
DECLARE i INT DEFAULT 0; 
WHILE i < n DO 
SET return_str = concat(return_str,substring(chars_str , FLOOR(1 + RAND()*62 ),1)); 
SET i = i +1; 
END WHILE; 
RETURN return_str; 
END
~~~

~~~mysql
CREATE  PROCEDURE `add_vote_memory`(IN n int)
BEGIN  
  DECLARE i INT DEFAULT 1;
    WHILE (i <= n ) DO
      INSERT into vote_record_memory  (user_id,vote_id,group_id,create_time ) VALUEs (rand_string(20),FLOOR(RAND() * 1000),FLOOR(RAND() * 100) ,now() );
            set i=i+1;
    END WHILE;
END
~~~

4.  调用存储过程

~~~mysql
CALL add_vote_memory(1000000)
~~~

5.  插入普通表

~~~mysql
INSERT into vote_record SELECT * from  vote_record_memory
~~~

## 2.SQL优化的相关规则

### 2.1Explain

使用explain可以查看SQL执行计划

![image-20200520141236200](http://tc.junhaox.cn/img/20200520141240.png)

重点关注以下字段：

1.  id，id相同从上到下顺序执行，id不同由大到小执行（子查询时存在）

2.  select_type

    -   simple：简单的select查询，查询中不包含子查询或者union
    -   primary：查询中包含任何复杂的子部分，最外层查询则被标记为primary
    -   subquery：在select或者where列表中包含子查询
    -   derived：在from中包含的子查询被标记为derived(衍生)，mysql或递归执行这些子查询，把结果放在临时表里
    -   union：若第二个select出现在union之后，则被标记为union；若union包含在from子句的子查询中，外层select将被标记为derived
    -   union result：从union表获取结果的select

3.  type，访问类型，SQL优化中一个很重要的指标，结果值从好到坏依次是**system** > **const** > **eq_ref** > **ref** > fulltext > ref_or_null > index_merge > unique_subquery > index_subquery > **range** > **index** > **ALL**

    **一般来说，好的sql查询至少达到range级别，最好能达到ref**

4.  possible_keys，查询涉及到的字段上存在索引，则该索引将被列出，但不一定被查询使用

5.  key，实际使用的索引，如果为null表示没有使用索引

6.  key_len，表示索引中使用的字节数，查询中使用的索引的长度（最大可能长度），并非实际使用长度，理论上长度越短越好。key_len是根据表定义计算而得的，不是通过表内检索出的

7.  ref，显示索引的那一列被使用了，如果可能，是一个常量const

























