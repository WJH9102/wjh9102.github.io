# HTTPClient使用

## 1.相关依赖

```xml
<dependency>
  <groupId>org.apache.httpcomponents</groupId>
  <artifactId>httpclient</artifactId>
</dependency>
```

## 2.使用HTTPClient发送请求

### 2.1无惨的GET请求

1. 构造HTTPClient
   - `CloseableHttpClient client = HttpClients.createDefault();`
2. 实例化HttpGet，并传入请求URL
   - `HttpGet httpGet = new HttpGet("https://www.montnets.com/");`
3. 发送请求，并接收响应
   - `response = client.execute(httpGet);`
4. 判断响应码是否正常，并提取出响应结果

```java
if (response.getStatusLine().getStatusCode() == 200) {
    HttpEntity entity = response.getEntity();
    System.out.println(EntityUtils.toString(entity, "UTF-8"));
    // 打印响应结果
    System.out.println(entity);
}
```

 ****​**完整的代码**​ ****

```java
package cn.junhaox.project_httpclient;

import cn.junhaox.entity.StatusCode;
import org.apache.http.HttpEntity;
import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.util.EntityUtils;

import java.io.IOException;

/**
 * @Author WJH
 * @Description
 * @date 2020/8/25 10:50
 * @Email ibytecode2020@gmail.com
 */
public class HttpClientDemo01 {


    public static void main(String[] args) {
        CloseableHttpClient client = null;
        CloseableHttpResponse response = null;
        try {
            client = HttpClients.createDefault();
            HttpGet httpGet = new HttpGet("https://www.montnets.com/");
            response = client.execute(httpGet);
            if (response.getStatusLine().getStatusCode() == StatusCode.HTTP_OK_CODE.getCode()) {
                HttpEntity entity = response.getEntity();
                System.out.println(EntityUtils.toString(entity, "UTF-8"));
                System.out.println(entity);
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            try {
                if (null != client) {
                    client.close();
                }
                if (null != response) {
                    response.close();
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
}

```

### 2.2有参的GET请求

对于GET请求的参数可以直接放到请求URL的?参数后面例如：`https://www.montnets.com?name=zs`；也可以通过`org.apache.http.client.utils.URIBuilder`构造带参数的GET请求

```java
URI uri = new URIBuilder()
    .setScheme("http") // 需要在这里指明请求协议
    // 这里不能加http -> http://dasai.lanqiao.cn/pages/dasai/news_detail.html
    .setHost("dasai.lanqiao.cn/pages/dasai/news_detail.html")
    .setParameter("id", "1828") // 设置参数
    .build();
// 构造出HttpGet
HttpGet httpGet = new HttpGet(uri);
```

构造出HttpGet之后的步骤就和无参GET请求一致了：发送请求->提取响应结果

### 2.3无参的POST请求

无参POST请求和无参GET请求基本一致，只需要将HttpGet换成HttpPost即可

### 2.4带参的POST请求

1. 构造HTTPClient
   - `CloseableHttpClient client = HttpClients.createDefault();`
2. 实例化HttpPost，并传入请求URL
   - `HttpPost httpPost= new HttpPost("https://www.montnets.com/");`
3. 在httpPost这设置请求参数

```java
// 请求参数集合
List<NameValuePair> pairList = new ArrayList<>();
// 键值对形式的请求参数
pairList.add(new BasicNameValuePair("id", "1"));
pairList.add(new BasicNameValuePair("name", "zs"));
pairList.add(new BasicNameValuePair("age", "23"));
UrlEncodedFormEntity httpEntity = new UrlEncodedFormEntity(pairList, "UTF-8");
// 设置请求参数
httpPost.setEntity(httpEntity);
```

4. 发送请求，并接收响应
   - `response = client.execute(httpPost);`
5. 判断响应码是否正常，并提取出响应结果

```java
if (response.getStatusLine().getStatusCode() == 200) {
    HttpEntity entity = response.getEntity();
    System.out.println(EntityUtils.toString(entity, "UTF-8"));
    // 打印响应结果
    System.out.println(entity);
}
```

 ****​**完整的代码**​ ****

```java
package cn.junhaox.project_httpclient;

import cn.junhaox.entity.StatusCode;
import org.apache.http.HttpEntity;
import org.apache.http.NameValuePair;
import org.apache.http.client.entity.UrlEncodedFormEntity;
import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.message.BasicNameValuePair;
import org.apache.http.util.EntityUtils;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * @Author WJH
 * @Description
 * @date 2020/8/25 10:50
 * @Email ibytecode2020@gmail.com
 */
public class HttpClientDemo02 {
    private static Pattern pattern = Pattern.compile("meta name=\"description\" content=\"(.+)\" />");


    public static void main(String[] args) {
        CloseableHttpClient client = HttpClients.createDefault();
        HttpPost httpPost = new HttpPost("https://www.montnets.com/");
        CloseableHttpResponse response = null;
        String des = null;
        try {
            List<NameValuePair> pairList = new ArrayList<>();
            pairList.add(new BasicNameValuePair("id", "1"));
            pairList.add(new BasicNameValuePair("name", "zs"));
            pairList.add(new BasicNameValuePair("age", "23"));
            UrlEncodedFormEntity httpEntity = new UrlEncodedFormEntity(pairList, "UTF-8");
            httpPost.setEntity(httpEntity);
            response = client.execute(httpPost);
            if (response.getStatusLine().getStatusCode() == StatusCode.HTTP_OK_CODE.getCode()) {
                HttpEntity entity = response.getEntity();
                String result = EntityUtils.toString(entity, "UTF-8");
                Matcher matcher = pattern.matcher(result);
                if (matcher.find()) {
                    des = matcher.group();
                }
                System.out.println(des);
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            try {
                if (null != client) {
                    client.close();
                }
                if (null != response) {
                    response.close();
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
}
```

## 3.使用连接池并设置连接属性

```java
package cn.junhaox.project_httpclient;

import cn.junhaox.entity.StatusCode;
import org.apache.http.HttpEntity;
import org.apache.http.client.config.RequestConfig;
import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.impl.conn.PoolingHttpClientConnectionManager;
import org.apache.http.util.EntityUtils;

import java.io.IOException;

/**
 * @Author WJH
 * @Description
 * @date 2020/8/25 10:50
 * @Email ibytecode2020@gmail.com
 */
public class HttpClientDemo03 {


    public static void main(String[] args) {
        // HTTPClient 连接池
        PoolingHttpClientConnectionManager pool = new PoolingHttpClientConnectionManager();
        // 连接最大数量
        pool.setMaxTotal(100);
        // 访问同一个网站的HTTPClient的数量
        pool.setDefaultMaxPerRoute(20);
        // 通过连接池获取HTTPClient
        CloseableHttpClient client = HttpClients.custom().setConnectionManager(pool).build();
        CloseableHttpResponse response = null;
        try {
            HttpGet httpGet = new HttpGet("https://www.montnets.com/");
            // 连接属性
            RequestConfig requestConfig = RequestConfig.custom().setConnectTimeout(3000)
                    .setConnectionRequestTimeout(5000)
                    .setSocketTimeout(5000).build();
            httpGet.setConfig(requestConfig);
            response = client.execute(httpGet);
            if (response.getStatusLine().getStatusCode() == StatusCode.HTTP_OK_CODE.getCode()) {
                HttpEntity entity = response.getEntity();
                System.out.println(EntityUtils.toString(entity, "UTF-8"));
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            try {
                if (null != client) {
                    client.close();
                }
                if (null != response) {
                    response.close();
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
}
```

## 4.POST请求发送JSON格式请求数据

在实例化HttpPost后可以设置StringEntity来发送Json数据

```java
// 普通对象
RequestParam param = new RequestParam();
param.setId("1828");
param.setAge("12");
param.setName("zs");
// 通过fastjson 将对象转为json数据，并构造StringEntity
StringEntity stringEntity = new StringEntity(JSON.toJSONString(param), "UTF-8");
// 设置请求参数
httpPost.setEntity(stringEntity);
```

## 5.springboot中使用HTTPClient

### 5.1配置文件配置参数

```yaml
http:
  # 连接池配置
  maxTotal: 100 # 连接池最大连接数
  defaultMaxPerRout: 20 # 访问同一个网站的HTTPClient的数量
  # 连接属性配置
  connectionTimeout: 3000 # 指建立连接的超时时间
  connectionRequestTimeout: 2000 # 指从连接池获取到连接的超时时间，如果是非连接池的话，该参数暂时没有发现有什么用处
  socketTimeout: 5000 # 指客户端和服务进行数据交互的时间，是指两者之间如果两个数据包之间的时间大于该时间则认为超时，而不是整个交互的整体时间，比如如果设置1秒超时，如果每隔0.8秒传输一次数据，传输10次，总共8秒，这样是不超时的。而如果任意两个数据包之间的时间超过了1秒，则超时。

```

### 5.2编写配置类

```java
package cn.junhaox.micro_httpclient.config;

import org.apache.http.client.config.RequestConfig;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClientBuilder;
import org.apache.http.impl.conn.PoolingHttpClientConnectionManager;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

/**
 * @Author WJH
 * @Description
 * @date 2020/8/25 14:28
 * @Email ibytecode2020@gmail.com
 */
@Configuration
public class HttpClientConfig {
    // 从配置文件中获取配置值
    @Value("${http.maxTotal}")
    private Integer maxTotal;
    @Value("${http.defaultMaxPerRout}")
    private Integer defaultMaxPerRout;
    @Value("${http.connectionTimeout}")
    private Integer connectionTimeout;
    @Value("${http.connectionRequestTimeout}")
    private Integer connectionRequestTimeout;
    @Value("${http.socketTimeout}")
    private Integer socketTimeout;

    /**
     * 实例化连接池
     * @return 连接池
     */
    @Bean("poolingHttpClientConnectionManager")
    public PoolingHttpClientConnectionManager poolingHttpClientConnectionManager() {
        PoolingHttpClientConnectionManager manager = new PoolingHttpClientConnectionManager();
        manager.setMaxTotal(maxTotal);
        manager.setDefaultMaxPerRoute(defaultMaxPerRout);
        return manager;
    }

    /**
     * 将HTTPClientBuilder放入ico容器
     * @param manager
     * @return HTTPClientBuilder
     */
    @Bean(name = "httpClientBuilder")
    public HttpClientBuilder httpClientBuilder(@Qualifier("poolingHttpClientConnectionManager") PoolingHttpClientConnectionManager manager) {
        HttpClientBuilder httpClientBuilder = HttpClientBuilder.create();
        httpClientBuilder.setConnectionManager(manager);
        return httpClientBuilder;
    }

    /**
     * 构造HTTPClient
     * @param httpClientBuilder
     * @return HTTPClient
     */
    @Bean(name = "httpClient")
    public CloseableHttpClient closeableHttpClient(@Qualifier("httpClientBuilder") HttpClientBuilder httpClientBuilder) {
        return httpClientBuilder.build();
    }

    /**
     * 设置请求相关配置
     * @return RequestConfig.Builder
     */
    @Bean(name = "builder")
    public RequestConfig.Builder builder() {
        return RequestConfig.custom()
                .setConnectTimeout(connectionTimeout)
                .setConnectionRequestTimeout(connectionRequestTimeout)
                .setSocketTimeout(socketTimeout);
    }

    /**
     * 设置请求相关配置
     * @param builder
     * @return requestConfig
     */
    @Bean(name = "requestConfig")
    public RequestConfig requestConfig(@Qualifier("builder") RequestConfig.Builder builder) {
        return builder.build();
    }
}

```

### 5.3编写业务类

```java
package cn.junhaox.micro_httpclient.service;

import cn.junhaox.entity.StatusCode;
import org.apache.http.HttpEntity;
import org.apache.http.NameValuePair;
import org.apache.http.client.config.RequestConfig;
import org.apache.http.client.entity.UrlEncodedFormEntity;
import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.client.utils.URIBuilder;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.message.BasicNameValuePair;
import org.apache.http.util.EntityUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

/**
 * @Author WJH
 * @Description
 * @date 2020/8/25 15:05
 * @Email ibytecode2020@gmail.com
 */
@Service
public class HttpClientService {

    @Autowired
    private RequestConfig requestConfig;

    @Autowired
    private CloseableHttpClient httpClient;

    /**
     * 不带参数的get请求
     * @param url 请求地址
     * @return 请求的响应值
     * @throws Exception 不处理异常
     */
    public String doGet(String url) throws Exception {
        HttpGet httpGet = new HttpGet(url);
        httpGet.setConfig(requestConfig);
        CloseableHttpResponse response = httpClient.execute(httpGet);
        if (response != null && response.getStatusLine().getStatusCode() == StatusCode.HTTP_OK_CODE.getCode()) {
            return EntityUtils.toString(response.getEntity(), "UTF-8");
        } else {
            return null;
        }
    }


    /**
     * 带参数的get请求
     * @param url 请求地址
     * @param map 参数
     * @return 请求的响应值
     * @throws Exception 不处理异常
     */
    public String doGet(String url, Map<String, Object> map) throws Exception {
        URIBuilder uriBuilder = new URIBuilder(url);
        if (map != null && map.size() > 0) {
            for (Map.Entry<String, Object> entry: map.entrySet()) {
                uriBuilder.setParameter(entry.getKey(), entry.getValue().toString());
            }
        }
        return doGet(uriBuilder.build().toString());
    }

    /**
     * 带参数的post请求
     * @param url 请求地址
     * @param map 请求参数
     * @return 响应参数
     * @throws Exception 不处理异常
     */
    public String doPost(String url, Map<String, Object> map) throws Exception {
        HttpPost httpPost = new HttpPost(url);
        httpPost.setConfig(requestConfig);
        // 请求参数设置
        if (map != null && map.size() > 0) {
            List<NameValuePair> pairList = new ArrayList<>();
            for (Map.Entry<String, Object> entry: map.entrySet()) {
                pairList.add(new BasicNameValuePair(entry.getKey(), ((String) entry.getValue())));
            }
            UrlEncodedFormEntity entity = new UrlEncodedFormEntity(pairList, "UTF-8");
            httpPost.setEntity(entity);
        }
        CloseableHttpResponse response = httpClient.execute(httpPost);
        if (response != null && response.getStatusLine().getStatusCode() == StatusCode.HTTP_OK_CODE.getCode()) {
            return EntityUtils.toString(response.getEntity());
        } else {
            return null;
        }
    }

    /**
     * 无参POST请求
     * @param url 请求地址
     * @return 响应参数
     * @throws Exception 不处理异常
     */
    public String doPost(String url) throws Exception {
        return doPost(url, null);
    }
    
    /**
     * 发送post请求，携带json格式数据
     * @param url 请求地址
     * @param data 请求数据
     * @return 响应参数
     * @throws Exception 不处理异常
     */
    public String doPostWithJson(String url, Object data) throws Exception {
        HttpPost httpPost = new HttpPost(url);
        httpPost.setHeader("Content-Type", "application/json; charset=utf-8");
        httpPost.setConfig(requestConfig);
        if (data == null) {
            return doPost(url);
        }
        String json = JSON.toJSONString(data);
        StringEntity entity = new StringEntity(json, "UTF-8");
        httpPost.setEntity(entity);
        CloseableHttpResponse response = httpClient.execute(httpPost);
        if (response != null && response.getStatusLine().getStatusCode() == StatusCode.HTTP_OK_CODE.getCode()) {
            return EntityUtils.toString(response.getEntity());
        } else {
            return null;
        }
    }
}

```

## 6.请求头的设置

HttpGet和HttpPost都可以通过setHeader方法设置请求头`httpPost.setHeader("Content-Type", "text/html; charset=utf-8");`
