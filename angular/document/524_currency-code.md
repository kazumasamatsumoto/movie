# #524 「通貨コードの指定」

## 概要
CurrencyPipeの第2引数に通貨コードを指定すると、特定の通貨でフォーマットできる。ISO 4217コード（USD, EUR, JPYなど）を使用する。

## 学習目標
- 通貨コードの指定方法を理解する
- 通貨記号やコード表示の違いを把握する
- 国際向けアプリでの通貨表示を学ぶ

## 技術ポイント
- `{{ value | currency:'USD' }}`
- 第3引数で`'symbol'`, `'code'`, `'name'`など表示形式を指定
- 第4引数で桁数フォーマット指定

## 📺 画面表示用コード（動画用）
```html
<p>{{ value | currency:'USD':'symbol' }}</p>
```

## 💻 詳細実装例（学習用）
```html
<p>USD: {{ amount | currency:'USD':'symbol' }}</p>
<p>EURコード: {{ amount | currency:'EUR':'code' }}</p>
<p>JPY狭い記号: {{ amount | currency:'JPY':'symbol-narrow' }}</p>
```

## ベストプラクティス
- 通貨コードはISO 4217に基づき大文字で指定
- 表示形式は仕様に合わせ`symbol`/`code`/`name`を選択
- 国際化対応ではユーザーごとに通貨コードを変えるためサービスで管理

## 注意点
- 未対応の通貨コードを指定するとエラーになることがある
- 同じ通貨でもロケールによって表示記号が異なる
- 変換前の値が文字列の場合は数値に変換してからPipeへ渡す

## 関連技術
- CurrencyPipeオプション
- LOCALE_ID
- ISO 4217
