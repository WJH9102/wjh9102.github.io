# two Sum II_

> 给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。
>
> 函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。
>
> 说明:
>
> - 返回的下标值（index1 和 index2）不是从零开始的。
> - 你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
>
> 示例:
>
> 输入: numbers = [2, 7, 11, 15], target = 9
> 输出: [1,2]
> 解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。

### 1.解决思路

> 维护两个变量left和right分别指向数组的第一个元素和最后一个元素，由于数组有序，计算numbers[left] + numbers[right]的值与target比较，如果大于target则需要一个更小的值right--，如果小于target则需要一个更大的值left++，如果等于target则返回[left+1, right+1]，整体需要满足left < right。

#### 1.1.Java代码

```java
static int[] twoSum(int target) {
    int[] a = {2, 7, 11, 15};
    int left = 0;
    int right = a.length - 1;
    int[] res = new int[2];
    while (left < right) {
        if (a[left] + a[right] < target) left++;
        else if (a[left] + a[right] > target) right--;
        else {
            res[0] = left + 1;
            res[1] = right + 1;
            return res;
        }
    }
    return null;
}
```

#### 1.2示意图

![](assets/network-asset-20200525164804-20250108100837-owe4dbp.gif)
