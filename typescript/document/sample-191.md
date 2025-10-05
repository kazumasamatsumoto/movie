# #191 「Angularフォームでのnumber型」

## 概要
TypeScript v5.9のAngularフォームでのnumber型について学習します。Angularのフォームでnumber型を扱う方法を理解します。

## 学習目標
- Angularフォームでのnumber型の使用方法を理解する
- FormControlでの型指定を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// Angularフォームでのnumber型
import { FormControl, FormGroup } from '@angular/forms';

// FormControlでのnumber型
let ageControl = new FormControl<number>(25);
let priceControl = new FormControl<number>(1500);

// FormGroupでのnumber型
let userForm = new FormGroup({
  age: new FormControl<number>(25),
  price: new FormControl<number>(1500)
});

// 実用的な例
let productForm = new FormGroup({
  price: new FormControl<number>(0),
  quantity: new FormControl<number>(1)
});
```

## 重要なポイント
1. **型指定**: FormControl<number>で型を指定
2. **FormGroup**: 複数のFormControlを管理
3. **実用性**: フォームの型安全性を保つ

## 次のステップ
次回は、数値バリデーションについて学習します。
