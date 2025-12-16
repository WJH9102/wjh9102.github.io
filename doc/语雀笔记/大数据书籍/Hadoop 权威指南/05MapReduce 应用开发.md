# 05MapReduce 应用开发

# 1.MapReduce编程流程

1. 首先写map函数和reduce函数，并使用单元测试来确保函数的运行符合预期。
2. 写一个驱动程序来运行作业。先从本地IDE中用一个小的数据集来运行它，从而改进mapper和reducer，使其能够正确处理类似输入。
3. 当程序能够预期通过小型数据集，将其部署到集群中运行，不断通过扩展测试用例来改进mapper和reducer。
4. 当程序正确执行后，可以进行优化调整。如做标准检查、任务剖析（task profiling）、借助钩子（hook）。

# 2.用于配置的API

Hadoop中的组件是通过Hadoop自己的配置API来配置的。一个Configuration类的实例代表配置属性及其取值的一个集合。Configuration从资源（.xml文件）中读取其属性值。

使 用 Configuration 类 的 一 般 过 程 是 ： 构 造 Configuration 对 象， 并 通 过 类 的addResource() 方法添加需要加载的资源 ；然后就可以使用 get 方法和 set 方法访问 / 设置配置项，资源会在第一次使用的时候自动加载到对象中。

> Hadoop 配置文件的根元素是 configuration，一般只包含子元素 property。每一个property 元素就是一个配置项，配置文件不支持分层或分级。每个配置项一般包括配置属性的名称 name、值 value 和一个关于配置项的描述 description ；元素 final 和 Java 中的关键字final 类似，意味着这个配置项是“固定不变的”，为true代表无法变更。final 一般不出现，但在合并资源的时候，可以防止配置项的值被覆盖。
>
> 合并资源指将多个配置文件合并，产生一个配置。
>
> 如果有两个配置文件，也就是两个资源，如core-default.xml 和 core-site.xml，通过 Configuration 类的 loadResources() 方法，把它们合并成一个配置。代码如下：
>
> Configurationconf = new Configuration();
>
> conf.addResource(“core-default.xml”);
>
> conf.addResource(“core-site.xml”);
>
> 如果这两个配置资源都包含了相同的配置项，而且前一个资源的配置项没有标记为final，那么，后面的配置将覆盖前面的配置。上面的例子中，core-site.xml 中的配置将覆盖core-default.xml 中的同名配置。如果在第一个资源（core-default.xml）中某配置项被标记为final，那么，在加载第二个资源的时候，会有警告提示。

# 3.辅助类GenericOptionsParser，Tool和ToolRunner

GenericOptionsParser是hadoop框架中解析命令行参数的基本类。它能够辨别一些标准的命令行参数，能够使应用程序轻易地指定namenode，jobtracker，以及其他额外的配置资源。

通常不直接使用GenericOptionsParser，而是实现Tool接口，通过ToolRunner来运行应用程序。

> **ToolRunner的主要功能：**
>
> 1. 创建（如果传入的是null），设置当前tool的Configuration
> 2. 处理命令行参数。
>
> **命令行参数:**
>
> 在tool的执行过程中，有两个地方可以读入命令行参数
>
> 1. main中的args：main函数中的args得到的是原始的明亮行参数，通常我们会传入一些跟hadoop运行时有关的参数，这中参数和某个tool的业务逻辑没啥关系，这是一般会通过-D key=val的方式传入。
> 2. run中的args：ToolRunner解析参数的作用是将这些参数提取并存入Configuration中，便于job提取，同时将剩余的toolargs传入run方法中。所以run方法得到的就是tool相关的args。

# 4.用MRUnit来写单元测试

MRUnit是一个测试库，用于将已知的输入传递给mapper或者检查reducer的输出是否符合预期。
书中给出了很多范例。
根据不同的测试对象要采用不同的测试模块来进行，MRUnit针对不同测试对象分别使用一下几种Driver：

1. MapDriver ，针对单独的Map测试
2. ReduceDriver，针对单独的Reduce测试。
3. MapReduceDriver ，将Map和Reduce连贯起来测试。
4. PipelineMapReduceDriver，将多个Map-Reduce pair贯穿测试。

# 5.本地运行测试数据

## 5.1在本地作业运行器上运行作业

1. 通过Tool接口就可以写MapReduce作业的驱动程序。
2. Hadoop有本地作业运行器（job runner），它是在MapReduce执行引擎运行单个JVM上的MapReduce作业的简化版本。

## 5.2在本地测试驱动程序

1. 使用本地作业运行器，在本地文件系统的测试文件上运行作业。
2. 使用一个mini集群来运行。

# 6.在集群上运行

Hadoop的web界面用来浏览作业信息，对于跟踪作业运行进度、查找作业完成后的统计信息和日志非常有用。

# 7.MapReduce工作流

复杂处理过程的解决方法：增加更多的作业，而非增加作业的复杂度。

利用多个mapper和reduer将任务拆分，后一个mapper的输入为前一个mapper的输出。

MapReduce的工作流(JobControl)有两种方式：

1. 线性链
2. 有向无环图（directed acyclic graph, DAG）
