# A Toolio Online HMAC Generator Documentation

## 1. Tool Introduction

The online HMAC generator provided by A Toolio calculates Hash-based Message Authentication Code (HMAC) using a secret key and hash function, suitable for developers to quickly generate HMAC for authentication in various development scenarios.

## 2. Function Description

### Input Section

1. **plain text**: Enter the plaintext that needs to be hashed.
2. **secret key**: Enter the secret key used to generate the HMAC.
3. **hashing function**: Select the hash function, defaults to SHA256, other functions can be selected as needed.
4. **output encoding**: Select the output encoding method, defaults to hexadecimal (base 16), other encoding methods are also available.

### Output Section

1. **HMAC of your text**: Displays the generated HMAC value and provides a copy button for easy copying of the result.

## 3. Operating Steps

**Step 1: Enter Plain Text and Secret Key**

Enter the plaintext content you want to hash in the "plain text" input field, then enter the secret key used to generate the HMAC in the "secret key" input field. This is the basic data for generating HMAC and must be entered accurately.

**Step 2: Select Hash Function**

Choose an appropriate hash function from the "hashing function" dropdown menu, such as SHA256, SHA1, etc. Depending on your actual needs, different hash functions will produce different HMAC results.

**Step 3: Select Output Encoding Method**

Select the desired output encoding method from the "output encoding" dropdown menu, such as hexadecimal (base 16), base64, etc. This determines the representation form of the generated HMAC value.

**Step 4: Generate and View HMAC**

After completing the above inputs and selections, the system will automatically calculate and display the HMAC value in the "HMAC of your text" area. You can directly view the result.

**Step 5: Copy HMAC**

If you need to use this HMAC value, click the copy button next to the result to copy the HMAC value to the clipboard for pasting in other places.