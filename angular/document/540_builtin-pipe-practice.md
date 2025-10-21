# #540 「組み込み Pipe の実践活用」

## 概要
組み込みPipeを組み合わせると、テンプレート上で日付・通貨・数値・文字列を統一フォーマットに整え、国際化や表示ロジックの簡潔化を実現できる。

## 学習目標
- 組み込みPipeを実用シナリオで活用する方法を理解する
- Pipeチェーンによる複数変換の手法を学ぶ
- Pipeを使った国際化・表示整形のメリットを把握する

## 技術ポイント
- 日付:`date`、通貨:`currency`、数値:`number`、割合:`percent`
- 文字列:`uppercase`/`lowercase`/`titlecase`
- Pipeチェーンで複数処理を順序通りに適用

## 📺 画面表示用コード（動画用）
```html
<p>{{ order.total | currency:'JPY':'symbol-narrow' }}</p>
<p>{{ order.createdAt | date:'yyyy/MM/dd HH:mm':'Asia/Tokyo' }}</p>
<p>{{ order.completion | percent:'1.0-1' }}</p>
<p>{{ order.customer | titlecase }}</p>
```

## 💻 詳細実装例（学習用）
```html
<div class="order-summary">
  <h2>{{ order.customerName | titlecase }} 様</h2>
  <p>注文日時: {{ order.createdAt | date:'full' }}</p>
  <p>合計金額: {{ order.total | currency:'JPY':'symbol-narrow':'1.0-0' }}</p>
  <p>支払済み: {{ order.paidAmount | currency:'JPY':'symbol-narrow' }}</p>
  <p>進捗: {{ order.progress | percent:'1.0-1' }}</p>
  <p>注文明細: {{ order.items | json }}</p>
</div>
```

## ベストプラクティス
- 組み込みPipeを積極活用し、表示フォーマットを一貫させる
- Pipeチェーン時は順序を意識し、意味のある組み合わせとする
- 多言語対応やロケール切り替えを見据えてLOCALE_IDを設定

## 注意点
- Pipeは表示専用のため、データ操作はコンポーネントやサービスで行う
- Pipeを多用するとパフォーマンスに影響する場合があるため必要な箇所に限定
- 複雑な整形が必要ならカスタムPipeの検討も視野に

## 関連技術
- CommonModule組み込みPipe
- LOCALE_ID / registerLocaleData
- カスタムPipe実装
