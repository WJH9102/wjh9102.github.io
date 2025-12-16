# Reverse Linked List_

> 反转一个单链表。
>
> ##### 示例:
>
> 输入: 1->2->3->4->5->NULL
> 输出: 5->4->3->2->1->NULL
>
> ##### 进阶:
>
> 你可以迭代或递归地反转链表。你能否用两种方法解决这道题？

### 1. 解决思路

> 设置3个节点pre、cur、next
>
> - 每次先判断cur是否为null，如果是则直接返回得到结果
> - 将cur.next保存在next中
> - 将cur.next指向pre
> - pre指向cur，cur指向next

#### 1.1Java代码

```java
static ListNode solution(ListNode head) {
    if (head == null) return null;
    ListNode pre = head;
    ListNode cur = head.next;
    pre.next = null;
    while (cur != null) {
        ListNode next = cur.next;
        cur.next = pre;
        pre = cur;
        cur = next;
    }
    return pre;
}
```

#### 1.2示意图

![](assets/network-asset-20200602103236-20250108100813-e36j6z6.gif)

#### 1.3递归代码

```java
public static ListNode reverseList(ListNode head) {
    if (head == null || head.next == null) return head;
    ListNode p = reverseList(head.next);
    head.next.next = head;
    head.next = null;
    return p;
}
```

##### 1.3.1解释

> - 假设链表是`[1, 2, 3, 4, 5]`从最底层最后一个reverseList(5)来看
>
> 1. 返回了5这个节点
> 2. reverseList(4)中
> 3. p为5
> 4. head.next.next = head 相当于 5 -> 4
> 5. 现在节点情况为 4 -> 5 -> 4
> 6. head.next = null,切断4 -> 5 这一条，现在只有 5 -> 4
> 7. 返回（return）p为5，5 -> 4
> 8. 返回上一层reverseList(3)
> 9. 处理完后返回的是4 -> 3
> 10. 依次向上
