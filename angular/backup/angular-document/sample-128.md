# #128 「Component 境界の設計」

## 概要
コンポーネント間の境界を明確に設計し、公開APIと内部実装を分離することで保守性を高める方法を学びます。

## 学習目標
- コンポーネントの公開API（Input/Output）を明確化する
- 内部状態と外部契約を分離する設計指針を理解する
- コンポーネント分割や命名のベストプラクティスを身につける

## 技術ポイント
- **公開API**: Input/Output、公開メソッド、Slot (`ng-content`)
- **内部実装**: 非公開な状態・メソッドはクラス内に閉じる
- **分割指針**: 複雑化したら小さなコンポーネントへ責務を分割

```typescript
@Input({ required: true }) product!: Product;
@Output() addToCart = new EventEmitter<number>();
```

```typescript
private readonly quantity = signal(1);
```

```html
<ng-content select="[suffix]"></ng-content>
```

## 💻 詳細実装例（学習用）
```typescript
// product-card.component.ts
import { Component, EventEmitter, Input, Output, computed, signal } from '@angular/core';

type Product = { id: number; name: string; price: number };

@Component({
  selector: 'app-product-card',
  standalone: true,
  templateUrl: './product-card.component.html',
  styleUrls: ['./product-card.component.css'],
})
export class ProductCardComponent {
  @Input({ required: true }) product!: Product;
  @Output() addToCart = new EventEmitter<{ id: number; quantity: number }>();

  private readonly quantity = signal(1);

  readonly totalPrice = computed(() => this.product.price * this.quantity());

  increment(): void {
    this.quantity.update((value) => value + 1);
  }

  decrement(): void {
    this.quantity.update((value) => Math.max(1, value - 1));
  }

  submit(): void {
    this.addToCart.emit({ id: this.product.id, quantity: this.quantity() });
  }
}
```

```html
<!-- product-card.component.html -->
<article class="product-card">
  <header>
    <h3>{{ product.name }}</h3>
    <ng-content select="[suffix]"></ng-content>
  </header>
  <section>
    <p>単価: {{ product.price | currency:'JPY' }}</p>
    <p>数量: {{ quantity() }}</p>
    <p>合計: {{ totalPrice() | currency:'JPY' }}</p>
    <button type="button" (click)="decrement()">-</button>
    <button type="button" (click)="increment()">+</button>
  </section>
  <footer>
    <button type="button" (click)="submit()">カートに入れる</button>
  </footer>
</article>
```

## ベストプラクティス
- 公開APIを最小限にし、Input/Outputの契約を明文化する
- クラス内部の状態はprivate/signalで管理し、外部から直接アクセスさせない
- `ng-content`などのスロットは限定的に公開し、ドキュメントで使用方法を記述する

## 注意点
- 役割が多くなったコンポーネントは責務ごとに分割し、境界を明確化する
- 内部APIを公開すると将来的なリファクタが難しくなるため慎重にする
- コンポーネント境界に大量のInput/Outputを追加する前に設計を見直す

## 関連技術
- Smart/Dumbコンポーネント分割
- Angular Style Guide（公開APIの設計）
- Signalsによる内部状態管理
