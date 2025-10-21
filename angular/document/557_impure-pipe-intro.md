# #557 「Impure Pipe - 非純粋パイプ」

## 概要
非純粋Pipeは`pure: false`に設定されたPipeで、変更検知のたびに`transform`が再実行される。可変データや非同期状態を扱う場合に用いられるがパフォーマンスに注意が必要。

## 学習目標
- 非純粋Pipeの動作を理解する
- `pure: false`の設定方法を学ぶ
- どのようなケースで非純粋Pipeを使うべきか把握する

## 技術ポイント
- `@Pipe({ name: 'filter', pure: false })`
- 参照が変わらなくても毎回`transform`が呼ばれる
- 副作用や外部依存がある場合に利用

## 📺 画面表示用コード（動画用）
```typescript
@Pipe({ name: 'filter', pure: false, standalone: true })
export class FilterPipe implements PipeTransform { ... }
```

## 💻 詳細実装例（学習用）
```typescript
transform<T>(list: T[], predicate: (item: T) => boolean): T[] {
  return list?.filter(predicate) ?? [];
}
```

## ベストプラクティス
- どうしても必要な場合のみ非純粋Pipeを選択
- 処理は軽量に保ち、重い処理はコンポーネントやサービスで行う
- 非純粋Pipeの利用をドキュメント化し注意喚起

## 注意点
- 変更検知ごとに再計算されるためリストが大きいと性能劣化
- transform内で副作用を発生させない
- `async` Pipeとの組み合わせなど別のアプローチも検討

## 関連技術
- Pure Pipe
- Change Detection
- RxJS/AsyncPipe
