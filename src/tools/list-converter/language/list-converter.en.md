### A Toolio - List Converter User Documentation

#### 1. Overview
The online List Converter is a powerful web-based tool designed to process array-based data. It allows users to apply various transformations to each row of data, including transposition, adding prefixes and suffixes, reversing lists, sorting lists, converting to lowercase, and truncating values.

#### 2. Feature Description

1. **Basic Data Processing Features**
   - **Trimming Items**: Removes extra whitespace characters from list items to keep the data clean.
   - **Removing Duplicates**: Automatically identifies and deletes duplicate list items to ensure data uniqueness.
   - **Keeping Line Breaks**: Allows you to retain line breaks during data processing, which is useful for maintaining specific formats.

2. **Data Sorting and Organization Features**
   - **Sorting Lists**: Provides multiple sorting methods such as alphabetical sorting to help users quickly organize data.
   - **Transpose Function**: Supports swapping rows and columns to meet special data structure conversion needs.

3. **Data Formatting Features**
   - **Adding Prefixes and Suffixes**: Enables you to add a specified prefix before each list item or a suffix after each item for uniform data formatting.
   - **Lowercase Conversion**: Converts all list items to lowercase to ensure uniform data format.
   - **Truncating Values**: Allows you to truncate each list item to control the length of the data.

4. **Custom Configuration Features**
   - **Delimiter Settings**: Allows users to define their own delimiters for data lists to accommodate various data formats.
   - **List Wrapping**: You can choose to add prefixes and suffixes to the entire list to enhance data readability and standardization.

#### 3. Usage Instructions

1. **Data Input**
   - Enter or paste the array data to be processed in the "Your input data" section.
   - Ensure the data format is correct and meets the tool's processing requirements.

2. **Feature Selection and Configuration**
   - Enable or disable toggle switches according to your needs, such as "Trim list items" and "Remove duplicates."
   - Fill in the configuration parameters in the relevant input fields, such as delimiters, prefixes, and suffixes.

3. **Data Processing and Output**
   - Click the processing button (if applicable), and the tool will automatically process the data based on the settings.
   - View the processed data results in the "Your transformed data" section.

#### 4. Common Use Cases

- **Data Cleaning**: When processing raw data, use features like deduplication and trimming to improve data quality.
- **Format Unification**: When generating configuration files or making requests, ensure data format consistency through operations like adding prefixes/suffixes and lowercase conversion.
- **Data Organization**: Before data analysis, use features like sorting and transposing to preliminarily organize data for easier subsequent processing.

#### 5. Notes

- Ensure the input data complies with the tool's processing logic to avoid processing anomalies due to formatting issues.
- Be mindful of web performance and processing limitations when handling large amounts of data.
- If you have special requirements or the tool's features are insufficient, try adjusting the tool's settings or combine it with other tools.

#### 6. Example Operations

1. **Deduplication and Sorting Example**
   - Input Data:`apple, orange, banana, apple`
   - Enable "Remove duplicates" and select "Sort alphabetically" in "Sort list."
   - Output Data:`apple, banana, orange`

2. **Adding Prefixes and Suffixes Example**
   - Input Data:`item1, item2, item3`
   - Set "Item prefix" to `ID:` and "Item suffix" to `-done`.
   - Output Data:`ID:item1-done, ID:item2-done, ID:item3-done`

3. **Keeping Line Breaks Example**
   - Input Data:`line1\nline2\nline3` (with line breaks)
   - Enable "Keep line breaks."
   - Output Data:`line1\nline2\nline3` (line breaks retained)

By following these features and steps, users can efficiently process array data to meet various data transformation needs.