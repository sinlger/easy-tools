# A Toolio - JWT 解析器使用文档

## 一、工具简介

A Toolio - JWT 解析器是一个便捷的在线工具，能够解析和解码 JSON Web Token（JWT），并清晰地展示其内容。它为开发者提供了一种快速查看 JWT 细节的方式，方便进行调试、验证和学习。

## 二、功能 说明

### （一）输入功能

  * **JWT 输入框** ：用户可以将需要解析的 JWT 粘贴到该输入框中。输入框的容量大，能够容纳各种长度的 JWT，为用户提供了灵活的输入方式。

### （二）解析功能

  * **Header 解析** ：能够准确解析 JWT 的头部信息，包括以下字段：
    * **alg（Algorithm）** ：显示 JWT 使用的加密算法，如 HS256 表示使用 HMAC 算法和 SHA-256 摘要算法。
    * **typ（Type）** ：显示 JWT 的类型，通常为 JWT。

  * **Payload 解析** ：可以详细解析 JWT 的负载部分，展示其中包含的各种声明信息，例如：
    * **sub（Subject）** ：标识该 JWT 所面向的用户或主体。
    * **name（Full name）** ：显示用户的全名。
    * **iat（Issued At）** ：标识该 JWT 被签发的时间，通常以时间戳形式显示，并可转换为具体日期时间格式。

### （三）展示功能

  * **结构化展示** ：将解析后的 JWT 内容以清晰的结构化表格形式展示，方便用户快速查看和理解每个字段的含义和值，使信息呈现更加直观和易读。

## 三、使用步骤

  1. **访问网址** ：通过浏览器访问 [https://atoolio.com/jwt-parser](https://atoolio.com/jwt-parser)，打开 JWT 解析器页面。
  2. **输入 JWT** ：将待解析的 JWT 粘贴到输入框中。
  3. **点击解析** ：点击解析按钮（通常为 “JWT to decode” 旁边的按钮，具体以页面实际显示为准），系统将自动对输入的 JWT 进行解析。
  4. **查看结果** ：在下方的展示区域查看解析后的 Header 和 Payload 信息，了解 JWT 的详细内容。

## 四、注意事项

  * 请确保输入的 JWT 格式正确，否则可能导致解析失败或结果不准确。
  * 该工具仅用于解析和查看 JWT 的内容，不保证对所有类型的 JWT 都能完全正确解析，尤其是使用特殊加密算法或非标准格式的 JWT。
  * 在使用过程中，若遇到问题或需求，可以联系网站提供的相关支持渠道（如 “Buy me a coffee” 可能暗示可通过该方式联系开发者获取进一步帮助）。

以上是 A Toolio - JWT 解析器的使用文档，旨在帮助用户更好地理解和使用该工具，从而高效地处理与 JWT 相关的任务。