# SQLserver

# 1.查看建表信息存储过程

```sql
 create Procedure sp_helptable
(
    @table varchar(100)
)
-- exec sp_helptable tablename
-- 增加获取注释信息(感谢 袁罗)
AS 
Begin
declare @sql table(s varchar(1000), id int identity)
-- 创建语句
insert into  @sql(s) values ('create table [' + @table + '] (')

--获取注释
SELECT
A.name AS table_name,
B.name AS column_name,
C.value AS column_description
into #columnsproperties
FROM sys.tables A
INNER JOIN sys.columns B ON B.object_id = A.object_id
LEFT JOIN sys.extended_properties C ON C.major_id = B.object_id AND C.minor_id = B.column_id
WHERE A.name = @table

-- 获取列的列表，拼接语句
insert into @sql(s)
select 
    '  ['+a.column_name+'] ' + 
    data_type + coalesce('('+cast(character_maximum_length as varchar)+')','') + ' ' +
    case when exists ( 
        select id from syscolumns
        where object_name(id)=@table
        and name=a.column_name
        and columnproperty(id,name,'IsIdentity') = 1 
    ) then
        'IDENTITY(' + 
        cast(ident_seed(@table) as varchar) + ',' + 
        cast(ident_incr(@table) as varchar) + ')'
    else ''
    end + ' ' +
    ( case when IS_NULLABLE = 'NO' then 'NOT ' else '' end ) + 'NULL ' + 
    coalesce('DEFAULT '+COLUMN_DEFAULT,'') + case when isnull(convert(varchar,b.column_description),'')<>'' then  '/**'+isnull(convert(varchar,b.column_description),'')+'**/,'
else ',' end
 from INFORMATION_SCHEMA.COLUMNS  a left join #columnsproperties b  
 on convert(varchar,a.column_name)=convert(varchar,b.column_name)
 where a.table_name = @table
 order by ordinal_position
-- 主键
declare @pkname varchar(100)
select @pkname = constraint_name from INFORMATION_SCHEMA.TABLE_CONSTRAINTS
where table_name = @table and constraint_type='PRIMARY KEY'
if ( @pkname is not null ) begin
    insert into @sql(s) values('  PRIMARY KEY (')
    insert into @sql(s)
        select '   ['+COLUMN_NAME+'],' from INFORMATION_SCHEMA.KEY_COLUMN_USAGE
        where constraint_name = @pkname
        order by ordinal_position
    -- 去除尾部多余的字符
    update @sql set s=left(s,len(s)-1) where id=@@identity
    insert into @sql(s) values ('  )')
end
else begin
    -- 去除尾部多余的字符
    update @sql set s=left(s,len(s)-1) where id=@@identity
end
-- 继续拼接
insert into @sql(s) values( ')' )
-- 输出结果
select s from @sql order by id
END
```

使用： `sp_helptable tablename` 
