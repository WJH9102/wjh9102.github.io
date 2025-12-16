# SpringMVC02

# 1.Controller中的细节

## 1.1@RequestMapping

### 1.1.1标记请求URL

只需要将该注解标记在相应的方法上即可。

```java
@Controller
public class HelloController {
    @RequestMapping("/hello")
    public ModelAndView hello() {
        return new ModelAndView("hello");
    }
}
```

这里 `@RequestMapping("/hello")` 表示当请求地址为 `/hello` 时，这个方法会被触发，其中这个地址可以是多个，会被映射到同一个方法。

```java
@Controller
public class HelloController {
    @RequestMapping({"/hello", "/hello2"})
    public ModelAndView hello() {
        return new ModelAndView("hello");
    }
}
```

这个配置，表示 `/hello` 和 `/hello2` 都可以访问到该方法。

### 1.1.2请求窄化

同一个项目中，会存在多个接口，例如订单相关的接口都是 `/order/xxx` 格式的，用户相关的接口都是 `/user/xxx` 格式的。为了方便处理，这里的前缀（就是 /order、/user）可以统一在 Controller 上面处理。

```java
@Controller
@RequestMapping("/user")
public class HelloController {
    @RequestMapping({"/hello","/hello2"})
    public ModelAndView hello() {
        return new ModelAndView("hello");
    }
}
```

当类上加了 @RequestMapping 注解之后，此时，要想访问到 hello ，地址就应该是 `/user/hello` 或者 `/user/hello2`

### 1.1.3请求方法限定

默认情况下，使用 `@RequestMapping` 注解定义好的方法，可以被 GET 请求访问到，也可以被 POST 请求访问到，但是 DELETE 请求以及 PUT 请求不可以访问到。

当然也可以指定具体的请求方法：

```java
@Controller
@RequestMapping("/user")
public class HelloController {
    @RequestMapping(value = "/hello",method = RequestMethod.GET)
    public ModelAndView hello() {
        return new ModelAndView("hello");
    }
}
```

通过 @RequestMapping 注解，指定了该接口只能被 GET 请求访问到，此时，该接口就不可以被 POST 以及其他请求访问到了。强行访问会报`405 Method Not Allowed`。

### 1.1.4指定响应类型及编码

```java
@Controller
@RequestMapping("/book")
public class BookController {
    @PostMapping(value = "/addBook", produces = "text/html;charset=utf-8")
    @ResponseBody
    public String addBook(Book book) {
        return book.toString();
    }
}
```

响应给客户端为字符串时可以指定 `produces` 用来防止乱码。

## 1.2Controller方法的返回值

### 1.2.1返回ModuleAndView

如果前后端不分离的情况下，我们大部分情况都是返回 ModuleAndView ，即 “数据 + 视图” 模型。

```java
@Controller
@RequestMapping("/user")
public class HelloController {
    @RequestMapping("/hello")
    public ModelAndView hello() {
        ModelAndView mv = new ModelAndView("hello");
        mv.addObject("username", "javaboy");
        return mv;
    }
}
```

Model 中，放我们的数据，然后在 ModelAndView 中指定视图名称。

### 1.2.2返回void

没有返回值。没有返回值，并不一定真的没有返回值，只是方法的返回值为 void，我们可以通过其他方式给前端返回。**实际上，这种方式也可以理解为 Servlet 中的那一套方案。**

- 通过 HttpServletRequest 做服务端跳转

```java
@RequestMapping("/hello2")
public void hello2(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
    req.getRequestDispatcher("/jsp/hello.jsp").forward(req,resp);//服务器端跳转
}
```

- 通过 HttpServletResponse 做重定向

```java
@RequestMapping("/hello3")
public void hello3(HttpServletRequest req, HttpServletResponse resp) throws IOException {
    resp.sendRedirect("/hello.jsp");
}
```

也可以自己手动指定响应头去实现重定向：

```java
@RequestMapping("/hello3")
public void hello3(HttpServletRequest req, HttpServletResponse resp) throws IOException {
    resp.setStatus(302);
    resp.addHeader("Location", "/jsp/hello.jsp");
}
```

- 通过 HttpServletResponse 给出响应

```java
@RequestMapping("/hello4")
public void hello4(HttpServletRequest req, HttpServletResponse resp) throws IOException {
    resp.setContentType("text/html;charset=utf-8");
    PrintWriter out = resp.getWriter();
    out.write("hello javaboy!");
    out.flush();
    out.close();
}
```

这种方式，既可以返回 JSON，也可以返回普通字符串。

### 1.2.3返回字符串

- 返回逻辑视图名

前面的 ModelAndView 可以拆分为两部分，Model 和 View，在 SpringMVC 中，Model 我们可以直接在参数中指定，然后返回值是逻辑视图名：

```java
@RequestMapping("/hello5")
public String hello5(Model model) {
    model.addAttribute("username", "javaboy");//这是数据模型
    return "hello";//表示去查找一个名为 hello 的视图
}
```

- 服务端跳转

```java
@RequestMapping("/hello5")
public String hello5() {
    return "forward:/jsp/hello.jsp";
}
```

forward 后面跟上跳转的路径。

- 客户端跳转

```java
@RequestMapping("/hello5")
public String hello5() {
    return "redirect:/user/hello";
}
```

这种，本质上就是浏览器重定向。

- 真的返回一个字符串

上面三个返回的字符串，都是由特殊含义的，如果一定要返回一个字符串，需要额外添加一个注意：@ResponseBody ，这个注解表示当前方法的返回值就是要展示出来返回值，没有特殊含义。

```java
@RequestMapping("/hello5")
@ResponseBody
public String hello5() {
    return "redirect:/user/hello";
}
```

上面代码表示就是想返回一段内容为 `redirect:/user/hello` 的字符串，他没有特殊含义。注意，这里如果单纯的返回一个中文字符串，是会乱码的，可以在 @RequestMapping 中添加 produces 属性来解决：

```java
@RequestMapping(value = "/hello5",produces = "text/html;charset=utf-8")
@ResponseBody
public String hello5() {
    return "Java 语言程序设计";
}
```
