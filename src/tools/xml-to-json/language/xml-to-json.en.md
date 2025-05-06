# XML to JSON Converter Tool Documentation

## 1. Introduction
This is an online XML to JSON conversion tool that can transform XML - formatted data into JSON format. It enhances development efficiency and is suitable for scenarios where data format conversion between XML and JSON is required.

## 2. Main Functions

### (1) XML Content Input
Paste or write the XML data you want to convert in the input area. For example, you can input the following XML content:
```
<a x="1.234" y="It's"/>
```

### (2) JSON Data Output
After clicking the conversion button, the tool will display the corresponding JSON - formatted data in the output area. For instance, the above XML will be converted into the following JSON data:
```json
{
  "a": {
    "_attributes": {
      "x": "1.234",
      "y": "It's"
    }
  }
}
```

### (3) Copy Function
In the JSON data output area, you can click the copy button to copy the generated JSON data to the clipboard, making it easy to paste and use elsewhere.

## 3. Use Cases
It is suitable for various scenarios where XML data needs to be converted into JSON format during the development process, such as interface data conversion, data interaction between different systems, and data format standardization. It allows for quick and easy format conversion.