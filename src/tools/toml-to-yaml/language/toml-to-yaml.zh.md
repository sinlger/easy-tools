# TOML 到 YAML 转换工具使用文档

## 概述

TOML 到 YAML 是一个在线工具，允许用户轻松地将 TOML（Tom's Obvious, Minimal Language）格式的配置文件转换为 YAML（YAML Ain't Markup Language）格式。这对于需要在不同系统间迁移配置或整合多种技术栈的开发者来说尤其有用。

## 界面布局

该工具的界面设计简洁直观，主要分为以下几个部分：

1. 左侧的文本框：这是用户输入或粘贴 TOML 格式文本的区域，标记为 “Your TOML”。
2. 右侧的文本框：用于显示转换后的 YAML 格式文本，标记为 “YAML from your TOML”。
3. 中间的转换按钮：用户在输入 TOML 文本后，可以点击这个按钮来执行转换操作。

## 功能描述

### 输入 TOML 文本

- 用户可以在左侧的文本框中直接输入 TOML 格式的配置内容。
- 也可以从其他文件或编辑器中复制 TOML 文本，然后粘贴到该文本框中。

### 转换操作

- 在输入或粘贴 TOML 文本后，点击界面中间的转换按钮。系统会立即对输入的 TOML 文本进行解析，并将其转换为 YAML 格式。
- 转换完成后，转换后的 YAML 文本会显示在右侧的文本框中。

### 查看 YAML 输出结果

- 右侧的文本框会完整显示转换后的 YAML 格式文本。
- 用户可以在这里查看转换结果是否准确，以及 YAML 文本的结构是否符合预期。

### 复制 YAML 文本

- 用户可以将右侧文本框中的 YAML 文本全选并复制，方便在其他地方使用，如粘贴到配置文件或发送给他人。

## 示例

### 示例 1：基本转换

**TOML 输入：**

```toml
# 这是一个简单的 TOML 示例
title = "TOML 示例"

[author]
name = "张三"
age = 28
email = "zhangsan@example.com"
```

**YAML 输出：**

```yaml
# 这是转换后的 YAML 示例
title: TOML 示例

author:
  name: 张三
  age: 28
  email: zhangsan@example.com
```

### 示例 2：复杂结构转换

**TOML 输入：**

```toml
# 复杂结构的 TOML 示例
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

**YAML 输出：**

```yaml
# 复杂结构的 YAML 示例
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

## 注意事项

- 当输入的 TOML 格式不正确时，转换可能会失败，系统可能会显示错误提示信息。
- 该工具支持大多数常见的 TOML 语法结构，但对于一些特殊的或不常用的语法，可能无法完美转换。
- 输出的 YAML 文本可能会根据不同的 YAML 版本和规范，存在一些微小的格式差异。