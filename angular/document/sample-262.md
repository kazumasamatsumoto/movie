# #262 「Component の再利用性向上」

## 概要
Componentの再利用性向上は、同じコンポーネントを様々な場面で使えるようにする設計技術です。汎用的なインターフェース、外部依存の排除、柔軟なカスタマイズ性により、開発効率と一貫性が向上します。

## 学習目標
- 再利用可能なコンポーネントの設計原則を理解する
- 汎用化のテクニックを習得する
- 柔軟性と使いやすさのバランスを学ぶ

## 技術ポイント
- **汎用化**: 特定のコンテキストに依存しない設計
- **カスタマイズ性**: 柔軟な設定オプション
- **疎結合**: 外部依存を最小化

## 📺 画面表示用コード

### 再利用性の低い例
```typescript
// ❌ 特定の用途に限定されている
@Component({
  selector: 'app-user-avatar',
  template: `
    <img
      [src]="'https://api.example.com/users/' + userId + '/avatar'"
      alt="User Avatar"
      style="width: 48px; height: 48px; border-radius: 50%;">
  `
})
export class UserAvatarComponent {
  @Input() userId!: string;
}
// 問題点:
// - URLがハードコード
// - サイズが固定
// - ユーザー専用（他のアバターに使えない）
```

### 再利用性の高い例
```typescript
// ✅ 汎用的で柔軟
@Component({
  selector: 'app-avatar',
  template: `
    <img
      [src]="imageUrl()"
      [alt]="alt()"
      [style.width.px]="size()"
      [style.height.px]="size()"
      [style.border-radius]="rounded() ? '50%' : '0'"
      [class]="customClass()"
      (click)="avatarClick.emit()">
  `,
  standalone: true
})
export class AvatarComponent {
  imageUrl = input.required<string>();
  alt = input('Avatar');
  size = input(48);
  rounded = input(true);
  customClass = input('');
  avatarClick = output<void>();
}
// 利点:
// - どんな画像にも使える
// - サイズをカスタマイズ可能
// - 形状を変更可能
// - スタイルを追加可能
```

### 設定可能な汎用ボタン
```typescript
@Component({
  selector: 'app-button',
  template: `
    <button
      [type]="type()"
      [disabled]="disabled() || loading()"
      [class]="getButtonClass()"
      (click)="handleClick()">

      @if (loading()) {
        <span class="spinner"></span>
      }

      @if (icon() && iconPosition() === 'left') {
        <span class="icon">{{ icon() }}</span>
      }

      <span class="label">
        <ng-content></ng-content>
      </span>

      @if (icon() && iconPosition() === 'right') {
        <span class="icon">{{ icon() }}</span>
      }
    </button>
  `,
  styles: [`
    button {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 8px 16px;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      transition: all 0.2s;
    }
    button:disabled {
      opacity: 0.5;
      cursor: not-allowed;
    }
    .btn-primary { background: #007bff; color: white; }
    .btn-secondary { background: #6c757d; color: white; }
    .btn-success { background: #28a745; color: white; }
    .btn-danger { background: #dc3545; color: white; }
    .btn-sm { padding: 4px 8px; font-size: 12px; }
    .btn-lg { padding: 12px 24px; font-size: 18px; }
  `],
  standalone: true
})
export class ButtonComponent {
  type = input<'button' | 'submit' | 'reset'>('button');
  variant = input<'primary' | 'secondary' | 'success' | 'danger'>('primary');
  size = input<'sm' | 'md' | 'lg'>('md');
  disabled = input(false);
  loading = input(false);
  icon = input<string>();
  iconPosition = input<'left' | 'right'>('left');
  customClass = input('');

  buttonClick = output<MouseEvent>();

  getButtonClass(): string {
    const classes = [
      `btn-${this.variant()}`,
      this.size() !== 'md' ? `btn-${this.size()}` : '',
      this.customClass()
    ];
    return classes.filter(c => c).join(' ');
  }

  handleClick(event: MouseEvent) {
    if (!this.disabled() && !this.loading()) {
      this.buttonClick.emit(event);
    }
  }
}
```

## 実践的な活用例

### 汎用カードコンポーネント
```typescript
@Component({
  selector: 'app-card',
  template: `
    <div
      [class]="getCardClass()"
      [style.width]="width()"
      (click)="cardClick.emit()">

      @if (showHeader()) {
        <div class="card-header">
          @if (headerTemplate()) {
            <ng-container *ngTemplateOutlet="headerTemplate()!" />
          } @else {
            <h3>{{ title() }}</h3>
            @if (closable()) {
              <button class="close" (click)="close.emit(); $event.stopPropagation()">
                ×
              </button>
            }
          }
        </div>
      }

      <div class="card-body" [style.padding]="padding()">
        <ng-content></ng-content>
      </div>

      @if (hasFooter()) {
        <div class="card-footer">
          <ng-content select="[footer]"></ng-content>
        </div>
      }
    </div>
  `,
  styles: [`
    .card {
      border: 1px solid #ddd;
      border-radius: 8px;
      background: white;
      overflow: hidden;
    }
    .card-elevated {
      box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    .card-outlined {
      border: 2px solid #007bff;
    }
    .card-header {
      padding: 16px;
      border-bottom: 1px solid #ddd;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .card-body {
      padding: 16px;
    }
    .card-footer {
      padding: 16px;
      border-top: 1px solid #ddd;
      background: #f8f9fa;
    }
  `],
  standalone: true
})
export class CardComponent {
  title = input<string>();
  width = input<string>('100%');
  padding = input<string>('16px');
  elevated = input(false);
  outlined = input(false);
  closable = input(false);
  customClass = input('');
  headerTemplate = input<TemplateRef<any>>();

  cardClick = output<void>();
  close = output<void>();

  showHeader = computed(() => this.title() || this.headerTemplate() || this.closable());
  hasFooter = signal(false);

  getCardClass(): string {
    const classes = [
      'card',
      this.elevated() ? 'card-elevated' : '',
      this.outlined() ? 'card-outlined' : '',
      this.customClass()
    ];
    return classes.filter(c => c).join(' ');
  }
}

// 使用例1: シンプル
@Component({
  template: `
    <app-card [title]="'ユーザー情報'">
      <p>名前: 山田太郎</p>
    </app-card>
  `
})
export class Example1Component {}

// 使用例2: カスタムヘッダー
@Component({
  template: `
    <app-card [headerTemplate]="customHeader">
      <p>コンテンツ</p>
      <div footer>
        <button>アクション</button>
      </div>
    </app-card>

    <ng-template #customHeader>
      <div class="custom-header">
        <span>カスタムヘッダー</span>
        <span>追加情報</span>
      </div>
    </ng-template>
  `
})
export class Example2Component {}

// 使用例3: スタイルカスタマイズ
@Component({
  template: `
    <app-card
      [elevated]="true"
      [width]="'400px'"
      [padding]="'24px'"
      [closable]="true"
      (close)="handleClose()">
      <p>カスタマイズされたカード</p>
    </app-card>
  `
})
export class Example3Component {}
```

### 汎用データテーブル
```typescript
interface TableColumn<T> {
  key: keyof T;
  label: string;
  width?: string;
  align?: 'left' | 'center' | 'right';
  sortable?: boolean;
  format?: (value: any, row: T) => string;
  template?: TemplateRef<any>;
}

@Component({
  selector: 'app-data-table',
  template: `
    <div class="table-container">
      <table [class]="customClass()">
        <thead>
          <tr>
            @for (col of columns(); track col.key) {
              <th
                [style.width]="col.width"
                [style.text-align]="col.align || 'left'"
                [class.sortable]="col.sortable"
                (click)="handleSort(col)">
                {{ col.label }}
                @if (col.sortable && sortBy() === col.key) {
                  <span class="sort-icon">
                    {{ sortDirection() === 'asc' ? '↑' : '↓' }}
                  </span>
                }
              </th>
            }
            @if (hasActions()) {
              <th [style.width]="actionsWidth()">{{ actionsLabel() }}</th>
            }
          </tr>
        </thead>

        <tbody>
          @if (loading()) {
            <tr>
              <td [attr.colspan]="columnCount()">
                <div class="loading">{{ loadingMessage() }}</div>
              </td>
            </tr>
          } @else if (data().length === 0) {
            <tr>
              <td [attr.colspan]="columnCount()">
                <div class="empty">{{ emptyMessage() }}</div>
              </td>
            </tr>
          } @else {
            @for (row of data(); track trackBy(row)) {
              <tr
                [class.selectable]="selectable()"
                [class.selected]="isSelected(row)"
                (click)="handleRowClick(row)">
                @for (col of columns(); track col.key) {
                  <td [style.text-align]="col.align || 'left'">
                    @if (col.template) {
                      <ng-container
                        *ngTemplateOutlet="col.template; context: { $implicit: row, value: row[col.key] }" />
                    } @else {
                      {{ formatValue(row[col.key], col, row) }}
                    }
                  </td>
                }
                @if (hasActions()) {
                  <td>
                    <ng-content select="[actions]"></ng-content>
                  </td>
                }
              </tr>
            }
          }
        </tbody>
      </table>

      @if (pagination()) {
        <div class="pagination">
          <button
            (click)="handlePageChange(currentPage() - 1)"
            [disabled]="currentPage() === 1">
            前へ
          </button>
          <span>{{ currentPage() }} / {{ totalPages() }}</span>
          <button
            (click)="handlePageChange(currentPage() + 1)"
            [disabled]="currentPage() === totalPages()">
            次へ
          </button>
        </div>
      }
    </div>
  `,
  styles: [`
    table {
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
    th.sortable {
      cursor: pointer;
      user-select: none;
    }
    tr.selectable {
      cursor: pointer;
    }
    tr.selectable:hover {
      background: #f9f9f9;
    }
    tr.selected {
      background: #e3f2fd;
    }
    .loading, .empty {
      text-align: center;
      padding: 32px;
      color: #666;
    }
  `],
  standalone: true
})
export class DataTableComponent<T> {
  data = input.required<T[]>();
  columns = input.required<TableColumn<T>[]>();

  // ソート
  sortBy = input<keyof T>();
  sortDirection = input<'asc' | 'desc'>('asc');

  // ページネーション
  pagination = input(false);
  currentPage = input(1);
  totalPages = input(1);

  // 選択
  selectable = input(false);
  selectedItems = input<T[]>([]);

  // アクション
  hasActions = input(false);
  actionsLabel = input('操作');
  actionsWidth = input('150px');

  // メッセージ
  loadingMessage = input('読み込み中...');
  emptyMessage = input('データがありません');
  loading = input(false);

  // カスタマイズ
  customClass = input('');
  trackByFn = input<(item: T) => any>();

  // イベント
  rowClick = output<T>();
  sort = output<{ key: keyof T; direction: 'asc' | 'desc' }>();
  pageChange = output<number>();
  selectionChange = output<T[]>();

  columnCount = computed(() =>
    this.columns().length + (this.hasActions() ? 1 : 0)
  );

  formatValue(value: any, column: TableColumn<T>, row: T): string {
    if (column.format) {
      return column.format(value, row);
    }
    return value?.toString() ?? '';
  }

  handleSort(column: TableColumn<T>) {
    if (!column.sortable) return;

    const direction =
      this.sortBy() === column.key && this.sortDirection() === 'asc'
        ? 'desc'
        : 'asc';

    this.sort.emit({ key: column.key, direction });
  }

  handleRowClick(row: T) {
    if (this.selectable()) {
      const selected = [...this.selectedItems()];
      const index = selected.indexOf(row);

      if (index > -1) {
        selected.splice(index, 1);
      } else {
        selected.push(row);
      }

      this.selectionChange.emit(selected);
    }

    this.rowClick.emit(row);
  }

  handlePageChange(page: number) {
    if (page >= 1 && page <= this.totalPages()) {
      this.pageChange.emit(page);
    }
  }

  isSelected(row: T): boolean {
    return this.selectedItems().includes(row);
  }

  trackBy(item: T): any {
    if (this.trackByFn()) {
      return this.trackByFn()!(item);
    }
    return item;
  }
}

// 使用例
@Component({
  template: `
    <app-data-table
      [data]="users()"
      [columns]="columns"
      [sortBy]="'name'"
      [pagination]="true"
      [currentPage]="1"
      [totalPages]="5"
      [selectable]="true"
      (sort)="handleSort($event)"
      (rowClick)="handleRowClick($event)">
    </app-data-table>
  `
})
export class UsersTableComponent {
  users = signal<User[]>([]);

  columns: TableColumn<User>[] = [
    {
      key: 'name',
      label: '名前',
      sortable: true
    },
    {
      key: 'email',
      label: 'メール',
      sortable: true
    },
    {
      key: 'createdAt',
      label: '登録日',
      format: (value) => new Date(value).toLocaleDateString()
    }
  ];

  handleSort(sort: any) {
    console.log('Sort:', sort);
  }

  handleRowClick(user: User) {
    console.log('Clicked:', user);
  }
}
```

### 汎用フォーム入力
```typescript
@Component({
  selector: 'app-form-input',
  template: `
    <div [class]="getContainerClass()">
      @if (label()) {
        <label [for]="id()">
          {{ label() }}
          @if (required()) {
            <span class="required">*</span>
          }
        </label>
      }

      <div class="input-wrapper">
        @if (prefix()) {
          <span class="prefix">{{ prefix() }}</span>
        }

        <input
          [id]="id()"
          [type]="type()"
          [placeholder]="placeholder()"
          [value]="value()"
          [disabled]="disabled()"
          [readonly]="readonly()"
          [min]="min()"
          [max]="max()"
          [step]="step()"
          [pattern]="pattern()"
          [autocomplete]="autocomplete()"
          (input)="handleInput($event)"
          (blur)="handleBlur()"
          (focus)="handleFocus()">

        @if (suffix()) {
          <span class="suffix">{{ suffix() }}</span>
        }

        @if (clearable() && value()) {
          <button
            type="button"
            class="clear"
            (click)="handleClear()">
            ×
          </button>
        }
      </div>

      @if (error()) {
        <span class="error">{{ error() }}</span>
      }

      @if (hint() && !error()) {
        <span class="hint">{{ hint() }}</span>
      }

      @if (showCharCount() && maxLength()) {
        <span class="char-count">
          {{ value().length }} / {{ maxLength() }}
        </span>
      }
    </div>
  `,
  styles: [`
    .form-input {
      display: flex;
      flex-direction: column;
      gap: 4px;
      margin-bottom: 16px;
    }
    label {
      font-weight: 500;
      font-size: 14px;
    }
    .required {
      color: red;
      margin-left: 4px;
    }
    .input-wrapper {
      position: relative;
      display: flex;
      align-items: center;
    }
    input {
      flex: 1;
      padding: 8px 12px;
      border: 1px solid #ddd;
      border-radius: 4px;
      font-size: 14px;
    }
    input:focus {
      outline: none;
      border-color: #007bff;
    }
    input:disabled {
      background: #f5f5f5;
      cursor: not-allowed;
    }
    .prefix, .suffix {
      padding: 0 8px;
      color: #666;
    }
    .clear {
      position: absolute;
      right: 8px;
      background: none;
      border: none;
      cursor: pointer;
      font-size: 20px;
    }
    .error {
      color: #dc3545;
      font-size: 12px;
    }
    .hint {
      color: #666;
      font-size: 12px;
    }
    .char-count {
      font-size: 12px;
      color: #666;
      text-align: right;
    }
  `],
  standalone: true
})
export class FormInputComponent {
  // 基本
  id = input.required<string>();
  type = input<'text' | 'email' | 'password' | 'number' | 'tel' | 'url'>('text');
  label = input<string>();
  placeholder = input('');
  value = input('');

  // 検証
  required = input(false);
  min = input<number>();
  max = input<number>();
  step = input<number>();
  pattern = input<string>();
  maxLength = input<number>();

  // 状態
  disabled = input(false);
  readonly = input(false);

  // UI
  prefix = input<string>();
  suffix = input<string>();
  clearable = input(false);
  showCharCount = input(false);

  // メッセージ
  error = input<string>();
  hint = input<string>();

  // その他
  autocomplete = input<string>();
  customClass = input('');

  // イベント
  valueChange = output<string>();
  inputBlur = output<void>();
  inputFocus = output<void>();

  getContainerClass(): string {
    return `form-input ${this.customClass()}`;
  }

  handleInput(event: Event) {
    const value = (event.target as HTMLInputElement).value;
    this.valueChange.emit(value);
  }

  handleBlur() {
    this.inputBlur.emit();
  }

  handleFocus() {
    this.inputFocus.emit();
  }

  handleClear() {
    this.valueChange.emit('');
  }
}
```

## ベストプラクティス

### 設定可能なプロパティ
```typescript
// ✅ 多くのオプションを提供
@Component({
  selector: 'app-modal'
})
export class ModalComponent {
  title = input<string>();
  width = input('500px');
  closable = input(true);
  closeOnOverlay = input(true);
  closeOnEscape = input(true);
  showHeader = input(true);
  showFooter = input(true);
}

// ❌ 固定値
@Component({
  selector: 'app-modal',
  template: `
    <div style="width: 500px">
      <!-- 固定値で柔軟性なし -->
    </div>
  `
})
export class ModalComponent {}
```

### デフォルト値の提供
```typescript
// ✅ 合理的なデフォルト値
@Component({
  selector: 'app-button'
})
export class ButtonComponent {
  variant = input<'primary' | 'secondary'>('primary'); // デフォルト値
  size = input<'sm' | 'md' | 'lg'>('md');
  type = input<'button' | 'submit'>('button');
}
```

### テンプレートのカスタマイズ
```typescript
// ✅ テンプレートを受け入れる
@Component({
  selector: 'app-list'
})
export class ListComponent<T> {
  items = input.required<T[]>();
  itemTemplate = input<TemplateRef<any>>();
}
```

## 注意点

### 過度な汎用化
すべてを設定可能にすると複雑になりすぎます。バランスを取ってください。

### パフォーマンス
多くのinput()は変更検知に影響します。必要なものだけを提供してください。

### ドキュメント
再利用可能なコンポーネントには適切なドキュメントを用意してください。

## 関連技術
- **Component API Design**: API設計
- **Template Customization**: テンプレートカスタマイズ
- **Content Projection**: コンテンツ投影
- **Configuration Pattern**: 設定パターン
- **Generic Components**: ジェネリックコンポーネント
