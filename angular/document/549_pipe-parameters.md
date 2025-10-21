# #549 「Pipe のパラメータ」

## 概要
Pipeのパラメータはtransformの第二引数以降で受け取り、テンプレートから値を渡す。参照型を扱う際は純粋Pipeの再評価条件に注意する。

## 学習目標
- Pipeパラメータの仕組みと制約を理解する
- 参照型パラメータが変更検知へ与える影響を学ぶ
- 引数の設計とドキュメント化のポイントを把握する

## 技術ポイント
- テンプレート: `{{ list | filter:predicate }}`, `{{ text | truncate:limit:suffix }}`
- transform: `transform(value: T, param1: U, param2?: V)`
- 参照型引数はimmutableに保つと純粋Pipeとの相性が良い

## 📺 画面表示用コード（動画用）
```html
<p>{{ text | truncate:30:'…' }}</p>
```

## 💻 詳細実装例（学習用）
```typescript
transform<T>(items: T[], predicate: (item: T) => boolean): T[] {
  if (!Array.isArray(items)) return [];
  return items.filter(predicate);
}
```

## ベストプラクティス
- 引数は少数に抑え、意味が分かりやすい順番に並べる
- 参照型を渡す場合は新しいオブジェクトを生成して純粋Pipeで再評価させる
- 引数のデフォルト値や型をドキュメント化し利用者へ伝える

## 注意点
- 非純粋Pipeに頼るとパフォーマンスが低下する
- オブジェクトや配列をテンプレートリ터ラルで直接渡すと毎回新しい参照になる
- 引数の数が多い場合はオプションオブジェクトなど別のAPIを検討

## 関連技術
- Pure/Impure Pipe
- PipeTransform
- Immutableデータ管理
