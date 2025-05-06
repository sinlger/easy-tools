# Phone Parser and Formatter User Guide

## Overview

This tool parses, validates and formats phone numbers, providing detailed information such as country code and number type.

## Usage Instructions

### 1. Select Country Code

- Choose the relevant country code from the "Default country code" dropdown menu
- Options include: China (+86), United States (+1), Japan (+81), etc.

### 2. Enter Phone Number

- Input the phone number to be processed in the "Phone number" field
- Various formats are supported (with/without country code, with/without separators)

### 3. View Results

- After submission, the following results will be automatically displayed:
  - Phone number validity verification
  - Country/region information
  - Number type (mobile/fixed/special number, etc.)
  - Standardized formatting display

## Examples

### Example 1: Validating a Chinese Mobile Number
- Select country code: China (+86)
- Enter number: 13800138000
- Results:
  - Valid number
  - China Mobile number segment
  - Standard format: +86 138-0013-8000

### Example 2: Validating a US Phone Number
- Select country code: United States (+1)
- Enter number: (408) 555-0123
- Results:
  - Valid number
  - Area code 408 corresponds to California
  - Standard format: +1-408-555-0123

### Example 3: Validating a Japanese Phone Number
- Select country code: Japan (+81)
- Enter number: 03-1234-5678
- Results:
  - Valid number
  - Tokyo area number
  - Standard format: +81-3-1234-5678

### Example 4: Invalid Number Validation
- Select country code: China (+86)
- Enter number: 1380013800A
- Results:
  - Invalid number
  - Error message: Contains non-digit characters

## Notes

- If the country code is not explicitly specified, it is recommended to select a possible country code first and then validate
- For international format numbers (with + sign), the country code will be automatically recognized
- Special numbers or newly assigned number segments in some countries may not be fully recognized
- Results are for reference only. Actual number status may change due to carrier adjustments

This tool is suitable for developers, data analysts, customer service personnel, and others who need to process and validate phone numbers.