# Text Encryption Tool User Guide

## I. Tool Introduction

This is a powerful text encryption tool primarily based on the bcrypt algorithm. It can encrypt text and compare hashed values with original text, making it suitable for security - related applications like password storage and verification.

## II. Accessing the Tool

Enter the tool - page URL in the browser address bar and hit Enter. Wait for the page elements to load completely.

## III. Operation Guide

### (I) Encrypting Text

  1. **Enter Text** : Input the text - to - be - encrypted in the "Your string" textbox, e.g., a user - set password during registration.
  2. **Set Salt Count** : Click the "+" / "-" buttons beside "Salt count" to set the salt iterations. Salt, a random string added before encryption, enhances security by preventing rainbow table attacks. A minimum of 10 iterations is recommended.
  3. **View Encryption Result** : After the above steps, the tool automatically encrypts the text and displays the hash value in the textbox below. The hash includes algorithm identifier, salt, and encrypted text info, e.g., "$2a$10$0HY6IJrUqS6LMG.LwGUuXemMiXTpBNloPRqFn/Dk5Esl7bj1sXA.xK".
  4. **Copy Hash Value** : Click the "Copy hash" button to copy the hash to the clipboard for storage in databases or other locations.

### (II) Comparing String with Hash

  1. **Enter String for Comparison** : In the "Compare string with hash" section, input the original text in the "Your string" textbox, such as a login password.
  2. **Enter Hash Value** : Input the pre - encrypted hash (from storage like a database) in the "Your hash" textbox.
  3. **View Comparison Result** : The tool automatically compares the text and hash, showing "Yes" (match) or "No" (no match) in the "Do they match?" area.

## IV. Parameter Explanations

### (I) Your string (Text - to - Encrypt Input Box)

This box receives the original text for encryption. In user registration, it captures the user - set password. The password is then encrypted and stored as a hash instead of plain text, ensuring security.

### (II) Salt count (Salt Iteration Setting)

Salt is a security mechanism in encryption. The iteration count determines the intensity and complexity of salt processing. More iterations increase cracking difficulty as attackers need more time and resources for brute - force attacks. It's a key parameter balancing security and performance, with a minimum of 10 iterations suggested.

### (III) Generated Hash Value (Encryption Result)

The hash value is a specially formatted encryption result with key components:

  * **Algorithm Identifier** : E.g., "$2a$", indicating the bcrypt algorithm version and type for identification in decryption or comparison.
  * **Salt Information** : Contains the random salt and iteration count, like "$10$0HY6IJrUqS6LMG.LwGUuXemMiXTpBNloPRqFn/". The "10" is the iteration count, and the following part is the random salt. The salt ensures the same password with different salts generates different hashes, boosting security.
  * **Encrypted Text Information** : The actual encrypted data from the bcrypt algorithm based on the original text and salt. In password verification, the system re - encrypts the user - entered password using the hash salt and algorithm, then compares the result with the stored hash.

### (IV) Compare string with hash (String - and - Hash Comparison Section)

  * **Your string (Original - Text Input Box for Verification)** : Inputs the text - to - verify, such as a login password. It's re - encrypted using the hash salt and algorithm for comparison with the stored hash.
  * **Your hash (Hash - Value Input Box)** : Inputs the pre - stored encrypted hash. During comparison, the system extracts the hash salt and algorithm information to encrypt the entered text with the same method.
  * **Do they match? (Comparison Result)** : Shows whether the entered text matches the hash, indicating if the user - entered password is correct. This allows secure user authentication without storing plain - text passwords.

## V. Notes

  1. **Prioritize Security** : For password management, always encrypt passwords with this tool instead of storing plain - text passwords. Choose an appropriate salt iteration count for enhanced security.
  2. **Data Storage and Transmission Security** : Ensure secure database storage for hash values and use HTTPS for transmission to prevent interception and tampering.
  3. **Accuracy of Comparison Verification** : In string - and - hash comparison, ensure the hash is complete and unmodified. Any hash modification or incorrect input will cause comparison failure.
  4. **Tool Usage Scenarios** : This tool is mainly for password encryption and verification. When using it in other encryption - or data - integrity - required scenarios, evaluate its suitability and security based on specific circumstances.

This guide helps you fully understand the tool's usage and parameters, enabling its proper application in projects requiring text encryption and verification to ensure data security.