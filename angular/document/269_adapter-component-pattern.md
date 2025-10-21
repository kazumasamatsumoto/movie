# #269 「Adapter Component パターン」

## 概要
Adapter Componentパターンは、データソースとUIコンポーネントの間に変換専用のコンポーネントを配置し、ViewModelへマッピングして表示を安定させる手法である。

## 学習目標
- Adapter Componentの役割を理解する
- 生データからViewModelへのマッピングを実装する
- テスト容易な純粋変換ロジックを設計する

## 技術ポイント
- Inputで受けたドメインデータをViewModelへ変換
- 純粋関数でマッピングを切り出す
- Presentation Componentとの連携

## 📺 画面表示用コード（動画用）
```typescript
export type OrderDto = {
  id: string;
  customer_name: string;
  amount: number;
};
```

```typescript
export type OrderVm = {
  readonly id: string;
  readonly customer: string;
  readonly total: string;
};
```

```typescript
@Component({ selector: 'app-order-adapter', standalone: true, imports: [OrderViewComponent], template: `<app-order-view [vm]="vm"></app-order-view>` })
export class OrderAdapterComponent {
  @Input({ required: true }) dto!: Readonly<OrderDto>;
  protected get vm(): OrderVm { return mapOrder(this.dto); }
}
```

## 💻 詳細実装例（学習用）
```typescript
export function mapOrder(source: Readonly<OrderDto>): OrderVm {
  return {
    id: source.id,
    customer: source.customer_name,
    total: new Intl.NumberFormat('ja-JP', { style: 'currency', currency: 'JPY' }).format(source.amount),
  };
}

@Component({
  selector: 'app-order-view',
  standalone: true,
  template: `<div>{{ vm.customer }} - {{ vm.total }}</div>`
})
export class OrderViewComponent {
  @Input({ required: true }) vm!: Readonly<OrderVm>;
}
```

## ベストプラクティス
- Adapterでマッピングを一元化し、View側でのデータ変換をなくす
- 変換処理は純粋関数化して単体テストを容易にする
- DTOとViewModelの型を明確に分離して破壊的変更を検出しやすくする

## 注意点
- Adapterが肥大化したらドメイン別に分割する
- Adapterでビジネスロジックを増やさず変換に徹する
- DTO形式が変わった際はテストを更新して差分を検知する

## 関連技術
- DTO/ViewModelパターン
- 純粋関数
- Presentation Component
