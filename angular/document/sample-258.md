# #258 「Pure Component の実装」

## 概要
Pure Componentは、同じ入力に対して常に同じ出力を返す、副作用のないコンポーネントです。外部状態に依存せず、純粋関数のみで構成されるため、予測可能性、テスタビリティ、パフォーマンスに優れています。

## 学習目標
- Pure Componentの原則を理解する
- 副作用のない実装方法を習得する
- 純粋性を保つベストプラクティスを学ぶ

## 技術ポイント
- **不変性**: データの変更を避ける
- **副作用なし**: 外部状態に依存しない
- **参照透過性**: 同じ入力→同じ出力

## 📺 画面表示用コード

### 基本的なPure Component
```typescript
@Component({
  selector: 'app-user-name',
  template: `<span>{{ formatName(user()) }}</span>`,
  changeDetection: ChangeDetectionStrategy.OnPush,
  standalone: true
})
export class UserNameComponent {
  user = input.required<User>();

  // 純粋関数: 同じ入力→同じ出力
  formatName(user: User): string {
    return `${user.firstName} ${user.lastName}`;
  }
}
```

### 純粋な計算ロジック
```typescript
@Component({
  selector: 'app-price-calculator',
  template: `
    <div>
      <p>単価: ¥{{ price() }}</p>
      <p>数量: {{ quantity() }}</p>
      <p>小計: ¥{{ calculateSubtotal(price(), quantity()) }}</p>
      <p>税込: ¥{{ calculateTotal(price(), quantity(), taxRate()) }}</p>
    </div>
  `,
  changeDetection: ChangeDetectionStrategy.OnPush,
  standalone: true
})
export class PriceCalculatorComponent {
  price = input.required<number>();
  quantity = input.required<number>();
  taxRate = input(0.1);

  // すべて純粋関数
  calculateSubtotal(price: number, quantity: number): number {
    return price * quantity;
  }

  calculateTotal(price: number, quantity: number, taxRate: number): number {
    const subtotal = this.calculateSubtotal(price, quantity);
    return subtotal * (1 + taxRate);
  }
}
```

### Signalを使ったPure Component
```typescript
@Component({
  selector: 'app-filtered-list',
  template: `
    @for (item of filteredItems(); track item.id) {
      <div>{{ item.name }}</div>
    }
  `,
  changeDetection: ChangeDetectionStrategy.OnPush,
  standalone: true
})
export class FilteredListComponent {
  items = input.required<Item[]>();
  filterText = input('');

  // computed は純粋な計算
  filteredItems = computed(() => {
    const filter = this.filterText().toLowerCase();
    return this.items().filter(item =>
      item.name.toLowerCase().includes(filter)
    );
  });
}
```

## 実践的な活用例

### データ変換とフォーマット
```typescript
interface Product {
  id: string;
  name: string;
  price: number;
  category: string;
  inStock: boolean;
}

@Component({
  selector: 'app-product-display',
  template: `
    <div class="product">
      <h3>{{ product().name }}</h3>
      <p class="price">{{ formatPrice(product().price) }}</p>
      <p class="category">{{ formatCategory(product().category) }}</p>
      <span [class]="getStockClass(product().inStock)">
        {{ getStockLabel(product().inStock) }}
      </span>
    </div>
  `,
  styles: [`
    .in-stock { color: green; }
    .out-of-stock { color: red; }
  `],
  changeDetection: ChangeDetectionStrategy.OnPush,
  standalone: true
})
export class ProductDisplayComponent {
  product = input.required<Product>();

  // 純粋関数: 価格フォーマット
  formatPrice(price: number): string {
    return `¥${price.toLocaleString()}`;
  }

  // 純粋関数: カテゴリフォーマット
  formatCategory(category: string): string {
    return category.charAt(0).toUpperCase() + category.slice(1);
  }

  // 純粋関数: 在庫状態のCSSクラス
  getStockClass(inStock: boolean): string {
    return inStock ? 'in-stock' : 'out-of-stock';
  }

  // 純粋関数: 在庫状態のラベル
  getStockLabel(inStock: boolean): string {
    return inStock ? '在庫あり' : '在庫なし';
  }
}
```

### リスト集計とフィルタリング
```typescript
interface Transaction {
  id: string;
  amount: number;
  type: 'income' | 'expense';
  date: Date;
  category: string;
}

@Component({
  selector: 'app-transaction-summary',
  template: `
    <div class="summary">
      <p>総収入: {{ formatAmount(totalIncome()) }}</p>
      <p>総支出: {{ formatAmount(totalExpense()) }}</p>
      <p>差額: {{ formatAmount(balance()) }}</p>

      <h3>カテゴリ別支出</h3>
      @for (item of expensesByCategory(); track item.category) {
        <div>
          {{ item.category }}: {{ formatAmount(item.total) }}
        </div>
      }
    </div>
  `,
  changeDetection: ChangeDetectionStrategy.OnPush,
  standalone: true
})
export class TransactionSummaryComponent {
  transactions = input.required<Transaction[]>();

  // 純粋な計算: 総収入
  totalIncome = computed(() =>
    this.transactions()
      .filter(t => t.type === 'income')
      .reduce((sum, t) => sum + t.amount, 0)
  );

  // 純粋な計算: 総支出
  totalExpense = computed(() =>
    this.transactions()
      .filter(t => t.type === 'expense')
      .reduce((sum, t) => sum + t.amount, 0)
  );

  // 純粋な計算: 差額
  balance = computed(() =>
    this.totalIncome() - this.totalExpense()
  );

  // 純粋な計算: カテゴリ別集計
  expensesByCategory = computed(() => {
    const expenses = this.transactions().filter(t => t.type === 'expense');
    const grouped = new Map<string, number>();

    expenses.forEach(t => {
      const current = grouped.get(t.category) || 0;
      grouped.set(t.category, current + t.amount);
    });

    return Array.from(grouped.entries()).map(([category, total]) => ({
      category,
      total
    }));
  });

  // 純粋関数: 金額フォーマット
  formatAmount(amount: number): string {
    return `¥${amount.toLocaleString()}`;
  }
}
```

### 日付と時刻の処理
```typescript
@Component({
  selector: 'app-event-card',
  template: `
    <div class="event">
      <h3>{{ event().title }}</h3>
      <p>{{ formatDate(event().startDate) }}</p>
      <p>{{ formatTimeRange(event().startDate, event().endDate) }}</p>
      <p>{{ formatDuration(event().startDate, event().endDate) }}</p>
      <span [class]="getStatusClass(event().startDate, event().endDate)">
        {{ getStatusLabel(event().startDate, event().endDate) }}
      </span>
    </div>
  `,
  changeDetection: ChangeDetectionStrategy.OnPush,
  standalone: true
})
export class EventCardComponent {
  event = input.required<Event>();

  // 純粋関数: 日付フォーマット
  formatDate(date: Date): string {
    return new Date(date).toLocaleDateString('ja-JP', {
      year: 'numeric',
      month: 'long',
      day: 'numeric'
    });
  }

  // 純粋関数: 時刻範囲フォーマット
  formatTimeRange(start: Date, end: Date): string {
    const startTime = new Date(start).toLocaleTimeString('ja-JP', {
      hour: '2-digit',
      minute: '2-digit'
    });
    const endTime = new Date(end).toLocaleTimeString('ja-JP', {
      hour: '2-digit',
      minute: '2-digit'
    });
    return `${startTime} - ${endTime}`;
  }

  // 純粋関数: 期間計算
  formatDuration(start: Date, end: Date): string {
    const diff = new Date(end).getTime() - new Date(start).getTime();
    const hours = Math.floor(diff / (1000 * 60 * 60));
    const minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
    return `${hours}時間${minutes}分`;
  }

  // 純粋関数: イベント状態判定
  getStatusClass(start: Date, end: Date): string {
    const now = new Date();
    const startDate = new Date(start);
    const endDate = new Date(end);

    if (now < startDate) return 'upcoming';
    if (now > endDate) return 'past';
    return 'ongoing';
  }

  // 純粋関数: ステータスラベル
  getStatusLabel(start: Date, end: Date): string {
    const statusClass = this.getStatusClass(start, end);
    const labels = {
      upcoming: '開催前',
      ongoing: '開催中',
      past: '終了'
    };
    return labels[statusClass as keyof typeof labels];
  }
}
```

### 配列操作とソート
```typescript
@Component({
  selector: 'app-sorted-list',
  template: `
    <div class="controls">
      <button
        *ngFor="let option of sortOptions"
        (click)="sortByChange.emit(option.key)">
        {{ option.label }}
      </button>
    </div>

    @for (item of sortedItems(); track item.id) {
      <div>{{ item.name }} - {{ item.value }}</div>
    }
  `,
  changeDetection: ChangeDetectionStrategy.OnPush,
  standalone: true
})
export class SortedListComponent<T extends { id: string }> {
  items = input.required<T[]>();
  sortBy = input<keyof T>();
  sortDirection = input<'asc' | 'desc'>('asc');

  sortByChange = output<keyof T>();

  sortOptions = [
    { key: 'name' as keyof T, label: '名前' },
    { key: 'value' as keyof T, label: '値' }
  ];

  // 純粋な計算: ソート
  sortedItems = computed(() => {
    const items = [...this.items()]; // 不変性を保つためコピー
    const key = this.sortBy();
    const direction = this.sortDirection();

    if (!key) return items;

    return items.sort((a, b) => {
      const aVal = a[key];
      const bVal = b[key];

      if (aVal < bVal) return direction === 'asc' ? -1 : 1;
      if (aVal > bVal) return direction === 'asc' ? 1 : -1;
      return 0;
    });
  });
}
```

### 条件付きスタイリング
```typescript
@Component({
  selector: 'app-progress-bar',
  template: `
    <div class="progress-container">
      <div
        class="progress-bar"
        [style.width.%]="percentage()"
        [style.background-color]="getColor(percentage())">
      </div>
      <span class="label">{{ formatPercentage(percentage()) }}</span>
    </div>
  `,
  styles: [`
    .progress-container {
      position: relative;
      width: 100%;
      height: 30px;
      background: #f0f0f0;
      border-radius: 4px;
    }
    .progress-bar {
      height: 100%;
      border-radius: 4px;
      transition: width 0.3s;
    }
  `],
  changeDetection: ChangeDetectionStrategy.OnPush,
  standalone: true
})
export class ProgressBarComponent {
  current = input.required<number>();
  total = input.required<number>();

  // 純粋な計算: パーセンテージ
  percentage = computed(() => {
    const total = this.total();
    if (total === 0) return 0;
    return Math.min(100, (this.current() / total) * 100);
  });

  // 純粋関数: 色の決定
  getColor(percentage: number): string {
    if (percentage < 30) return '#f44336';
    if (percentage < 70) return '#ff9800';
    return '#4caf50';
  }

  // 純粋関数: パーセンテージフォーマット
  formatPercentage(percentage: number): string {
    return `${percentage.toFixed(1)}%`;
  }
}
```

### テキスト処理とバリデーション
```typescript
@Component({
  selector: 'app-text-validator',
  template: `
    <div class="validator">
      <p>文字数: {{ getCharCount(text()) }} / {{ maxLength() }}</p>
      <p>単語数: {{ getWordCount(text()) }}</p>

      @if (hasError(text(), maxLength())) {
        <p class="error">{{ getErrorMessage(text(), maxLength()) }}</p>
      }

      <ul class="checks">
        @for (check of validationChecks(text()); track check.name) {
          <li [class.valid]="check.valid">
            {{ check.name }}: {{ check.valid ? '✓' : '✗' }}
          </li>
        }
      </ul>
    </div>
  `,
  changeDetection: ChangeDetectionStrategy.OnPush,
  standalone: true
})
export class TextValidatorComponent {
  text = input.required<string>();
  maxLength = input(100);

  // 純粋関数: 文字数カウント
  getCharCount(text: string): number {
    return text.length;
  }

  // 純粋関数: 単語数カウント
  getWordCount(text: string): number {
    return text.trim().split(/\s+/).filter(w => w.length > 0).length;
  }

  // 純粋関数: エラー判定
  hasError(text: string, maxLength: number): boolean {
    return text.length > maxLength;
  }

  // 純粋関数: エラーメッセージ
  getErrorMessage(text: string, maxLength: number): string {
    const over = text.length - maxLength;
    return `${over}文字オーバーしています`;
  }

  // 純粋な計算: バリデーションチェック
  validationChecks = computed(() => {
    const text = this.text();
    return [
      {
        name: '長さチェック',
        valid: text.length <= this.maxLength()
      },
      {
        name: '空白チェック',
        valid: text.trim().length > 0
      },
      {
        name: '数字を含む',
        valid: /\d/.test(text)
      },
      {
        name: '英字を含む',
        valid: /[a-zA-Z]/.test(text)
      }
    ];
  });
}
```

## ベストプラクティス

### 純粋関数の使用
```typescript
// ✅ 純粋関数
formatDate(date: Date): string {
  return new Date(date).toLocaleDateString();
}

// ❌ 副作用あり
formatDate(date: Date): string {
  this.lastFormattedDate = date; // 外部状態変更
  return new Date(date).toLocaleDateString();
}
```

### 不変性の保持
```typescript
// ✅ 元の配列を変更しない
sortedItems = computed(() =>
  [...this.items()].sort((a, b) => a.name.localeCompare(b.name))
);

// ❌ 元の配列を変更
sortedItems = computed(() =>
  this.items().sort((a, b) => a.name.localeCompare(b.name))
);
```

### OnPush戦略の適用
```typescript
// ✅ Pure Componentには必須
@Component({
  selector: 'app-pure',
  changeDetection: ChangeDetectionStrategy.OnPush,
  // ...
})
export class PureComponent {
  data = input.required<Data>();
}
```

### 外部依存の排除
```typescript
// ✅ 入力のみに依存
@Component({
  template: `{{ formatValue(value()) }}`
})
export class PureComponent {
  value = input.required<number>();

  formatValue(val: number): string {
    return val.toFixed(2);
  }
}

// ❌ グローバル状態に依存
@Component({
  template: `{{ formatValue(value()) }}`
})
export class ImpureComponent {
  value = input.required<number>();

  formatValue(val: number): string {
    return val.toFixed(window.appConfig.decimals); // 外部依存
  }
}
```

## 注意点

### 日付とランダム値
`new Date()`や`Math.random()`は純粋ではありません。これらは入力として受け取ってください。

### DOM操作
Pure Componentは直接DOMを操作すべきではありません。

### 非同期処理
データ取得などの非同期処理はContainerコンポーネントで行ってください。

### パフォーマンス
`computed()`は自動的にメモ化されるため、複雑な計算も効率的です。

## 関連技術
- **OnPush Strategy**: 変更検知最適化
- **computed()**: メモ化された計算
- **Immutability**: 不変性
- **Functional Programming**: 関数型プログラミング
- **Stateless Component**: 状態を持たないコンポーネント
