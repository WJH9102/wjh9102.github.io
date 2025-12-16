# Partition List_

> 给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。
>
> 你应当保留两个分区中每个节点的初始相对位置。
>
> 示例:
>
> 输入: head = 1->4->3->2->5->2, x = 3
> 输出: 1->2->2->4->3->5

### 1.解决思路

> 定义两个虚拟头结点dummyNode1和dummyNode2，分别用来保存小于x的节点和大于等于x的节点，然后将dummyNode2置于dummyNode1之后即可保持各节点之间的相对位置关系

#### 1.1Java代码

```java
static ListNode solution(ListNode head, int x) {
    ListNode dummyNode1 = new ListNode(0);
    ListNode dummyNode2 = new ListNode(0);
    ListNode p1 = dummyNode1;
    ListNode p2 = dummyNode2;
    ListNode p = head;
    while (p != null) {
        if (p.val < x) {
            p1.next = p;
            p1 = p1.next;
        } else {
            p2.next = p;
            p2 = p2.next;
        }
        p = p.next;
    }
    p2.next = null;
    p1.next = dummyNode2.next;
    return dummyNode1.next;
}
```

#### 1.2示意图

![](assets/network-asset-20200601092156-20250108100804-zfoxf1h.gif)
