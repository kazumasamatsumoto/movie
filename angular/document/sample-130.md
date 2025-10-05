# #130 「Component 通信の実践例」

## 概要
Angular v20におけるコンポーネント通信の実践的な活用例。Eコマース、ダッシュボード、フォーム管理などの実際のプロジェクトで使用される具体的な実装パターンを学び、実践的なスキルを習得する。

## 学習目標
- 実際のプロジェクトでの活用例を理解する
- 具体的な実装パターンを学ぶ
- 実践的なスキルを習得する

## 技術ポイント
- Eコマースアプリケーションでの商品選択
- ダッシュボードでのリアルタイム更新
- フォーム管理での状態共有
- 複雑なユーザーインタラクション

## 📺 画面表示用コード

### Eコマース商品選択
```typescript
@Injectable()
export class ShoppingCartService {
  private _cartItems = signal<CartItem[]>([]);
  cartItems = this._cartItems.asReadonly();
  
  addToCart(product: Product) {
    this._cartItems.update(items => {
      const existingItem = items.find(item => item.id === product.id);
      if (existingItem) {
        return items.map(item => 
          item.id === product.id 
            ? { ...item, quantity: item.quantity + 1 }
            : item
        );
      }
      return [...items, { ...product, quantity: 1 }];
    });
  }
}

@Component({
  selector: 'app-product-card',
  template: `
    <div class="product-card">
      <h3>{{ product.name }}</h3>
      <p>{{ product.price | currency }}</p>
      <button (click)="addToCart()">カートに追加</button>
    </div>
  `
})
export class ProductCardComponent {
  @Input() product!: Product;
  
  private cartService = inject(ShoppingCartService);
  
  addToCart() {
    this.cartService.addToCart(this.product);
  }
}
```

### ダッシュボードリアルタイム更新
```typescript
@Injectable()
export class DashboardService {
  private _metrics = signal<DashboardMetrics>({
    users: 0,
    orders: 0,
    revenue: 0
  });
  metrics = this._metrics.asReadonly();
  
  updateMetrics(newMetrics: DashboardMetrics) {
    this._metrics.set(newMetrics);
  }
}

@Component({
  selector: 'app-metrics-widget',
  template: `
    <div class="metrics-widget">
      <div>ユーザー: {{ metrics().users }}</div>
      <div>注文数: {{ metrics().orders }}</div>
      <div>売上: {{ metrics().revenue | currency }}</div>
    </div>
  `
})
export class MetricsWidgetComponent {
  private dashboardService = inject(DashboardService);
  metrics = this.dashboardService.metrics;
}
```

### フォーム状態管理
```typescript
@Injectable()
export class FormStateService {
  private _formData = signal<FormData>({});
  private _isValid = signal(false);
  
  formData = this._formData.asReadonly();
  isValid = this._isValid.asReadonly();
  
  updateField(field: string, value: any) {
    this._formData.update(data => ({
      ...data,
      [field]: value
    }));
    this.validateForm();
  }
  
  private validateForm() {
    const data = this._formData();
    this._isValid.set(
      Object.keys(data).length > 0 && 
      Object.values(data).every(value => value !== '')
    );
  }
}
```

## 実践的な活用例
- オンラインショッピングサイト
- 管理ダッシュボード
- 複雑なフォームアプリケーション
- リアルタイムチャットアプリ

## ベストプラクティス
- 実際のユースケースに基づいた設計
- パフォーマンスを考慮した実装
- ユーザビリティを重視した設計
- スケーラビリティを考慮した実装

## 注意点
- 実装の複雑さを管理する
- パフォーマンステストを実施する
- ユーザビリティテストを行う

## 関連技術
- 実践的なアプリケーション開発
- 状態管理
- ユーザーインタラクション
- パフォーマンス最適化
