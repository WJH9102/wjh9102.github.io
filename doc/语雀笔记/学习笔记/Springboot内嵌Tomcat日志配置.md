# Springboot内嵌Tomcat日志配置

```yaml
server:
  tomcat:
    # 生成的访问日志的目录
    basedir: my-tomcat
    # 开启访问日志，默认的日志位置在项目临时目录中
    accesslog:
      enabled: true
      # 日志前缀
      prefix: www_log
      # 日志后缀
      suffix: .log
      # 日志文件名中的日期格式
      file-date-format: .yyyyMMdd
      # 生成的日志文件类容格式也可以调整
      # %h 请求客户端的 IP
      # %l 用户的身份
      # %u 用户名
      # %t 请求时间
      # %r 请求地址
      # %s 响应状态码
      # %b 响应数据大小
      # pattern: %h %l %u %t "%r" %s %b 启动会报错，需要使用""引起来，如下
      pattern: "%h %l %u %t \"%r\" %s %b"
```

yml中以特殊字符开头可能会报错，此时可以将值用`""`引起来
