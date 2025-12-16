# Reverse Linked List II_

> 反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
>
> 说明:
> 1 ≤ m ≤ n ≤ 链表长度。
>
> 示例:
>
> 输入: 1->2->3->4->5->NULL, m = 2, n = 4
> 输出: 1->4->3->2->5->NULL

### 1. 解决思路

> 首先找到m点的前置节点，记为pre，然后对m到n的局部链表做反转操作，同时记下反转后的链表的尾结点为last，头结点为front，在反转过程中找到n点的后置节点记为cur，局部链表反转完成后只需要将pre.next 指向 front，将last.next指向cur即可。

#### 1.1Java代码

```java
static ListNode reverseBetween(ListNode head, int m, int n) {
    if (head == null) return null;
    ListNode dummy = new ListNode(0);
    dummy.next = head;
    ListNode cur = dummy;
    // m的前置节点
    ListNode pre;
    // 反转后局部链表的尾结点，反转前局部链表的头结点
    ListNode last;
    // 反转后局部链表的头结点，反转前局部链表的尾结点
    ListNode front;
    // 找到m的前置节点
    for (int i = 1; i <= m - 1; i++) {
        cur = cur.next;
    }
    // 保存m的前置节点为pre
    pre = cur;
    // 最开始last和front都指向局部链表的头结点
    // 循环过程中last不做任何操作
    last = cur.next;
    front = cur.next;
    // cur指向局部链表的第二个节点
    // 与front构造出反转整个链表的样式
    cur = front.next;
    // 反转局部链表的具体操作，参考反转链表
    // 最后cur是指向局部链表之外的
    for (int i = m; i < n; i++) {
        ListNode next = cur.next;
        cur.next = front;
        front = cur;
        cur = next;
    }
    // 拼接链表
    last.next = cur;
    pre.next = front;
    return dummy.next;
}
```

### 2.头插法

> 假设链表 1->2->3->4->5，反转2到4的局部链表
>
> 找到m的前置节点记为pre，head指向pre.next，即初始时局部链表的头结点
>
> 1. 记下head.next，为next，将head.next = next.next 即 2->4->5
> 2. 将next.next = pre.next 即3->2
> 3. 将pre.next = next 即1->3，得到1->3->2->4->5
> 4. 重复1、2、3变化如下
>    - 2->5
>    - 4->3
>    - 1->4，得到1->4->3->2->5

#### 2.2Java代码

```java
public static ListNode reverseBetween(ListNode head, int m, int n) {
    ListNode dummy = new ListNode(0);
    dummy.next = head;
    ListNode pre = dummy;
    for(int i = 1; i < m; i++){
        pre = pre.next;
    }
    head = pre.next;
    for(int i = m; i < n; i++){
        ListNode nex = head.next;
        head.next = nex.next;
        nex.next = pre.next;
        pre.next = nex;
    }
    return dummy.next;
}
```
