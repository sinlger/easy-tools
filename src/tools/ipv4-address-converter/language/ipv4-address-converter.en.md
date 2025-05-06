# IPv4 Address Converter User Guide

## 1. Tool Introduction
The IPv4 Address Converter is an online tool that converts IPv4 addresses into various numeral systems and IPv6 formats. It is designed to assist developers and network professionals in obtaining different representations of IPv4 addresses, which can be useful for network configuration, programming, and security analysis.

## 2. Features

### (1) IPv4 Address Input
- Enter a valid IPv4 address (e.g., 192.168.1.1) into the input box. After entering the address, click the "Convert" button or press the Enter key to initiate the conversion process.

### (2) Decimal Conversion
- **Function**: Converts an IPv4 address into a decimal number.
- **Usage**: After inputting the IPv4 address, the tool automatically calculates and displays its corresponding decimal value. This value is derived by converting each of the four bytes of the IPv4 address into decimal numbers and then combining them through a specific calculation method.

### (3) Hexadecimal Conversion
- **Function**: Converts an IPv4 address into a hexadecimal representation.
- **Usage**: After entering the IPv4 address, the tool automatically converts each byte into a two-digit hexadecimal number and combines them into a complete hexadecimal string. For example, the IPv4 address 192.168.1.1 is converted into the hexadecimal form C0A80101.

### (4) Binary Conversion
- **Function**: Converts an IPv4 address into a binary representation.
- **Usage**: After inputting the IPv4 address, the tool converts each byte into an 8-bit binary number and then concatenates the four bytes into a 32-bit binary string. For example, the IPv4 address 192.168.1.1 is converted into the binary form 11000000101010000000000100000001.

### (5) IPv6 Format Conversion
- **Function**: Converts an IPv4 address into an IPv6 format representation.
- **Usage**: The tool converts the IPv4 address into two IPv6 formats:
  1. Full IPv6 address format: The first 8 bytes of the IPv6 address are filled with 0s, the last 8 bytes are the hexadecimal form of the IPv4 address, and "ffff" is added before the IPv4 part as an identifier. For example, the IPv4 address 192.168.1.1 is converted into the full IPv6 format 0000:0000:0000:0000:0000:ffff:c0a8:0101.
  2. Shortened IPv6 format: Omits the consecutive 0s in the IPv6 address, resulting in a more concise representation. For example, the IPv4 address 192.168.1.1 is converted into the shortened IPv6 format ::ffff:c0a8:0101.