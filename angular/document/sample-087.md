# #087 Lifecycle とSignals の組み合わせ

## 概要
Angular v20におけるLifecycle HooksとSignalsの組み合わせを学びます。新しいリアクティブシステムとの統合、効率的な状態管理、モダンな実装パターンについて解説します。

## 学習目標
- SignalsとLifecycle Hooksの組み合わせを理解する
- 効率的な状態管理方法を習得する
- モダンな実装パターンを身につける

## 📺 画面表示用コード

```typescript
// SignalsとLifecycle Hooksの組み合わせ
export class SignalLifecycleComponent implements OnInit, OnDestroy {
  // Signalsの定義
  data = signal<any[]>([]);
  loading = signal(false);
  error = signal<string | null>(null);
  
  ngOnInit() {
    this.initializeSignals();
    this.loadData();
  }
  
  ngOnDestroy() {
    // クリーンアップ処理
  }
  
  private initializeSignals() {
    // 初期状態の設定
    this.data.set([]);
    this.loading.set(false);
    this.error.set(null);
  }
  
  private loadData() {
    this.loading.set(true);
    this.error.set(null);
    
    this.dataService.getData().subscribe({
      next: (result) => {
        this.data.set(result);
        this.loading.set(false);
      },
      error: (err) => {
        this.error.set('データの取得に失敗しました');
        this.loading.set(false);
      }
    });
  }
}
```

```typescript
// 計算されたSignals
export class ComputedSignalComponent implements OnInit {
  items = signal<any[]>([]);
  filter = signal('');
  
  // 計算されたSignal
  filteredItems = computed(() => {
    const items = this.items();
    const filter = this.filter();
    
    if (!filter) return items;
    
    return items.filter(item => 
      item.name.toLowerCase().includes(filter.toLowerCase())
    );
  });
  
  ngOnInit() {
    this.loadItems();
  }
  
  private loadItems() {
    this.itemService.getItems().subscribe(items => {
      this.items.set(items);
    });
  }
}
```

## 技術ポイント

### 1. Signalsの基本
- **signal()**: リアクティブな状態の定義
- **computed()**: 計算された値の定義
- **effect()**: 副作用の実行

### 2. Lifecycle Hooksとの統合
- **ngOnInit**: Signalsの初期化
- **ngOnDestroy**: クリーンアップ処理
- **ngOnChanges**: 入力プロパティとの連携

### 3. 効率的な状態管理
- リアクティブな状態更新
- 自動的な依存関係の管理
- パフォーマンスの最適化

## 実践的な活用例

### 1. フォーム状態の管理
```typescript
export class FormSignalComponent implements OnInit {
  // フォーム状態のSignals
  formData = signal<FormData>({});
  isDirty = signal(false);
  isValid = signal(false);
  
  // 計算されたSignals
  canSubmit = computed(() => 
    this.isDirty() && this.isValid()
  );
  
  ngOnInit() {
    this.initializeForm();
  }
  
  private initializeForm() {
    this.formData.set({
      name: '',
      email: ''
    });
    this.isDirty.set(false);
    this.isValid.set(false);
  }
  
  onFieldChange(field: string, value: any) {
    const currentData = this.formData();
    this.formData.set({
      ...currentData,
      [field]: value
    });
    this.isDirty.set(true);
    this.validateForm();
  }
  
  private validateForm() {
    const data = this.formData();
    const isValid = data.name && data.email;
    this.isValid.set(isValid);
  }
}
```

### 2. データ取得とキャッシュ
```typescript
export class DataCacheComponent implements OnInit, OnDestroy {
  // データのSignals
  cache = signal<Map<string, any>>(new Map());
  loading = signal<Set<string>>(new Set());
  
  // 計算されたSignals
  isLoading = computed(() => this.loading().size > 0);
  
  ngOnInit() {
    this.loadInitialData();
  }
  
  ngOnDestroy() {
    // クリーンアップ処理
  }
  
  private loadInitialData() {
    this.loadData('users');
    this.loadData('posts');
  }
  
  private loadData(key: string) {
    if (this.cache().has(key)) {
      return; // キャッシュから取得
    }
    
    this.loading.update(loading => new Set(loading).add(key));
    
    this.dataService.getData(key).subscribe({
      next: (data) => {
        this.cache.update(cache => {
          const newCache = new Map(cache);
          newCache.set(key, data);
          return newCache;
        });
        this.loading.update(loading => {
          const newLoading = new Set(loading);
          newLoading.delete(key);
          return newLoading;
        });
      },
      error: (error) => {
        this.loading.update(loading => {
          const newLoading = new Set(loading);
          newLoading.delete(key);
          return newLoading;
        });
      }
    });
  }
}
```

### 3. リアクティブなUI状態
```typescript
export class ReactiveUIComponent implements OnInit {
  // UI状態のSignals
  isMenuOpen = signal(false);
  selectedItem = signal<string | null>(null);
  searchQuery = signal('');
  
  // 計算されたSignals
  filteredItems = computed(() => {
    const query = this.searchQuery();
    const items = this.getAllItems();
    
    if (!query) return items;
    
    return items.filter(item => 
      item.toLowerCase().includes(query.toLowerCase())
    );
  });
  
  ngOnInit() {
    this.initializeUI();
  }
  
  private initializeUI() {
    this.isMenuOpen.set(false);
    this.selectedItem.set(null);
    this.searchQuery.set('');
  }
  
  toggleMenu() {
    this.isMenuOpen.update(open => !open);
  }
  
  selectItem(item: string) {
    this.selectedItem.set(item);
    this.isMenuOpen.set(false);
  }
  
  onSearch(query: string) {
    this.searchQuery.set(query);
  }
}
```

## ベストプラクティス

1. **適切なSignalの選択**: 用途に応じたSignalの選択
2. **効率的な更新**: 効率的な状態更新
3. **計算された値の活用**: computed()の適切な使用
4. **パフォーマンス**: 不要な再計算の回避

## 注意点

- 適切なSignalの使用
- メモリリークの防止
- パフォーマンスへの影響を考慮
- 既存コードとの統合

## 関連技術
- Angular Signals
- リアクティブプログラミング
- 状態管理
- パフォーマンス最適化
