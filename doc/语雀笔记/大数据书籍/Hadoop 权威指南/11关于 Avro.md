# 11关于 Avro

Apache Avro 是一个独立于编程语言的数据序列化系统。旨在解决 Hadoop 中 Writable 类型的不足：缺乏语言的可移植性。

Avro 以 JSON 格式存储数据定义，使其便于阅读和解释；数据本身以二进制格式存储，以达到紧凑且高效的目的。其主要功能是对可随时间变化的数据模式提供强大支持。

# 1.Avro 数据类型和模式

Avro 定义了少量的基本数据类型，通过编写模式的方式，它们可被用于构建应用特定的数据机构。

**Avro 的基本类型：**

|**类型**|**描述**|**模式示例**|
| -------| -----------------| ---------|
|null|空值|"null"|
|boolean|二进制值|"boolean"|
|int|32位带符号整数|"int"|
|long|64位带符号整数|"long"|
|float|单精度浮点数|"float"|
|double|双精度浮点数|"double"|
|bytes|8位无符号字节序列|"bytes"|
|string|Unicode 字符序列|"string"|

**Avro 的复杂类型：**

- array：一个排过序的对象集合。特定数组中的所有对象必须模式相同

```json
{
  "type": "array",
  "items": "long"
}
```

- map：未排过序的键值对。键必须是字符串，值可以是任何一种类型，但一个特定的 map 中的所有值必须模式相同

```json
{
  "type": "map",
  "values": "string"
}
```

- record：一个任意类型的命名字段集合

```json
{
  "type": "record",
  "name": "WeatherRecord",
  "doc": "A weather reading."
  "fields": [
  {"name": "year", "type": "int"},
  {"name": "temperature", "type": "int"},
  {"name": "stationId", "type": "string"},
  ]
}
```

- enum：一个命名的值集合

```json
{
  "type": "enum",
  "name": "Cutlery",
  "doc": "An eating utensil.",
  "symbols": ["KNIFE", "FORK", "SPOON"]
}
```

- fixed：一组固定数量的8位无符号字节

```json
{
  "type": "fixed",
  "name": "Md5Hash",
  "size": 16
}
```

- union：模式的并集。并集可用 JSON 数组表示，其中每个元素为一个模式。并集表示的数据必须与其内的某个模式相匹配

```json
[
  "null",
  "string",
  {"type": "map", "values": "string"}
]
```

# 2.内存中的序列化和反序列化

使用 Java 编写程序从数据流中读/写 Avro 数据。Avro 模式文件的常用扩展名是`.avsc`，我们可以使用以下两行代码进行加载 file.avsc 模式文件：

```java
Schema.Parser parser = new Schema.Parser();
Schema schema = parser.parse(getCalss().getResourceAsStream("file.avsc"))
```

# 3.Avro 数据文件

Avro 的对象容器文件格式主要用于存储 Avro 对象序列。这与 Hadoop 顺序文件的设计非常相似，它们最大的区别在于 Avro 数据文件主要是面向跨语言使用而设计的，因此，我们可以使用 Python 语言写入文件，并用 C 语言来读取文件。

在数据文件的头部中含有元数据，它包括一个 Avro 模式和一个 sync marker（同步标识），紧接着是一系列包含序列化 Avro 对象的数据块。

# 4.模式解析

模式解析规则可以直接解决模式从一个版本演化为另一个版本是可能产生的问题。

对于 Avro 模式演化来说，另一种有用的技术是使用别名。别名允许你在读 Avro 数据的模式与写 Avro 数据的模式中使用不同的字段名称。

# 5.排序顺序

Avro 定义了对象的排列顺序。大多数 Avro 类型的排列顺序与用户期望符合，例如，数值型按照数值的升序进行排序。而其他有一些类型，例如，枚举则是通过符号的定义顺序进行排序，额不是根据符号的字符串值来进行排序。

除了 record 之外，所有的类型均按照 Avro 规范中预先定义的规则来排序，这些规则不能被用户改写。但对于记录，可以通过指定 order 属性来控制排列顺序，它有三个值：ascending（默认值）、descending（降序）或 ignore（排序比较时会忽略此字段）
