# #546 「transform() メソッド」

## 概要
`transform()`メソッドはPipeが実行する変換処理を実装する場所で、入力値と追加引数を受け取り、整形後の値を返す。

## 学習目標
- transformメソッドの役割とシグネチャを理解する
- 純粋関数として処理を書く重要性を学ぶ
- エラーハンドリングやデフォルト値の設定方法を把握する

## 技術ポイント
- `transform(value: T, ...args: U[]): R`
- 入力チェックを行い安全に処理
- 戻り値はテンプレートに直接表示される

## 📺 画面表示用コード（動画用）
```typescript
transform(value: string, limit = 20, suffix = '...'): string {
  if (!value || value.length <= limit) return value;
  return value.slice(0, limit) + suffix;
}
```

## 💻 詳細実装例（学習用）
```typescript
transform(value: number, digits: string = '1.0-0'): string {
  const pipe = new DecimalPipe('ja-JP');
  return pipe.transform(value, digits) ?? '';
}
```

## ベストプラクティス
- 入力値がundefined/nullの場合のフォールバックを用意
- 複雑な処理はサービスへ切り出しtransformで呼び出す
- 処理が重い場合は純粋Pipeであることを確認し、非純粋は避ける

## 注意点
- transform内で副作用を伴う処理は避ける
- PromiseやObservableを直接返さず同期的に完結させる
- ミュータブルなオブジェクトを変換する際はコピーを返す

## 関連技術
- PipeTransform
- DecimalPipeなど組み込みPipeの再利用
- エラーハンドリング
