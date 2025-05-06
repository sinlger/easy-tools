# SQL Prettify and Formatting Tool User Manual

## I. Tool Introduction

SQL Prettify and Formatting Tool is an online platform used to format and beautify SQL query statements. It supports various SQL dialects and helps developers read and write SQL code more clearly.

## II. Feature Description

### (a) Basic Features

1. **SQL Prettifying**: Converts messy SQL query statements into a well - formatted and readable version. For example:
   * Original query:

```
select field1,field2,field3 from my_table where my_condition;
```

   * Prettified:

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



### (b) Configuration Options

1. **Dialect Selection**: Provides multiple SQL dialect options such as Standard SQL, MySQL, PostgreSQL, SQL Server, etc. Choosing a suitable dialect ensures the formatted SQL statement complies with specific database syntax.
2. **Keyword Case Settings**: Allows conversion of SQL keywords to UPPERCASE, lowercase, or Capitalized to unify the code style. For example:
   * Original query:

```
select * from table;
```

   * With keywords in uppercase:

```
SELECT * FROM table;
```

   * With keywords in lowercase:

```
select * from table;
```

   * With keywords capitalized:

```
Select * From table;
```



3. **Indentation Style Adjustment**: Offers options like Standard, 2 spaces, and 4 spaces to meet different code format preferences. For example:
   * Standard indentation:

```
SELECT
    field1,
    field2
FROM
    my_table
WHERE
    condition;
```

   * 2 - space indentation:

```
SELECT
  field1,
  field2
FROM
  my_table
WHERE
  condition;
```

   * 4 - space indentation:

```
SELECT
    field1,
    field2
FROM
    my_table
WHERE
    condition;
```



### (c) Input and Output

1. **Input Area**: Paste or enter the original SQL query statement to be prettified in the left - hand textbox.
2. **Output Area**: The right - hand textbox displays the formatted and prettified SQL statement in real - time. A copy button is available for users to copy the prettified SQL statement to the clipboard for use elsewhere.

## III. Steps to Use

1. Open the [SQL Prettify and Formatting Tool](https://it-tools.tech/sql-prettify) webpage.
2. Paste or enter your SQL query statement in the input area.
3. Select the appropriate options for dialect, keyword case, and indentation style according to your needs.
4. View the prettified SQL statement in the output area. If satisfied, click the copy button to copy it.

## IV. Examples

### Example 1: Simple Query Prettifying

1. Input:

```
select name, age from users where age > 25;
```

2. Settings:
   * Dialect: Standard SQL
   * Keyword case: UPPERCASE
   * Indentation style: Standard

3. Output:

```
SELECT
    name,
    age
FROM
    users
WHERE
    age > 25;
```



### Example 2: Complex Query Prettifying

1. Input:

```
select orders.order_id, customers.name, products.product_name from orders join customers on orders.customer_id = customers.customer_id join order_items on orders.order_id = order_items.order_id join products on order_items.product_id = products.product_id where orders.order_date between '2024-01-01' and '2024-12-31';
```

2. Settings:
   * Dialect: MySQL
   * Keyword case: lowercase
   * Indentation style: 2 spaces

3. Output:

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

With the above user manual, you should be able to skillfully use the SQL Prettify and Formatting Tool to optimize your SQL code and enhance its readability and maintainability.