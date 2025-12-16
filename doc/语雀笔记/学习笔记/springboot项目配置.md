# springboot项目配置

# 1.配置禁用部分HTTP方法

```java
@Bean
public ConfigurableServletWebServerFactory configurableServletWebServerFactory() {
    TomcatServletWebServerFactory factory = new TomcatServletWebServerFactory();
    factory.addContextCustomizers(context -> {
        SecurityConstraint securityConstraint = new SecurityConstraint();
        securityConstraint.setUserConstraint("CONFIDENTIAL");
        SecurityCollection collection = new SecurityCollection();
        // 配置需要禁用的方法
        collection.addPattern("/*");
        collection.addMethod("HEAD");
        collection.addMethod("OPTIONS");
        collection.addMethod("TRACE");
        collection.addMethod("COPY");
        collection.addMethod("SEARCH");
        collection.addMethod("PROPFIND");
        collection.addMethod("PATCH");
        collection.addMethod("LINK");
        collection.addMethod("UNLINK");
        collection.addMethod("PURGE");
        collection.addMethod("LOCK");
        collection.addMethod("UNLOCK");
        collection.addMethod("VIEW");
        securityConstraint.addCollection(collection);
        context.addConstraint(securityConstraint);
    });
    return factory;
}
```
