# RSA Key Pair Generator User Guide

## I. Tool Overview

This tool online allows for the easy generation of new random RSA private and public pem certificate key pairs. It is suitable for developers who need to quickly create RSA key pairs during the development process.

## II. Function Explanation

### (I) Key Length Setting

  * **Function**: Users can set the key length (in bits) within a specified range.
  * **Operation**: Enter the desired key length in the input box following "Bits", such as the commonly used 2048 bits. The tool supports a certain range of bit lengths to ensure the generated keys meet security and application requirements.
  * **Purpose**: The longer the key length, the higher the security usually is, but the encryption and decryption speed may slow down accordingly. A balance needs to be struck based on actual application scenarios.

### (II) Refresh Key Pair

  * **Function**: Quickly generates a new random RSA key pair.
  * **Operation**: Click the "Refresh key-pair" button, and the system will regenerate a new public and private key pair based on the currently set key length.
  * **Purpose**: When multiple different key pairs are needed for testing or use, there is no need to manually adjust other parameters. With one click of the refresh button, new key pairs can be quickly obtained, improving work efficiency.

### (III) Public Key Display and Management

  * **Function**: Displays the generated RSA public key and provides convenient operations for users.
  * **Content Display**: In the "Public key" section, the public key is displayed in the standard pem format, enclosed by "-----BEGIN PUBLIC KEY-----" and "-----END PUBLIC KEY-----". It can be directly used for public key configuration in applications.
  * **Copy Operation**: The adjacent copy button allows users to quickly copy the public key content to the clipboard, making it convenient to paste into other places where the public key is needed, such as configuration files and code.

### (IV) Private Key Display and Management

  * **Function**: Displays the generated RSA private key and offers a convenient operation for users.
  * **Content Display**: In the "Private key" section, the private key is also presented in the standard pem format, enclosed by "-----BEGIN RSA PRIVATE KEY-----" and "-----END RSA PRIVATE KEY-----". Users can directly access it when they need to use the private key for encryption, decryption, or signing operations.
  * **Copy Operation**: The adjacent copy button enables users to easily copy the private key content so that they can use it in a secure environment, such as server-side key storage and application key configuration.

## III. Usage Scenario Examples

  1. When developers are working on applications based on the RSA encryption algorithm and need to quickly generate test key pairs, they can set an appropriate key length in this tool and refresh to generate the key pairs. Then, they can use the public key in the encryption code section and the private key in the decryption section for testing.
  2. When setting up secure communication protocols (such as SSL/TLS), if self-signed certificates or key pairs for test environments are needed, this tool can be used to generate them. The public and private keys can then be configured in the corresponding server and client locations.

## IV. Precautions

  * Ensure that you use this tool in a secure network environment to prevent the theft of the generated key pairs.
  * Private keys are highly sensitive. Once generated, they should be properly kept to avoid leakage, as anyone in possession of the private key may impersonate you to perform related operations or decrypt sensitive information.
  * According to the actual security policies of the application, key pairs should be regularly replaced to reduce the risk of key compromise or leakage.