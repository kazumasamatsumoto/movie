# #514 「組み込み Pipe の種類」

## 概要
Angularには日付・通貨・数値・百分率・文字列（大文字/小文字/タイトルケース）などの組み込みPipeが用意されており、テンプレートでの表示整形を簡単に行える。

## 学習目標
- 組み込みPipeの種類と用途を把握する
- CommonModuleをインポートすると利用できることを理解する
- 各Pipeの代表的な使用例を知る

## 技術ポイント
- DatePipe, CurrencyPipe, DecimalPipe, PercentPipe, UpperCasePipe, LowerCasePipe, TitleCasePipe
- `AsyncPipe`, `SlicePipe`, `JsonPipe`なども有用
- Pipeは純粋関数として動作し、副作用を持たない

## 📺 画面表示用コード（動画用）
```html
{{ today | date:'yyyy/MM/dd' }}
{{ price | currency:'JPY' }}
{{ ratio | percent:'1.0-1' }}
{{ title | titlecase }}
```

## 💻 詳細実装例（学習用）
```html
<ul>
  <li>日付: {{ today | date:'medium' }}</li>
  <li>通貨: {{ amount | currency:'USD':'symbol' }}</li>
  <li>数値: {{ level | number:'1.2-2' }}</li>
  <li>割合: {{ completion | percent:'1.0-0' }}</li>
  <li>大文字: {{ username | uppercase }}</li>
  <li>小文字: {{ username | lowercase }}</li>
  <li>タイトル: {{ articleTitle | titlecase }}</li>
  <li>JSON: {{ config | json }}</li>
  <li>配列一部: {{ list | slice:0:3 }}</li>
  <li>非同期: {{ data$ | async }}</li>
```

## ベストプラクティス
- 表示フォーマットは極力組み込みPipeを活用し、再発明を避ける
- Pipeの組み合わせで多くの整形が実現できるため、テンプレートをシンプルに
- 日付や通貨はロケールセットと組み合わせて国際化に対応

## 注意点
- Pipeを多用するとパフォーマンスに影響する場合があるので必要な箇所に限定
- 非純粋Pipeを自作する場合はCDの影響を理解する
- 各Pipeはロケールに依存するため、表示形式が地域によって変わる点に注意

## 関連技術
- CommonModule
- i18n (LOCALE_ID, registerLocaleData)
- カスタムPipe
