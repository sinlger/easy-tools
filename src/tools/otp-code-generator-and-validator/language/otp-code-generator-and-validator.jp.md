# A Toolio - OTPコードジェネレータ 使用ドキュメント

## 1. 機能概要

この**OTPコードジェネレータ**は多要素認証に使用され、時間ベースのワンタイムパスワード（OTP）を生成および検証することで、ユーザーに対して「もう1つのセキュリティ層」を提供します。

## 2. 機能モジュール

### (1) キー管理

1. **シークレットキー入力**: "Secret" フィールドにカスタムキーを入力するか、またはツールが生成したデフォルトキーを使用します。

2. **キー切り替え**: キーフィールド横にあるリセットアイコンをクリックすると、簡単に新しいシークレットキーに切り替えることができます。

3. **16進数形式での表示**: "Secret in hexadecimal" フィールドには対応するキーの16進数形式が自動的に表示されます。