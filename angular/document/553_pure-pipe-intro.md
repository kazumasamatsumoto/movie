# #553 「Pure Pipe - 純粋パイプ」

## 概要
純粋Pipeは入力値の参照が変わった場合のみ再評価されるパイプで、デフォルト設定。副作用を持たない純粋関数として実装し、パフォーマンスに優れる。

## 学習目標
- 純粋Pipeの動作原理を理解する
- 参照が変わらない場合は再評価されない仕組みを学ぶ
- パフォーマンス面のメリットを把握する

## 技術ポイント
- `@Pipe({ name: 'myPipe', pure: true })`（デフォルト）
- プリミティブは値比較、オブジェクト/配列は参照比較
- 副作用を避け純粋な変換のみ行う

## 📺 画面表示用コード（動画用）
```typescript
@Pipe({ name: 'truncate', standalone: true })
export class TruncatePipe implements PipeTransform { ... }
```

## 💻 詳細実装例（学習用）
```typescript
transform(list: string[]): string[] {
  return list.map(item => item.trim());
}
```

## ベストプラクティス
- immutableなデータ構造と組み合わせて高いパフォーマンスを確保
- 重い処理でも純粋Pipeなら変更検知の最適化が効く
- 副作用が必要な処理は別の手段（コンポーネント/サービス）へ分離

## 注意点
- mutableな配列を変更しても参照が同じなら再評価されない
- 参照型を再計算したい場合は新しいオブジェクトを返す
- 純粋であることを保つためtransform内で状態変更しない

## 関連技術
- Impure Pipe
- Change Detection
- immutabilityパターン
