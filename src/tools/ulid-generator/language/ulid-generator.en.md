# ULID Generator User Manual

## 1. Introduction
The ULID Generator creates random Universally Unique Lexicographically Sortable Identifiers (ULID). These identifiers are unique and sortable, making them useful in distributed systems and database records.

## 2. Features

### (1) Quantity Setting
Set the number of ULIDs to generate via the “Quantity” option. The initial value is 1, and you can adjust the number using the increment/decrement buttons on the right.

### (2) Format Selection
Two output formats are available:
1. **Raw**: Displays ULIDs in plain text for easy viewing and use.
2. **JSON**: Outputs ULIDs in JSON format for program calls and parsing.

### (3) Generation and Operations
Click the “Refresh” button to generate new ULIDs. Click the “Copy” button to copy the generated ULID to the clipboard for use in other applications.

## 3. Examples

### Example 1: Generating a Single ULID (Raw Format)
Set “Quantity” to 1, select “Raw” format, and click “Refresh”. A ULID like the following will be generated:
```
01JTJFE7397K54Z6XD2ZQFHDD3
```

### Example 2: Batch Generating ULIDs (JSON Format)
Set “Quantity” to 3, select “JSON” format, and click “Refresh”. ULIDs in JSON format will be generated as follows:
```json
{
  "ulids": [
    "01JTJFE7397K54Z6XD2ZQFHDD3",
    "01JTJFE7397K54Z6XD2ZQFHDD4",
    "01JTJFE3797K54Z6XD2ZQFHDD5"
  ]
}
```