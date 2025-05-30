# 在线设备信息功能介绍

## 概述

在线设备信息工具可获取当前设备的详细信息，包括屏幕、设备等多方面数据，旨在帮助开发者了解设备特性，辅助网页布局设计及调试工作。

## 屏幕信息

  1. **屏幕大小** ：以像素为单位显示屏幕的宽度和高度，如 2560x1392 像素，为网页布局设计提供参考，确保页面元素在不同屏幕尺寸下合理展示。
  2. **方向** ：明确屏幕是处于 landscape-primary（横屏 - 主方向）还是 portrait-primary（竖屏 - 主方向）等状态，有助于针对不同设备方向优化页面显示效果。
  3. **方向角度** ：指示屏幕相对于竖直方向的旋转角度，例如 0° 表示屏幕未旋转，可作为设计响应式布局时的参考依据。
  4. **色深** ：展示屏幕支持的色彩深度，如 24 位色，色深越高，屏幕能呈现的颜色种类越多，对图像和视频显示质量有直接影响。
  5. **像素比率** ：反映设备物理像素与 CSS 像素的比例关系，1 dppx 表示设备的物理像素与 CSS 像素一一对应，对高清图片显示及页面渲染精度有重要意义。
  6. **窗口大小** ：呈现当前浏览器窗口的宽度和高度，如 1865x1316 像素，为自适应网页设计提供实时的窗口尺寸数据。

## 设备信息

  1. **浏览器供应商** ：明确当前使用的浏览器是由哪家公司开发，如 Google Inc.，方便开发者根据不同浏览器特性进行兼容性处理。
  2. **语言** ：列出设备上配置的语言，如 zh-CN, en, en-GB, en-US，帮助开发者按语言偏好定制内容，实现多语言网站的功能。
  3. **平台** ：显示设备的操作系统平台，如 Win32，助力开发者针对不同操作系统优化网页表现及功能。
  4. **用户代理** ：提供浏览器的用户代理字符串，详细信息包含浏览器名称、版本及兼容性标识等，是开发者进行浏览器版本检测和功能适配的重要依据。