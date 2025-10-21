# #566 「Filter Pipe - フィルタリング」

## 概要
FilterPipeは配列を条件で絞り込むPipeだが、純粋Pipeでは参照が変わらない限り再評価されないため、mutableな配列更新と組み合わせる場合は非純粋Pipeかimmutable戦略を検討する。

## 学習目標
- FilterPipeの基本的な使い方と課題を理解する
- 純粋/非純粋Pipeでの挙動の違いを把握する
- 可変配列を扱う際の対策を学ぶ

## 技術ポイント
- `transform(list: T[], predicate: (item: T) => boolean): T[]`
- 純粋Pipeなら新しい配列を生成して渡す
- 非純粋Pipe(pure:false)なら常に再評価される

## 📺 画面表示用コード（動画用）
```html
<li *ngFor="let item of items | filter:byCategory">{{ item.name }}</li>
```

## 💻 詳細実装例（学習用）
```typescript
@Pipe({ name: 'filter', standalone: true })
export class FilterPipe implements PipeTransform {
  transform<T>(list: readonly T[], predicate: (item: T) => boolean): T[] {
    if (!Array.isArray(list)) return [];
    return list.filter(predicate);
  }
}
```

## ベストプラクティス
- immutable更新と組み合わせて純粋Pipeのまま利用
- フィルタリングはコンポーネントやサービスで行い結果をPipeで表示
- 非純粋Pipeを使う場合は処理を軽量に保ちパフォーマンス測定

## 注意点
- 大量データを毎回filterすると描画が遅くなる
- predicate関数に副作用を含めない
- 非純粋Pipeにすると全変更検知で再計算されるため慎重に

## 関連技術
- Pure/Impure Pipe
- Immutableデータ
- RxJSでのフィルタ処理
