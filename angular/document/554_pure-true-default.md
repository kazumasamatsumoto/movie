# #554 「pure: true - デフォルト」

## 概要
@Pipeデコレータの`pure`プロパティはデフォルトで`true`になっており、純粋Pipeとして動作する。入力参照が変わる場合のみ再評価される。

## 学習目標
- `pure: true`の挙動を理解する
- デフォルト設定が純粋Pipeである理由を学ぶ
- 再評価条件を把握する

## 技術ポイント
- `@Pipe({ name: 'myPipe', pure: true })`
- プリミティブ値は値比較、参照型は参照比較
- Angularの変更検知で効率的に扱われる

## 📺 画面表示用コード（動画用）
```typescript
@Pipe({ name: 'example', pure: true, standalone: true })
export class ExamplePipe implements PipeTransform { ... }
```

## 💻 詳細実装例（学習用）
```typescript
transform(value: number[]): number {
  return value.reduce((sum, v) => sum + v, 0);
}
```

## ベストプラクティス
- 特別な理由がなければpure設定のまま使用
- 参照型の再評価が必要な場合はimmutableな更新を行う
- allowlist/denylistなどの軽量な処理に適用

## 注意点
- 配列のpushなど参照を変えない更新は検知されない
- 高頻度で変わるデータを扱う非純粋Pipeとの差を理解
- PromiseやObservableの結果を直接扱わない（AsyncPipeを利用）

## 関連技術
- Impure Pipe
- Change Detection Strategy
- Immutableデータ管理
