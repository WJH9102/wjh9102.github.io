# Contains Duplicate II_

> 给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的 绝对值 至多为 k。
>
> 示例 1:
>
> 输入: nums = [1,2,3,1], k = 3
> 输出: true
> 示例 2:
>
> 输入: nums = [1,0,1,1], k = 1
> 输出: true
> 示例 3:
>
> 输入: nums = [1,2,3,1,2,3], k = 2
> 输出: false

### 1.解决思路

> 1. 维护一个散列表HashSet，保证散列表长度小于等于k
> 2. 遍历数组并向散列表中添加数组元素
>    - 如果添加成功则判断散列表的长度是否大于k，如果大于k则删除元素nums[i-k]否则不作任何操作
>    - 如果添加失败则直接返回true

#### 1.1Java代码

```java
class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        HashSet<Integer> set = new HashSet<>();

        for (int i = 0; i < nums.length; i++) {
            if (set.add(nums[i])) {
                if (set.size() > k) set.remove(nums[i - k]);
            } else {
                return true;
            }
        }
        return false;
    }
}
```

#### 1.2示意图

![](assets/network-asset-20200526093543-20250108100744-sqprq34.gif)

‍
