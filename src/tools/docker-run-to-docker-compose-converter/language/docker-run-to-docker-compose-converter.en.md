# Docker Run to docker-compose Converter User Guide

## 1. Tool Introduction

The Docker Run to docker-compose Converter is a handy online tool designed to help developers swiftly transform docker run commands into docker-compose files. It simplifies container orchestration configuration and boosts development efficiency.

## 2. Key Features

  1. **Command Conversion**

     * Users can paste complex docker run commands into the input box, such as “docker run -p 80:80 -v /var/run/docker.sock:/tmp/docker.sock:ro --restart always --log-opt max - size=1g nginx”.
     * The tool automatically parses the parameters in the command, including port mapping (-p 80:80), volume mounting (-v /var/run/docker.sock:/tmp/docker.sock:ro), restart policy (--restart always), log options (--log-opt max - size=1g), and image name (nginx).

  2. **Generating docker-compose File Content**

     * Based on the parsed docker run command parameters, it generates the corresponding docker-compose file content.
     * The generated yaml - formatted file includes version declaration (e.g., version: '3.9'), service definition (services), image specification (image), log configuration (logging and its options), restart policy (restart), volume mounting (volumes), and port mapping (ports), providing a comprehensive container orchestration configuration for users to use directly or modify further.

  3. **File Download**

     * The “Download docker - compose.yml” button allows users to download the generated docker-compose file content to their local environment for easy application and management of container services.

## 3. Use Cases

This tool is ideal for developers working on Docker projects. When they need to convert the configuration of a single - container run command into a multi - container docker - compose configuration file, it enables quick conversion, reducing the likelihood of errors from manual yaml file creation. It’s especially useful in building complex microservices architectures or distributed systems, where it can significantly simplify the initial container orchestration setup.