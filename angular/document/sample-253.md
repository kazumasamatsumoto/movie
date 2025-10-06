# #253 「Smart/Dumb パターンの実践」

## 概要
Smart/Dumbパターンは、ロジックと表示を明確に分離する設計パターンです。Smart Componentがビジネスロジックと状態管理を担当し、Dumb Componentが純粋な表示を担当することで、テスタビリティ、再利用性、保守性が大幅に向上します。

## 学習目標
- Smart/Dumbパターンの実装方法を習得する
- 適切なコンポーネント分割の判断基準を理解する
- パターン適用のベストプラクティスを学ぶ

## 技術ポイント
- **明確な分離**: ロジックと表示の責任分担
- **データフロー**: 単方向データフロー
- **再利用性**: Dumbコンポーネントの汎用化

## 📺 画面表示用コード

### 基本パターン
```typescript
// Smart Component
@Component({
  selector: 'app-user-container',
  template: `
    <app-user-list
      [users]="users()"
      [loading]="loading()"
      (userSelect)="handleSelect($event)"
    />
  `
})
export class UserContainerComponent {
  private service = inject(UserService);
  users = signal<User[]>([]);
  loading = signal(false);

  async ngOnInit() {
    this.loading.set(true);
    this.users.set(await this.service.getUsers());
    this.loading.set(false);
  }

  handleSelect(user: User) {
    console.log('Selected:', user);
  }
}

// Dumb Component
@Component({
  selector: 'app-user-list',
  template: `
    @for (user of users(); track user.id) {
      <div (click)="userSelect.emit(user)">
        {{ user.name }}
      </div>
    }
  `
})
export class UserListComponent {
  users = input<User[]>([]);
  loading = input(false);
  userSelect = output<User>();
}
```

## 実践的な活用例(continued)

### Todo アプリケーション
```typescript
// Smart: Todo Container
@Component({
  selector: 'app-todo-container',
  template: `
    <app-todo-header
      (addTodo)="handleAdd($event)"
    />
    <app-todo-list
      [todos]="filteredTodos()"
      (toggle)="handleToggle($event)"
      (delete)="handleDelete($event)"
    />
    <app-todo-footer
      [activeCount]="activeCount()"
      [filter]="filter()"
      (filterChange)="setFilter($event)"
      (clearCompleted)="clearCompleted()"
    />
  `
})
export class TodoContainerComponent {
  private todoService = inject(TodoService);

  todos = signal<Todo[]>([]);
  filter = signal<'all' | 'active' | 'completed'>('all');

  filteredTodos = computed(() => {
    const todos = this.todos();
    const currentFilter = this.filter();

    switch (currentFilter) {
      case 'active': return todos.filter(t => !t.completed);
      case 'completed': return todos.filter(t => t.completed);
      default: return todos;
    }
  });

  activeCount = computed(() =>
    this.todos().filter(t => !t.completed).length
  );

  ngOnInit() {
    this.loadTodos();
  }

  async loadTodos() {
    this.todos.set(await this.todoService.getAll());
  }

  async handleAdd(text: string) {
    const todo = await this.todoService.create({ text, completed: false });
    this.todos.update(todos => [...todos, todo]);
  }

  async handleToggle(id: string) {
    await this.todoService.toggle(id);
    this.todos.update(todos =>
      todos.map(t => t.id === id ? { ...t, completed: !t.completed } : t)
    );
  }

  async handleDelete(id: string) {
    await this.todoService.delete(id);
    this.todos.update(todos => todos.filter(t => t.id !== id));
  }

  setFilter(filter: 'all' | 'active' | 'completed') {
    this.filter.set(filter);
  }

  async clearCompleted() {
    const completed = this.todos().filter(t => t.completed);
    await Promise.all(completed.map(t => this.todoService.delete(t.id)));
    this.todos.update(todos => todos.filter(t => !t.completed));
  }
}

// Dumb: Todo Header
@Component({
  selector: 'app-todo-header',
  template: `
    <input
      #input
      placeholder="何をする?"
      (keyup.enter)="add(input.value); input.value = ''"
    >
  `,
  standalone: true
})
export class TodoHeaderComponent {
  addTodo = output<string>();

  add(text: string) {
    if (text.trim()) {
      this.addTodo.emit(text);
    }
  }
}

// Dumb: Todo List
@Component({
  selector: 'app-todo-list',
  template: `
    @for (todo of todos(); track todo.id) {
      <app-todo-item
        [todo]="todo"
        (toggle)="toggle.emit($event)"
        (delete)="delete.emit($event)"
      />
    }
  `,
  standalone: true,
  imports: [TodoItemComponent]
})
export class TodoListComponent {
  todos = input<Todo[]>([]);
  toggle = output<string>();
  delete = output<string>();
}

// Dumb: Todo Item
@Component({
  selector: 'app-todo-item',
  template: `
    <div class="todo-item">
      <input
        type="checkbox"
        [checked]="todo().completed"
        (change)="toggle.emit(todo().id)"
      >
      <span [class.completed]="todo().completed">
        {{ todo().text }}
      </span>
      <button (click)="delete.emit(todo().id)">×</button>
    </div>
  `,
  styles: [`
    .completed { text-decoration: line-through; color: #999; }
  `],
  standalone: true
})
export class TodoItemComponent {
  todo = input.required<Todo>();
  toggle = output<string>();
  delete = output<string>();
}

// Dumb: Todo Footer
@Component({
  selector: 'app-todo-footer',
  template: `
    <div class="footer">
      <span>{{ activeCount() }} 件のタスク</span>
      <div class="filters">
        <button
          [class.active]="filter() === 'all'"
          (click)="filterChange.emit('all')">
          すべて
        </button>
        <button
          [class.active]="filter() === 'active'"
          (click)="filterChange.emit('active')">
          未完了
        </button>
        <button
          [class.active]="filter() === 'completed'"
          (click)="filterChange.emit('completed')">
          完了済み
        </button>
      </div>
      <button (click)="clearCompleted.emit()">
        完了済みを削除
      </button>
    </div>
  `,
  standalone: true
})
export class TodoFooterComponent {
  activeCount = input.required<number>();
  filter = input<'all' | 'active' | 'completed'>('all');
  filterChange = output<'all' | 'active' | 'completed'>();
  clearCompleted = output<void>();
}
```

### ショッピングカート
```typescript
// Smart: Cart Container
@Component({
  selector: 'app-cart-container',
  template: `
    <app-cart-summary
      [items]="items()"
      [total]="total()"
      [itemCount]="itemCount()"
    />
    <app-cart-items
      [items]="items()"
      (updateQuantity)="handleUpdateQuantity($event)"
      (removeItem)="handleRemoveItem($event)"
    />
    <app-cart-checkout
      [total]="total()"
      [canCheckout]="canCheckout()"
      (checkout)="handleCheckout()"
    />
  `
})
export class CartContainerComponent {
  private cartService = inject(CartService);
  private router = inject(Router);

  items = signal<CartItem[]>([]);

  total = computed(() =>
    this.items().reduce((sum, item) => sum + item.price * item.quantity, 0)
  );

  itemCount = computed(() =>
    this.items().reduce((sum, item) => sum + item.quantity, 0)
  );

  canCheckout = computed(() => this.items().length > 0);

  ngOnInit() {
    this.loadCart();
  }

  async loadCart() {
    this.items.set(await this.cartService.getItems());
  }

  async handleUpdateQuantity({ id, quantity }: { id: string; quantity: number }) {
    await this.cartService.updateQuantity(id, quantity);
    this.items.update(items =>
      items.map(item =>
        item.id === id ? { ...item, quantity } : item
      )
    );
  }

  async handleRemoveItem(id: string) {
    await this.cartService.removeItem(id);
    this.items.update(items => items.filter(item => item.id !== id));
  }

  async handleCheckout() {
    await this.cartService.checkout();
    this.router.navigate(['/checkout']);
  }
}

// Dumb: Cart Summary
@Component({
  selector: 'app-cart-summary',
  template: `
    <div class="summary">
      <h2>カート ({{ itemCount() }}件)</h2>
      <p class="total">合計: ¥{{ total().toLocaleString() }}</p>
    </div>
  `,
  standalone: true
})
export class CartSummaryComponent {
  items = input<CartItem[]>([]);
  total = input.required<number>();
  itemCount = input.required<number>();
}

// Dumb: Cart Items
@Component({
  selector: 'app-cart-items',
  template: `
    @for (item of items(); track item.id) {
      <div class="cart-item">
        <img [src]="item.image" [alt]="item.name">
        <div class="details">
          <h3>{{ item.name }}</h3>
          <p>¥{{ item.price.toLocaleString() }}</p>
        </div>
        <div class="quantity">
          <button (click)="updateQty(item, -1)">-</button>
          <span>{{ item.quantity }}</span>
          <button (click)="updateQty(item, 1)">+</button>
        </div>
        <button (click)="removeItem.emit(item.id)">削除</button>
      </div>
    }
  `,
  standalone: true
})
export class CartItemsComponent {
  items = input<CartItem[]>([]);
  updateQuantity = output<{ id: string; quantity: number }>();
  removeItem = output<string>();

  updateQty(item: CartItem, delta: number) {
    const newQuantity = item.quantity + delta;
    if (newQuantity > 0) {
      this.updateQuantity.emit({ id: item.id, quantity: newQuantity });
    }
  }
}
```

### 設計手順
```typescript
// Step 1: Dumb Componentから設計
@Component({
  selector: 'app-product-card',
  template: `
    <div class="product">
      <img [src]="product().image">
      <h3>{{ product().name }}</h3>
      <p>¥{{ product().price.toLocaleString() }}</p>
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
}

// Step 2: Dumbを組み合わせた中間Dumb
@Component({
  selector: 'app-product-grid',
  template: `
    <div class="grid">
      @for (product of products(); track product.id) {
        <app-product-card
          [product]="product"
          (addToCart)="productAddedToCart.emit($event)"
        />
      }
    </div>
  `,
  standalone: true,
  imports: [ProductCardComponent]
})
export class ProductGridComponent {
  products = input<Product[]>([]);
  productAddedToCart = output<Product>();
}

// Step 3: Smart Containerで統合
@Component({
  selector: 'app-products-container',
  template: `
    <app-product-filter
      [filter]="filter()"
      (filterChange)="setFilter($event)"
    />
    <app-product-grid
      [products]="filteredProducts()"
      (productAddedToCart)="handleAddToCart($event)"
    />
  `
})
export class ProductsContainerComponent {
  private productService = inject(ProductService);
  private cartService = inject(CartService);

  products = signal<Product[]>([]);
  filter = signal<ProductFilter>({});

  filteredProducts = computed(() => {
    return this.applyFilter(this.products(), this.filter());
  });

  async ngOnInit() {
    this.products.set(await this.productService.getAll());
  }

  setFilter(filter: ProductFilter) {
    this.filter.set(filter);
  }

  async handleAddToCart(product: Product) {
    await this.cartService.add(product);
  }

  private applyFilter(products: Product[], filter: ProductFilter): Product[] {
    // フィルタリングロジック
    return products;
  }
}
```

## ベストプラクティス

### 責任の明確化
```typescript
// ✅ Smart: ロジックのみ
export class SmartComponent {
  private service = inject(Service);
  data = signal([]);
  async load() { /* ロジック */ }
}

// ✅ Dumb: 表示のみ
export class DumbComponent {
  data = input([]);
  click = output();
}
```

### ファイル構成
```
features/
  users/
    containers/
      user-list.container.ts     # Smart
    components/
      user-list.component.ts     # Dumb
      user-card.component.ts     # Dumb
```

### 単方向データフロー
```typescript
// ✅ 親→子: Input、子→親: Output
<app-child
  [data]="parentData()"
  (action)="handleAction($event)"
/>
```

## 注意点

### 過度な分離
すべてのコンポーネントをSmart/Dumbに分ける必要はありません。小規模な機能では統合も検討してください。

### パフォーマンス
Dumb ComponentにOnPush戦略を適用することで、パフォーマンスが向上します。

### テスト戦略
- Smart: サービスをモックしてロジックをテスト
- Dumb: 入出力のみテスト（簡単）

## 関連技術
- **Container/Presentational Pattern**: React由来のパターン
- **OnPush Strategy**: 変更検知最適化
- **Signal**: 状態管理
- **Dependency Injection**: サービス注入
- **Component Architecture**: アーキテクチャ設計
