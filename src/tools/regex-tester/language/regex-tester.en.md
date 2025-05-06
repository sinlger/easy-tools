# IT Tools - Regex Tester User Manual

## I. Overview

IT Tools offers an online regex testing utility that enables users to test regular expressions against sample text. Its clean interface and practical functionality make it ideal for regex learners and developers.

## II. Feature Details

### (a) Regex Input Section

Enter the regex you want to test in the text box. A regex cheat sheet link is provided for easy reference. For example, the regex \w+ can match one or more word characters.

### (b) Regex Options

Includes options for global search (g), case-insensitive search (i), multiline (m), singleline (s), Unicode (u), and Unicode sets (v). Users can select the options according to their needs.

- Global Search (g): Find all matches throughout the text.
- Case-Insensitive Search (i): Ignore case differences in text matching.
- Multiline (m): Treat the input as multiple lines for start and end matching in each line.
- Singleline (s): Treat the entire input as a single line for cross-line matching.
- Unicode (u): Enable Unicode support for matching Unicode characters.
- Unicode Sets (v): Support Unicode character sets.

For instance, the regex \d{3}-\d{3}-\d{4} with the global option enabled can match multiple phone number formats in the text.

### (c) Text to Match Input Section

Enter the text you want to match in the text box. The tool will perform the match based on the input regex and options. For example, inputting the text "Match the words in this text" and using the regex \w+ will match each word in the text.

### (d) Matches Result Display Section

Displays the match results. If the match is successful, all matches will be listed; if not, a "No match" message will be shown. For example, using the regex https?://\w+\.\w+/\S* to match URLs in the text can find URLs that fit the format.

### (e) Sample Text Section

Provides sample matching text for reference, helping users quickly understand how to input text and what match results to expect.

### (f) Regex Diagram Function

Generates a visual diagram of the regex to help users better understand its structure and logic. For example, the regex [A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,} for email addresses can show the structure, including the username part's character composition, the @ symbol, and the domain format.

## III. Examples

### Example 1: Matching Words

- Regex: \w+
- Text to Match: This is a sample text with multiple words.
- Match Results: Matches all the words in the text.

### Example 2: Matching Phone Numbers

- Regex: \d{3}-\d{3}-\d{4}
- Text to Match: Contact phone: 123-456-7890.
- Match Results: Matches "123-456-7890".

### Example 3: Matching Email Addresses

- Regex: [A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}
- Text to Match: Please email to example@example.com.
- Match Results: Matches "example@example.com".

These examples help users quickly learn how to use the tool for regex testing and understand the application scenarios of different regex patterns.