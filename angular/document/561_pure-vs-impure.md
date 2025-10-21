# #561 「Pure vs Impure の使い分け」

## 概要
純粋Pipeは参照変更時のみ再評価される高速なPipeで、非純粋Pipeは変更検知ごとに再計算されるが可変データを扱える。用途に応じて適切に使い分ける必要がある。

## 学習目標
- 純粋Pipeと非純粋Pipeの違いを理解する
- どのようなケースで非純粋Pipeが必要になるか把握する
- パフォーマンスと柔軟性のトレードオフを学ぶ

## 技術ポイント
- `pure: true`（デフォルト）は参照変更のみ再評価
- `pure: false`はすべての変更検知で再評価
- 可変データや外部状態に依存する場合のみ非純粋を検討

## 📺 画面表示用コード（動画用）
```typescript
@Pipe({ name: 'filter', pure: false, standalone: true })
export class FilterPipe implements PipeTransform { ... }
```

## 💻 詳細実装例（学習用）
```typescript
@Pipe({ name: 'immutableFilter', standalone: true })
export class ImmutableFilterPipe implements PipeTransform {
  transform<T>(list: readonly T[], predicate: (item: T) => boolean): T[] {
    return list.filter(predicate);
  }
}
```

## ベストプラクティス
- データがimmutableなら純粋Pipeを利用しパフォーマンスを確保
- 非純粋Pipeが必要な場合は処理を軽量化し、ドキュメントで注意喚起
- Pipe以外のアプローチ（コンポーネント処理、RxJS）も検討

## 注意点
- 非純粋Pipeは多用するとパフォーマンス問題を引き起こす
- 純粋Pipeでも参照が変わらない更新は反映されないためデータ更新戦略が必要
- 仕様変更時に純粋/非純粋が逆になる場合は挙動確認

## 関連技術
- PipeTransform
- Change Detection
- Immutableデータ管理
