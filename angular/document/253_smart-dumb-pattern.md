# #253 「Smart/Dumb パターンの実践」

## 概要
Smart/Dumbパターンは、Smart Componentが状態とデータ取得を担当し、Dumb ComponentがUI描画とイベント通知に集中することで責務を明確に分離する設計である。

## 学習目標
- Smart/Dumbパターンの役割分担を理解する
- SignalとEventEmitterを用いた双方向のやり取りを実践する
- Feature単位での再利用しやすい構成を設計する

## 技術ポイント
- Standalone Componentによる軽量構成
- Signal Storeによる状態管理
- Input/Outputでの疎結合な連携

## 📺 画面表示用コード（動画用）
```typescript
@Component({ selector: 'app-orders-container', standalone: true, imports: [OrdersViewComponent], template: `<app-orders-view [orders]="orders()" (refresh)="reload()" />` })
export class OrdersContainerComponent {
  private readonly store = inject(OrdersStore);
  readonly orders = this.store.orders;
  reload(): void { this.store.load(); }
}
```

```typescript
@Component({
  selector: 'app-orders-view',
  standalone: true,
  template: `<ul>@for (order of orders; track order.id) {<li>{{ order.customer }} - {{ order.total | currency:'JPY' }}</li>}</ul><button (click)="refresh.emit()">再読み込み</button>`,
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class OrdersViewComponent {
  @Input({ required: true }) orders: ReadonlyArray<Order> = [];
  @Output() refresh = new EventEmitter<void>();
}
```

```typescript
@Injectable({ providedIn: 'root' })
export class OrdersStore {
  private readonly ordersSignal = signal<ReadonlyArray<Order>>([]);
  readonly orders = computed(() => this.ordersSignal());
  load(): void { /* API呼び出しでordersSignalを更新 */ }
}
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-orders-feature',
  standalone: true,
  imports: [OrdersContainerComponent],
  template: `
    <section>
      <h2>最新の注文</h2>
      <app-orders-container></app-orders-container>
    </section>
  `
})
export class OrdersFeatureComponent implements OnInit {
  private readonly store = inject(OrdersStore);

  ngOnInit(): void {
    this.store.load();
  }
}
```

## ベストプラクティス
- Smart ComponentにHTTPやSignal Storeを集約し、副作用を1箇所に閉じ込める
- Dumb Componentは`ChangeDetectionStrategy.OnPush`で純粋関数的に振る舞わせる
- Input/OutputのインターフェースをTypeで定義し、用途を明確化する

## 注意点
- Smart Componentが肥大化しないよう機能単位で分割する
- Dumb Componentにビジネスロジックを持たせない
- イベントハンドラは同期的に処理されるため、エラー制御はSmart側に置く

## 関連技術
- Angular Signals
- Standalone Component
- Featureモジュール設計
