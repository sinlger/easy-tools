# Basic Authentication Generator User Guide

## Overview

This Basic Authentication Generator creates Base64 - encoded HTTP headers from usernames and passwords, streamlining the development process.

## Usage

### Enter UsernameType

 your username into the "Username" field.

### Enter Password

Input the corresponding password into the "Password" field. It will be hidden for security.

### View Authorization Header

After entering both credentials, the tool automatically generates an authorization header in this format:

```
Authorization header:
Authorization: Basic [Base64 - encoded string]
```

Here, "Basic" indicates the authentication method, and the string is your credentials encoded in Base64.

### Copy Authorization Header

Click the "Copy header" button to copy the header to your clipboard for easy pasting elsewhere.