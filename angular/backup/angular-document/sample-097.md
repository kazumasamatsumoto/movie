# #097 「@Input() プリミティブ型の受け渡し」

## 概要
文字列・数値・真偽値などプリミティブ型を@Input()で受け渡す際の基本と、子コンポーネントでの扱い方を学びます。

## 学習目標
- プリミティブ型のデータフローを理解する
- 子コンポーネントでの読み取り専用利用を徹底する
- 親へ変更を返したい場合の考え方を習得する

## 技術ポイント
- **値渡し**: プリミティブはコピーされるため子で変更しても親へ影響しない
- **テンプレート利用**: 直接表示やパイプでフォーマット
- **変更通知**: 値を変えたい場合は@Output()で親へ伝える


```typescript
@Input() price = 0;
```

```html
<app-price-tag [price]="item.price"></app-price-tag>
```

```html
<span>{{ price | currency:'JPY' }}</span>
```

## 💻 詳細実装例（学習用）
```typescript
import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-price-tag',
  standalone: true,
  templateUrl: './price-tag.component.html',
})
export class PriceTagComponent {
  @Input() price = 0;
  @Input() currencyCode: string = 'JPY';
  @Input() highlight = false;
}
```

```html
<!-- price-tag.component.html -->
<span
  class="price-tag"
  [class.highlight]="highlight"
>
  {{ price | currency: currencyCode:'symbol':'1.0-0' }}
</span>
```

```typescript
// parent.component.ts
import { Component } from '@angular/core';
import { PriceTagComponent } from './price-tag.component';

@Component({
  selector: 'app-product-row',
  standalone: true,
  imports: [PriceTagComponent],
  templateUrl: './product-row.component.html',
})
export class ProductRowComponent {
  price = 1280;
  currencyCode = 'JPY';
}
```

```html
<!-- product-row.component.html -->
<app-price-tag
  [price]="price"
  [currencyCode]="currencyCode"
  [highlight]="price < 1500"
></app-price-tag>
```

## ベストプラクティス
- プリミティブ値は子で更新せず、変更が必要ならイベントで親へ知らせる
- 表示フォーマットはパイプに委譲し、ロジックをコンポーネント内に書かない
- 初期値を設定しておくことで親が渡さなくても安全な状態を維持する

## 注意点
- テンプレートで`[price]="price"`とtwo-way bindingを勘違いしやすいため命名に気を付ける
- booleanプロパティをバインディングするときは真偽値を明示し、文字列にならないようにする
- プリミティブを@Input()にするときはnullableかどうかを明確に示す

## 関連技術
- Angularパイプ（currency, number, dateなど）
- @Output()でのイベント通知
- Signalsとの組み合わせ（SignalInput）
