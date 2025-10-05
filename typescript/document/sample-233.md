# #233 「ORとデフォルト値」

## 概要
TypeScript v5.9のORとデフォルト値について学習します。||演算子でデフォルト値を設定する方法を理解します。

## 学習目標
- ORとデフォルト値の設定方法を理解する
- 安全なデフォルト値設定を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// ORとデフォルト値
let userName: string | null = null;
let userAge: number | undefined = undefined;
let isActive: boolean | null = null;

// デフォルト値の設定
let displayName: string = userName || "Guest";
let displayAge: number = userAge || 0;
let displayStatus: boolean = isActive || false;

// 実用的な例
let userInput: string = "";
let defaultText: string = "デフォルトテキスト";
let result: string = userInput || defaultText; // "デフォルトテキスト"
```

## 重要なポイント
1. **デフォルト値**: 値がfalsyの場合にデフォルト値を設定
2. **安全な設定**: nullやundefinedを安全に処理
3. **実用性**: ユーザー入力の安全な処理に活用

## 次のステップ
次回は、論理否定NOTについて学習します。
