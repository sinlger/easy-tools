# SVGプレースホルダジェネレータ 使用ドキュメント

## 1. ツール概要

SVGプレースホルダジェネレータは、カスタマイズ可能なSVG形式のプレースホルダ画像を迅速に生成するためのオンラインツールです。これらのプレースホルダは、アプリケーション開発における仮画像表示に利用され、実際の画像コンテンツがない状態でもインターフェースレイアウトやデザインの確認作業をサポートします。

## 2. 機能説明

### （1）サイズ設定

* **幅と高さ**：入力欄からプレースホルダ画像の幅・高さ（ピクセル単位）を個別に指定可能です。また「+」「-」ボタンで寸法調整が簡単に行えます。
* **正確なサイズを使用**：このオプションを有効にすると、生成されるSVGプレースホルダは指定した幅・高さに厳密に従って表示されます。

### （2）カラー設定

* **背景色**：十六進数カラーコード（例 "#cccccc"）を入力することで、プレースホルダの背景色をカスタマイズできます。
* **文字色**：同じく十六進数カラーコード（例 "#333333"）を入力し、プレースホルダ上に表示される文字色を設定します。

### （3）テキスト設定

* **フォントサイズ**：数値を入力して適切な単位（例 px）を選択することで、プレースホルダに表示される文字サイズを調整可能です。
* **カスタムテキスト**：テキスト入力欄に任意の表示内容を入力できます。デフォルトでは「幅 x 高さ」（例 "600x350"）が表示されます。

### （4）プレビューと出力

* **リアルタイムプレビュー**：右側にあるプレビューエリアで、設定したパラメータに基づいて生成されたSVGプレースホルダ画像の即時プレビューが確認できます。
* **SVG HTML要素**：生成されたSVGコードを直接コピーしてWeb開発プロジェクト内で使用可能です。
* **Base64でのSVG**：SVG画像をBase64エンコードされた文字列として提供し、特定の特殊なコーディング形式が必要なシナリオで役立ちます。

## 3. 使用手順

1. [SVGプレースホルダジェネレータサイト](https://atoolio.com/svg-placeholder-generator)を開きます。
2. 必要なプレースホルダの幅と高さを設定します。例えば、800px幅、450px高さのプレースホルダを作成したい場合、「Width (in px)」欄に"800"、「Height (in px)」欄に"450"と入力してください。
3. 背景色と文字色をカスタマイズします。背景を淡い青（例 "#e6f7ff"）、文字を濃い青（例 "#1890ff"）にしたい場合は、それぞれ対応する入力欄に該当のカラーコードを入力します。
4. フォントサイズとカスタムテキストを設定します。フォントサイズが20pxで表示テキストを"Sample"にする場合、「Font size」欄に"20"を、「Custom text」欄に"Sample"を入力します。
5. 右側のプレビュー領域で、生成されたプレースホルダ画像が期待通りであるか確認します。
6. 実際の用途に応じて、「SVG HTML element」のコードまたは「SVG in Base64」のエンコード済み文字列をコピーし、開発プロジェクトに貼り付けます。また、「Download svg」ボタンをクリックすれば、生成されたSVGファイルを直接ダウンロード可能です。