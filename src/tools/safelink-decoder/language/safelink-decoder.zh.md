# Outlook Safelink 解码器使用文档

## 一、工具简介
Outlook Safelink 解码器是一款用于解码微软 Outlook 邮件服务中的 SafeLink 链接的工具。它能够将经过 SafeLink 处理的链接还原为原始 URL，方便用户查看链接的真实指向。

## 二、功能介绍
该工具的主要功能是解码 Outlook SafeLink 链接，即将微软 Outlook 为保护用户安全而生成的加密、重定向式的链接还原为原始网络地址。

## 三、使用方法

### 输入
在输入框中粘贴您想要解码的 Outlook SafeLink 链接。该链接通常是微软 Outlook 为了安全考虑而对原始链接进行加密处理后生成的，具有特定的格式。

### 输出
点击“Decode”按钮后，工具会处理您输入的链接并在输出框中显示解码后的原始 URL。如果输入的链接格式不正确或无法识别，将显示“Error: Invalid SafeLinks URL provided”的错误提示信息。

## 四、使用示例

### 示例 1
输入 SafeLink：
`https://nam02.safelinks.protection.outlook.com/?url=https%3A%2F%2Fexample.com&data=...`（省略部分内容）
解码后输出：
`https://example.com`

### 示例 2
输入 SafeLink：
`https://nam02.safelinks.protection.outlook.com/?url=https%3A%2F%2Fmicrosoft.com&data=...`（省略部分内容）
解码后输出：
`https://microsoft.com`

### 示例 3
输入一个无效或格式错误的链接，如：
`https://nam02.safelinks.protection.outlook.com/?url=invalidurl&data=...`
将显示错误信息：
`Error: Invalid SafeLinks URL provided`

## 五、注意事项
- 确保输入的链接是完整的 Outlook SafeLink 链接。