# TOMLからYAMLへの変換ツール　使用ドキュメント

## 概要

TOMLからYAMLへは、ユーザーが簡単にTOML（Tom's Obvious, Minimal Language）形式の設定ファイルをYAML（YAML Ain't Markup Language）形式に変換できるオンラインツールです。これは、異なるシステム間で設定を移行したり、複数の技術スタックを統合したい開発者にとって特に便利です。

## インターフェースレイアウト

このツールのインターフェースはシンプルで直感的な設計になっており、主に以下の部分から構成されています：

1. 左側のテキストボックス：ユーザーがTOML形式のテキストを入力または貼り付けることができる領域で、「Your TOML」とラベル付けられています。
2. 右側のテキストボックス：変換後のYAML形式のテキストを表示するために使われ、「YAML from your TOML」とラベル付けられています。
3. 中央の変換ボタン：ユーザーはTOMLテキストを入力した後、このボタンをクリックして変換操作を行います。

## 機能説明

### TOMLテキストの入力

- ユーザーは左側のテキストボックスに直接TOML形式の設定内容を入力できます。
- 他のファイルやエディターからTOMLテキストをコピーし、このテキストボックスに貼り付けることもできます。

### 変換操作

- 入力または貼り付けたTOMLテキストの後、中央の変換ボタンをクリックします。システムは即座に入力されたTOMLテキストを解析し、YAML形式に変換します。
- 変換が完了すると、変換後のYAMLテキストが右側のテキストボックスに表示されます。

### YAML出力結果の確認

- 右側のテキストボックスには変換後のYAMLテキストが完全に表示されます。
- ユーザーはここで変換結果が正確であるか、およびYAMLテキストの構造が予想通りであるかを確認できます。

### YAMLテキストのコピー

- ユーザーは右側のテキストボックス内のYAMLテキストを全選択してコピーでき、これを他の場所で使用するのに便利です。

## 例

### 例1：基本的な変換

**TOML入力：**

```toml
# これは簡単なTOMLの例です
title = "TOMLの例"

[author]
name = "張三"
age = 28
email = "zhangsan@example.com"
```

**YAML出力：**

```yaml
# これは変換後のYAMLの例です
title: TOMLの例

author:
  name: 張三
  age: 28
  email: zhangsan@example.com
```

### 例2：複雑な構造の変換

**TOML入力：**

```toml
# 複雑な構造を持つTOMLの例
database:
  host = "localhost"
  port = 3306
  user = "admin"
  password = "securepassword"

[features]
logging = true
debug = false

[[servers]]
name = "main-server"
port = 8080

[[servers]]
name = "secondary-server"
port = 8081
```

**YAML出力：**

```yaml
# 複雑な構造を持つYAMLの例
database:
  host: localhost
  port: 3306
  user: admin
  password: securepassword

features:
  logging: true
  debug: false

servers:
  - name: main-server
    port: 8080
  - name: secondary-server
    port: 8081
```

## 注意事項

- 入力されたTOMLのフォーマットが正しくない場合、変換に失敗し、システムがエラーメッセージを表示する可能性があります。
- このツールはほとんどの一般的なTOML構文構造をサポートしていますが、特殊またはあまり使われない構文については完全な変換が不可能な場合があります。
- 出力されるYAMLテキストは、使用されるYAMLのバージョンや仕様によって、わずかなフォーマットの違いが生じることがあります。