# #526 「表示形式の指定」

## 概要
CurrencyPipeの第3引数で表示形式を指定でき、`'symbol'`, `'symbol-narrow'`, `'code'`, `'name'`などから選択して通貨表示をコントロールできる。

## 学習目標
- 表示形式オプションの違いを理解する
- 記号とコードを使い分ける場面を学ぶ
- ユーザー向け表示とデータ表示の使い分けを把握する

## 技術ポイント
- `'symbol'`: ロケールの標準記号（例: ¥, $）
- `'symbol-narrow'`: 短い記号（例: ￥ → ¥）
- `'code'`: 通貨コード（JPY, USD）
- `'name'`: 通貨名（Japanese Yen）

## 📺 画面表示用コード（動画用）
```html
<p>{{ value | currency:'JPY':'symbol-narrow' }}</p>
```

## 💻 詳細実装例（学習用）
```html
<ul>
  <li>Symbol: {{ 1234 | currency:'USD':'symbol' }}</li>
  <li>Narrow: {{ 1234 | currency:'USD':'symbol-narrow' }}</li>
  <li>Code: {{ 1234 | currency:'USD':'code' }}</li>
  <li>Name: {{ 1234 | currency:'USD':'name' }}</li>
</ul>
```

## ベストプラクティス
- UI表示には`symbol`や`symbol-narrow`を使用し、コード表示が必要な箇所では`code`
- 明細書などでは通貨コードや名前を表示し誤解を防止
- 表示形式をコンポーネントのInputとして外部指定できるよう設計

## 注意点
- `'name'`はロケールによって訳語が異なるため確認が必要
- `'symbol-narrow'`が定義されていない通貨もある
- 小数桁指定は第4引数で別途行う

## 関連技術
- CurrencyPipeオプション
- i18n
- Intl.NumberFormat
