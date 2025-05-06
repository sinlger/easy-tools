# IT Tools - OTP Code Generator User Guide

## 1. Feature Overview
This OTP code generator is designed for multi - factor authentication. It can create and verify time - based one - time passwords (OTP), offering an extra layer of security.

## 2. Feature Modules
### (1) Key Management
- **Key Input**: Enter your custom key in the "Secret" box, or use the default key by provided the tool.
- **Key Switching**: Click the loop icon next to the key box to quickly generate a new key.
- **Hexadecimal Key Display**: The "Secret in hexadecimal" box automatically shows the hexadecimal format of the key.

### (2) OTP Display and Verification
- **Current OTP Retrieval**: View the current 6 - digit OTP in the "Current OTP" section.
- **OTP Switching Preview**: Use "Previous" and "Next" to see OTPs from the last and next time periods.
- **Remaining Time提示**: The green progress bar below shows the remaining validity time of the current OTP. "Next in Xs" indicates the seconds until the next OTP takes effect.

### (3) Time and Iteration Information
- **Epoch Time Display**: The "Epoch" box shows the corresponding timestamp for time verification.
- **Iteration Count**: The "Count" box under "Iteration" displays the current number of iterations.
- **Padded Hexadecimal Display**: The "Padded hex" box shows填充的十六进制数据 related to the iteration.

### (4) QR Code and Key URI
- **QR Code Generation**: A QR code is generated for quickly adding accounts in OTP - supporting devices like phone authentication apps.
- **Open Key URI**: Click "Open Key URI in new tab" to open the account - related link in a new tab for further operations or viewing complete account configuration info.

## 3. Usage Process
1. **Initial Setup**: Use the default key or enter a custom key.
2. **View OTP**: Check the current OTP and note the remaining time.
3. **Multi - device Configuration**: Use the QR code or Key URI to add the OTP account in authentication apps on devices like phones.
4. **Verification**: Enter the current OTP during multi - factor authentication.

## 4. Notes
- Ensure accurate device time as OTP generation relies on time synchronization.
- The key is crucial. If using a custom key, keep it safe to prevent leakage.
- This tool suits developers for testing or individuals to understand OTP principles. For production environments, use it with professional authentication systems.