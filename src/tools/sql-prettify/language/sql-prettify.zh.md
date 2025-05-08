# SQL 美化和格式化工具使用文档

## 一、工具简介

SQL 美化和格式化工具是一个在线平台，用于将编写的 SQL 查询语句进行格式化和美化。它支持多种 SQL 方言，能够帮助开发者更清晰地阅读和编写 SQL 代码。

## 二、功能说明

### （一）基本功能

  1. **SQL 美化** ：将杂乱无章的 SQL 查询语句转换为格式规范、易于阅读的版本。例如：

     * 原始查询：

```
select field1,field2,field3 from my_table where my_condition;
```

     * 美化后：

```
SELECT
    field1,
    field2,
    field3
FROM
    my_table
WHERE
    my_condition;
```



### （二）配置选项

  1. **方言（Dialect）选择** ：提供多种 SQL 方言选项，如 Standard SQL（标准 SQL）、MySQL、PostgreSQL、SQL Server 等。选择适合您数据库的方言，可确保格式化后的 SQL 语句符合特定数据库的语法规范。
  2. **关键词大小写（Keyword case）设置** ：可以选择将 SQL 关键词转换为大写（UPPERCASE）、小写（lowercase）或首字母大写（Capitalized），使代码风格统一。例如：

     * 原始查询：

```
select * from table;
```

     * 设置关键词为大写后：

```
SELECT * FROM table;
```

     * 设置关键词为小写后：

```
select * from table;
```

     * 设置关键词为首字母大写后：

```
Select * From table;
```



  3. **缩进风格（Indent style）调整** ：有 Standard（标准）、2 spaces（2 个空格）、4 spaces（4 个空格）等选项。不同的缩进风格可满足个人或团队的代码格式偏好。例如：

     * 标准缩进：

```
SELECT
    field1,
    field2
FROM
    my_table
WHERE
    condition;
```

     * 2 个空格缩进：

```
SELECT
  field1,
  field2
FROM
  my_table
WHERE
  condition;
```

     * 4 个空格缩进：

```
SELECT
    field1,
    field2
FROM
    my_table
WHERE
    condition;
```



### （三）输入与输出

  1. **输入区域** ：在左侧的文本框中粘贴或输入需要美化的原始 SQL 查询语句。
  2. **输出区域** ：右侧的文本框会实时显示格式化和美化后的 SQL 语句。同时，右侧有一个复制按钮，方便用户将美化后的 SQL 语句复制到剪贴板，以便在其他地方使用。

## 三、使用步骤

  1. 打开 [SQL 美化和格式化工具](https://atoolio.com/sql-prettify) 网页。
  2. 在输入区域粘贴或输入您的 SQL 查询语句。
  3. 根据需求，在方言、关键词大小写和缩进风格的下拉菜单中选择合适的选项。
  4. 查看右侧输出区域中美化后的 SQL 语句，如满意可点击复制按钮将其复制。

## 四、示例

### 示例一：简单查询美化

  1. 输入：

```
select name, age from users where age > 25;
```

  2. 设置：
     * 方言：Standard SQL
     * 关键词大小写：UPPERCASE
     * 缩进风格：Standard

  3. 输出：

```
SELECT
    name,
    age
FROM
    users
WHERE
    age > 25;
```



### 示例二：复杂查询美化

  1. 输入：

```
select orders.order_id, customers.name, products.product_name from orders join customers on orders.customer_id = customers.customer_id join order_items on orders.order_id = order_items.order_id join products on order_items.product_id = products.product_id where orders.order_date between '2024-01-01' and '2024-12-31';
```

  2. 设置：
     * 方言：MySQL
     * 关键词大小写：lowercase
     * 缩进风格：2 spaces

  3. 输出：

```
select
  orders.order_id,
  customers.name,
  products.product_name
from
  orders
join
  customers on orders.customer_id = customers.customer_id
join
  order_items on orders.order_id = order_items.order_id
join
  products on order_items.product_id = products.product_id
where
  orders.order_date between '2024-01-01' and '2024-12-31';
```



通过以上使用文档，您应该能够熟练地使用这个 SQL 美化和格式化工具来优化您的 SQL 代码，提高代码的可读性和可维护性。