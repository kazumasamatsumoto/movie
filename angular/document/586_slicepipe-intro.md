# #586 「SlicePipe - 配列・文字列の切り出し」

## 概要
SlicePipeは配列や文字列の一部を切り出すPipeで、startとendインデックスを指定してサブセットを表示できる。ページネーションやプレビューに便利。

## 学習目標
- SlicePipeの用途と基本構文を理解する
- start/endパラメータの指定方法を学ぶ
- 配列/文字列いずれにも適用できることを把握する

## 技術ポイント
- `{{ array | slice:start:end }}`
- endを省略すると末尾まで
- 文字列に使うと部分文字列を返す

## 📺 画面表示用コード（動画用）
```html
<li *ngFor="let item of items | slice:0:5">{{ item }}</li>
```

## 💻 詳細実装例（学習用）
```html
<p>{{ description | slice:0:100 }}...</p>
<ul>
  <li *ngFor="let item of products | slice:(page-1)*pageSize:(page)*pageSize">
    {{ item.name }}
  </li>
</ul>
```

## ベストプラクティス
- 配列を破壊せずビュー用に部分表示できる
- ページネーションなど簡易的な用途で活用
- 書籍や記事のイントロ表示など文字列にも適用

## 注意点
- 大量データのページネーションはPipeよりもサービス側で処理が望ましい
- Negativeインデックスはユースケースに応じて利用可能（末尾から）
- Pipeは純粋なので参照が変わらないと再評価されない点に注意

## 関連技術
- Array.slice
- Paginationコンポーネント
- Pure Pipe
