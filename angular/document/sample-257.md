# #257 「Stateful vs Stateless Component」

## 概要
Stateful Componentは内部状態を持ち管理するコンポーネント、Stateless Componentは状態を持たず入力のみに依存するコンポーネントです。それぞれの特性を理解し、適切に使い分けることで、保守性の高いアプリケーションを構築できます。

## 学習目標
- Stateful/Statelessの特徴を理解する
- 適切な使い分けの判断基準を習得する
- 各パターンの実装方法を学ぶ

## 技術ポイント
- **Stateful**: 状態管理、ライフサイクル制御
- **Stateless**: 純粋な入出力、高い再利用性
- **選択基準**: 機能要件に基づく判断

## 📺 画面表示用コード

### Stateless Component（状態なし）
```typescript
@Component({
  selector: 'app-user-card',
  template: `
    <div class="card">
      <h3>{{ user().name }}</h3>
      <p>{{ user().email }}</p>
      <button (click)="select.emit(user())">選択</button>
    </div>
  `,
  standalone: true
})
export class UserCardComponent {
  // 入力のみ、内部状態なし
  user = input.required<User>();
  select = output<User>();
}
```

### Stateful Component（状態あり）
```typescript
@Component({
  selector: 'app-user-list',
  template: `
    <input
      [(ngModel)]="searchQuery"
      placeholder="検索...">

    @for (user of filteredUsers(); track user.id) {
      <app-user-card
        [user]="user"
        (select)="handleSelect($event)"
      />
    }
  `,
  standalone: true,
  imports: [UserCardComponent, FormsModule]
})
export class UserListComponent {
  // 内部状態を持つ
  private userService = inject(UserService);

  users = signal<User[]>([]);
  searchQuery = signal('');

  filteredUsers = computed(() =>
    this.users().filter(u =>
      u.name.includes(this.searchQuery())
    )
  );

  async ngOnInit() {
    this.users.set(await this.userService.getAll());
  }

  handleSelect(user: User) {
    console.log('Selected:', user);
  }
}
```

### 判断基準の例
```typescript
// ✅ Stateless: データ表示のみ
@Component({
  selector: 'app-price-display',
  template: `<span>¥{{ price().toLocaleString() }}</span>`
})
export class PriceDisplayComponent {
  price = input.required<number>();
}

// ✅ Stateful: ユーザー操作で状態変化
@Component({
  selector: 'app-toggle-button',
  template: `
    <button (click)="toggle()">
      {{ isOn() ? 'ON' : 'OFF' }}
    </button>
  `
})
export class ToggleButtonComponent {
  isOn = signal(false); // 内部状態

  toggle() {
    this.isOn.update(v => !v);
  }
}
```

## 実践的な活用例

### Stateless: 純粋な表示コンポーネント
```typescript
// カード表示（状態なし）
@Component({
  selector: 'app-product-card',
  template: `
    <div class="card">
      <img [src]="product().image" [alt]="product().name">
      <h3>{{ product().name }}</h3>
      <p>{{ formatPrice(product().price) }}</p>
      <button (click)="addToCart.emit(product())">
        カートに追加
      </button>
    </div>
  `,
  standalone: true
})
export class ProductCardComponent {
  product = input.required<Product>();
  addToCart = output<Product>();

  // 純粋関数（状態変更なし）
  formatPrice(price: number): string {
    return `¥${price.toLocaleString()}`;
  }
}

// バッジ表示（状態なし）
@Component({
  selector: 'app-status-badge',
  template: `
    <span [class]="'badge badge-' + status()">
      {{ label() }}
    </span>
  `,
  styles: [`
    .badge-success { background: green; }
    .badge-error { background: red; }
  `],
  standalone: true
})
export class StatusBadgeComponent {
  status = input.required<'success' | 'error' | 'warning'>();
  label = input.required<string>();
}

// アバター表示（状態なし）
@Component({
  selector: 'app-avatar',
  template: `
    <img
      [src]="imageUrl()"
      [alt]="name()"
      [style.width.px]="size()"
      [style.height.px]="size()"
      class="avatar">
  `,
  styles: [`
    .avatar {
      border-radius: 50%;
      object-fit: cover;
    }
  `],
  standalone: true
})
export class AvatarComponent {
  imageUrl = input.required<string>();
  name = input.required<string>();
  size = input(40);
}
```

### Stateful: 状態管理が必要なコンポーネント
```typescript
// アコーディオン（状態あり）
@Component({
  selector: 'app-accordion',
  template: `
    <div class="accordion">
      <div class="header" (click)="toggle()">
        {{ title() }}
        <span>{{ isOpen() ? '▲' : '▼' }}</span>
      </div>
      @if (isOpen()) {
        <div class="content">
          <ng-content></ng-content>
        </div>
      }
    </div>
  `,
  standalone: true
})
export class AccordionComponent {
  title = input.required<string>();

  // 内部UI状態
  isOpen = signal(false);

  toggle() {
    this.isOpen.update(v => !v);
  }
}

// タブ切り替え（状態あり）
@Component({
  selector: 'app-tabs',
  template: `
    <div class="tabs">
      <div class="tab-headers">
        @for (tab of tabs(); track tab.id) {
          <button
            [class.active]="activeTab() === tab.id"
            (click)="selectTab(tab.id)">
            {{ tab.label }}
          </button>
        }
      </div>
      <div class="tab-content">
        @for (tab of tabs(); track tab.id) {
          @if (activeTab() === tab.id) {
            <div>{{ tab.content }}</div>
          }
        }
      </div>
    </div>
  `,
  standalone: true
})
export class TabsComponent {
  tabs = input.required<Tab[]>();

  // アクティブなタブの状態管理
  activeTab = signal<string>('');

  ngOnInit() {
    const tabs = this.tabs();
    if (tabs.length > 0) {
      this.activeTab.set(tabs[0].id);
    }
  }

  selectTab(id: string) {
    this.activeTab.set(id);
  }
}

// カウンター（状態あり）
@Component({
  selector: 'app-counter',
  template: `
    <div class="counter">
      <button (click)="decrement()">-</button>
      <span>{{ count() }}</span>
      <button (click)="increment()">+</button>
      <button (click)="reset()">リセット</button>
    </div>
  `,
  standalone: true
})
export class CounterComponent {
  initialValue = input(0);

  // カウントの状態管理
  count = signal(0);

  ngOnInit() {
    this.count.set(this.initialValue());
  }

  increment() {
    this.count.update(v => v + 1);
  }

  decrement() {
    this.count.update(v => v - 1);
  }

  reset() {
    this.count.set(this.initialValue());
  }
}
```

### Statelessからの状態の外部化
```typescript
// Before: Stateful（内部状態）
@Component({
  selector: 'app-search-box-stateful',
  template: `
    <input
      [value]="query"
      (input)="onInput($event)">
  `
})
export class SearchBoxStatefulComponent {
  query = signal(''); // 内部状態

  onInput(event: Event) {
    const value = (event.target as HTMLInputElement).value;
    this.query.set(value);
    // 検索実行...
  }
}

// After: Stateless（状態を外部化）
@Component({
  selector: 'app-search-box-stateless',
  template: `
    <input
      [value]="query()"
      (input)="queryChange.emit($any($event.target).value)">
  `
})
export class SearchBoxStatelessComponent {
  query = input('');
  queryChange = output<string>();
}

// 親コンポーネントで状態管理
@Component({
  selector: 'app-search-container',
  template: `
    <app-search-box-stateless
      [query]="query()"
      (queryChange)="handleQueryChange($event)"
    />
  `
})
export class SearchContainerComponent {
  query = signal(''); // 親で状態管理

  handleQueryChange(value: string) {
    this.query.set(value);
    // 検索実行...
  }
}
```

### 複合例: StatefulとStatelessの組み合わせ
```typescript
// Stateless: 個別の商品カード
@Component({
  selector: 'app-product-item',
  template: `
    <div class="item">
      <h3>{{ product().name }}</h3>
      <p>{{ product().price }}</p>
      <button (click)="select.emit(product())">
        選択
      </button>
    </div>
  `,
  standalone: true
})
export class ProductItemComponent {
  product = input.required<Product>();
  select = output<Product>();
}

// Stateful: 商品リストとフィルタリング
@Component({
  selector: 'app-product-list',
  template: `
    <div class="filters">
      <input
        [(ngModel)]="searchQuery"
        placeholder="検索...">

      <select [(ngModel)]="selectedCategory">
        <option value="">すべて</option>
        @for (cat of categories(); track cat) {
          <option [value]="cat">{{ cat }}</option>
        }
      </select>
    </div>

    <div class="list">
      @for (product of filteredProducts(); track product.id) {
        <app-product-item
          [product]="product"
          (select)="handleSelect($event)"
        />
      }
    </div>
  `,
  standalone: true,
  imports: [ProductItemComponent, FormsModule]
})
export class ProductListComponent {
  products = input.required<Product[]>();
  categories = input<string[]>([]);

  // 内部フィルタ状態
  searchQuery = signal('');
  selectedCategory = signal('');

  // 計算された結果
  filteredProducts = computed(() => {
    let result = this.products();

    const query = this.searchQuery();
    if (query) {
      result = result.filter(p =>
        p.name.toLowerCase().includes(query.toLowerCase())
      );
    }

    const category = this.selectedCategory();
    if (category) {
      result = result.filter(p => p.category === category);
    }

    return result;
  });

  handleSelect(product: Product) {
    console.log('Selected:', product);
  }
}
```

### モーダルダイアログ: Stateful実装
```typescript
@Component({
  selector: 'app-modal',
  template: `
    @if (isOpen()) {
      <div class="overlay" (click)="close()">
        <div class="modal" (click)="$event.stopPropagation()">
          <div class="header">
            <h2>{{ title() }}</h2>
            <button (click)="close()">×</button>
          </div>
          <div class="body">
            <ng-content></ng-content>
          </div>
          <div class="footer">
            <button (click)="close()">閉じる</button>
          </div>
        </div>
      </div>
    }
  `,
  standalone: true
})
export class ModalComponent {
  title = input.required<string>();

  // モーダルの開閉状態
  isOpen = signal(false);

  open() {
    this.isOpen.set(true);
  }

  close() {
    this.isOpen.set(false);
  }
}
```

### フォーム入力: Stateful vs Stateless
```typescript
// Stateless: 制御されたコンポーネント
@Component({
  selector: 'app-input-controlled',
  template: `
    <input
      [value]="value()"
      (input)="valueChange.emit($any($event.target).value)">
  `
})
export class InputControlledComponent {
  value = input('');
  valueChange = output<string>();
}

// Stateful: 非制御コンポーネント
@Component({
  selector: 'app-input-uncontrolled',
  template: `
    <input
      [(ngModel)]="internalValue"
      (ngModelChange)="valueChange.emit(internalValue)">
  `,
  imports: [FormsModule]
})
export class InputUncontrolledComponent {
  internalValue = signal(''); // 内部状態
  valueChange = output<string>();
}
```

## ベストプラクティス

### Stateless優先
```typescript
// ✅ 可能な限りStatelessに
@Component({
  selector: 'app-display',
  template: `<div>{{ data() }}</div>`
})
export class DisplayComponent {
  data = input.required<string>();
}

// ❌ 不必要な状態管理
@Component({
  selector: 'app-display',
  template: `<div>{{ localData() }}</div>`
})
export class DisplayComponent {
  data = input.required<string>();
  localData = signal(''); // 不要な内部状態

  ngOnChanges() {
    this.localData.set(this.data()); // 冗長
  }
}
```

### UI状態はStatefulで
```typescript
// ✅ UI状態は内部管理
@Component({
  selector: 'app-dropdown',
  template: `
    <button (click)="toggle()">メニュー</button>
    @if (isOpen()) {
      <ul><li>項目</li></ul>
    }
  `
})
export class DropdownComponent {
  isOpen = signal(false); // UI状態は内部管理が適切

  toggle() {
    this.isOpen.update(v => !v);
  }
}
```

### ビジネス状態は外部化
```typescript
// ✅ ビジネス状態は親で管理
@Component({
  selector: 'app-cart-item',
  template: `
    <div>
      {{ item().name }}
      <button (click)="remove.emit(item().id)">削除</button>
    </div>
  `
})
export class CartItemComponent {
  item = input.required<CartItem>();
  remove = output<string>(); // 状態変更は親に委譲
}
```

## 注意点

### 状態の配置場所
- **UI状態**: コンポーネント内部（開閉、選択など）
- **ビジネス状態**: 親コンポーネントまたはサービス

### パフォーマンス
- Stateless componentには`OnPush`が有効
- Stateful componentは適切な変更検知戦略を選択

### テスト
- Stateless: 入力→出力のテストが容易
- Stateful: 状態遷移のテストが必要

### 再利用性
- Stateless: 高い再利用性
- Stateful: コンテキスト依存の可能性

## 関連技術
- **Signal**: 状態管理
- **input()/output()**: データバインディング
- **OnPush Strategy**: 変更検知最適化
- **Smart/Dumb Pattern**: コンポーネント設計
- **Controlled/Uncontrolled Components**: フォーム制御
