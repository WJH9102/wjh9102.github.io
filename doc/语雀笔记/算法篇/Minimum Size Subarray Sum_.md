# Minimum Size Subarray Sum_

> 给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组。如果不存在符合条件的连续子数组，返回 0。
>
> 示例:
>
> 输入: s = 7, nums = [2,3,1,2,4,3]
>
> 输出: 2
>
> 解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。

### 1.解决思路

> 维护两个指针l和r，分别记录子数组的左右边界
>
> 1. r右移直到r到达数组边界或者sum大于等于s
> 2. sum -= nums[l]，同时l右移
> 3. 重复1,2记录l - r + 1的最小值

#### 1.1Java代码

```java
static int Minimum_Size_Subarray_Sum(int target) {
    int[] a = {2,3,1,10,4,3};
    int len = a.length + 1;
    int l = 0;
    int r = -1;
    int sum = 0;
    while (l < a.length) {
        if (r + 1 < a.length && sum < target) sum += a[++r];
        else sum -= a[l++];
        if (sum >= target) len = Math.min(len, r - l + 1);
        System.out.println(sum);
    }
    System.out.println(l + ", " + r);

    if (len == a.length + 1) return 0;

    return len;
}
```

###
