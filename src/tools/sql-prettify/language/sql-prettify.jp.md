# SQL整形および美化工具 使用ドキュメント

## 1. ツール概要

SQL整形および美化工具は、オンライン上でSQLクエリをフォーマットし、見やすくするためのプラットフォームです。複数のSQL方言に対応しており、開発者がSQLコードを読みやすく・書きやすくするサポートを提供します。

## 2. 機能説明

### (1) **基本機能**

1. **SQLの美化（フォーマット）**：乱雑なSQLクエリを構造化され、理解しやすい形式に変換します。例：

* 元のクエリ：
```sql
select field1,field2,field3 from my_table where my_condition;
```

* 美化後：
```sql
SELECT
    field1,
    field2,
    field3
FROM
    my_table
WHERE
    my_condition;
```


### (2) **設定オプション**

1. **方言（Dialect）選択**：Standard SQL、MySQL、PostgreSQL、SQL Serverなど、さまざまなSQL方言が利用可能です。ご使用中のデータベースに合った方言を選択することで、フォーマットされたSQL文がその特定データベースの構文規則に準拠するようになります。
2. **キーワードの大小文字（Keyword case）**：SQLのキーワードを大文字（UPPERCASE）、小文字（lowercase）、または先頭のみ大文字（Capitalized）に変更できます。これによりコードスタイルを統一することが可能です。例：

* 元のクエリ：
```sql
select * from table;
```

* キーワードを大文字にした場合：
```sql
SELECT * FROM table;
```

* キーワードを小文字にした場合：
```sql
select * from table;
```

* キーワードを先頭だけ大文字にした場合：
```sql
Select * From table;
```


3. **インデントスタイル（Indent style）**：標準（Standard）、2つのスペース（2 spaces）、4つのスペース（4 spaces）などのインデントスタイルから選択可能です。これにより個人やチーム内のコードフォーマットの好みに合わせて調整できます。例：

* 標準のインデント：
```sql
SELECT
    field1,
    field2
FROM
    my_table
WHERE
    condition;
```

* 2つのスペースでインデント：
```sql
SELECT
  field1,
  field2
FROM
  my_table
WHERE
  condition;
```

* 4つのスペースでインデント：
```sql
SELECT
    field1,
    field2
FROM
    my_table
WHERE
    condition;
```


### (3) **入力と出力の領域**

1. **入力領域**：左側のテキストボックス内に整形したいSQLクエリをコピー＆ペーストしたり、直接入力することができます。
2. **出力領域**：右側のテキストボックスには整形および美化された結果がリアルタイムで表示されます。また、出力領域にはコピー用ボタンがあり、美化されたSQLクエリをクリップボードに保存して、他の場所でも簡単に使えるようにしています。

## 3. 利用手順

1. [SQL整形ツールのウェブサイト](https://atoolio.com/sql-prettify)を開きます。
2. 左側の入力領域にSQLクエリを貼り付けたり、直接入力します。
3. 必要に応じて「方言」、「キーワードの大小文字」、「インデントスタイル」のドロップダウンメニューから適切なオプションを選択します。
4. 右側の出力領域に表示される整形済みのSQL文を確認します。内容に満足したら、コピー用ボタンをクリックしてクリップボードに保存します。