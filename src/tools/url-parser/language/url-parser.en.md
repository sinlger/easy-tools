# URL Parser User Guide

## I. Tool Overview
The URL Parser is an online tool designed to break down a URL string into its various components, including protocol, username, password, hostname, port, path, parameters, etc. It helps developers quickly understand the structure of a URL and its detailed information, making it convenient for building, debugging, and analyzing network requests.

## II. Feature Explanation

  1. **Input Box**
     * Provides an input box for entering the URL string to be parsed.

  2. **Parsing Result Display**
     * **Protocol** ：Shows the protocol part of the URL, such as “https:”, indicating the network transmission protocol used by the URL.
     * **Username** ：If the URL contains username information, it will be displayed here, used to identify the user identity provided in the URL.
     * **Password** ：Correspondingly displays the password part in the URL, combined with the username for user authentication.
     * **Hostname** ：Displays the domain name corresponding to the URL, such as “atoolio.com”, indicating the name of the target server.
     * **Port** ：Shows the port number specified in the URL, used to determine the specific port on the server providing the service. Different protocols have different default ports by default, such as port 80 for HTTP and port 443 for HTTPS.
     * **Path** ：Displays the path part of the URL, such as “/url-parser”, pointing to the location of specific resources or services on the server.
     * **Params** ：Lists the query parameter part of the URL, starting with “?”, followed by multiple “key-value pair” parameters, such as “?key1=value&key2=value2”. These parameters are used to pass additional information and instructions to the server.
     * **Detailed Parameter Display** ：Displays each key-value pair of the query parameters separately, clearly showing the name and corresponding value of each parameter for a more intuitive view of the specific content of each parameter.

## III. Usage Steps

  1. Open your browser and visit the [URL Parser](https://atoolio.com/url-parser) webpage.
  2. Enter the URL string you want to parse in the input box, for example, “https://me:pwd@atoolio.com:3000/url-parser?key1=value&key2=value2#the-hash”.
  3. Click the parse button (usually the Enter key can also trigger the parsing), and the tool will automatically parse the entered URL and display the detailed information of each component below.
  4. View the parsing results and copy the corresponding component content as needed for subsequent development, debugging, or other operations.

## IV. Examples

  1. **Example 1**
     * Input URL: “http://user:pass@example.com:8080/page?param1=hello&param2=world”
     * Parsing Results:
       * Protocol: http:
       * Username: user
       * Password: pass
       * Hostname: example.com
       * Port: 8080
       * Path: /page
       * Params: ?param1=hello&param2=world
       * Detailed Parameter Display:
         * param1: hello
         * param2: world

  2. **Example 2**
     * Input URL: “https://www.google.com/s?wd=URL parser”
     * Parsing Results:
       * Protocol: https:
       * Username: (None)
       * Password: (None)
       * Hostname: www.google.com
       * Port: (Default port 443, not displayed)
       * Path: /s
       * Params: ?wd=URL parser
       * Detailed Parameter Display:
         * wd: URL parser