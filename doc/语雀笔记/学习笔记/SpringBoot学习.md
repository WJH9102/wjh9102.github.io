# SpringBoot学习

## 1.SpringBoot中的全局异常处理

定义一个GlobalExceptionHandler

```java
@RestControllerAdvice
public class GlobalExceptionHandler {
    @ExceptionHandler(SQLException.class)
    public RespBeen sqlException(SQLException e) {
        if (e instanceof MySQLIntegrityConstraintViolationException) {
            return RespBeen.error("该数据有关联数据，操作失败");
        }
        return RespBeen.error("数据库异常，操作失败");
    }
}
```

‍
