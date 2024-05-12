# Java注解

>   注解是一系列元数据，它提供数据用来解释程序代码，但是注解并非是所解释的代码本身的一部分。注解对于代码的运行效果没有直接影响。
>
>   -   提供信息给编译器： 编译器可以利用注解来探测错误和警告信息
>   -   编译阶段时的处理： 软件工具可以用来利用注解信息来生成代码、Html文档或者做其它相应处理。（Lombok的@Data注解）
>   -   运行时的处理： 某些注解可以在程序运行的时候接受代码的提取（通过反射机制来获取）

### 1. 注解的语法

通过@interface来声明一个注解

~~~java
public @interface TestAnno01 {
}
~~~

### 2.注解的属性

注解的属性也称作注解的成员变量。注解只有成员变量没有方法，注解通过没有形参的“方法”来声明成员变量，方法返回值为变量的类型，成员变量可以有默认值，通过`default`来修饰

~~~java
public @interface TestAnno01 {
    String msg() default "默认消息";
    int id();
}
~~~

### 3.元注解

>   元注解是可以注解到注解上的注解，或者说元注解是一种基本注解，但是它能够应用到其它的注解上面。
>
>   如果难于理解的话，你可以这样理解。元注解也是一张标签，但是它是一张特殊的标签，它的作用和目的就是给其他普通的标签进行解释说明的。
>
>   元标签有 `@Retention`、`@Documented`、`@Target`、`@Inherited`、`@Repeatable `5 种。

#### 3.1@Retention

Retention是保留的意思，当@Retention修饰一个注解时，它解释说明了这个注解的存活时间。

-   RetentionPolicy.SOURCE 注解只在源码阶段保留，在编译器进行编译时它将被丢弃忽视。
-   RetentionPolicy.CLASS 注解只被保留到编译进行的时候，它并不会被加载到 JVM 中。
-   RetentionPolicy.RUNTIME 注解可以保留到程序运行的时候，它会被加载进入到 JVM 中，所以在程序运行时可以获取到它们（通过反射）。

#### 3.2@Document

顾名思义，这个元注解肯定是和文档有关。它的作用是能够将注解中的元素包含到 Javadoc 中去。

#### 3.3@Target

@Target制定了被它修饰的注解的使用场景，即一旦被@Target修饰后这个注解的使用场景就被限定了，也即如果没有被@Target修饰的注解可以使用在任意场景。

-   ElementType.ANNOTATION_TYPE 可以给一个注解进行注解
-   ElementType.CONSTRUCTOR 可以给构造方法进行注解
-   ElementType.FIELD 可以给属性进行注解
-   ElementType.LOCAL_VARIABLE 可以给局部变量进行注解
-   ElementType.METHOD 可以给方法进行注解
-   ElementType.PACKAGE 可以给一个包进行注解
-   ElementType.PARAMETER 可以给一个方法内的参数进行注解
-   ElementType.TYPE 可以给一个类型进行注解，比如类、接口、枚举

#### 3.4@Inherited

Inherited是继承的意思，但是它并不是说注解本身可以继承，而是说如果一个超类被 @Inherited 注解过的注解进行注解的话，那么如果它的子类没有被任何注解应用的话，那么这个子类就继承了超类的注解。

#### 3.5@Repeatable

Repeatable 是可重复的意思。@Repeatable 是 Java 1.8 才加进来的，所以算是一个新的特性。表示一个注解可以同时多次的修饰一个类、方法、属性。

它有固定的使用方式：

首先需要一个注解容器，容器用来存放可重复注解，并且该注解容器必须有一个被 @Repeatable 注解过的注解数组的属性`value`

~~~java
@interface Persons{
    Person[] value();
}
~~~

定义一个被 @Repeatable 注解注解的注解

~~~java
@Repeatable(Persons.class)
@interface Person{
    String role();
}
~~~

给一个示例，通过反射动态获取被@Person多次修饰的类的@Person的属性值

~~~java
// SuperMan.java
import java.lang.annotation.Repeatable;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;

/**
 * @Author WJH
 * @Description
 * @date 2020/5/15 16:39
 */
@Person(role = "hero")
@Person(role = "man")
@Person(role = "people")
public class SuperMan {
}

@Retention(RetentionPolicy.RUNTIME)
@Repeatable(Persons.class)
@interface Person{
    String role();
}

@Retention(RetentionPolicy.RUNTIME)
@interface Persons{
    Person[] value();
}
~~~

~~~java
// 通过反射动态获取值
public class Test01 {
    public static void main(String[] args) {
        boolean isAnno = SuperMan.class.isAnnotationPresent(Persons.class);
        if (isAnno) {
            Persons ann = SuperMan.class.getAnnotation(Persons.class);
            Person[] roles = ann.value();
            for (Person role : roles) {
                System.out.println(role.role());
            }
        }
    }
}
/*输出
hero
man
people
*/
~~~

### 4.Java内置注解

-   @Deprecate
-   @Override
-   @SuppressWarnings
-   @SafeVarargs
-   @FunctionallInterface

### 5.注解与反射

通过反射可以获取类、方法、属性是否被某些注解所修饰以及注解的属性值，前提是该注解必须被`@Retention(RetentionPolicy.RUNTIME)`修饰，否则反射期间无法获取该注解的任何信息

给一个综合示例

>   程序员 A : 我写了一个类，它的名字叫做 NoBug，因为它所有的方法都没有错误。
>   我：自信是好事，不过为了防止意外，让我测试一下如何？
>   程序员 A: 怎么测试？
>   我：把你写的代码的方法都加上 @MyCheck 这个注解就好了。
>   程序员 A: 好的。

**MyCheck.java**

~~~java
@Retention(RetentionPolicy.RUNTIME)
public @interface MyCheck {
}
~~~

**NoBug.java**

~~~java
/**
 * 没有bug的类
 */
public class NoBug {
    @MyCheck
    public void suanShu(){
        System.out.println("1234567890");
    }
    @MyCheck
    public void jiafa(){
        System.out.println("1+1="+1+1);
    }
    @MyCheck
    public void jiefa(){
        System.out.println("1-1="+(1-1));
    }
    @MyCheck
    public void chengfa(){
        System.out.println("3 x 5="+ 3*5);
    }
    @MyCheck
    public void chufa(){
        System.out.println("6 / 0="+ 6 / 0);
    }

    public void ziwojieshao(){
        System.out.println("我写的程序没有 bug!");
    }
}
~~~

**TestNoBug.java**

```java
public class TestNoBug {
    public static void main(String[] args) {
        NoBug noBug = new NoBug();
        // 拿到Class对象
        Class clazz = noBug.getClass();
        // 通过反射获取对象中的所有方法
        Method[] methods = clazz.getMethods();
        // 记录日志
        StringBuilder log = new StringBuilder();
        int errNum = 0;
        for (Method method : methods) {
            // 判断某方法是否被@MyCheck修饰
            if (method.isAnnotationPresent(MyCheck.class)){
                try {
                    // 反射修改方法访问权限
                    method.setAccessible(true);
                    // 反射执行方法
                    method.invoke(noBug, null);
                } catch (Exception e) {
                    errNum++;
                    log.append(method.getName());
                    log.append(" ");
                    log.append("has error:");
                    log.append("\n\r  caused by ");
                    //记录测试过程中，发生的异常的名称
                    log.append(e.getCause().getClass().getSimpleName());
                    log.append("\n\r");
                    //记录测试过程中，发生的异常的具体信息
                    log.append(e.getCause().getMessage());
                    log.append("\n\r");
                }
            }
        }
        log.append(clazz.getSimpleName());
        log.append(" has  ");
        log.append(errNum);
        log.append(" error.");
        System.out.println(log);
    }
}
```

>   总而言之，注解的使用不影响代码，如果需要它对代码产生影响则需要自己通过代码处理。













































