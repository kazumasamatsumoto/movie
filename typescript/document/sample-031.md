# #031 「複数行文字列の実例 - HTMLテンプレート」

## 概要
TypeScript v5.9の複数行文字列実例について学習します。HTMLテンプレートをテンプレートリテラルで記述する方法を理解します。

## 学習目標
- HTMLテンプレートの記述方法を理解する
- 動的なHTML生成を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// HTMLテンプレートの例
let product = {
  name: "TypeScript学習本",
  price: 2980,
  description: "TypeScriptの基礎から応用まで"
};

// HTMLテンプレート
let productCard: string = `
<div class="product-card">
  <h3 class="product-title">${product.name}</h3>
  <p class="product-description">${product.description}</p>
  <div class="product-price">¥${product.price}</div>
  <button class="add-to-cart">カートに追加</button>
</div>
`;

// 実用的な例
let user = { name: "Alice", role: "admin" };
let userProfile: string = `
<div class="profile">
  <h2>${user.name}</h2>
  <span class="role-badge">${user.role}</span>
</div>
`;
```

## 重要なポイント
1. **HTML構造**: 複雑なHTML構造も簡単に記述
2. **動的データ**: 変数を使って動的なHTMLを生成
3. **可読性**: HTMLの構造が視覚的に分かりやすい

## 次のステップ
次回は、テンプレートリテラルのインデントについて学習します。