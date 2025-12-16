# Swap Nodes in Pairs_

> 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
>
> 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
>
> 示例:
>
> 给定 1->2->3->4, 你应该返回 2->1->4->3.

### 1.解决思路

> 1. 建立虚拟头结点指向当前链表，构建指针p指向虚拟节点
> 2. 遍历链表构建指针node1、node2、node，node1和node2为要交换的节点，3者关系：p.next = node1，node1.next = node2，node2.next = node
> 3. 交换node1和node2，node1.next = node，node2.next = node1，p.next = node2，p = node1。
> 4. 重复2,3知道p.next或者p.next.next为null时退出循环

#### 1.1Java代码

```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode swapPairs(ListNode head) {
        ListNode dummyNode = new ListNode(0);
        dummyNode.next = head;
        ListNode p = dummyNode;
        while (p.next != null && p.next.next != null) {
            ListNode node1 = p.next;
            ListNode node2 = node1.next;
            ListNode node = node2.next;
            node1.next = node;
            node2.next = node1;
            p.next = node2;
            p = node1;
        }
        return dummyNode.next;
    }
}
```

#### 1.2示意图

![](assets/network-asset-20200529095417-20250108100832-np8jca1.gif)
