# #010 「TypeScript で Component を書く」

## 概要
AngularはTypeScriptで開発します。型安全性により、コンパイル時にエラーを検出し、開発効率と品質が向上します。

## 学習目標
- TypeScriptの基本的な型システムを理解する
- Component開発でのTypeScript活用方法を習得する
- 型安全な開発のメリットを理解する

## 技術ポイント
- **型定義**: 変数・プロパティの型指定
- **インターフェース**: オブジェクトの構造定義
- **アクセス修飾子**: public、private、protected

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```typescript
// 型定義の基本
@Component({
  selector: 'app-user',
  template: '<p>{{name}}: {{age}}歳</p>'
})
export class UserComponent {
  name: string = 'John';
  age: number = 25;
  isActive: boolean = true;
}
```

```typescript
// インターフェースの使用
interface User {
  id: number;
  name: string;
  email: string;
}

@Component({
  selector: 'app-profile',
  template: '<h2>{{user.name}}</h2>'
})
export class ProfileComponent {
  user: User = { id: 1, name: 'John', email: 'john@example.com' };
}
```

```typescript
// アクセス修飾子
@Component({
  selector: 'app-secure',
  template: '<p>{{publicData}}</p>'
})
export class SecureComponent {
  public publicData = 'visible';
  private privateData = 'hidden';

  public getData(): string {
    return this.privateData;
  }
}
```

## 💻 詳細実装例（学習用）

### TypeScriptの基本型
```typescript
import { Component } from '@angular/core';

@Component({
  selector: 'app-types-demo',
  standalone: true,
  template: `
    <div>
      <p>String: {{message}}</p>
      <p>Number: {{count}}</p>
      <p>Boolean: {{isActive}}</p>
      <p>Array: {{items.join(', ')}}</p>
    </div>
  `
})
export class TypesDemoComponent {
  // プリミティブ型
  message: string = 'Hello TypeScript';
  count: number = 42;
  isActive: boolean = true;

  // 配列
  items: string[] = ['Apple', 'Banana', 'Orange'];
  numbers: Array<number> = [1, 2, 3, 4, 5];

  // タプル
  coordinate: [number, number] = [10, 20];

  // any型（使用は最小限に）
  dynamicValue: any = 'can be anything';

  // unknown型（anyより安全）
  unknownValue: unknown = 'needs type checking';

  // void型（戻り値なし）
  logMessage(): void {
    console.log(this.message);
  }

  // null と undefined
  nullableValue: string | null = null;
  optionalValue?: string;  // string | undefined
}
```

### インターフェースとタイプエイリアス
```typescript
import { Component } from '@angular/core';

// インターフェース
interface Product {
  id: number;
  name: string;
  price: number;
  category: string;
  inStock: boolean;
}

// タイプエイリアス
type ProductId = number;
type ProductCategory = 'electronics' | 'clothing' | 'food';
type ProductStatus = 'available' | 'out-of-stock' | 'discontinued';

// 複雑な型
interface CartItem extends Product {
  quantity: number;
  addedAt: Date;
}

@Component({
  selector: 'app-product-list',
  standalone: true,
  template: `
    <div>
      <h2>Products</h2>
      <div *ngFor="let product of products">
        {{product.name}} - ¥{{product.price}}
      </div>
    </div>
  `
})
export class ProductListComponent {
  products: Product[] = [
    {
      id: 1,
      name: 'Laptop',
      price: 1200,
      category: 'electronics',
      inStock: true
    },
    {
      id: 2,
      name: 'T-Shirt',
      price: 20,
      category: 'clothing',
      inStock: true
    }
  ];

  cart: CartItem[] = [];

  addToCart(product: Product, quantity: number): void {
    const cartItem: CartItem = {
      ...product,
      quantity,
      addedAt: new Date()
    };
    this.cart.push(cartItem);
  }

  getProductById(id: ProductId): Product | undefined {
    return this.products.find(p => p.id === id);
  }

  filterByCategory(category: ProductCategory): Product[] {
    return this.products.filter(p => p.category === category);
  }
}
```

### ジェネリクス
```typescript
import { Component } from '@angular/core';

// ジェネリックインターフェース
interface ApiResponse<T> {
  data: T;
  status: number;
  message: string;
}

interface PaginatedResponse<T> {
  items: T[];
  total: number;
  page: number;
  pageSize: number;
}

// ジェネリッククラス
class DataStore<T> {
  private items: T[] = [];

  add(item: T): void {
    this.items.push(item);
  }

  getAll(): T[] {
    return this.items;
  }

  find(predicate: (item: T) => boolean): T | undefined {
    return this.items.find(predicate);
  }
}

interface User {
  id: number;
  name: string;
  email: string;
}

@Component({
  selector: 'app-generic-demo',
  standalone: true,
  template: `
    <div>
      <h2>Users</h2>
      <p *ngFor="let user of users">{{user.name}}</p>
    </div>
  `
})
export class GenericDemoComponent {
  private userStore = new DataStore<User>();
  users: User[] = [];

  async ngOnInit() {
    // ジェネリックを使ったAPI呼び出し
    const response = await this.fetchUsers();
    this.users = response.data;
  }

  private async fetchUsers(): Promise<ApiResponse<User[]>> {
    // モックレスポンス
    return {
      data: [
        { id: 1, name: 'John', email: 'john@example.com' },
        { id: 2, name: 'Jane', email: 'jane@example.com' }
      ],
      status: 200,
      message: 'Success'
    };
  }

  private async fetchPaginatedUsers(page: number): Promise<PaginatedResponse<User>> {
    return {
      items: this.users,
      total: 100,
      page: page,
      pageSize: 10
    };
  }
}
```

### クラスの継承と実装
```typescript
import { Component, OnInit, OnDestroy } from '@angular/core';

// 抽象クラス
abstract class BaseComponent implements OnInit, OnDestroy {
  protected isLoading = false;
  protected error: string | null = null;

  ngOnInit(): void {
    this.initialize();
  }

  ngOnDestroy(): void {
    this.cleanup();
  }

  protected abstract initialize(): void;
  protected abstract cleanup(): void;

  protected setLoading(loading: boolean): void {
    this.isLoading = loading;
  }

  protected setError(error: string): void {
    this.error = error;
  }
}

// インターフェース実装
interface Searchable {
  search(query: string): void;
  clearSearch(): void;
}

@Component({
  selector: 'app-user-list',
  standalone: true,
  template: `
    <div>
      @if (isLoading) {
        <p>Loading...</p>
      } @else if (error) {
        <p>Error: {{error}}</p>
      } @else {
        <ul>
          <li *ngFor="let user of filteredUsers">{{user.name}}</li>
        </ul>
      }
    </div>
  `
})
export class UserListComponent extends BaseComponent implements Searchable {
  users: Array<{ id: number; name: string }> = [];
  filteredUsers: Array<{ id: number; name: string }> = [];
  private searchQuery = '';

  protected initialize(): void {
    this.loadUsers();
  }

  protected cleanup(): void {
    console.log('Cleaning up UserListComponent');
  }

  private async loadUsers() {
    this.setLoading(true);
    try {
      // API呼び出しのシミュレーション
      this.users = [
        { id: 1, name: 'John' },
        { id: 2, name: 'Jane' }
      ];
      this.filteredUsers = [...this.users];
    } catch (err) {
      this.setError('Failed to load users');
    } finally {
      this.setLoading(false);
    }
  }

  search(query: string): void {
    this.searchQuery = query.toLowerCase();
    this.filteredUsers = this.users.filter(user =>
      user.name.toLowerCase().includes(this.searchQuery)
    );
  }

  clearSearch(): void {
    this.searchQuery = '';
    this.filteredUsers = [...this.users];
  }
}
```

### 型ガードとユーティリティ型
```typescript
import { Component } from '@angular/core';

interface Dog {
  type: 'dog';
  breed: string;
  bark(): void;
}

interface Cat {
  type: 'cat';
  color: string;
  meow(): void;
}

type Pet = Dog | Cat;

// ユーティリティ型
interface FullUser {
  id: number;
  name: string;
  email: string;
  password: string;
  role: string;
}

type PublicUser = Omit<FullUser, 'password'>;
type UserCredentials = Pick<FullUser, 'email' | 'password'>;
type PartialUser = Partial<FullUser>;
type ReadonlyUser = Readonly<FullUser>;
type UserRole = FullUser['role'];

@Component({
  selector: 'app-type-guards',
  standalone: true,
  template: `<div>Type Guards Demo</div>`
})
export class TypeGuardsComponent {
  pets: Pet[] = [
    { type: 'dog', breed: 'Labrador', bark: () => console.log('Woof!') },
    { type: 'cat', color: 'Orange', meow: () => console.log('Meow!') }
  ];

  // 型ガード関数
  isDog(pet: Pet): pet is Dog {
    return pet.type === 'dog';
  }

  isCat(pet: Pet): pet is Cat {
    return pet.type === 'cat';
  }

  handlePet(pet: Pet): void {
    if (this.isDog(pet)) {
      // ここではpetはDog型として扱われる
      console.log(`Dog breed: ${pet.breed}`);
      pet.bark();
    } else if (this.isCat(pet)) {
      // ここではpetはCat型として扱われる
      console.log(`Cat color: ${pet.color}`);
      pet.meow();
    }
  }

  // ユーティリティ型の使用
  publicUser: PublicUser = {
    id: 1,
    name: 'John',
    email: 'john@example.com',
    role: 'user'
  };

  updateUser(updates: PartialUser): void {
    // 一部のプロパティのみ更新可能
    this.publicUser = { ...this.publicUser, ...updates };
  }
}
```

### デコレータと型
```typescript
import { Component, Input, Output, EventEmitter } from '@angular/core';

interface ButtonConfig {
  variant: 'primary' | 'secondary' | 'danger';
  size: 'small' | 'medium' | 'large';
  disabled: boolean;
}

@Component({
  selector: 'app-typed-button',
  standalone: true,
  template: `
    <button
      [class]="buttonClass"
      [disabled]="config.disabled"
      (click)="handleClick()"
    >
      {{label}}
    </button>
  `
})
export class TypedButtonComponent {
  // Input with type
  @Input() label: string = 'Click me';
  @Input() config: ButtonConfig = {
    variant: 'primary',
    size: 'medium',
    disabled: false
  };

  // Output with type
  @Output() clicked = new EventEmitter<MouseEvent>();
  @Output() longPress = new EventEmitter<{ duration: number }>();

  get buttonClass(): string {
    return `btn btn-${this.config.variant} btn-${this.config.size}`;
  }

  handleClick(): void {
    if (!this.config.disabled) {
      const event = new MouseEvent('click');
      this.clicked.emit(event);
    }
  }

  handleLongPress(duration: number): void {
    this.longPress.emit({ duration });
  }
}
```

### strictモードでの開発
```typescript
// tsconfig.json で strict: true を有効化
import { Component } from '@angular/core';

interface StrictUser {
  id: number;
  name: string;
  email: string;
  age?: number;  // オプショナル
}

@Component({
  selector: 'app-strict-demo',
  standalone: true,
  template: `<div>{{user?.name ?? 'No user'}}</div>`
})
export class StrictDemoComponent {
  // strictNullChecks: null/undefinedを明示的に扱う
  user: StrictUser | null = null;
  users: StrictUser[] = [];

  // strictFunctionTypes: 関数の型チェックを厳密に
  updateUser(updater: (user: StrictUser) => StrictUser): void {
    if (this.user) {
      this.user = updater(this.user);
    }
  }

  // noImplicitAny: 暗黙のany型を禁止
  findUser(id: number): StrictUser | undefined {
    return this.users.find(u => u.id === id);
  }

  // strictPropertyInitialization: プロパティの初期化を強制
  // ❌ これはエラーになる（初期化されていない）
  // requiredValue: string;

  // ✅ これは正しい
  requiredValue: string = 'initialized';

  // ✅ または constructor で初期化
  anotherValue: string;
  constructor() {
    this.anotherValue = 'initialized in constructor';
  }

  // nullish coalescing と optional chaining
  getUserAge(): number {
    return this.user?.age ?? 0;  // age が undefined なら 0
  }

  getUserEmail(): string {
    return this.user?.email || 'no-email@example.com';
  }
}
```

## ベストプラクティス

1. **strict モードを有効化**: tsconfig.jsonでstrict: true
2. **明示的な型定義**: anyの使用を最小限に
3. **インターフェースの活用**: オブジェクト構造を明確に定義
4. **ジェネリクスの使用**: 再利用可能な型安全なコード

## 注意点

- any型の使用は最小限に（型安全性が失われる）
- strict モードでは null/undefined の扱いに注意
- 型定義が複雑になりすぎないよう注意
- エディタの型チェックを活用

## 関連技術
- TypeScript
- Type Safety
- Static Typing
- Interface Design
