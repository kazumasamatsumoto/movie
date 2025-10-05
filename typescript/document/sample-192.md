# #192 「数値バリデーション」

## 概要
TypeScript v5.9の数値バリデーションについて学習します。数値の有効性を検証する方法を理解します。

## 学習目標
- 数値バリデーションの重要性を理解する
- Validatorsの使用方法を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// 数値バリデーション
import { FormControl, Validators } from '@angular/forms';

// 基本的なバリデーション
let ageControl = new FormControl(25, [
  Validators.required,
  Validators.min(0),
  Validators.max(120)
]);

let priceControl = new FormControl(1500, [
  Validators.required,
  Validators.min(0)
]);

// 実用的な例
let productForm = new FormGroup({
  price: new FormControl(0, [
    Validators.required,
    Validators.min(1)
  ]),
  quantity: new FormControl(1, [
    Validators.required,
    Validators.min(1)
  ])
});
```

## 重要なポイント
1. **Validators**: バリデーション機能の提供
2. **min/max**: 数値の範囲チェック
3. **実用性**: フォームの入力検証に活用

## 次のステップ
次回は、Nest.jsのDTOとnumber型について学習します。
