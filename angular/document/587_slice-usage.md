# #587 「{{ array | slice:start:end }}」

## 概要
SlicePipeの具体的な使用例として、配列や文字列の一部をテンプレートで簡単に切り出す方法を示す。

## 学習目標
- SlicePipeのパラメータ指定例を理解する
- 配列/文字列での利用パターンを学ぶ
- start/end指定の動作を把握する

## 技術ポイント
- `start`は0-based、`end`は非包含（end位置は含まれない）
- `end`省略で末尾まで、負の値で末尾からのオフセット
- Pipeは純粋であり参照が変わらない限り再評価されない

## 📺 画面表示用コード（動画用）
```html
<li *ngFor="let item of items | slice:start:end">{{ item }}</li>
<p>{{ text | slice:0:10 }}…</p>
```

## 💻 詳細実装例（学習用）
```html
<p>プレビュー: {{ article.body | slice:0:120 }}...</p>
<ul>
  <li *ngFor="let member of team | slice:0:3">{{ member.name }}</li>
</ul>
```

## ベストプラクティス
- ページネーションやプレビューで簡易的に使用
- 文字列と配列いずれにも使えるので汎用性が高い
- Pipeチェーンでさらに他の加工を組み合わせる（例: titlecase）

## 注意点
- 大規模データはPipeよりもサービス/コンポーネント側で処理
- Negativeインデックスを使用する場合の挙動を確認
- Pipeは元データを破壊しないが、再評価条件に注意

## 関連技術
- Array.slice
- Pagination
- Pipeチェーン
