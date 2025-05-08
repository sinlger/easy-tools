# A Toolio String Obfuscator User Guide

## I. Tool Overview

A Toolio offers an online String Obfuscator. It's designed to obfuscate sensitive strings (like secrets, IBANs, or tokens). This enables secure sharing while maintaining identifiability without exposing the actual content.

## II. Feature Explanation

### (i) Input Box

  - **String to obfuscate** : Enter the string you want to obfuscate here. It can be any text, such as account numbers, passwords, ID numbers, or card numbers.

### (ii) Setting Options

  - **Keep first** : Set the number of characters to keep at the beginning of the string. The default value is 4. You can adjust the number by clicking the “−” or “+” button.
  - **Keep last** : Set the number of characters to keep at the end of the string. The default value is 4. Similarly, you can adjust it using the “−” or “+” button.
  - **Keep spaces** : Controls whether spaces in the string are preserved. It's enabled by default. If enabled, the obfuscated string will retain the original space positions; if disabled, spaces will be ignored.

### (iii) Output Box

  - Displays the obfuscated string. Characters not kept are replaced with “*”.

### (iv) Copy Button

  - Located to the right of the output box. Clicking it copies the obfuscated string to the clipboard for easy pasting.

## III. Usage Steps

  1. Go to the [A Toolio String Obfuscator](https://atoolio.com/string-obfuscator) webpage.
  2. Enter the string to be obfuscated in the **String to obfuscate** box.
  3. Adjust the **Keep first** and **Keep last** values and decide whether to keep spaces.
  4. View the obfuscated string in the output box.
  5. Copy it by clicking the copy button if needed.

## IV. Examples

### Example 1

  * Input string: `1234567890`
  * Set **Keep first** to 2, **Keep last** to 2, and disable **Keep spaces**.
  * Obfuscated result: `12******89`

### Example 2

  * Input string: `My secret code is ABC123`
  * Set **Keep first** to 3, **Keep last** to 3, and enable **Keep spaces**.
  * Obfuscated result: `My************ABC`

### Example 3

  * Input string: `IBAN: DE1234567890123456`
  * Set **Keep first** to 5, **Keep last** to 4, and disable **Keep spaces**.
  * Obfuscated result: `IBAN: DE1*************56`