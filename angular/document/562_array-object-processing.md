# #562 「配列・オブジェクトの処理」

## 概要
配列やオブジェクトをPipeで処理する場合、純粋Pipeでは参照が変わらない限り再評価されないため、immutableな更新や非純粋Pipeの検討が必要になる。

## 学習目標
- 配列/オブジェクトを扱うPipeの再評価条件を理解する
- immutableな更新で参照を変更する手法を学ぶ
- 非純粋Pipeを使う際の注意点を把握する

## 技術ポイント
- 純粋Pipe: `value === previousValue`で比較
- `items = [...items, newItem]`のように参照を変える
- 非純粋Pipeは`pure: false`で毎回再評価

## 📺 画面表示用コード（動画用）
```typescript
// immutable更新例
this.items = this.items.filter(item => item !== removed);
```

## 💻 詳細実装例（学習用）
```typescript
@Pipe({ name: 'filter', standalone: true })
export class FilterPipe implements PipeTransform {
  transform<T>(list: readonly T[], predicate: (item: T) => boolean): T[] {
    return list.filter(predicate);
  }
}
```

## ベストプラクティス
- 配列/オブジェクトの更新はスプレッドやmapで新しい参照を生成
- 変更検知が効かない場合は非純粋Pipeよりもデータ更新戦略を見直す
- NgRxなどの状態管理ライブラリと相性が良い

## 注意点
- mutable更新（push/splice）は純粋Pipeで検知されない
- 非純粋Pipeに頼るとパフォーマンス低下
- 大量データの配列処理はPipeではなくコンポーネント/サービスで行う

## 関連技術
- Immutableデータパターン
- Impure Pipe
- State管理（NgRxなど）
