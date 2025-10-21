# #258 「Pure Component の実装」

## 概要
Pure Componentは入力が変化した場合にのみ再レンダリングされるよう設計されたコンポーネントで、予測可能な表示を保つことでパフォーマンスとテスト性を高める。

## 学習目標
- ChangeDetectionStrategy.OnPushの効果を理解する
- イミュータブルなViewModelの受け渡しを実践する
- テンプレートでの副作用を排除する方法を学ぶ

## 技術ポイント
- OnPushによる差分検知
- readonlyなInput契約
- 純粋Pipeとの組み合わせ

## 📺 画面表示用コード（動画用）
```typescript
@Component({
  selector: 'app-product-price',
  standalone: true,
  template: `<p>{{ vm.name }}: {{ vm.price | currency:'JPY' }}</p>`,
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class ProductPriceComponent {
  @Input({ required: true }) vm!: Readonly<ProductPriceVm>;
}
```

```typescript
@Pipe({ name: 'discount', standalone: true, pure: true })
export class DiscountPipe implements PipeTransform {
  transform(price: number, rate: number): number {
    return Math.round(price * (1 - rate));
  }
}
```

```typescript
export type ProductPriceVm = {
  readonly name: string;
  readonly price: number;
};
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-product-price-card',
  standalone: true,
  imports: [ProductPriceComponent, DiscountPipe],
  template: `
    <article>
      <app-product-price [vm]="vm"></app-product-price>
      <p>割引後: {{ vm.price | discount:vm.discountRate | currency:'JPY' }}</p>
    </article>
  `,
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class ProductPriceCardComponent {
  @Input({ required: true }) vm!: Readonly<ProductPriceVm & { discountRate: number }>;
}
```

## ベストプラクティス
- Inputはreadonlyにし、オブジェクトの再割り当てで変化を伝える
- テンプレートの演算は純粋Pipeに移し、副作用を排除する
- OnPushとイミュータブルデータをセットで採用する

## 注意点
- Inputに可変オブジェクトを渡すとOnPushの効果が薄れる
- Signalを直接Inputで受け取ると純粋性が損なわれる可能性がある
- 重たい計算は事前にViewModelへ整形しておく

## 関連技術
- Angular Signals
- Change Detection戦略
- Pure Pipe
