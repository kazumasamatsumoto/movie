# #252 「Dumb Component - 純粋なコンポーネント」

## 概要
Dumb Component（純粋なコンポーネント）は、ビジネスロジックを持たない表示専用のコンポーネントです。@Input()でデータを受け取り、@Output()でイベントを発行するだけのシンプルな構造により、高い再利用性とテスタビリティを実現します。

## 学習目標
- Dumb Componentの特徴と利点を理解する
- 純粋な表示ロジックの実装方法を習得する
- 再利用可能なコンポーネント設計を学ぶ

## 技術ポイント
- **@Input()**: データの受け取り
- **@Output()**: イベントの発行
- **依存なし**: サービス注入を避ける

## 📺 画面表示用コード

### 基本的なDumb Component
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
  user = input.required<User>();
  select = output<User>();
}
```

### リスト表示
```typescript
@Component({
  selector: 'app-user-list',
  template: `
    @if (loading()) {
      <p>読み込み中...</p>
    } @else {
      @for (user of users(); track user.id) {
        <app-user-card
          [user]="user"
          (select)="userSelected.emit($event)"
        />
      }
    }
  `,
  standalone: true,
  imports: [UserCardComponent]
})
export class UserListComponent {
  users = input<User[]>([]);
  loading = input(false);
  userSelected = output<User>();
}
```

### フォーム表示
```typescript
@Component({
  selector: 'app-user-form',
  template: `
    <form (ngSubmit)="handleSubmit()">
      <input [(ngModel)]="formData.name" name="name">
      <input [(ngModel)]="formData.email" name="email">
      <button type="submit" [disabled]="saving()">
        {{ saving() ? '保存中...' : '保存' }}
      </button>
    </form>
  `,
  standalone: true,
  imports: [FormsModule]
})
export class UserFormComponent {
  initialValue = input<User | null>(null);
  saving = input(false);
  submit = output<UserFormData>();

  formData = { name: '', email: '' };

  ngOnInit() {
    const initial = this.initialValue();
    if (initial) {
      this.formData = { ...initial };
    }
  }

  handleSubmit() {
    this.submit.emit(this.formData);
  }
}
```

## 実践的な活用例(continued)

### 汎用カードコンポーネント
```typescript
@Component({
  selector: 'app-card',
  template: `
    <div class="card" [class.elevated]="elevated()">
      @if (title()) {
        <div class="card-header">
          <h3>{{ title() }}</h3>
          @if (closable()) {
            <button (click)="close.emit()">×</button>
          }
        </div>
      }
      <div class="card-body">
        <ng-content></ng-content>
      </div>
      @if (hasActions()) {
        <div class="card-footer">
          <ng-content select="[actions]"></ng-content>
        </div>
      }
    </div>
  `,
  styles: [`
    .card {
      border: 1px solid #ddd;
      border-radius: 8px;
      padding: 16px;
    }
    .elevated {
      box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
  `],
  standalone: true
})
export class CardComponent {
  title = input<string>();
  elevated = input(false);
  closable = input(false);
  close = output<void>();

  hasActions = signal(false);

  ngAfterContentInit() {
    // スロットコンテンツの有無をチェック
  }
}
```

### データテーブル
```typescript
interface Column<T> {
  key: keyof T;
  label: string;
  sortable?: boolean;
}

@Component({
  selector: 'app-data-table',
  template: `
    <table>
      <thead>
        <tr>
          @for (column of columns(); track column.key) {
            <th (click)="handleSort(column)">
              {{ column.label }}
              @if (column.sortable) {
                <span class="sort-icon">
                  {{ getSortIcon(column.key) }}
                </span>
              }
            </th>
          }
        </tr>
      </thead>
      <tbody>
        @for (row of data(); track row.id) {
          <tr (click)="rowClick.emit(row)">
            @for (column of columns(); track column.key) {
              <td>{{ row[column.key] }}</td>
            }
          </tr>
        }
      </tbody>
    </table>
  `,
  standalone: true
})
export class DataTableComponent<T> {
  data = input.required<T[]>();
  columns = input.required<Column<T>[]>();
  sortBy = input<keyof T>();
  sortDirection = input<'asc' | 'desc'>('asc');

  rowClick = output<T>();
  sort = output<{ key: keyof T; direction: 'asc' | 'desc' }>();

  handleSort(column: Column<T>) {
    if (!column.sortable) return;

    const direction = this.sortBy() === column.key && this.sortDirection() === 'asc'
      ? 'desc'
      : 'asc';

    this.sort.emit({ key: column.key, direction });
  }

  getSortIcon(key: keyof T): string {
    if (this.sortBy() !== key) return '⇅';
    return this.sortDirection() === 'asc' ? '↑' : '↓';
  }
}
```

### ステータスバッジ
```typescript
type Status = 'success' | 'warning' | 'error' | 'info';

@Component({
  selector: 'app-badge',
  template: `
    <span
      class="badge"
      [class]="'badge-' + status()"
      [class.badge-large]="size() === 'large'">
      @if (icon()) {
        <span class="icon">{{ icon() }}</span>
      }
      {{ text() }}
    </span>
  `,
  styles: [`
    .badge {
      display: inline-flex;
      align-items: center;
      gap: 4px;
      padding: 4px 8px;
      border-radius: 4px;
      font-size: 12px;
    }
    .badge-success { background: #d4edda; color: #155724; }
    .badge-warning { background: #fff3cd; color: #856404; }
    .badge-error { background: #f8d7da; color: #721c24; }
    .badge-info { background: #d1ecf1; color: #0c5460; }
    .badge-large { font-size: 14px; padding: 6px 12px; }
  `],
  standalone: true
})
export class BadgeComponent {
  status = input<Status>('info');
  text = input.required<string>();
  icon = input<string>();
  size = input<'small' | 'large'>('small');
}
```

### ペジネーション
```typescript
@Component({
  selector: 'app-pagination',
  template: `
    <div class="pagination">
      <button
        (click)="goToPage(currentPage() - 1)"
        [disabled]="currentPage() === 1">
        前へ
      </button>

      @for (page of visiblePages(); track page) {
        <button
          (click)="goToPage(page)"
          [class.active]="page === currentPage()">
          {{ page }}
        </button>
      }

      <button
        (click)="goToPage(currentPage() + 1)"
        [disabled]="currentPage() === totalPages()">
        次へ
      </button>
    </div>
  `,
  styles: [`
    .pagination {
      display: flex;
      gap: 4px;
    }
    button.active {
      background: #007bff;
      color: white;
    }
  `],
  standalone: true
})
export class PaginationComponent {
  currentPage = input.required<number>();
  totalPages = input.required<number>();
  maxVisible = input(5);

  pageChange = output<number>();

  visiblePages = computed(() => {
    const current = this.currentPage();
    const total = this.totalPages();
    const max = this.maxVisible();

    const pages: number[] = [];
    const half = Math.floor(max / 2);

    let start = Math.max(1, current - half);
    let end = Math.min(total, start + max - 1);

    if (end - start + 1 < max) {
      start = Math.max(1, end - max + 1);
    }

    for (let i = start; i <= end; i++) {
      pages.push(i);
    }

    return pages;
  });

  goToPage(page: number) {
    if (page >= 1 && page <= this.totalPages()) {
      this.pageChange.emit(page);
    }
  }
}
```

### モーダルダイアログ
```typescript
@Component({
  selector: 'app-modal',
  template: `
    @if (isOpen()) {
      <div class="modal-overlay" (click)="handleOverlayClick()">
        <div class="modal-content" (click)="$event.stopPropagation()">
          <div class="modal-header">
            <h2>{{ title() }}</h2>
            @if (closable()) {
              <button (click)="close.emit()">×</button>
            }
          </div>
          <div class="modal-body">
            <ng-content></ng-content>
          </div>
          @if (hasFooter()) {
            <div class="modal-footer">
              <ng-content select="[footer]"></ng-content>
            </div>
          }
        </div>
      </div>
    }
  `,
  styles: [`
    .modal-overlay {
      position: fixed;
      inset: 0;
      background: rgba(0,0,0,0.5);
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .modal-content {
      background: white;
      border-radius: 8px;
      max-width: 500px;
      width: 90%;
    }
  `],
  standalone: true
})
export class ModalComponent {
  isOpen = input(false);
  title = input.required<string>();
  closable = input(true);
  closeOnOverlay = input(true);

  close = output<void>();

  hasFooter = signal(false);

  handleOverlayClick() {
    if (this.closeOnOverlay()) {
      this.close.emit();
    }
  }
}
```

### ローディングスピナー
```typescript
@Component({
  selector: 'app-spinner',
  template: `
    <div class="spinner-container" [class]="'size-' + size()">
      <div class="spinner" [style.border-top-color]="color()"></div>
      @if (message()) {
        <p class="message">{{ message() }}</p>
      }
    </div>
  `,
  styles: [`
    .spinner {
      border: 3px solid #f3f3f3;
      border-radius: 50%;
      border-top: 3px solid;
      animation: spin 1s linear infinite;
    }
    .size-small .spinner { width: 20px; height: 20px; }
    .size-medium .spinner { width: 40px; height: 40px; }
    .size-large .spinner { width: 60px; height: 60px; }
    @keyframes spin {
      0% { transform: rotate(0deg); }
      100% { transform: rotate(360deg); }
    }
  `],
  standalone: true
})
export class SpinnerComponent {
  size = input<'small' | 'medium' | 'large'>('medium');
  color = input('#3498db');
  message = input<string>();
}
```

## ベストプラクティス

### 入出力の明確化
```typescript
// ✅ 明確な入出力定義
@Component({
  selector: 'app-item'
})
export class ItemComponent {
  item = input.required<Item>();
  selected = input(false);
  itemClick = output<Item>();
}

// ❌ あいまいな命名
@Component({
  selector: 'app-item'
})
export class ItemComponent {
  data = input<any>(); // 型が不明確
  action = output<any>(); // 何のイベントか不明
}
```

### サービス注入を避ける
```typescript
// ✅ Dumb: サービスなし
@Component({
  selector: 'app-display'
})
export class DisplayComponent {
  data = input.required<Data>();
}

// ❌ サービス注入（Smartの責任）
@Component({
  selector: 'app-display'
})
export class DisplayComponent {
  private service = inject(DataService); // 避けるべき
}
```

### 純粋な表示ロジック
```typescript
// ✅ computed での派生表示
displayText = computed(() => {
  return this.text().toUpperCase();
});

// ✅ 純粋な関数
formatDate(date: Date): string {
  return date.toLocaleDateString('ja-JP');
}
```

## 注意点

### 状態の管理
Dumb Componentは状態を持たないのが理想ですが、UI状態（展開/折りたたみ等）は許容されます。

### OnPush戦略
Dumb Componentは`ChangeDetectionStrategy.OnPush`と相性が良く、パフォーマンス最適化に有効です。

### 過度な複雑化
表示ロジックが複雑になりすぎた場合、複数のDumb Componentに分割してください。

### テスト
入出力が明確なため、単体テストが容易です。モックの準備が最小限で済みます。

## 関連技術
- **@Input/@Output**: データバインディング
- **input()/output()**: Signal入出力
- **OnPush**: 変更検知戦略
- **Standalone Components**: 独立コンポーネント
- **Presentation Pattern**: アーキテクチャパターン
