# Online User-Agent Analyzer: User Guide

## I. Tool Introduction
This online user-agent analyzer can accurately detect and analyze browser, engine, OS, CPU, and device type/model from a user-agent string, helping developers quickly get client-related details.

## II. Feature Description

### (I) Browser Identification
It accurately identifies the browser type and version. For example, if "Edge 135.0.0.0" is displayed, it means the client is using Edge version 135.0.0.0.

### (II) Engine Identification
It clearly shows the rendering engine and its version. For instance, "Blink 135.0.0.0" indicates the engine is Blink version 135.0.0.0.

### (III) OS Identification
It provides detailed OS name and version information, such as "Windows 10".

### (IV) Device Information Identification
It can get device type, model, and vendor (if available). If not, it will show "No device model/type/vendor available".

### (V) CPU Information Identification
It identifies CPU details, like "amd64" for the CPU architecture.

## III. Usage Examples

### Example 1: Common Desktop Browser
Take the user-agent string Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0 as an example.
After inputting it into the analyzer:

  * **Browser**: It identifies it as Edge 135.0.0.0.
  * **Engine**: It corresponds to Blink 135.0.0.0.
  * **OS**: It is Windows 10.
  * **Device**: No specific device model, type, or vendor is available, and the corresponding prompt will be shown.
  * **CPU**: It is amd64.

### Example 2: Mobile Browser
Take the user-agent string Mozilla/5.0 (iPhone; CPU iPhone OS 16_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 as an example.
After inputting it into the analyzer:

  * **Browser**: It identifies it as Safari and its corresponding version on iOS (the specific version depends on the actual parsing).
  * **Engine**: It shows the Webkit engine and its related details (including version).
  * **OS**: It is iOS and its corresponding version (such as 16_6_1).
  * **Device**: It can get the device as iPhone (depending on the parsing result).
  * **CPU**: It shows the CPU architecture suitable for mobile devices (if identifiable).