# 删除链表的倒数第N个节点_

> 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
>
> 示例：
>
> 给定一个链表: 1->2->3->4->5, 和 n = 2.
>
> 当删除了倒数第二个节点后，链表变为 1->2->3->5.
> 说明：
>
> 给定的 n 保证是有效的。
>
> 进阶：
>
> 你能尝试使用一趟扫描实现吗？

### 1. 解决思路

> 使用快慢指针，设置虚拟头结点dummy指向head
>
> 设置快慢指针，q和p，让q先走n+1步，让q和p直接间隔n个节点，然后p和q同步走，直到q指向null，删除p的下一个节点即可

#### 1.1Java代码

```java
static ListNode solution(ListNode head, int n) {
    ListNode dummy = new ListNode(0);
    dummy.next = head;
    ListNode p = dummy;
    ListNode q = dummy;
    int i = 0;
    while (q != null) {
        if (i > n) {
            p = p.next;
        }
        i++;
        q = q.next;
    }
    p.next = p.next.next;
    return dummy.next;
}
```

#### 1.2示意图

![](assets/network-asset-20200604153210-20250108100940-l18gua1.gif)
