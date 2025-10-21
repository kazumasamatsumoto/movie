# #560 「パフォーマンスへの影響」

## 概要
非純粋Pipeは変更検知のたびにtransformを実行するため、重い処理を含むと描画パフォーマンスが低下し、UIのレスポンスが悪化する恐れがある。

## 学習目標
- 非純粋Pipeがパフォーマンスへ与える影響を理解する
- Pipe内の処理を最適化する方法を学ぶ
- 代替手段（コンポーネント/サービス/RxJS）の検討ポイントを把握する

## 技術ポイント
- transformはすべての変更検知サイクルで呼ばれる
- 重い処理、配列操作、大量の計算は避ける
- キャッシュやmemoizationが必要なら別のレイヤーで行う

## 📺 画面表示用コード（動画用）
```typescript
transform(items: T[], predicate: (item: T) => boolean): T[] {
  return items?.filter(predicate) ?? [];
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
- 遅い処理をPipeに入れず、コンポーネントやサービスで事前にデータを加工
- 非純粋Pipeが必要な場合は処理を軽量に保つ
- 性能を測定し問題がないことを確認

## 注意点
- 大量データや複雑な計算を非純粋Pipeで行うとフレーム落ちが発生
- Pipeをスタックするほど再計算が多くなる
- Change Detection戦略(OnPush)でも非純粋Pipeは頻繁に呼ばれる

## 関連技術
- Performance Profiling
- Change Detection戦略
- RxJSデータ加工
