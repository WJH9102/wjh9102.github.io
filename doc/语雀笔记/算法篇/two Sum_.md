# two Sum_

> 给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。
>
> 你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。
>
> 示例:
>
> 给定 nums = [2, 7, 11, 15], target = 9
>
> 因为 nums[0] + nums[1] = 2 + 7 = 9
> 所以返回 [0, 1]

### 1.解决思路

> 使用哈希散列的方法，维护一个Map用来记录数组的值和下标，遍历数组，定义变量complement用来记录当前值和target的差值，然后在此次遍历中在Map中寻找是否有与complement一致的键，如果有则返回complement对应的值和当前数组下标i，如果没有则在Map中保存当前数字的值和下标。

#### 1.1Java代码

```java
static int[] twoSum(int target) {
    int[] res = new int[2];
    Map<Integer, Integer> record = new HashMap<>();

    int[] a = {2, 7, 11, 15,2, 7, 11, 15,2, 7, 11, 15,2, 7, 11, 15};
    int complement = -1;

    for (int i = 0; i < a.length; i++) {
        complement = target - a[i];
        Integer j = record.get(complement);
        if (null != j && i != j) {
            res[0] = j;
            res[1] = i;
            return res;
        }
        record.put(a[i], i);
    }
    throw new RuntimeException("No two sum solution");
}
```

#### 1.2示意图

![](assets/network-asset-20200525165032-20250108100843-c77aw8u.gif)
