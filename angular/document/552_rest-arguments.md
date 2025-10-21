# #552 「可変長引数の実装」

## 概要
Pipeで可変長引数を受け取る際はrestパラメータを用い、テンプレートから渡された引数を配列として処理できる。

## 学習目標
- restパラメータを使って可変長引数を受け取る方法を理解する
- テンプレートから任意個の引数を渡す構文を学ぶ
- 引数を配列として処理する実装パターンを把握する

## 技術ポイント
- `transform(value: T, ...args: string[])`
- テンプレート: `{{ value | myPipe:'a':'b':'c' }}`
- args配列の順序をドキュメント化

## 📺 画面表示用コード（動画用）
```typescript
transform(value: string, ...parts: string[]): string {
  return [value, ...parts].join(' ');
}
```

## 💻 詳細実装例（学習用）
```typescript
transform(value: string, ...parts: string[]): string {
  if (!parts.length) return value;
  return `${value} (${parts.join(', ')})`;
}
```

## ベストプラクティス
- 可変長引数の内容を明確に定義し、テンプレート使用例をドキュメント化
- args配列の長さが足りない場合のフォールバックを実装
- オプションが多い場合はオブジェクト引数やカスタム設定を検討

## 注意点
- 可変長引数は順序で意味が変わるため使いすぎると可読性が下がる
- 参照型引数はimmutableで渡すことを推奨
- Pipeの引数はテンプレートからのみ渡せることを理解

## 関連技術
- Restパラメータ
- PipeTransform
- カスタムPipeドキュメント
