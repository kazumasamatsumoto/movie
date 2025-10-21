
# #533 「UpperCasePipe - 大文字変換」

## 概要
UpperCasePipeは文字列をすべて大文字に変換し、同じテンプレート内で統一された大文字表記を実現する。

## 学習目標
- UpperCasePipeの用途と効果を理解する
- ロケール依存の文字ケース変換を把握する
- テンプレート内で簡潔に文字列を整形する

## 技術ポイント
- `{{ text | uppercase }}`
- ロケールによって特定の文字の変換結果が異なる場合がある
- 元の文字列を変更せず表示のみ変換

## 📺 画面表示用コード（動画用）
```html
<p>{{ username | uppercase }}</p>
```

## 💻 詳細実装例（学習用）
```html
<p>タグ: {{ article.tag | uppercase }}</p>
<p>プロジェクト名: {{ project.name | uppercase }}</p>
```

## ベストプラクティス
- UIラベルやボタンなどで統一感を出すために活用
- 元のデータは変えず表示だけ変換できるので安全
- ロケールによる特殊ケース（トルコ語のiなど）に注意

## 注意点
- 大文字変換は視認性に影響するためUX観点で適切か検討
- 入力値がnull/undefinedの場合は空文字になる
- 多言語対応で意図しない変換が起こる可能性

## 関連技術
- LowerCasePipe
- TitleCasePipe
- Internationalization
