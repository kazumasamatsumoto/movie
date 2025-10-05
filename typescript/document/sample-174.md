# #174 「型安全な変換」

## 概要
TypeScript v5.9の型安全な変換について学習します。TypeScriptの型システムを活用した安全な変換方法を理解します。

## 学習目標
- 型安全な変換の重要性を理解する
- 型ガードの使用方法を理解する
- ユニオン型を活用した変換を理解する

## 画面表示用コード

```typescript
// 型安全な変換
function isNumber(value: unknown): value is number {
  return typeof value === "number" && Number.isFinite(value);
}

function safeConvert(value: unknown): number | null {
  if (isNumber(value)) {
    return value;
  }
  
  if (typeof value === "string") {
    let converted = Number(value);
    return Number.isNaN(converted) ? null : converted;
  }
  
  return null;
}

// 実用的な例
let userInput: unknown = "25";
let userAge: number | null = safeConvert(userInput);

if (userAge !== null) {
  console.log(`年齢: ${userAge}`);
}
```

## 重要なポイント
1. **型安全**: TypeScriptの型システムを活用
2. **型ガード**: 型の判定を行う関数
3. **ユニオン型**: 複数の型を扱う

## 次のステップ
次回は、数値変換まとめについて学習します。
