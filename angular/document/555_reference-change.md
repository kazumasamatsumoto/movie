# #555 「参照の変更のみで再実行」

## 概要
純粋Pipeは参照型の入力値が同じインスタンスである限り再評価されないため、配列やオブジェクトは参照を変更して渡す必要がある。

## 学習目標
- 参照比較による再評価条件を理解する
- mutableなデータを扱う際の注意点を学ぶ
- Immutable戦略とPipeの相性を把握する

## 技術ポイント
- `value === previousValue`で比較、同一参照なら再実行しない
- 新しい配列/オブジェクトを作成してからPipeへ渡す
- Immutable.jsやspread構文で参照を変更

## 📺 画面表示用コード（動画用）
```typescript
this.items = [...this.items, newItem]; // 新しい参照でPipeが再評価
```

## 💻 詳細実装例（学習用）
```typescript
addItem(item: string): void {
  this.items = [...this.items, item];
}
```

## ベストプラクティス
- Pipeで配列/オブジェクトを扱う場合は参照を変更する
- 変更検知最適化のためimmutableデータ構造を採用
- 非純粋Pipeを避けPurePipe＋immutable戦略を優先

## 注意点
- 深いネストのオブジェクトは部分コピーでは参照が変わらない場合がある
- 非純粋Pipeは性能に影響するため最後の手段
- AsyncPipeなど組み合わせる場合は再評価タイミングも考慮

## 関連技術
- Immutableデータ
- Impure Pipe
- Change Detection
