# A Toolio 在线加密/解密工具使用文档

## 功能概述

A Toolio 提供的在线加密/解密工具，支持使用多种加密算法（如 AES、TripleDES、Rabbit 或 RC4）对文本进行加密和解密操作。用户可以方便地加密明文或解密密文，满足日常开发或学习中的加密需求。

## 加密功能

  1. **明文输入** ：在 “Encrypt”（加密）区域的 “Your text”（文本您的）输入框中，输入需要加密的明文内容。例如输入 “Lorem ipsum dolor sit amet”。
  2. **设置密钥** ：在 “Your secret key”（您的密钥）输入框中，设置一个用于加密的密钥，如 “my secret key”。密钥是加密过程中不可或缺的重要参数，务必妥善保管。
  3. **选择加密算法** ：通过 “Encryption algorithm”（加密算法）下拉菜单，选择合适的加密算法，如 AES、TripleDES、Rabbit 或 RC4。不同算法具有不同的安全性和性能特点，可根据实际需求选择。
  4. **查看加密结果** ：完成上述设置后，工具会自动在 “Your text encrypted”（您的加密文本）区域显示加密后的密文，如 “U2FsdGVkX19wCAAvFjYehC+Haqkp3/xRGF4yN17gt6/FgnlHRvikeCuOvDyAIBvG”。

## 解密功能

  1. **密文输入** ：在 “Decrypt”（解密）区域的 “Your encrypted text”（您的加密文本）输入框中，输入需要解密的密文内容，如 “U2FsdGVkX1/EC3+6P5dbbkZ3e1kQ5o2yzuU0NHTjmrKnLBEwreV489Kr0DIB+uBs”。
  2. **输入密钥** ：在 “Your secret key”（您的密钥）输入框中，输入与加密时相同的密钥 “my secret key”。正确的密钥是成功解密的关键。
  3. **选择加密算法** ：通过 “Encryption algorithm”（加密算法）下拉菜单，选择与加密时一致的算法，例如 AES。
  4. **查看解密结果** ：工具会在 “Your decrypted text”（您的解密文本）区域显示解密后的明文，如 “Lorem ipsum dolor sit amet”。

## 其他注意事项

  * **安全性** ：虽然该工具方便快捷，但处理敏感信息时，建议在安全的网络环境下使用，并确保密钥的安全性，避免泄露。
  * **算法选择** ：不同的加密算法适用于不同的场景，AES 是目前较为广泛使用且安全可靠的加密算法之一；TripleDES 相对较老但仍在某些系统中使用；Rabbit 和 RC4 也有各自的特点和适用范围，用户可根据实际需求和安全性要求进行选择。