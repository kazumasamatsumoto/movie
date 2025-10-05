# #210 「boolean配列」

## 概要
TypeScript v5.9のboolean配列について学習します。boolean型の要素を持つ配列の基本的な使用方法を理解します。

## 学習目標
- boolean配列の基本を理解する
- 配列の操作方法を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// boolean配列
let flags: boolean[] = [true, false, true];
let states: boolean[] = [false, true, false];

// 配列の操作
flags.push(true);
flags[0] = false;

// 実用的な例
let userPermissions: boolean[] = [true, false, true, true];
let formValidations: boolean[] = [true, true, false];

// 配列の要素にアクセス
console.log(userPermissions[0]); // true
console.log(formValidations[2]); // false
```

## 重要なポイント
1. **配列型**: boolean[]で型を指定
2. **要素操作**: push()やインデックスで操作
3. **実用性**: 複数の状態管理に活用

## 次のステップ
次回は、booleanリテラル型について学習します。
