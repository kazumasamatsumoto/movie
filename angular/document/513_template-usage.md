# #513 「テンプレートでの使用」

## 概要
テンプレートでPipeを使用すると、コンポーネントロジックを変更せずに表示フォーマットを整形できる。日付や数値などの表示を統一するのに役立つ。

## 学習目標
- Pipeをテンプレート内で適用するケースを理解する
- 変換を複数箇所で再利用するメリットを学ぶ
- Pipeを利用してコンポーネントをシンプルに保つ方法を把握する

## 技術ポイント
- `{{ value | pipeName }}`で即座に変換
- 属性バインディングでも使用可能（例: `[value]="price | currency"`）
- `ngFor`の中など繰り返しでも利用できる

## 📺 画面表示用コード（動画用）
```html
<p *ngFor="let item of orders">
  注文日: {{ item.orderedAt | date:'mediumDate' }} / 金額: {{ item.amount | currency:'JPY':'symbol-narrow' }}
</p>
```

## 💻 詳細実装例（学習用）
```html
<table>
  <tr>
    <th>商品</th>
    <th>価格</th>
    <th>注文日</th>
  </tr>
  <tr *ngFor="let item of cart">
    <td>{{ item.name | titlecase }}</td>
    <td>{{ item.price | currency:'JPY':'symbol-narrow' }}</td>
    <td>{{ item.orderedAt | date:'yyyy/MM/dd HH:mm' }}</td>
  </tr>
</table>
```

## ベストプラクティス
- 繰り返し表示でもPipeを使うことで整形ロジックを共通化
- 複雑なロジックはコンポーネントで処理し、表示に特化した部分だけPipeに任せる
- Pipeは軽量で純粋な関数であることを意識し、テンプレートの可読性を高める

## 注意点
- 高パフォーマンスを必要とする場面ではPipeの計算コストに注意
- 非純粋Pipeはレンダリングごとに呼ばれるので慎重に使用
- テンプレート内で複雑な式とPipeを組み合わせると読みにくくなるため適度に分割

## 関連技術
- CommonModuleに含まれる組み込みPipe
- カスタムPipe
- テンプレート構文
