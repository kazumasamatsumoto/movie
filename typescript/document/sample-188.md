# #188 「BigIntの使用例」

## 概要
TypeScript v5.9のBigIntの使用例について学習します。大きな数値の計算やIDの扱いなどの実用的な使用例を理解します。

## 学習目標
- BigIntの実用的な使用例を理解する
- 大きな数値の計算方法を理解する
- ID生成の活用方法を理解する

## 画面表示用コード

```typescript
// BigIntの使用例
let userId: bigint = 1234567890123456789n;
let transactionId: bigint = BigInt("9876543210987654321");

// 演算
let newId: bigint = userId + 1n;
let multiplied: bigint = userId * 2n;

// 実用的な例
function generateId(): bigint {
  return BigInt(Date.now()) * 1000n + BigInt(Math.floor(Math.random() * 1000));
}

let newUserId: bigint = generateId();
console.log(newUserId.toString());
```

## 重要なポイント
1. **大きな数値**: number型の制限を超える数値
2. **ID生成**: ユニークなIDの生成
3. **実用性**: 暗号化やトランザクションIDに活用

## 次のステップ
次回は、浮動小数点のベストプラクティスについて学習します。
