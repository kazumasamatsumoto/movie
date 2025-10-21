# #277 「Feature Component の設計」

## 概要
Feature Componentは特定のユースケースや業務フローをまとめ、Container/Presentationやサービスを束ねて提供する機能単位のコンポーネントである。

## 学習目標
- Feature Componentの責務と構成要素を理解する
- Signal Storeを用いた状態集約を学ぶ
- Routerやタブとの連携で視認性を高める

## 技術ポイント
- Feature単位のStandalone Component
- Signal Storeによる状態管理
- 子コンポーネントの調整役

## 📺 画面表示用コード（動画用）
```typescript
@Component({
  selector: 'app-orders-feature',
  standalone: true,
  imports: [OrdersContainerComponent],
  template: `<app-orders-container></app-orders-container>`
})
export class OrdersFeatureComponent {}
```

```typescript
@Injectable({ providedIn: 'root' })
export class OrdersFeatureStore {
  private readonly orders = signal<ReadonlyArray<OrderVm>>([]);
  readonly state = computed(() => ({ orders: this.orders() }));
  load(): void { /* API呼び出しでordersを更新 */ }
}
```

```typescript
export type OrderVm = {
  readonly id: string;
  readonly total: number;
};
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-orders-page',
  standalone: true,
  imports: [OrdersFeatureComponent, RouterOutlet],
  template: `
    <app-orders-feature></app-orders-feature>
    <router-outlet></router-outlet>
  `
})
export class OrdersPageComponent implements OnInit {
  private readonly store = inject(OrdersFeatureStore);

  ngOnInit(): void {
    this.store.load();
  }
}
```

## ベストプラクティス
- Feature Componentを調整役にし、詳細ロジックはContainerやサービスに委譲する
- Feature Storeで状態を集中管理し、子コンポーネントへViewModelを提供する
- Routerやレイアウトと連携して関連画面をまとめる

## 注意点
- Featureが肥大化した場合はサブFeatureへ分割する
- Feature ComponentにUIの詳細を詰め込まない
- Storeの公開APIは必要最小限に保つ

## 関連技術
- Angular Router
- Signal Store
- モジュールレス構成
