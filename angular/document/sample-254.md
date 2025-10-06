# #254 「Presentation Component - 表示専用」

## 概要
Presentation Componentは、UIの描画とユーザーインタラクションのみを担当する完全に表示専用のコンポーネントです。ビジネスロジックや状態管理を持たず、受け取ったデータを忠実に表示し、ユーザーアクションをイベントとして発行します。

## 学習目標
- Presentation Componentの設計原則を理解する
- ステートレスなコンポーネント実装を習得する
- 高い再利用性を実現する方法を学ぶ

## 技術ポイント
- **ステートレス**: 内部状態を持たない設計
- **純粋な表示**: UIレンダリングのみに集中
- **明確な契約**: 入出力の型定義

## 📺 画面表示用コード

### 基本パターン
```typescript
@Component({
  selector: 'app-product-card',
  template: `
    <div class="card">
      <img [src]="product().imageUrl" [alt]="product().name">
      <h3>{{ product().name }}</h3>
      <p class="price">¥{{ product().price.toLocaleString() }}</p>
      <button (click)="buyClick.emit(product())">購入</button>
    </div>
  `,
  standalone: true
})
export class ProductCardComponent {
  product = input.required<Product>();
  buyClick = output<Product>();
}
```

### リスト表示
```typescript
@Component({
  selector: 'app-product-grid',
  template: `
    <div class="grid">
      @for (product of products(); track product.id) {
        <app-product-card
          [product]="product"
          (buyClick)="productSelected.emit($event)"
        />
      }
    </div>
  `,
  standalone: true,
  imports: [ProductCardComponent]
})
export class ProductGridComponent {
  products = input<Product[]>([]);
  productSelected = output<Product>();
}
```

### 条件付き表示
```typescript
@Component({
  selector: 'app-status-message',
  template: `
    @switch (status()) {
      @case ('success') {
        <div class="alert success">{{ message() }}</div>
      }
      @case ('error') {
        <div class="alert error">{{ message() }}</div>
      }
      @case ('warning') {
        <div class="alert warning">{{ message() }}</div>
      }
    }
  `,
  standalone: true
})
export class StatusMessageComponent {
  status = input.required<'success' | 'error' | 'warning'>();
  message = input.required<string>();
}
```

## 実践的な活用例

### ユーザープロファイル表示
```typescript
interface UserProfile {
  id: string;
  name: string;
  email: string;
  avatar: string;
  bio: string;
  stats: {
    posts: number;
    followers: number;
    following: number;
  };
}

@Component({
  selector: 'app-user-profile',
  template: `
    <div class="profile">
      <div class="profile-header">
        <img [src]="user().avatar" class="avatar">
        <div class="info">
          <h2>{{ user().name }}</h2>
          <p class="email">{{ user().email }}</p>
        </div>
        @if (editable()) {
          <button (click)="edit.emit()">編集</button>
        }
      </div>

      <div class="bio">{{ user().bio }}</div>

      <div class="stats">
        <div class="stat">
          <span class="count">{{ user().stats.posts }}</span>
          <span class="label">投稿</span>
        </div>
        <div class="stat">
          <span class="count">{{ user().stats.followers }}</span>
          <span class="label">フォロワー</span>
        </div>
        <div class="stat">
          <span class="count">{{ user().stats.following }}</span>
          <span class="label">フォロー中</span>
        </div>
      </div>

      @if (showActions()) {
        <div class="actions">
          <button (click)="follow.emit(user().id)">
            フォロー
          </button>
          <button (click)="message.emit(user().id)">
            メッセージ
          </button>
        </div>
      }
    </div>
  `,
  styles: [`
    .profile {
      border: 1px solid #ddd;
      border-radius: 8px;
      padding: 24px;
    }
    .profile-header {
      display: flex;
      align-items: center;
      gap: 16px;
    }
    .avatar {
      width: 80px;
      height: 80px;
      border-radius: 50%;
    }
    .stats {
      display: flex;
      gap: 32px;
      margin-top: 16px;
    }
    .stat {
      display: flex;
      flex-direction: column;
      align-items: center;
    }
    .count {
      font-size: 24px;
      font-weight: bold;
    }
  `],
  standalone: true
})
export class UserProfileComponent {
  user = input.required<UserProfile>();
  editable = input(false);
  showActions = input(true);

  edit = output<void>();
  follow = output<string>();
  message = output<string>();
}
```

### データテーブル表示
```typescript
interface TableColumn<T> {
  key: keyof T;
  label: string;
  width?: string;
  align?: 'left' | 'center' | 'right';
  format?: (value: any) => string;
}

@Component({
  selector: 'app-data-table',
  template: `
    <table class="data-table">
      <thead>
        <tr>
          @for (col of columns(); track col.key) {
            <th
              [style.width]="col.width"
              [style.text-align]="col.align || 'left'">
              {{ col.label }}
            </th>
          }
          @if (hasActions()) {
            <th>操作</th>
          }
        </tr>
      </thead>
      <tbody>
        @if (data().length === 0) {
          <tr>
            <td [attr.colspan]="columns().length + (hasActions() ? 1 : 0)">
              {{ emptyMessage() }}
            </td>
          </tr>
        } @else {
          @for (row of data(); track row.id) {
            <tr (click)="rowClick.emit(row)">
              @for (col of columns(); track col.key) {
                <td [style.text-align]="col.align || 'left'">
                  {{ formatValue(row[col.key], col) }}
                </td>
              }
              @if (hasActions()) {
                <td>
                  <button (click)="edit.emit(row); $event.stopPropagation()">
                    編集
                  </button>
                  <button (click)="delete.emit(row); $event.stopPropagation()">
                    削除
                  </button>
                </td>
              }
            </tr>
          }
        }
      </tbody>
    </table>
  `,
  styles: [`
    .data-table {
      width: 100%;
      border-collapse: collapse;
    }
    th, td {
      padding: 12px;
      border: 1px solid #ddd;
    }
    th {
      background: #f5f5f5;
      font-weight: bold;
    }
    tr:hover {
      background: #f9f9f9;
      cursor: pointer;
    }
  `],
  standalone: true
})
export class DataTableComponent<T extends { id: string }> {
  data = input.required<T[]>();
  columns = input.required<TableColumn<T>[]>();
  emptyMessage = input('データがありません');
  hasActions = input(true);

  rowClick = output<T>();
  edit = output<T>();
  delete = output<T>();

  formatValue(value: any, column: TableColumn<T>): string {
    if (column.format) {
      return column.format(value);
    }
    return value?.toString() ?? '';
  }
}
```

### フォーム入力表示
```typescript
@Component({
  selector: 'app-input-field',
  template: `
    <div class="field">
      <label [for]="id()">
        {{ label() }}
        @if (required()) {
          <span class="required">*</span>
        }
      </label>

      <input
        [id]="id()"
        [type]="type()"
        [placeholder]="placeholder()"
        [disabled]="disabled()"
        [value]="value()"
        (input)="valueChange.emit($any($event.target).value)"
      >

      @if (error()) {
        <span class="error">{{ error() }}</span>
      }

      @if (hint()) {
        <span class="hint">{{ hint() }}</span>
      }
    </div>
  `,
  styles: [`
    .field {
      display: flex;
      flex-direction: column;
      gap: 4px;
      margin-bottom: 16px;
    }
    label {
      font-weight: 500;
    }
    .required {
      color: red;
    }
    input {
      padding: 8px;
      border: 1px solid #ddd;
      border-radius: 4px;
    }
    input:disabled {
      background: #f5f5f5;
    }
    .error {
      color: red;
      font-size: 12px;
    }
    .hint {
      color: #666;
      font-size: 12px;
    }
  `],
  standalone: true
})
export class InputFieldComponent {
  id = input.required<string>();
  label = input.required<string>();
  type = input<'text' | 'email' | 'password' | 'number'>('text');
  value = input<string>('');
  placeholder = input<string>('');
  required = input(false);
  disabled = input(false);
  error = input<string>();
  hint = input<string>();

  valueChange = output<string>();
}
```

### カード一覧表示
```typescript
interface Article {
  id: string;
  title: string;
  excerpt: string;
  coverImage: string;
  author: string;
  publishedAt: Date;
  tags: string[];
  readTime: number;
}

@Component({
  selector: 'app-article-card',
  template: `
    <article class="card">
      <img
        [src]="article().coverImage"
        [alt]="article().title"
        class="cover">

      <div class="content">
        <h3 (click)="titleClick.emit(article())">
          {{ article().title }}
        </h3>

        <p class="excerpt">{{ article().excerpt }}</p>

        <div class="tags">
          @for (tag of article().tags; track tag) {
            <span
              class="tag"
              (click)="tagClick.emit(tag)">
              #{{ tag }}
            </span>
          }
        </div>

        <div class="meta">
          <span class="author">{{ article().author }}</span>
          <span class="date">{{ formatDate(article().publishedAt) }}</span>
          <span class="read-time">{{ article().readTime }}分</span>
        </div>
      </div>

      @if (showActions()) {
        <div class="actions">
          <button (click)="bookmark.emit(article())">
            ブックマーク
          </button>
          <button (click)="share.emit(article())">
            共有
          </button>
        </div>
      }
    </article>
  `,
  styles: [`
    .card {
      border: 1px solid #ddd;
      border-radius: 8px;
      overflow: hidden;
    }
    .cover {
      width: 100%;
      height: 200px;
      object-fit: cover;
    }
    .content {
      padding: 16px;
    }
    h3 {
      margin: 0 0 8px 0;
      cursor: pointer;
    }
    h3:hover {
      color: #007bff;
    }
    .tags {
      display: flex;
      gap: 8px;
      margin: 12px 0;
    }
    .tag {
      padding: 4px 8px;
      background: #f0f0f0;
      border-radius: 4px;
      font-size: 12px;
      cursor: pointer;
    }
    .meta {
      display: flex;
      gap: 16px;
      font-size: 14px;
      color: #666;
    }
  `],
  standalone: true
})
export class ArticleCardComponent {
  article = input.required<Article>();
  showActions = input(true);

  titleClick = output<Article>();
  tagClick = output<string>();
  bookmark = output<Article>();
  share = output<Article>();

  formatDate(date: Date): string {
    return new Date(date).toLocaleDateString('ja-JP');
  }
}
```

### ナビゲーションメニュー
```typescript
interface MenuItem {
  id: string;
  label: string;
  icon?: string;
  href?: string;
  children?: MenuItem[];
}

@Component({
  selector: 'app-nav-menu',
  template: `
    <nav class="menu">
      @for (item of items(); track item.id) {
        <div class="menu-item">
          <a
            [class.active]="item.id === activeId()"
            (click)="itemClick.emit(item)">
            @if (item.icon) {
              <span class="icon">{{ item.icon }}</span>
            }
            <span class="label">{{ item.label }}</span>
          </a>

          @if (item.children && item.children.length > 0) {
            <div class="submenu">
              @for (child of item.children; track child.id) {
                <a
                  [class.active]="child.id === activeId()"
                  (click)="itemClick.emit(child)">
                  {{ child.label }}
                </a>
              }
            </div>
          }
        </div>
      }
    </nav>
  `,
  styles: [`
    .menu {
      display: flex;
      flex-direction: column;
    }
    .menu-item a {
      display: flex;
      align-items: center;
      gap: 8px;
      padding: 12px 16px;
      text-decoration: none;
      color: #333;
      cursor: pointer;
    }
    .menu-item a:hover {
      background: #f5f5f5;
    }
    .menu-item a.active {
      background: #007bff;
      color: white;
    }
    .submenu {
      padding-left: 24px;
    }
  `],
  standalone: true
})
export class NavMenuComponent {
  items = input.required<MenuItem[]>();
  activeId = input<string>();

  itemClick = output<MenuItem>();
}
```

## ベストプラクティス

### 純粋な表示ロジック
```typescript
// ✅ 計算は純粋関数で
formatPrice(price: number): string {
  return `¥${price.toLocaleString()}`;
}

displayText = computed(() =>
  this.text().toUpperCase()
);

// ❌ ビジネスロジックは避ける
async saveData() {
  await this.service.save(); // Presentation Componentには不適切
}
```

### 明確な型定義
```typescript
// ✅ 厳密な型定義
product = input.required<Product>();
quantity = input<number>(1);

// ❌ any や不明確な型
data = input<any>(); // 避けるべき
```

### イベントの発行
```typescript
// ✅ 具体的なイベント名
addToCart = output<Product>();
removeFromCart = output<string>();

// ❌ 汎用的な名前
action = output<any>(); // 何をするか不明確
```

## 注意点

### 状態管理
Presentation Componentは状態を持つべきではありません。UI状態（開閉など）は例外的に許容されます。

### 依存性
サービスやストアの注入は避け、すべてのデータを入力で受け取ってください。

### 再利用性
特定のコンテキストに依存しない設計を心がけ、様々な場面で再利用できるようにしてください。

### OnPush戦略
変更検知最適化のため、`ChangeDetectionStrategy.OnPush`の使用を推奨します。

## 関連技術
- **Dumb Component**: 同様の概念
- **input()/output()**: Signal入出力
- **OnPush Strategy**: 変更検知最適化
- **Standalone Components**: 独立コンポーネント
- **Component Architecture**: アーキテクチャ設計
