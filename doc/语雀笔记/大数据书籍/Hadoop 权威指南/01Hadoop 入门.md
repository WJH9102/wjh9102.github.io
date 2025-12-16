# 01Hadoop 入门

# 1.Hadoop基本概念

## 1.1Hadoop是什么

Hadoop是一个由道格·卡丁创建的 apache 基金会开发的分布式系统基础架构，用来处理海量数据存储和海量数据分析计算问题。

## 1.2Hadoop的发展史

1. 道格·卡丁为了实现与 Google 类似的全文搜索功能，在 Lucene 框架上进行优化升级查询引擎和索引引擎，起源于开源网络搜索引擎 Apache Nutch，后者本身也是 Lucene 的一部分。
2. 等人用2年的业余时间实现了 DFS 和 MapReduce 机制，使 Nutch 性能飙升。
3. 2005年，Hadoop 作为 Lucene 的子项目 Nutch 的一部分正式引入 Apache 基金会。
4. 2006年2月被分离出来，成为一套完整独立的软件，起名为 Hadoop。

## 1.3Hadoop的优势

1. 扩容能力（Scalable）：Hadoop 是在可用的计算机集群间分配数据并完成计算任务的，这些集群可用方便的扩展到数以千计个节点中。
2. 成本低（Economical）：Hadoop 通过普通廉价的机器组成服务器集群来分发以及处理数据，以至于成本很低。
3. 高效率（Efficient）：通过并发数据，Hadoop 可以在节点之间动态并行的移动数据，使得速度非常快。
4. 可靠性（Rellable）：能自动维护数据的多份复制，并且在任务失败后能自动地重新部署（redeploy）计算任务。所以Hadoop的按位存储和处理数据的能力值得人们信赖。

# 2.关于MapReduce

## 2.1MapReduce定义

MapReduce 是一个分布式运算程序的编程框架，是用户开发“基于 Hadoop 数据分析应用”的核心框架。其核心功能是将用户编写的业务逻辑代码和自带默认组件整合成一个完整的 分布式运算程序，并发运行在一个 Hadoop 集群上。

## 2.2MapReduce核心思想

MapReduce运算程序一般分为两个阶段：Map 阶段和 Reduce 阶段

1. Map 阶段：读取数据，将数据处理为 K V 键值对格式并输出
2. Reduce 阶段：将 Map 阶段的输出作为输入 ，进行数据流处理

## 2.3Java版MapReduce

用户编写程序主要包括两部分：Mapper 和 Reducer

1. Mapper 阶段：
   1. 继承 MapReduceBase 类和实现 Mapper 接口，接口泛型指明了输入及输出格式
   2. 业务逻辑编写在 map() 方法中
   3. 输出 K V 形式的数据
2. Recuder 阶段：
   1. 继承 Reducer 类即可，类泛型指明了输入及输出格式，需要注意的是输入格式需要与 Map 阶段的输出格式一致
   2. 业务逻辑编写在 reduce() 方法中
   3. 输出 K V 形式的数据
