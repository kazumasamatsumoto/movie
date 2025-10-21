# #525 「'USD' / 'EUR' / 'JPY'」

## 概要
CurrencyPipeは指定した通貨コードに応じて記号やフォーマットを切り替える。`'USD'`, `'EUR'`, `'JPY'`など代表的な例を通して挙動を確認する。

## 学習目標
- 複数通貨のフォーマット例を理解する
- 通貨ごとの記号・桁区切りの違いを把握する
- 表示形式とロケールの組み合わせを学ぶ

## 技術ポイント
- `{{ value | currency:'USD':'symbol' }}` → `$1,234.00`
- `{{ value | currency:'EUR':'symbol' }}` → `€1,234.00`
- `{{ value | currency:'JPY':'symbol' }}` → `￥1,234`

## 📺 画面表示用コード（動画用）
```html
<li>{{ value | currency:'USD':'symbol' }}</li>
<li>{{ value | currency:'EUR':'symbol' }}</li>
<li>{{ value | currency:'JPY':'symbol' }}</li>
```

## 💻 詳細実装例（学習用）
```html
<ul>
  <li>USD: {{ 1234.5 | currency:'USD':'symbol' }}</li>
  <li>EUR: {{ 1234.5 | currency:'EUR':'symbol' }}</li>
  <li>JPY: {{ 1234.5 | currency:'JPY':'symbol' }}</li>
</ul>
```

## ベストプラクティス
- 国際化対応ではユーザーの通貨設定に応じてコードを切り替える
- 桁区切りと小数桁を通貨仕様に合わせて設定（円は小数なしなど）
- 通貨コードは型/定数で管理しマジックコードを避ける

## 注意点
- ロケールによって同じ通貨でも表示形式が異なる
- 変換前の数値が浮動小数の場合、小数桁の扱いを明確にする
- 通貨換算はPipeではなくアプリケーションロジックで行う

## 関連技術
- CurrencyPipe
- LOCALE_ID
- 国際化と通貨処理
