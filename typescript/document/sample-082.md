# #082 「テンプレートバインディング」

## 概要
TypeScript v5.9のテンプレートバインディングについて学習します。コンポーネントのプロパティをテンプレートに表示する機能を理解します。

## 学習目標
- テンプレートバインディングの基本を理解する
- {{}}記法の使用方法を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// テンプレートバインディング
import { Component } from '@angular/core';

@Component({
  selector: 'app-product',
  template: `
    <h2>{{productName}}</h2>
    <p>{{description}}</p>
    <span>{{price}}</span>
    <div>{{status}}</div>
  `
})
export class ProductComponent {
  productName: string = "TypeScript学習本";
  description: string = "TypeScriptの基礎から応用まで";
  price: string = "¥2,980";
  status: string = "在庫あり";
}
```

## 重要なポイント
1. **{{}}記法**: プロパティをテンプレートに表示
2. **データバインディング**: コンポーネントとテンプレートの連携
3. **実用性**: 動的なデータ表示に活用

## 次のステップ
次回は、Nest.jsのDTOとstring型について学習します。