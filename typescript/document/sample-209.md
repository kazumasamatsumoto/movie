# #209 「三項演算子」

## 概要
TypeScript v5.9の三項演算子でのboolean型使用について学習します。三項演算子の条件式でboolean型の変数を使用する方法を理解します。

## 学習目標
- 三項演算子でのboolean型使用を理解する
- 条件付きの値設定を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// 三項演算子での使用
let isActive: boolean = true;
let isCompleted: boolean = false;

// 基本的な使用
let status: string = isActive ? "アクティブ" : "非アクティブ";
let message: string = isCompleted ? "完了" : "未完了";

// 実用的な例
let userLoggedIn: boolean = true;
let displayText: string = userLoggedIn ? "ログイン中" : "ログアウト中";

console.log(status);    // "アクティブ"
console.log(message);   // "未完了"
console.log(displayText); // "ログイン中"
```

## 重要なポイント
1. **条件付き値**: 条件に応じて値を設定
2. **簡潔性**: if文より簡潔に記述
3. **実用性**: 表示テキストの制御に活用

## 次のステップ
次回は、boolean配列について学習します。
