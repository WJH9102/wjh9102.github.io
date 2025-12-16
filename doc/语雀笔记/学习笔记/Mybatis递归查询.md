# Mybatis递归查询

在进行树状数据结构查询时如果知道树的深度，即层级可控可以采用多次自连接的方式来进行查询，例如对于菜单的查询，由于一般菜单最多不会超过三级就可以采用多次自连接的方式。

**层级可控的查询**

```xml
<resultMap id="MenuWithChildren" type="org.javaboy.vhr.model.Menu" extends="BaseResultMap">
  <id column="id1" property="id"/>
  <result column="name1" property="name"/>
  <collection property="children" ofType="org.javaboy.vhr.model.Menu">
    <id column="id2" property="id"/>
    <result column="name2" property="name"/>
    <collection property="children" ofType="org.javaboy.vhr.model.Menu">
      <id column="id3" property="id"/>
      <result column="name3" property="name"/>
    </collection>
  </collection>
</resultMap>
<select id="getAllMenus" resultMap="MenuWithChildren">
  SELECT
    m1.`id` AS id1,
    m1.`name` AS name1,
    m2.`id` AS id2,
    m2.`name` AS name2,
    m3.`id` AS id3,
    m3.`name` AS name3
  FROM
    menu m1,
    menu m2,
    menu m3
  WHERE
    m1.`id` = m2.`parentId`
  AND m2.`id` = m3.`parentId`
  AND m3.`enabled` = TRUE
  ORDER BY
    m1.`id`,
    m2.`id`,
    m3.`id`
</select>
```

但是对于层级不可控的树状数据结构进行查询时，无法知道自连接的次数，同时这种树状结构一般层级较深，不适合自连接。这时可以采用Mybatis提供的collection进行递归查询，从根节点开始逐层递归查询。

```xml
<resultMap id="BaseResultMap" type="cn.junhaox.vhrBack.model.Department" >
  <id column="id" property="id" jdbcType="INTEGER" />
  <result column="name" property="name" jdbcType="VARCHAR" />
  <result column="parentId" property="parentid" jdbcType="INTEGER" />
  <result column="depPath" property="deppath" jdbcType="VARCHAR" />
  <result column="enabled" property="enabled" jdbcType="BIT" />
  <result column="isParent" property="isparent" jdbcType="BIT" />
  <collection property="children" ofType="cn.junhaox.vhrBack.model.Department" 
              select="selectDeptByPid" column="id"/>
</resultMap>

<sql id="Base_Column_List" >
  id, name, parentId, depPath, enabled, isParent
</sql>

<select id="selectDeptByPid" resultMap="BaseResultMap">
  select 
  <include refid="Base_Column_List"/> 
  from department 
  where 
  department.parentId = #{pid} 
  and department.enabled=true;
</select>
```

在调用`selectDeptByPid`方法时，先根据根节点的pid进行查询，返回值为 `BaseResultMap` 在对children赋值时又调用 `selectDeptByPid` 对children进行赋值，但是`selectDeptByPid` 需要一个入参 `#{pid}` ，这时可以通过`column`来指定，`column`绑定的是上一个查询中的`column`的值。
