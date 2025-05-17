# Outlook Safelink デコーダー 使用ドキュメント

## 1. ツール概要
**Outlook Safelink デコーダー**は、Microsoft Outlook メールサービスが生成する SafeLink リンクを復号するためのツールです。Outlook Safelinkによって暗号化されたリンクを元のURLに戻すことができ、ユーザーがリンク先の実際のアドレスを簡単に確認できるようになります。

## 2. 機能説明
このツールの主な機能は、Microsoft Outlook がセキュリティ向上のために生成した暗号化・リダイレクトされたリンクを元のウェブアドレスに変換することです。

## 3. 使用方法

### 入力
入力欄にデコードしたいOutlook SafeLinkを貼り付けます。このリンクはMicrosoft Outlookによってセキュリティ目的で暗号化されており、特定のフォーマットを持っています。

### 出力
"Decode"ボタンをクリックすると、ツールが入力されたリンクを処理し、出力欄に復号された元のURLを表示します。もし入力されたリンクが正しくフォーマットされていない場合や認識できない場合は、エラーメッセージ "Error: Invalid SafeLinks URL provided" が表示されます。

## 4. 使用例

### 例 1
入力 (SafeLink):
`https://nam02.safelinks.protection.outlook.com/?url=https%3A%2F%2Fexample.com&data=...`
デコード後の出力:
`https://example.com`

### 例 2
入力 (SafeLink):
`https://nam02.safelinks.protection.outlook.com/?url=https%3A%2F%2Fmicrosoft.com&data=...`
デコード後の出力:
`https://microsoft.com`

### 例 3
無効または誤った形式のリンクを入力した場合:
`https://nam02.safelinks.protection.outlook.com/?url=invalidurl&data=...`
エラーメッセージ:
`Error: Invalid SafeLinks URL provided`

## 5. 注意事項
- 入力するリンクが完全なOutlook Safelinkであることを確認してください。