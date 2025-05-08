# TOML to JSON Online Converter Tool User Documentation

## 1. Tool Introduction

TOML to JSON is a convenient online conversion tool that can parse TOML - formatted data and convert it to JSON format. Users simply need to paste TOML data into the left - hand text box, and the corresponding JSON result will be automatically generated on the right.

## 2. Function Details

### 1. Input TOML Data

  * In the "Your TOML" text box on the left, users can paste or manually enter data in TOML format. The text box supports multi - line text input, providing ample space for users to input complex TOML configuration information.

### 2. Output JSON Result

  * Once TOML data is entered in the left - hand text box, the tool will automatically parse and convert it. The resulting JSON data will be displayed in the "JSON from your TOML" text box on the right. Users can view, copy, or further process this JSON data.

## 3. Steps to Use

  1. Open the tool page ([https://atoolio.com/toml - to - json](https://atoolio.com/toml-to-json)).
  2. In the "Your TOML" text box on the left, paste or enter the TOML data you want to convert.
  3. The system will automatically convert the data, and the "JSON from your TOML" text box on the right will display the converted JSON data.

## 4. Features

  * User - friendly: The interface is clean and intuitive, with a simple workflow that requires no complex settings or configurations. This enables users to quickly get started.
  * Real - time conversion: After entering TOML data, the tool automatically converts it and displays the result without the need to manually click a conversion button, thereby improving conversion efficiency.
  * Online usage: There is no need to install any software. As long as you have a device with internet access, you can use this tool anytime, anywhere to convert TOML data to JSON.

## 5. Examples

### Example 1: Simple TOML to JSON Conversion

Assume we have the following TOML data:
```toml
title = "TOML Example"
owner = "John Doe"
```

After pasting it into the "Your TOML" text box on the left, the tool automatically converts it to the following JSON data:
```json
{
  "title": "TOML Example",
  "owner": "John Doe"
}
```

### Example 2: TOML to JSON Conversion with Nested Structures

We have more complex TOML data:
```toml
[database]
server = "192.168.1.1"
ports = [8001, 8002, 8003]
connection_max = 5000
```

After inputting this into the tool, the resulting JSON data is:
```json
{
  "database": {
    "server": "192.168.1.1",
    "ports": [8001, 8002, 8003],
    "connection_max": 5000
  }
}
```

The above is the user documentation for the TOML to JSON online conversion tool. Users can conveniently convert TOML data to JSON format using this tool according to their actual needs, meeting data processing requirements in various scenarios.