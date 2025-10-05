# #055 テンプレート式のベストプラクティス

## 概要
Angular v20におけるテンプレート式のベストプラクティスを学びます。パフォーマンス、保守性、可読性を考慮した適切なテンプレート式の書き方と、避けるべきアンチパターンについて解説します。

## 学習目標
- テンプレート式のベストプラクティスを理解する
- パフォーマンスを考慮した書き方を習得する
- 保守性の高いコードの書き方を身につける

## 📺 画面表示用コード

```html
<!-- 良い例：シンプルなプロパティアクセス -->
<p>{{user.name}}</p>
<p>{{user.isActive ? 'アクティブ' : '非アクティブ'}}</p>
```

```html
<!-- 悪い例：複雑なロジック -->
<p>{{user.firstName + ' ' + user.lastName + ' (' + user.age + '歳)'}}</p>
```

```typescript
// コンポーネントで複雑なロジックを処理
export class UserComponent {
  user = { firstName: '太郎', lastName: '田中', age: 25 };
  
  get displayName() {
    return `${this.user.firstName} ${this.user.lastName} (${this.user.age}歳)`;
  }
}
```

```html
<!-- 改善後：getterを使用 -->
<p>{{displayName}}</p>
```

## 技術ポイント

### 1. 良い例：シンプルなプロパティアクセス
```html
<p>{{user.name}}</p>
<p>{{user.isActive ? 'アクティブ' : '非アクティブ'}}</p>
```

### 2. 悪い例：複雑なロジック
```html
<p>{{user.firstName + ' ' + user.lastName + ' (' + user.age + '歳)'}}</p>
```

### 3. 改善：getterを使用
```typescript
export class UserComponent {
  user = { firstName: '太郎', lastName: '田中', age: 25 };
  
  get displayName() {
    return `${this.user.firstName} ${this.user.lastName} (${this.user.age}歳)`;
  }
}
```

```html
<p>{{displayName}}</p>
```

## 実践的な活用例

### 1. 計算済みプロパティの活用
```typescript
export class ProductComponent {
  products = signal([
    { name: '商品A', price: 1000, discount: 0.1 },
    { name: '商品B', price: 2000, discount: 0.2 }
  ]);
  
  get totalPrice() {
    return this.products().reduce((sum, product) => {
      return sum + (product.price * (1 - product.discount));
    }, 0);
  }
  
  get formattedTotalPrice() {
    return `¥${this.totalPrice.toLocaleString()}`;
  }
}
```

```html
<div *ngFor="let product of products()">
  <h3>{{product.name}}</h3>
  <p>価格: ¥{{product.price.toLocaleString()}}</p>
  <p>割引後: ¥{{(product.price * (1 - product.discount)).toLocaleString()}}</p>
</div>
<p>合計: {{formattedTotalPrice}}</p>
```

### 2. 条件付き表示の最適化
```typescript
export class ConditionalComponent {
  user = signal<User | null>(null);
  isLoading = signal(false);
  error = signal<string | null>(null);
  
  get hasUser() {
    return this.user() !== null;
  }
  
  get showContent() {
    return this.hasUser && !this.isLoading() && !this.error();
  }
}
```

```html
@if (showContent) {
  <div class="user-content">
    <h2>{{user()!.name}}</h2>
    <p>{{user()!.email}}</p>
  </div>
} @else if (isLoading()) {
  <div class="loading">読み込み中...</div>
} @else if (error()) {
  <div class="error">{{error()}}</div>
} @else {
  <div class="no-data">ユーザーが見つかりません</div>
}
```

### 3. フォーマット関数の活用
```typescript
export class FormattingComponent {
  date = signal(new Date());
  amount = signal(1234567);
  
  formatDate(date: Date): string {
    return date.toLocaleDateString('ja-JP', {
      year: 'numeric',
      month: 'long',
      day: 'numeric'
    });
  }
  
  formatCurrency(amount: number): string {
    return new Intl.NumberFormat('ja-JP', {
      style: 'currency',
      currency: 'JPY'
    }).format(amount);
  }
}
```

```html
<p>日付: {{formatDate(date())}}</p>
<p>金額: {{formatCurrency(amount())}}</p>
```

### 4. 配列操作の最適化
```typescript
export class ArrayComponent {
  items = signal([
    { id: 1, name: 'アイテム1', category: 'A', active: true },
    { id: 2, name: 'アイテム2', category: 'B', active: false },
    { id: 3, name: 'アイテム3', category: 'A', active: true }
  ]);
  
  get activeItems() {
    return this.items().filter(item => item.active);
  }
  
  get itemsByCategory() {
    return this.items().reduce((acc, item) => {
      if (!acc[item.category]) {
        acc[item.category] = [];
      }
      acc[item.category].push(item);
      return acc;
    }, {} as Record<string, any[]>);
  }
}
```

```html
<h3>アクティブなアイテム ({{activeItems.length}}件)</h3>
@for (item of activeItems; track item.id) {
  <div>{{item.name}}</div>
}

<h3>カテゴリ別</h3>
@for (category of Object.keys(itemsByCategory); track category) {
  <h4>{{category}} ({{itemsByCategory[category].length}}件)</h4>
  @for (item of itemsByCategory[category]; track item.id) {
    <div>{{item.name}}</div>
  }
}
```

## ベストプラクティス

### 1. シンプルな式を使用
```html
<!-- 良い例 -->
<p>{{userName}}</p>
<p>{{isLoggedIn ? 'ログイン中' : '未ログイン'}}</p>

<!-- 悪い例 -->
<p>{{user ? user.profile ? user.profile.name : '名無し' : 'ユーザーなし'}}</p>
```

### 2. 複雑なロジックはコンポーネントで処理
```typescript
// テンプレートで複雑な処理を避ける
export class ComplexComponent {
  data = signal<any[]>([]);
  
  get processedData() {
    return this.data()
      .filter(item => item.active)
      .sort((a, b) => a.priority - b.priority)
      .slice(0, 10);
  }
}
```

### 3. 副作用のない式
```html
<!-- 良い例：副作用なし -->
<p>{{getDisplayValue()}}</p>

<!-- 悪い例：副作用あり -->
<p>{{incrementCounter()}}</p>
```

### 4. 型安全性の確保
```typescript
export class TypeSafeComponent {
  user = signal<User | null>(null);
  
  get safeUserName() {
    return this.user()?.name ?? 'ゲスト';
  }
  
  get safeUserAge() {
    return this.user()?.age ?? 0;
  }
}
```

## アンチパターン

### 1. テンプレートでの重い処理
```html
<!-- 避けるべき -->
<p>{{expensiveCalculation()}}</p>
```

### 2. 長すぎる式
```html
<!-- 避けるべき -->
<p>{{user.firstName + ' ' + user.lastName + ' (' + user.age + '歳) - ' + user.department + ' - ' + user.role}}</p>
```

### 3. 副作用のある式
```html
<!-- 避けるべき -->
<p>{{logValue()}}</p>
<p>{{updateCounter()}}</p>
```

## 注意点

- テンプレート式は表示に専念する
- 複雑なロジックはコンポーネント側で処理
- パフォーマンスを考慮した実装
- Angular v20のSignalとの組み合わせも検討

## 関連技術
- テンプレート式
- プロパティバインディング
- getter/setter
- Angular v20のSignal
- パフォーマンス最適化
