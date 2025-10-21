# #588 「KeyValuePipe - オブジェクト反復」

## 概要
KeyValuePipeはオブジェクトやMapを`{ key, value }`ペアの配列に変換し、テンプレートで`*ngFor`を使って反復できるようにする。

## 学習目標
- KeyValuePipeの目的と使い方を理解する
- オブジェクト/Mapをテンプレートでループする手法を学ぶ
- 出力順序（オブジェクトはキーソート、Mapは挿入順）を把握する

## 技術ポイント
- `object | keyvalue` → `{ key, value }[]`
- オブジェクトはキーで昇順ソート、Mapは挿入順
- `compareFn`引数でソート順をカスタマイズ可能

## 📺 画面表示用コード（動画用）
```html
<div *ngFor="let entry of settings | keyvalue">
  {{ entry.key }}: {{ entry.value }}
}</div>
```

## 💻 詳細実装例（学習用）
```html
<table>
  <tr *ngFor="let entry of userInfo | keyvalue">
    <th>{{ entry.key }}</th>
    <td>{{ entry.value }}</td>
  </tr>
</table>
```

## ベストプラクティス
- シンプルな設定オブジェクトをテンプレートで表示する際に便利
- `compareFn`を渡してソート順をカスタマイズ
- Mapを扱う場合は挿入順が保たれるため、順序を意識した設計が可能

## 注意点
- オブジェクトのキーが記号や空文字の場合の表示を考慮
- 参照が変わらない限り純粋Pipeとして再評価されない
- 大きなオブジェクトを丸ごと表示するとパフォーマンス影響

## 関連技術
- Map/Record
- keyvalue compareFn
- テンプレート反復構文
