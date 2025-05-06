# TOML to YAML Converter Tool User Guide

## Overview

The TOML to YAML converter is an online tool that enables users to effortlessly convert TOML (Tom's Obvious, Minimal Language) formatted configuration files into YAML (YAML Ain't Markup Language) format. This is particularly beneficial for developers who need to transfer configurations between different systems or integrate various technology stacks.

## Interface Layout

The tool features a clean and intuitive interface, consisting of the following main sections:

1. Left Text Box: This is where users can input or paste TOML-formatted text, labeled as "Your TOML".
2. Right Text Box: This displays the converted YAML-formatted text, labeled as "YAML from your TOML".
3. Conversion Button: Located in the middle of the interface, users can click this button to initiate the conversion process after entering TOML text.

## Feature Description

### Input TOML Text

- Users can directly input TOML-formatted configuration content into the left text box.
- Alternatively, they can copy TOML text from other files or editors and paste it into this text box.

### Conversion Operation

- After entering or pasting TOML text, click the conversion button in the middle. The system will immediately parse the input TOML text and convert it into YAML format.
- Once the conversion is complete, the resulting YAML text will be displayed in the right text box.

### View YAML Output Result

- The right text box will fully display the converted YAML-formatted text.
- Users can review the conversion result here to ensure its accuracy and that the YAML text structure meets their expectations.

### Copy YAML Text

- Users can select and copy the YAML text from the right text box, making it convenient for use elsewhere, such as pasting into configuration files or sharing with others.

## Examples

### Example 1: Basic Conversion

**TOML Input:**

```toml
# This is a simple TOML example
title = "TOML Example"

[author]
name = "Zhang San"
age = 28
email = "zhangsan@example.com"
```

**YAML Output:**

```yaml
# This is the converted YAML example
title: TOML Example

author:
  name: Zhang San
  age: 28
  email: zhangsan@example.com
```

### Example 2: Complex Structure Conversion

**TOML Input:**

```toml
# TOML example with complex structure
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

**YAML Output:**

```yaml
# YAML example with complex structure
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

## Notes

- If the input TOML format is incorrect, the conversion may fail, and the system may display an error message.
- The tool supports most common TOML syntax structures, but may not perfectly convert some special or less commonly used syntax.
- The output YAML text may exhibit minor formatting differences depending on the YAML version and specifications.