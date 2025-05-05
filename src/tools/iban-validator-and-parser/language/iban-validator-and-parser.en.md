# Online IBAN Validator and Parser User Guide

## 1. Tool Introduction
This is an online IBAN (International Bank Account Number) validator and parser. It can verify and analyze IBAN codes to check their validity and provide relevant information.

## 2. Functional Description

### IBAN Validation
- **Input IBAN Code**: Enter the IBAN code to be validated in the input box. Ensure the code is accurate and complete.
- **Validation Result**:
    - **Valid IBAN**: If the IBAN is valid, the tool will display a success message and provide the following parsed information:
        - **Country**: Shows the country to which the IBAN belongs.
        - **BBAN**: Displays the Basic Bank Account Number (BBAN), which is crucial for bank account identification.
        - **QR-IBAN Check**: Indicates whether it is a QR-IBAN, which is often used in scenarios like QR code payments.
        - **IBAN Friendly Format**: Converts the IBAN code into a more readable friendly format, usually with spaces added every four digits.
    - **Invalid IBAN**: If the IBAN is invalid, the tool will display a failure message, indicating that the code has issues and cannot pass the validation.

### IBAN Parsing
When the input IBAN code is valid, the tool automatically parses the following detailed information:
- **Country**: Determines the country associated with the IBAN, which is important for international transactions and fund flows.
- **BBAN (Basic Bank Account Number)**: Provides the core identifier for bank account identification, crucial for completing transactions and fund settlements.
- **QR-IBAN Check**: Identifies whether the IBAN is a QR-IBAN, helping users understand if it meets specific payment scenario requirements, such as QR code payments.
- **IBAN Friendly Format**: Converts the IBAN code into a more readable format for easier viewing and use.

### Examples for Reference
The tool offers some valid IBAN examples for users to understand the correct IBAN format. Here are some examples:
- **FR76 3000 6000 0112 3456 7890 189**: A French IBAN example with country code “FR”, BBAN “30006000011234567890189”, and it is not a QR-IBAN.
- **DE89 3704 0044 0532 0130 00**: A German IBAN example with country code “DE”, BBAN “370400440532013000”, and it is not a QR-IBAN.
- **GB29 NWBK 6016 1331 9268 19**: A British IBAN example with country code “GB”, BBAN “NWBK60161331926819”, and it is not a QR-IBAN.

Users can click the copy button next to the examples to copy the IBAN code to the input box for quick validation and parsing.

## 3. Usage Steps
1. Open the online IBAN Validator and Parser page.
2. Enter the IBAN code to be validated in the input box.
3. Click the “Check for validity” button (or press the Enter key) to perform the validation.
4. View the validation result. If valid, further parse the country, BBAN, and other detailed information; if invalid, check and correct the IBAN code based on the prompt.
5. If you need to refer to examples, check the valid IBAN examples provided on the page and click the copy button to copy the example to the input box for operation.

## 4. Precautions
1. **Input Accuracy**: Ensure the entered IBAN code is accurate. Any character error may lead to validation failure. Double-check the code or consult the relevant financial institution if uncertain.
2. **Internet Connection Requirement**: The tool is online and requires a stable internet connection. Without it, validation and parsing operations cannot be performed.
3. **Privacy and Security**: When using the tool, ensure that the entered IBAN information does not involve sensitive or confidential personal or business financial information to avoid potential risks of information leakage. Although the tool usually handles data securely, exercise caution when inputting and transmitting sensitive information over the internet.