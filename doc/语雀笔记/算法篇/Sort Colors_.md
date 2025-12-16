# Sort Colors_

> 给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
>
> 此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
>
> 注意:
> 不能使用代码库中的排序函数来解决这道题。
>
> 示例:
>
> 输入: [2,0,2,1,1,0]
>
> 输出: [0,0,1,1,2,2]

### 1.解决思路

> 维护两个变量zero和two，zero从左往右滑动，two从右往左滑动，遍历nums当nums[i] == 1时i++；当nums[i] == 2时，two--，然后交换nums[i] 和 nums[two]；然后观察nums[i]；当nums[i] == 0时，zero++，交换nums[i] 和 nums[zero]，i++；当i == two时退出循环。

#### 1.1Java代码

```java
static void sortColors() {
    int[] a = {2,0,2,1,1,0};
    int zero = -1;
    int two = a.length;
    for (int i = 0; i < two; ){
        if (a[i] == 1) {
            i ++;
        } else if (a[i] == 2) {
            a[i] = a[--two];
            a[two] = 2;
        } else {
            a[i] = a[++zero];
            a[zero] = 0;
            i++;
        }
    }
    Arrays.stream(a).forEach(System.out::println);
}
```

#### 1.2.示意图

![](assets/network-asset-20200525164656-20250108100826-ingzswb.gif)
