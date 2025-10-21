# #252 「Dumb Component - 純粋なコンポーネント」

## 概要
Dumb Componentは入力されたデータをそのまま表示し、イベントを親へ通知することに専念する表示専用コンポーネントである。

## 学習目標
- Dumb Componentの責務と制約を明確にする
- Input/Outputでインターフェースを定義する方法を学ぶ
- OnPush戦略で再レンダリングを最適化する

## 技術ポイント
- ChangeDetectionStrategy.OnPushによる純粋コンポーネント化
- イミュータブルなViewModelの受け渡し
- EventEmitterでのイベント通知

## 📺 画面表示用コード（動画用）
```typescript
@Component({
  selector: 'app-order-summary',
  standalone: true,
  template: `
    <h3>{{ order.title }}</h3>
    <p>{{ order.total | currency:'JPY' }}</p>
  `,
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class OrderSummaryComponent {
  @Input({ required: true }) order!: Readonly<Order>;
}
```

```typescript
@Component({
  selector: 'app-order-summary-actions',
  standalone: true,
  template: `<button type="button" (click)="confirm.emit()">確定</button>`,
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class OrderSummaryActionsComponent {
  @Output() confirm = new EventEmitter<void>();
}
```

```typescript
export type Order = {
  readonly title: string;
  readonly total: number;
};
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-order-summary-card',
  standalone: true,
  imports: [OrderSummaryComponent, OrderSummaryActionsComponent],
  template: `
    <article class="card">
      <app-order-summary [order]="order"></app-order-summary>
      <app-order-summary-actions (confirm)="onConfirm()"></app-order-summary-actions>
    </article>
  `,
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class OrderSummaryCardComponent {
  @Input({ required: true }) order!: Readonly<Order>;
  @Output() confirmed = new EventEmitter<void>();

  onConfirm(): void {
    this.confirmed.emit();
  }
}
```

## ベストプラクティス
- ビジネスロジックはコンポーネント外へ委譲し、UI表示に集中させる
- イミュータブルなデータをInputで受け取り、参照の変更で再描画を制御する
- Outputは意味のあるイベント名にして利用側の可読性を高める

## 注意点
- EventEmitterは同期的に発火するため、親側での副作用に注意する
- フォーム制御や状態管理を持たせない
- Templateでの複雑な計算はPipeへ切り出し描画コストを抑える

## 関連技術
- Smart/Container Component
- Angular Signals
- Standalone Component
