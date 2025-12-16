# Java 集合

## 1.Java 集合的排序方式

- 元素实现 `Compareable` 接口
- 借助 `Comparator` 接口
- 通过 `Stream` 流

## 2.fail-fast 和 fail-safe

我们通常说的 fail-fast 机制，默认是指 Java 集合的一种错误检测机制。当多个线程对部分集合进行结构上的改变操作时，就有可能产生 fail-fast 机制，这时就会抛出`ConcurrentModificationException`。

fail-safe 机制的集合类在遍历时不是直接在集合内容上访问的，而是先复制原有的集合内容，在拷贝的集合上进行遍历。`java.util.concurrent`包下的容器都是 fail-safe 的，可以在多线程环境下使用。

## 3.遍历时修改

- 通过 Iterator 迭代器修改
- 通过构造安全的集合进行修改
- 通过 Stream 流修改
