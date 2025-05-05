# Docker Run 到 docker - compose 转换器使用文档

## 一、工具简介

Docker Run 到 docker - compose 转换器是一款便捷的在线工具，旨在帮助开发者将 docker run 命令行快速转换为 docker - compose 文件，简化容器编排配置流程，提高开发效率。

## 二、主要功能

  1. **命令转换**

     * 用户可将复杂的 docker run 命令粘贴到指定输入框中，例如 “docker run -p 80:80 -v /var/run/docker.sock:/tmp/docker.sock:ro --restart always --log-opt max - size=1g nginx”。
     * 工具会自动解析命令中的各项参数，如端口映射（-p 80:80）、卷挂载（-v /var/run/docker.sock:/tmp/docker.sock:ro）、重启策略（--restart always）、日志选项（--log-opt max - size=1g）以及镜像名称（nginx）等。

  2. **生成 docker - compose 文件内容**

     * 基于解析后的 docker run 命令参数，生成对应的 docker - compose 文件内容。
     * 生成的 yaml 格式文件包含版本声明（如 version: '3.9'）、服务定义（services）、镜像指定（image）、日志配置（logging 及其 options）、重启策略（restart）、卷挂载（volumes）以及端口映射（ports）等关键配置项，完整呈现容器的编排信息，方便用户直接使用或进一步修改。

  3. **文件下载**

     * 提供 “Download docker - compose.yml” 按钮，用户可一键将生成的 docker - compose 文件内容下载到本地，便于在实际项目环境中应用和管理容器服务。

## 三、使用场景

适用于开发者在 Docker 项目开发过程中，当需要将单个容器的运行配置转换为多容器编排的 docker - compose 配置文件时，能够快速完成转换，减少手动编写 yaml 文件可能出现的错误，提升开发和部署效率，尤其在构建复杂的微服务架构或分布式应用系统时，可有效简化容器编排的初始配置工作。