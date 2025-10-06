# #256 「Presentation/Container 分離」

## 概要
Presentation/Container分離は、UIの表示（Presentation）とビジネスロジック（Container）を明確に分離する設計パターンです。この分離により、テスタビリティ、再利用性、保守性が向上し、チーム開発でも役割分担が明確になります。

## 学習目標
- Presentation/Container分離の原則を理解する
- 適切な分離ポイントの見極め方を習得する
- 実践的な分離手法を学ぶ

## 技術ポイント
- **明確な境界**: データとロジックの責任分離
- **単方向フロー**: データの流れを一方向に
- **疎結合**: コンポーネント間の依存を最小化

## 📺 画面表示用コード

### 基本的な分離パターン
```typescript
// Presentation Component
@Component({
  selector: 'app-user-profile',
  template: `
    <div class="profile">
      <h2>{{ user().name }}</h2>
      <p>{{ user().email }}</p>
      <button (click)="edit.emit()">編集</button>
    </div>
  `,
  standalone: true
})
export class UserProfileComponent {
  user = input.required<User>();
  edit = output<void>();
}

// Container Component
@Component({
  selector: 'app-user-profile-container',
  template: `
    <app-user-profile
      [user]="user()"
      (edit)="handleEdit()"
    />
  `,
  standalone: true,
  imports: [UserProfileComponent]
})
export class UserProfileContainerComponent {
  private userService = inject(UserService);
  private router = inject(Router);

  user = signal<User | null>(null);

  async ngOnInit() {
    const data = await this.userService.getCurrentUser();
    this.user.set(data);
  }

  handleEdit() {
    this.router.navigate(['/profile/edit']);
  }
}
```

### リスト表示の分離
```typescript
// Presentation
@Component({
  selector: 'app-product-list',
  template: `
    @if (loading()) {
      <div class="loading">読み込み中...</div>
    } @else {
      @for (product of products(); track product.id) {
        <div class="product" (click)="select.emit(product)">
          <h3>{{ product.name }}</h3>
          <p>¥{{ product.price }}</p>
        </div>
      }
    }
  `,
  standalone: true
})
export class ProductListComponent {
  products = input<Product[]>([]);
  loading = input(false);
  select = output<Product>();
}

// Container
@Component({
  selector: 'app-products-container',
  template: `
    <app-product-list
      [products]="products()"
      [loading]="loading()"
      (select)="handleSelect($event)"
    />
  `
})
export class ProductsContainerComponent {
  private productService = inject(ProductService);

  products = signal<Product[]>([]);
  loading = signal(false);

  async ngOnInit() {
    this.loading.set(true);
    this.products.set(await this.productService.getAll());
    this.loading.set(false);
  }

  handleSelect(product: Product) {
    console.log('Selected:', product);
  }
}
```

### フォームの分離
```typescript
// Presentation
@Component({
  selector: 'app-login-form',
  template: `
    <form (ngSubmit)="submit.emit(formData)">
      <input
        [(ngModel)]="formData.email"
        placeholder="メール"
        name="email">
      <input
        [(ngModel)]="formData.password"
        type="password"
        placeholder="パスワード"
        name="password">

      @if (error()) {
        <p class="error">{{ error() }}</p>
      }

      <button type="submit" [disabled]="submitting()">
        {{ submitting() ? 'ログイン中...' : 'ログイン' }}
      </button>
    </form>
  `,
  standalone: true,
  imports: [FormsModule]
})
export class LoginFormComponent {
  error = input<string>();
  submitting = input(false);
  submit = output<LoginData>();

  formData = { email: '', password: '' };
}

// Container
@Component({
  selector: 'app-login-container',
  template: `
    <app-login-form
      [error]="error()"
      [submitting]="submitting()"
      (submit)="handleSubmit($event)"
    />
  `
})
export class LoginContainerComponent {
  private authService = inject(AuthService);
  private router = inject(Router);

  error = signal<string | null>(null);
  submitting = signal(false);

  async handleSubmit(data: LoginData) {
    this.submitting.set(true);
    this.error.set(null);

    try {
      await this.authService.login(data);
      this.router.navigate(['/dashboard']);
    } catch (err) {
      this.error.set('ログインに失敗しました');
    } finally {
      this.submitting.set(false);
    }
  }
}
```

## 実践的な活用例

### ダッシュボードの分離
```typescript
// Presentation: ダッシュボード表示
@Component({
  selector: 'app-dashboard-view',
  template: `
    <div class="dashboard">
      <app-stats-card
        [stats]="stats()"
        [loading]="loading()"
      />

      <app-recent-activity
        [activities]="activities()"
      />

      <app-chart
        [data]="chartData()"
      />

      <button (click)="refresh.emit()">更新</button>
    </div>
  `,
  standalone: true,
  imports: [StatsCardComponent, RecentActivityComponent, ChartComponent]
})
export class DashboardViewComponent {
  stats = input<DashboardStats>();
  activities = input<Activity[]>([]);
  chartData = input<ChartData[]>([]);
  loading = input(false);
  refresh = output<void>();
}

// Container: データ管理とロジック
@Component({
  selector: 'app-dashboard-container',
  template: `
    <app-dashboard-view
      [stats]="stats()"
      [activities]="activities()"
      [chartData]="chartData()"
      [loading]="loading()"
      (refresh)="loadDashboardData()"
    />
  `
})
export class DashboardContainerComponent {
  private statsService = inject(StatsService);
  private activityService = inject(ActivityService);
  private chartService = inject(ChartService);

  stats = signal<DashboardStats | undefined>(undefined);
  activities = signal<Activity[]>([]);
  chartData = signal<ChartData[]>([]);
  loading = signal(false);

  ngOnInit() {
    this.loadDashboardData();
  }

  async loadDashboardData() {
    this.loading.set(true);

    try {
      const [stats, activities, chartData] = await Promise.all([
        this.statsService.getStats(),
        this.activityService.getRecent(),
        this.chartService.getData()
      ]);

      this.stats.set(stats);
      this.activities.set(activities);
      this.chartData.set(chartData);
    } catch (err) {
      console.error('データ取得エラー:', err);
    } finally {
      this.loading.set(false);
    }
  }
}
```

### 検索機能の分離
```typescript
// Presentation: 検索UI
@Component({
  selector: 'app-search-view',
  template: `
    <div class="search">
      <input
        [value]="query()"
        (input)="search.emit($any($event.target).value)"
        placeholder="検索...">

      <app-filter-panel
        [filters]="filters()"
        (filterChange)="filterChange.emit($event)"
      />

      <div class="results">
        @if (searching()) {
          <div>検索中...</div>
        } @else if (results().length === 0) {
          <div>結果がありません</div>
        } @else {
          @for (item of results(); track item.id) {
            <app-search-result-item
              [item]="item"
              (click)="itemClick.emit(item)"
            />
          }
        }
      </div>
    </div>
  `,
  standalone: true,
  imports: [FilterPanelComponent, SearchResultItemComponent]
})
export class SearchViewComponent {
  query = input('');
  filters = input<SearchFilters>({});
  results = input<SearchResult[]>([]);
  searching = input(false);

  search = output<string>();
  filterChange = output<SearchFilters>();
  itemClick = output<SearchResult>();
}

// Container: 検索ロジック
@Component({
  selector: 'app-search-container',
  template: `
    <app-search-view
      [query]="query()"
      [filters]="filters()"
      [results]="filteredResults()"
      [searching]="searching()"
      (search)="handleSearch($event)"
      (filterChange)="handleFilterChange($event)"
      (itemClick)="handleItemClick($event)"
    />
  `
})
export class SearchContainerComponent {
  private searchService = inject(SearchService);
  private router = inject(Router);

  query = signal('');
  filters = signal<SearchFilters>({});
  rawResults = signal<SearchResult[]>([]);
  searching = signal(false);

  filteredResults = computed(() => {
    return this.applyFilters(this.rawResults(), this.filters());
  });

  async handleSearch(query: string) {
    this.query.set(query);

    if (query.length < 2) {
      this.rawResults.set([]);
      return;
    }

    this.searching.set(true);

    try {
      const results = await this.searchService.search(query);
      this.rawResults.set(results);
    } finally {
      this.searching.set(false);
    }
  }

  handleFilterChange(filters: SearchFilters) {
    this.filters.set(filters);
  }

  handleItemClick(item: SearchResult) {
    this.router.navigate(['/items', item.id]);
  }

  private applyFilters(
    results: SearchResult[],
    filters: SearchFilters
  ): SearchResult[] {
    return results.filter(result => {
      if (filters.category && result.category !== filters.category) {
        return false;
      }
      if (filters.minPrice && result.price < filters.minPrice) {
        return false;
      }
      if (filters.maxPrice && result.price > filters.maxPrice) {
        return false;
      }
      return true;
    });
  }
}
```

### モーダルダイアログの分離
```typescript
// Presentation: モーダルUI
@Component({
  selector: 'app-confirmation-modal',
  template: `
    @if (isOpen()) {
      <div class="modal-overlay" (click)="cancel.emit()">
        <div class="modal" (click)="$event.stopPropagation()">
          <h2>{{ title() }}</h2>
          <p>{{ message() }}</p>

          <div class="actions">
            <button (click)="cancel.emit()">
              キャンセル
            </button>
            <button
              (click)="confirm.emit()"
              [disabled]="processing()">
              {{ processing() ? '処理中...' : '確認' }}
            </button>
          </div>
        </div>
      </div>
    }
  `,
  standalone: true
})
export class ConfirmationModalComponent {
  isOpen = input(false);
  title = input.required<string>();
  message = input.required<string>();
  processing = input(false);

  confirm = output<void>();
  cancel = output<void>();
}

// Container: モーダル制御
@Component({
  selector: 'app-delete-confirmation-container',
  template: `
    <app-confirmation-modal
      [isOpen]="isOpen()"
      [title]="'削除の確認'"
      [message]="'本当に削除しますか?'"
      [processing]="processing()"
      (confirm)="handleConfirm()"
      (cancel)="handleCancel()"
    />
  `
})
export class DeleteConfirmationContainerComponent {
  private deleteService = inject(DeleteService);
  private notification = inject(NotificationService);

  isOpen = signal(false);
  processing = signal(false);
  itemId = signal<string | null>(null);

  open(id: string) {
    this.itemId.set(id);
    this.isOpen.set(true);
  }

  async handleConfirm() {
    const id = this.itemId();
    if (!id) return;

    this.processing.set(true);

    try {
      await this.deleteService.delete(id);
      this.notification.success('削除しました');
      this.isOpen.set(false);
    } catch (err) {
      this.notification.error('削除に失敗しました');
    } finally {
      this.processing.set(false);
    }
  }

  handleCancel() {
    this.isOpen.set(false);
  }
}
```

### ページネーションの分離
```typescript
// Presentation: ページネーションUI
@Component({
  selector: 'app-paginated-view',
  template: `
    <div class="content">
      @for (item of items(); track item.id) {
        <app-item-card [item]="item" />
      }
    </div>

    <div class="pagination">
      <button
        (click)="pageChange.emit(currentPage() - 1)"
        [disabled]="currentPage() === 1">
        前へ
      </button>

      <span>{{ currentPage() }} / {{ totalPages() }}</span>

      <button
        (click)="pageChange.emit(currentPage() + 1)"
        [disabled]="currentPage() === totalPages()">
        次へ
      </button>
    </div>
  `,
  standalone: true,
  imports: [ItemCardComponent]
})
export class PaginatedViewComponent<T> {
  items = input.required<T[]>();
  currentPage = input.required<number>();
  totalPages = input.required<number>();

  pageChange = output<number>();
}

// Container: ページネーションロジック
@Component({
  selector: 'app-items-container',
  template: `
    <app-paginated-view
      [items]="currentPageItems()"
      [currentPage]="currentPage()"
      [totalPages]="totalPages()"
      (pageChange)="handlePageChange($event)"
    />
  `
})
export class ItemsContainerComponent {
  private itemService = inject(ItemService);

  allItems = signal<Item[]>([]);
  currentPage = signal(1);
  pageSize = 10;

  totalPages = computed(() =>
    Math.ceil(this.allItems().length / this.pageSize)
  );

  currentPageItems = computed(() => {
    const start = (this.currentPage() - 1) * this.pageSize;
    return this.allItems().slice(start, start + this.pageSize);
  });

  async ngOnInit() {
    const items = await this.itemService.getAll();
    this.allItems.set(items);
  }

  handlePageChange(page: number) {
    if (page >= 1 && page <= this.totalPages()) {
      this.currentPage.set(page);
    }
  }
}
```

## ベストプラクティス

### 責任の明確化
```typescript
// ✅ Presentation: 表示のみ
export class PresentationComponent {
  data = input.required<Data>();
  action = output<void>();
}

// ✅ Container: ロジックのみ
export class ContainerComponent {
  private service = inject(Service);
  data = signal<Data>();
}

// ❌ 混在は避ける
export class MixedComponent {
  private service = inject(Service); // Container の責任
  // ... 複雑な表示ロジック // Presentation の責任
}
```

### データフローの一貫性
```typescript
// ✅ 単方向フロー
<app-presentation
  [data]="data()"          // Container → Presentation
  (action)="handle($event)" // Presentation → Container
/>

// ❌ 双方向バインディングは慎重に
<app-component [(value)]="value" />
```

### 適切な粒度
```typescript
// ✅ 機能ごとに分離
app-user-profile-container/
  app-user-profile/ (Presentation)
  app-user-stats/   (Presentation)

// ❌ 過度な分割
app-user-name-container/  // 小さすぎる
  app-user-name/
```

## 注意点

### 過度な分離
すべてのコンポーネントを分離する必要はありません。小規模な機能では統合も検討してください。

### パフォーマンス
Presentation Componentには`OnPush`戦略を適用して、変更検知を最適化してください。

### テスト戦略
- Presentation: 入出力の検証（簡単）
- Container: サービスをモックしてロジックをテスト

### ファイル構成
```
features/users/
  containers/
    user-list.container.ts
  components/
    user-list.component.ts
    user-card.component.ts
```

## 関連技術
- **Smart/Dumb Pattern**: 同様の概念
- **OnPush Strategy**: 変更検知最適化
- **Signal**: 状態管理
- **Dependency Injection**: サービス注入
- **Component Architecture**: アーキテクチャ設計
