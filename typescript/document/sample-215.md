# #215 「基本まとめ」

## 概要
TypeScript v5.9のboolean型基本まとめについて学習します。boolean型の要点と重要な機能のまとめを理解します。

## 学習目標
- boolean型の要点を整理する
- 主要な機能の使い分けを理解する
- 実用的な応用を理解する

## 画面表示用コード

```typescript
// boolean型基本まとめ

// 1. 型宣言
let isActive: boolean = true;
let isCompleted: boolean = false;

// 2. 型推論
let userLoggedIn = true;    // boolean型と推論
let formValid = false;      // boolean型と推論

// 3. 条件分岐
if (isActive) {
  console.log("アクティブです");
}

// 4. 配列
let flags: boolean[] = [true, false, true];

// 5. 実用的な例
let userPermissions: boolean[] = [true, false, true];
```

## 重要なポイント
1. **型宣言**: : booleanで型を指定
2. **型推論**: 自動的な型推論
3. **条件分岐**: if文やwhile文で使用
4. **配列**: boolean[]で配列を宣言
5. **実用性**: アプリケーションの制御に活用

## 次のステップ
次回は、論理演算子について学習します。
