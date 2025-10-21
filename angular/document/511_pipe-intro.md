# #511 「Pipe とは？データ変換」

## 概要
Pipeはテンプレート内で値を整形・変換するための機能で、データ自体は変えず表示だけを加工できる。`value | pipeName`の構文で利用する。

## 学習目標
- Pipeの役割とテンプレート構文を理解する
- パイプをチェーンして複数変換を行う方法を把握する
- Pipeを使うメリット（表示ロジックの簡潔化）を学ぶ

## 技術ポイント
- `{{ value | pipeName }}`で使用
- `value | pipeA | pipeB`で連続加工
- 組み込みPipeはCommonModuleをインポートするだけで利用可能

## 📺 画面表示用コード（動画用）
```html
<p>{{ birthday | date:'yyyy/MM/dd' }}</p>
```

## 💻 詳細実装例（学習用）
```html
<p>誕生日: {{ user.birthday | date:'yyyy/MM/dd HH:mm' }}</p>
<p>価格: {{ cart.total | currency:'JPY':'symbol-narrow' }}</p>
<p>割引: {{ cart.discount | percent:'1.0-1' }}</p>
```

## ベストプラクティス
- テンプレートでの表示ロジックをPipeに委ね、コンポーネントのコードをシンプルに保つ
- Pipeをチェーンする際は処理順に注意し、複雑になりすぎたらカスタムPipeを検討
- 組み込みPipeを活用することで国際化やフォーマット整形が簡単に

## 注意点
- Pipeは純粋関数が前提。非純粋Pipeはパフォーマンスに影響
- 大量データへのPipe適用はパフォーマンスを考慮
- Pipeで丸めやフォーマットする際はデータの実際の値が変わらないことを意識

## 関連技術
- Angular組み込みPipe
- カスタムPipe
- 国際化（i18n）
