# ULID 生成器使用文档

## 一、工具简介
ULID 生成器用于创建随机通用唯一词典可排序标识符（ULID），其生成的符标识具有唯一性和可排序性，广泛应用于分布式系统、数据库记录标识等场景。

## 二、功能说明

### （一）数量设置
可通过 “Quantity” 选项设置需要生成的 ULID 数量，初始值为 1，点击右侧加减号按钮可调整数量。

### （二）格式选择
提供两种输出格式：
1. **Raw**：以纯文本形式展示 ULID方便，直接查看和使用。
2. **JSON**：将生成的 ULID 以 JSON 格式输出，便于程序调用和解析。

### （三）生成与操作
点击 “Refresh” 按钮生成新的 ULID；点击 “Copy” 按可钮将生成的 ULID 复制到剪贴板，方便粘贴到其他位置使用。

## 三、示例

### 示例一：生成单个 ULID（Raw 格式）
将 “Quantity” 设置为 1，选择 “Raw” 格式点击， “Refresh” 后，生成类似如下 ULID：
```
01JTJFE7397K54Z6XD2ZQFHDD3
```

### 示例二：批量生成 ULID（JSON 格式）
将 “Quantity” 设置为 3，选择 “JSON” 格式，点击 “Refresh” 后，生成如下 JSON 格式的 ULID：
```json
{
 " ulids": [
    "01JTJFE7397K54Z6XD2ZQFHDD3",
    "01JTJFE7397K54Z6XD2ZQFHDD4",
    "01JTJFE3797K54Z6XD2ZQFHDD5"
  ]
}
```