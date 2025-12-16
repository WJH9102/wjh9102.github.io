# Reverse String_

> 编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。
>
> 不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。
>
> 你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。
>
> 示例 1：
>
> 输入：["h","e","l","l","o"]
> 输出：["o","l","l","e","h"]
> 示例 2：
>
> 输入：["H","a","n","n","a","h"]
> 输出：["h","a","n","n","a","H"]

### 1.解决思路

> 使用双指针，m和n分别指向字符数组首尾，交换m和n位置的字符，m++、n--，当m >= n时循环结束

#### 1.1Java代码

```java
public void reverseString(char[] s) {
    int m = 0;
    int n = s.length - 1;
    char temp;
    while (m < n) {
        temp = s[m];
        s[m++] = s[n];
        s[n--] = temp;
    }
}
```

#### 1.2示意图

![](assets/network-asset-20200527092242-20250108100819-txjdpls.gif)
