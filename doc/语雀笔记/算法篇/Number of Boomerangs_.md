# Number of Boomerangs_

> 给定平面上 n 对不同的点，“回旋镖” 是由点表示的元组 (i, j, k) ，其中 i 和 j 之间的距离和   i 和 k 之间的距离相等（需要考虑元组的顺序）。
>
> 找到所有回旋镖的数量。你可以假设 n 最大为 500，所有点的坐标在闭区间 [-10000, 10000] 中。
>
> 示例:
>
> 输入:
> [[0,0],[1,0],[2,0]]
>
> 输出:
> 2
>
> 解释:
> 两个回旋镖为 [[1,0],[0,0],[2,0]] 和 [[1,0],[2,0],[0,0]]

### 1.解决思路

> 对于点a、b、c，如果ab = ac则该元组有两种排列方式：abc和acb
>
> 对于平面上n个点到a点的距离相等则有2 * Cn2种排列方式
>
> 遍历点数组，以每个点为锚点计算其它点到锚点的距离并记录下来，然后分别带入n(n-1)计算结果并累加到res中

#### 1.1Java代码

```java
class Solution {
    public int numberOfBoomerangs(int[][] points) {
        int result = 0;
        for (int[] pointA : points) {
            Map<Integer, Integer> distances = new HashMap<>();
            for (int[] pointB : points) {
                int distance = (pointA[0] - pointB[0]) * (pointA[0] - pointB[0]) + (pointA[1] - pointB[1]) * (pointA[1] - pointB[1]);
                distances.put(distance, distances.getOrDefault(distance, 0) + 1);
            }
            for (int item : distances.values()) {
                result += item * (item - 1);
            }
        }
        return result;
    }
}
```

#### 1.2示意图

![](assets/network-asset-20200525165134-20250108100756-gwqgoth.gif)
