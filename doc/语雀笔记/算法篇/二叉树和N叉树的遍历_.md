# 二叉树和N叉树的遍历_

```java
//N叉树
public class NTree {
    public int val;
    public List<NTree> children;

    public NTree() {}

    public NTree(int _val) {
        val = _val;
    }

    public NTree(int _val, List<NTree> _children) {
        val = _val;
        children = _children;
    }

    public static NTree create() {
        List<NTree> nullNode = new ArrayList<>();
        NTree n5 = new NTree(5, nullNode);
        NTree n6 = new NTree(6, nullNode);
        List<NTree> n3Child = new ArrayList<>();
        n3Child.add(n5);
        n3Child.add(n6);
        NTree n3 = new NTree(3, n3Child);
        NTree n2 = new NTree(2, nullNode);
        NTree n4 = new NTree(4, nullNode);
        List<NTree> n1Child = new ArrayList<>();
        n1Child.add(n3);
        n1Child.add(n2);
        n1Child.add(n4);
        return new NTree(1, n1Child);
    }

}
```

```java
// 二叉树
public class TreeNode {
    public int val;
    public TreeNode left;
    public TreeNode right;

    TreeNode(int x) {
        val = x;
    }

    /*
                1
            /       \
        2              3
    /       \      /       \
   4         5    6         7

     */
    String s = "\t\t\t\t1\r\n\t\t\t/\t\t\\\r\n\t\t2\t\t\t\b\b\b3\r\n\t/\t\t\\\t\b\b\b/\t\b\b\b\\\r\n\b\b\b4\t\t\b5\t\b\b6\t\t\b7";
    public static TreeNode create () {
        TreeNode root = new TreeNode(1);

        TreeNode l1 = new TreeNode(2);
        TreeNode r1 = new TreeNode(3);
        root.left = l1;
        root.right = r1;

        TreeNode ll1 = new TreeNode(4);
        TreeNode rr1 = new TreeNode(5);
        l1.left = ll1;
        l1.right = rr1;


        TreeNode ll2 = new TreeNode(6);
        TreeNode rr2 = new TreeNode(7);
        r1.left = ll2;
        r1.right = rr2;
        return root;
    }

    @Override
    public String toString() {
        return "\t\t\t1\r\n\t2\t\t\t\t3\r\n4\t\t5\t\t6\t\t7";
    }
}
```

```java
public class Demo23 {

    private static List<Integer> solution = new ArrayList<>();
    private static List<Integer> solution1 = new ArrayList<>();
    private static List<Integer> solution2 = new ArrayList<>();
    private static List<Integer> solution3 = new ArrayList<>();
    private static List<Integer> solution4 = new ArrayList<>();
    private static List<Integer> solution5 = new ArrayList<>();
    private static List<Integer> solution6 = new ArrayList<>();
    private static List<Integer> solution7 = new ArrayList<>();
    private static List<Integer> solution8 = new ArrayList<>();
    private static List<Integer> solution9 = new ArrayList<>();

    public static void main(String[] args) {
        NTree root = NTree.create();
        solution(root);
        System.out.println(solution);
        solution1(root);
        System.out.println(solution1);
        System.out.println("-----------------------");
        TreeNode tree = TreeNode.create();
        System.out.println(tree);
        System.out.println("-----------------------");
        solution2(tree);
        System.out.println(solution2);
        solution3(tree);
        System.out.println(solution3);
        System.out.println("-----------------------");
        solution4(tree);
        System.out.println(solution4);
        solution5(tree);
        System.out.println(solution5);
        System.out.println("-----------------------");
        solution6(tree);
        System.out.println(solution6);
        solution7(tree);
        System.out.println(solution7);
        System.out.println("-----------------------");
    }

    /**
     * n 叉树的后序遍历递归方式
     * @param root
     */
    public static void solution(NTree root) {

        if (root == null) return;

        if (root.children != null) {
            for (NTree child : root.children) {
                solution(child);
            }
        }
        solution.add(root.val);
    }

    /**
     * n 叉树的后续遍历迭代方式
     * @param root
     */
    public static void solution1(NTree root) {
        LinkedList<NTree> stack1 = new LinkedList<>();
        LinkedList<NTree> stack2 = new LinkedList<>();
        stack1.push(root);
        while (!stack1.isEmpty()) {
            NTree p = stack1.pop();
            stack2.push(p);
            if (p.children != null) {
                for (NTree child : p.children) {
                    stack1.push(child);
                }
            }
        }

        while (!stack2.isEmpty()) {
            solution1.add(stack2.pop().val);
        }
    }


    /**
     * 二叉树的后序遍历递归方式
     * @param root
     */
    public static void solution2(TreeNode root) {
        if (root != null) {
            solution2(root.left);
            solution2(root.right);
            solution2.add(root.val);
        }
    }


    /**
     * 二叉树的后序遍历迭代方式
     * @param root
     */
    public static void solution3(TreeNode root) {
        LinkedList<TreeNode> stack = new LinkedList<>();
        TreeNode head = root;
        stack.push(root);
        while (!stack.isEmpty()) {
            TreeNode t = stack.peek();
            if ((t.left == null && t.right == null) || t.left == head || t.right == head) {
                t = stack.pop();
                solution3.add(t.val);
                head = t;
            } else {
                if (t.right != null) stack.push(t.right);
                if (t.left != null) stack.push(t.left);
            }
        }

    }

    /**
     * 二叉树的中序遍历递归方式
     * @param root
     */
    public static void solution4(TreeNode root) {
        if (root != null) {
            solution4(root.left);
            solution4.add(root.val);
            solution4(root.right);
        }
    }

    /**
     * 二叉树的中序遍历迭代方式
     * @param root
     */
    public static void solution5(TreeNode root) {
        TreeNode p = root;
        LinkedList<TreeNode> stack = new LinkedList<>();
        while (!stack.isEmpty() || p != null) {
            while (p != null) {
                stack.push(p);
                p = p.left;
            }
            TreeNode t = stack.pop();
            solution5.add(t.val);
            p = t.right;
        }
    }

    /**
     * 二叉树的前序遍历递归方式
     * @param root
     */
    public static void solution6(TreeNode root) {
        if (root != null) {
            solution6.add(root.val);
            solution6(root.left);
            solution6(root.right);
        }
    }

    /**
     * 二叉树的前序遍历迭代方式
     * @param root
     */
    public static void solution7(TreeNode root) {
        LinkedList<TreeNode> stack = new LinkedList<>();
        stack.push(root);
        while (!stack.isEmpty()) {
            TreeNode t = stack.pop();
            solution7.add(t.val);
            if (t.right != null) stack.push(t.right);
            if (t.left != null) stack.push(t.left);
        }
    }

}
```
