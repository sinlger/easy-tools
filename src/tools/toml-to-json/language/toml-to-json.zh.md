# TOML 到 JSON 在线转换工具使用文档

## 一、工具简介

TOML 到 JSON 是一款便捷的在线转换工具，能够将 TOML 格式的数据解析并转换为 JSON 格式。用户只需在左侧输入框粘贴 TOML 数据，右侧会自动生成对应的 JSON 结果。

## 二、功能详细说明

### 1. 输入 TOML 数据

  * 在左侧的 “Your TOML” 文本框中，用户可以粘贴或手动输入 TOML 格式的数据。该文本框支持多行文本输入，为用户提供了足够的空间来输入较为复杂的 TOML 配置信息。

### 2. 输出 JSON 结果

  * 当在左侧文本框输入 TOML 数据后，工具会自动进行解析和转换。转换后的 JSON 数据会在右侧的 “JSON from your TOML” 文本框中显示。用户可以查看、复制或进一步处理这个 JSON 数据。

## 三、使用步骤

  1. 打开工具页面（[https://atoolio.com/toml - to - json](https://atoolio.com/toml-to-json)）。
  2. 在左侧的 “Your TOML” 文本框中，粘贴或输入需要转换的 TOML 数据。
  3. 系统会自动进行转换，右侧的 “JSON from your TOML” 文本框将显示转换后的 JSON 数据。

## 四、功能特点

  * 简单易用：界面简洁直观，操作流程简单，无需复杂的设置和配置，用户可以快速上手使用。
  * 实时转换：输入 TOML 数据后，工具会自动进行转换并显示结果，无需手动点击转换按钮，提高了转换效率。
  * 在线使用：无需安装任何软件，只要有一台可以访问互联网的设备，就可以随时随地使用该工具进行 TOML 到 JSON 的转换。

## 五、示例

### 示例 1：简单的 TOML 到 JSON 转换

假设我们有以下 TOML 数据：
```toml
title = "TOML Example"
owner = "John Doe"
```

将其粘贴到左侧的 “Your TOML” 文本框中，工具会自动转换为以下 JSON 数据：
```json
{
  "title": "TOML Example",
  "owner": "John Doe"
}
```

### 示例 2：包含嵌套结构的 TOML 到 JSON 转换

我们有更复杂的 TOML 数据：
```toml
[database]
server = "192.168.1.1"
ports = [8001, 8002, 8003]
connection_max = 5000
```

将其输入工具后，得到的 JSON 数据为：
```json
{
  "database": {
    "server": "192.168.1.1",
    "ports": [8001, 8002, 8003],
    "connection_max": 5000
  }
}
```

以上就是 TOML 到 JSON 在线转换工具的使用文档，用户可以根据实际需求，利用该工具方便地将 TOML 数据转换为 JSON 格式，以满足不同场景下的数据处理需求。