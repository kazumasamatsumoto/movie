# #559 「毎回の変更検知で再実行」

## 概要
非純粋Pipeは変更検知が走るたびに`transform`が再実行されるため、DOMイベントやタイマー、Observable更新などの影響を受けやすい。

## 学習目標
- 非純粋Pipeの再実行タイミングを理解する
- 変更検知の仕組みとPipe評価の関係を学ぶ
- パフォーマンスへの影響を把握する

## 技術ポイント
- `pure: false`指定時はすべてのチェックサイクルでtransform呼び出し
- 外部入力が変わらなくても再計算
- 重い処理を避ける／キャッシュ機構を検討

## 📺 画面表示用コード（動画用）
```typescript
transform(list: T[], predicate: (item: T) => boolean): T[] {
  console.log('filter pipe executed');
  return list?.filter(predicate) ?? [];
}
```

## 💻 詳細実装例（学習用）
```typescript
@Pipe({ name: 'filter', pure: false, standalone: true })
export class FilterPipe implements PipeTransform {
  transform<T>(list: T[], predicate: (item: T) => boolean): T[] {
    return list?.filter(predicate) ?? [];
  }
}
```

## ベストプラクティス
- 非純粋Pipeで重い処理を行わない
- 値をキャッシュし、必要な場合のみ計算する工夫を行う
- 変更検知の頻度を把握したうえで使用

## 注意点
- 大量データのフィルタやソートを非純粋Pipeで行うと大幅に遅くなる
- Debugログなどをtransform内に仕込むと大量出力される
- Pipeは純粋に戻れないため、利用前に十分検討

## 関連技術
- Change Detection
- Pure Pipe
- RxJSでの事前処理
