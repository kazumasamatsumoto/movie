# #558 「pure: false の設定」

## 概要
非純粋Pipeを作成するには`@Pipe`デコレータで`pure: false`を指定する。これにより入力参照が同じでも変更検知ごとにtransformが実行される。

## 学習目標
- `pure: false`の設定方法を理解する
- 変更検知タイミングとの関係を学ぶ
- 設定変更によるパフォーマンスへの影響を把握する

## 技術ポイント
- `@Pipe({ name: 'filter', pure: false })`
- 非純粋Pipeは毎回transformが呼ばれる
- 可変データの変化を検知できる

## 📺 画面表示用コード（動画用）
```typescript
@Pipe({ name: 'filter', pure: false, standalone: true })
export class FilterPipe implements PipeTransform { ... }
```

## 💻 詳細実装例（学習用）
```typescript
@Pipe({
  name: 'search',
  pure: false,
  standalone: true
})
export class SearchPipe implements PipeTransform {
  transform(items: string[], keyword: string): string[] {
    return items?.filter(item => item.includes(keyword)) ?? [];
  }
}
```

## ベストプラクティス
- 非純粋Pipeの処理は軽量に保つ
- 非純粋Pipeを使用する理由をドキュメントで明示
- 可能ならObservableやコンポーネント処理で代替する

## 注意点
- 大きな配列や重い処理を非純粋Pipeで扱うとパフォーマンスが劣化
- transformで副作用を発生させると予期せぬ結果になる
- Change Detectionが頻繁に走る環境では特に注意

## 関連技術
- Pure Pipe
- Change Detection
- RxJS/AsyncPipe
