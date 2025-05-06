# IT Tools - JWT Parser User Guide

## 1. Tool Introduction

The IT Tools - JWT Parser is a convenient online utility that parses and decodes JSON Web Tokens (JWT). It offers developers a quick way to view JWT details for debugging, verification, and learning purposes.

## 2. Features

### (1) Input Function

  * **JWT Input Box** : Users can paste the JWT to be parsed into this box. It has a large capacity to accommodate JWTs of various lengths.

### (2) Parsing Function

  * **Header Parsing** : Accurately parses the header information of a JWT, including:
    * **alg (Algorithm)** : Displays the encryption algorithm used by the JWT, e.g., HS256 means the HMAC algorithm and SHA - 256 digest algorithm are employed.
    * **typ (Type)** : Displays the type of the JWT, which is usually JWT.

  * **Payload Parsing** : Can thoroughly parse the payload part of a JWT and show the various claim information it contains, for example:
    * **sub (Subject)** : Identifies the user or subject that the JWT is intended for.
    * **name (Full name)** : Shows the full name of the user.
    * **iat (Issued At)** : Identifies the time when the JWT was issued, typically in timestamp format, and can be converted to a specific date and time format.

### (3) Display Function

  * **Structured Display** : Presents the parsed content of the JWT in a clear structured table format. This makes it easy for users to quickly view and understand the meaning and value of each field, providing an intuitive and readable display of the information.

## 3. Steps to Use

  1. **Visit the Website** : Open a browser and go to<https://it-tools.tech/jwt-parser> to access the JWT Parser page.
  2. **Input JWT** : Paste the JWT to be parsed into the input box.
  3. **Click Parse** : Click the parse button (usually the button next to “JWT to decode”, the exact appearance depends on the page display), and the system will automatically parse the input JWT.
  4. **View Results** : Check the parsed Header and Payload information in the display area below to understand the detailed content of the JWT.

## 4. Notes

  * Ensure the input JWT is in the correct format; otherwise, it may result in parsing failure or inaccurate results.
  * This tool is only for parsing and viewing the content of JWTs. It doesn’t guarantee complete and accurate parsing of all types of JWTs, especially those using special encryption algorithms or non - standard formats.
  * If you encounter any issues or have any requirements during use, you can contact the relevant support channels provided by the website (such as “Buy me a coffee” might imply that you can contact the developer via this method to get further assistance).