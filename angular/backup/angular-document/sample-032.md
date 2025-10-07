# #032 「{{ }} 式の評価 - 計算とメソッド呼び出し」

## 概要
補間バインディング内では、プロパティの表示だけでなく、TypeScript式の評価、算術演算、メソッド呼び出しなどが可能です。シンプルな変換や計算をテンプレート内で直接実行できます。

## 学習目標
- 補間内での式の評価方法を理解する
- 算術演算や文字列操作の実装方法を学ぶ
- メソッド呼び出しの適切な使い方を理解する

## 技術ポイント
- TypeScript式の評価
- 算術演算子の使用
- メソッド呼び出しとパラメータ渡し
- 三項演算子の活用

## 📺 画面表示用コード（動画用）

```typescript
// component.ts
export class PriceComponent {
  price = 1000;
  getTotal() { return this.price * 1.1; }
}
```

```html
<!-- template.html -->
<p>税込: {{price * 1.1}}円</p>
<p>合計: {{getTotal()}}円</p>
```

```html
<!-- 三項演算子 -->
<p>{{price >= 1000 ? '高額' : '通常'}}</p>
```

## 💻 詳細実装例（学習用）

```typescript
// product.component.ts
import { Component } from '@angular/core';

@Component({
  selector: 'app-product',
  standalone: true,
  template: `
    <div class="product">
      <h2>{{productName}}</h2>

      <!-- 算術演算 -->
      <p>価格: {{price}}円</p>
      <p>税込: {{price * 1.1}}円</p>
      <p>割引後: {{price * 0.8}}円</p>

      <!-- 文字列結合 -->
      <p>商品コード: {{category + '-' + productId}}</p>

      <!-- メソッド呼び出し -->
      <p>ポイント: {{calculatePoints(price)}}pt</p>
      <p>送料: {{getShippingFee()}}円</p>

      <!-- 三項演算子 -->
      <p class="stock">{{stock > 0 ? '在庫あり' : '在庫切れ'}}</p>
      <p>{{price >= 5000 ? '送料無料' : '送料別途'}}</p>

      <!-- 論理演算 -->
      <p>{{isMember && price >= 3000 ? '会員割引適用' : ''}}</p>
    </div>
  `,
  styles: [`
    .product { padding: 20px; }
    .stock { font-weight: bold; }
  `]
})
export class ProductComponent {
  productName = 'ワイヤレスマウス';
  price = 3980;
  category = 'PC';
  productId = '12345';
  stock = 15;
  isMember = true;

  calculatePoints(price: number): number {
    return Math.floor(price * 0.01);
  }

  getShippingFee(): number {
    return this.price >= 5000 ? 0 : 500;
  }
}
```

## ベストプラクティス
- シンプルな計算や変換のみテンプレートで実行する
- 複雑なロジックはコンポーネントのメソッドに移動する
- 繰り返し使う式はgetterやメソッドにまとめる
- パフォーマンスを考慮し、重い処理はテンプレート外で実行する

## 注意点
- メソッド呼び出しは変更検知のたびに実行される可能性がある
- 副作用のあるメソッドは呼び出さない（データ変更など）
- 複雑な式は可読性を損なうため避ける
- null/undefinedチェックを適切に行う

## 関連技術
- Getter/Setter
- Pure Pipe（式の代替として効率的）
- Computed Signals（v20での新しいアプローチ）
- 変更検知メカニズム
