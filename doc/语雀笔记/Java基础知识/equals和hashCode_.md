# equals和hashCode_

## 1.==和equals的区别

1. ==是比较运算符，equals最初始Object中的一个方法
2. ==比较的是引用地址（内存地址），equals比较的是内容的相等（在自定义对象中内容的相等可以自己来定义）
3. Object中的equals方法就是“==”，只不过在其子类中一般都会重写equals方法，将其重写为比较内容相等的方法，例如String
4. ==还可以用来比较基本数据类型

## 2.自定义equals方法

1. 判断传入对象与当前对象是否相等，相等返回true，否则进2
2. 判断传入对象是否是当前类的实例，相等进3，否则返回false
3. 根据需求判断传入对象与当前对象内容是否相同，相同返回true，否则返回false
4. 例如规定Student对象的id和name属性相等时就认为对象相等

```java
package junhaox.cn.string;

public class Student {
	private int id;
	private String name;
	private int age;

	//setter/getter/constructor...
	
	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj instanceof Student) {
			Student anStudent = (Student) obj;
			if (this.id == anStudent.getId() && this.name.equals(anStudent.getName())) {
				return true;
			}else {
				return false;
			}
		}else{
			return false;
		}
	}
```

## 3.重写equals方法同时要重写hashCode方法

1. hashCode在Java中的应用场景：用于快速定位，一般使用与带“hash”的集合中，如HashMap，HashSet等
2. 在HashMap中内容相同的键不能重复（或者说添加内容相同的键时后者的value会覆盖前者的value）；在HashSet中内容相同的元素只能添加一次（重复添加会返回false：添加失败）
3. hash集合的设计理念：首先根据对象的hashCode判断对象是否相同，hashCode相同则在根据equals判断内容是否相同

```java
public static void main(String[] args){
    Set set = new HashSet();
    /*
    没有重写hashCode之前
    3个Student对象分别指向不同的内存空间，
    所以为3个不同的对象，但是（1）和（3）的内容明显相同
    （通过equals判断），
    显然有些矛盾
    */
    set.add(new Student(1, "zs", 23));//true （1）
    set.add(new Student(2, "ls", 23));//true （2）
    set.add(new Student(1, "zs", 23));//true （3）
}
```

4. hashCode方法

```java
@Override
public int hashCode() {
    int hash = Integer.hashCode(this.id)+this.name.hashCode();
    return hash;
}
```

```java
public static void main(String[] args){
    Set set = new HashSet();
    /*
    没有重写hashCode之后
    通过hashCode判断（1）和（3）hashCode值相同，
    在通过equals判断（1）和（3）的内容确实相同，所以添加失败
    */
    set.add(new Student(1, "zs", 23));//true （1）
    set.add(new Student(2, "ls", 23));//true （2）
    set.add(new Student(1, "zs", 23));//false （3）
}
```

5. hashCode的说明：
   1. 两对象相等（引用地址），则hashCode一定相等
   2. 两对象的hashCode相等，这两个对象不一定相等
   3. 两对象不等（引用地址），这两个对象的hashCode不一定不等
   4. 两对象的hashCode不等，则这两个对象一定不等
