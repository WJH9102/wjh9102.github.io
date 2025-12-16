# Linux相关

# 1.find命令

```shell
# 指定目录下列出所有指定文件名的文件
find /home -name "hello.txt"
# 指定目录下列出所有包含指定前缀的文件
find /home -name "hello*"
# 指定目录下列出所有包含指定前缀并忽略大小写的文件
find /home -iname "hello*"
```

# 2.grep命令

```shell
# 指定文件中找出包含指定字符串的行，并打印
grep "hello" hello.txt
# 从标准输出流中找出指定字符串
grep -o "hello\[[0-9a-z]\]"
# 从标准输出流中过滤掉包含指定字符串的行
ps -ef | grep tomcat | grep -v "grep"
```

# 3.awk命令

```plain
hello world
hello java
hello go
你好 颤三
哈哈哈 哦哦哦
```

```shell
# 打印指定列
awk '{print $1, $2}' hello.txt
[root@bigdata01 wjh]# awk '{print $1, $2}' hello.txt
hello world
hello java
hello go
你好 颤三
哈哈哈 哦哦哦

# 打印满足指定条件的指定列
awk '$1=="hello" || NR==1 {print $1}' hello.txt
[root@bigdata01 wjh]# awk '$1=="hello" || NR==1 {print $1}' hello.txt
hello
hello
hello

# 统计指定行出现的次数
awk '{arr[$1]++}END{for (i in arr) print i "\t" arr[i]}' hello.txt
[root@bigdata01 wjh]# awk '{arr[$1]++}END{for (i in arr) print i "\t" arr[i]}' hello.txt
哈哈哈  1
hello   3
你好    1
```

# 4.sed命令

```shell
# 将以hel打头的字符串替换为haha
sed -i 's/^hel/haha/' hello.txt
# 将以 . 结尾的字符串替换为 ;
sed -i 's/\.$/\;/' hello.txt
# 将指定文本 o 全局替换为 p 如果不指定 g 全局匹配则只会替换每一行第一次出现的 o
sed -i 's/o/p/g' hello.txt
# 删除空行
sed -i '/^ *$/d' hello.txt
# 删除包含指定字符串的行
sed -i '/java/d' hello.txt
```
