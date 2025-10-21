# #548 「戻り値の型定義」

## 概要
カスタムPipeはtransformメソッドの戻り値に型注釈を付けることで、テンプレート使用時の補完や型安全性を高められる。

## 学習目標
- transformの戻り値に型を設定する重要性を理解する
- ジェネリクスや型ガードを活用する方法を学ぶ
- Pipeの出力をテンプレートやコンポーネントで扱う際の安全性を把握する

## 技術ポイント
- `transform(value: string): string`
- 複合型の場合は`value: string | null`, `return string | null`など明示
- Contextに応じてジェネリクスで入力/出力を制約

## 📺 画面表示用コード（動画用）
```typescript
transform(value: number, digits: string = '1.0-0'): string { ... }
```

## 💻 詳細実装例（学習用）
```typescript
transform<T>(list: T[], predicate: (item: T) => boolean): T[] {
  if (!Array.isArray(list)) return [];
  return list.filter(predicate);
}
```

## ベストプラクティス
- 戻り値をanyにせず、実際の出力型を明確にする
- null/undefinedを返す可能性がある場合は型に含め、テンプレートで安全に扱う
- transform内で型チェックを行い予期しない入力を防ぐ

## 注意点
- Pipeの戻り値とテンプレート内の期待値が一致しないとエラーの原因になる
- タイプミスを防ぐため型エイリアスやインターフェースを活用
- 戻り値が複雑な場合は別クラス/型で構造を定義する

## 関連技術
- TypeScript型注釈
- Generics
- Template型チェック
