# #058 バインディングのパフォーマンス考慮

## 概要
Angular v20におけるバインディングのパフォーマンス最適化について学びます。OnPush戦略、trackBy関数、Signalベースのリアクティブプログラミングを活用して、効率的で高速なアプリケーションを構築する方法を解説します。

## 学習目標
- バインディングのパフォーマンス最適化手法を理解する
- OnPush戦略とtrackBy関数の活用方法を習得する
- Signalベースの最適化技術を身につける

## 📺 画面表示用コード

```typescript
// OnPush戦略のコンポーネント
import { Component, ChangeDetectionStrategy } from '@angular/core';

@Component({
  selector: 'app-list',
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class ListComponent {
  items = signal([{id: 1, name: 'アイテム1'}]);
  
  trackByFn(index: number, item: any) {
    return item.id; // 効率的な追跡
  }
}
```

```html
<!-- @forでのtrackBy使用 -->
@for (item of items(); track trackByFn($index, item)) {
  <div>{{item.name}}</div>
}
```

```typescript
// Signalベースの最適化
import { signal, computed } from '@angular/core';

export class OptimizedComponent {
  private data = signal(0);
  
  // 計算結果をキャッシュ
  expensiveResult = computed(() => {
    return this.data() * 1000;
  });
}
```

## 技術ポイント

### 1. OnPush戦略のコンポーネント
```typescript
import { Component, ChangeDetectionStrategy } from '@angular/core';

@Component({
  selector: 'app-list',
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class ListComponent {
  items = signal([{id: 1, name: 'アイテム1'}]);
  
  trackByFn(index: number, item: any) {
    return item.id; // 効率的な追跡
  }
}
```

### 2. @forでのtrackBy使用
```html
@for (item of items(); track trackByFn($index, item)) {
  <div>{{item.name}}</div>
}
```

### 3. Signalベースの最適化
```typescript
import { signal, computed } from '@angular/core';

export class OptimizedComponent {
  private data = signal(0);
  
  // 計算結果をキャッシュ
  expensiveResult = computed(() => {
    return this.data() * 1000;
  });
}
```

## 実践的な活用例

### 1. 大きなリストの最適化
```typescript
export class LargeListComponent {
  items = signal<Item[]>([]);
  filter = signal('');
  sortBy = signal<'name' | 'date'>('name');
  
  // フィルタリングとソートをcomputedで最適化
  filteredAndSortedItems = computed(() => {
    const items = this.items();
    const filter = this.filter();
    const sortBy = this.sortBy();
    
    let filtered = items;
    if (filter) {
      filtered = items.filter(item => 
        item.name.toLowerCase().includes(filter.toLowerCase())
      );
    }
    
    return filtered.sort((a, b) => {
      if (sortBy === 'name') {
        return a.name.localeCompare(b.name);
      } else {
        return new Date(b.date).getTime() - new Date(a.date).getTime();
      }
    });
  });
  
  // 効率的なtrackBy関数
  trackByItemId(index: number, item: Item): number {
    return item.id;
  }
  
  // ページネーション用のcomputed
  currentPage = signal(1);
  pageSize = signal(20);
  
  paginatedItems = computed(() => {
    const items = this.filteredAndSortedItems();
    const start = (this.currentPage() - 1) * this.pageSize();
    const end = start + this.pageSize();
    return items.slice(start, end);
  });
}
```

```html
<div class="controls">
  <input [(ngModel)]="filter" placeholder="検索...">
  <select [(ngModel)]="sortBy">
    <option value="name">名前順</option>
    <option value="date">日付順</option>
  </select>
</div>

<!-- 最適化されたリスト表示 -->
@for (item of paginatedItems(); track trackByItemId($index, item)) {
  <div class="item">
    <h3>{{item.name}}</h3>
    <p>{{item.description}}</p>
    <small>{{item.date | date}}</small>
  </div>
}

<!-- ページネーション -->
<div class="pagination">
  <button (click)="currentPage.update(p => Math.max(1, p - 1))">前へ</button>
  <span>ページ {{currentPage()}}</span>
  <button (click)="currentPage.update(p => p + 1)">次へ</button>
</div>
```

### 2. フォームのパフォーマンス最適化
```typescript
export class OptimizedFormComponent {
  formData = signal({
    name: '',
    email: '',
    phone: '',
    address: ''
  });
  
  // バリデーション結果をcomputedで最適化
  validationErrors = computed(() => {
    const data = this.formData();
    const errors: Record<string, string> = {};
    
    if (!data.name.trim()) {
      errors.name = '名前は必須です';
    }
    
    if (!data.email.trim()) {
      errors.email = 'メールアドレスは必須です';
    } else if (!this.isValidEmail(data.email)) {
      errors.email = '有効なメールアドレスを入力してください';
    }
    
    return errors;
  });
  
  // フォームの有効性をcomputedで判定
  isFormValid = computed(() => {
    return Object.keys(this.validationErrors()).length === 0;
  });
  
  private isValidEmail(email: string): boolean {
    const pattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return pattern.test(email);
  }
  
  updateField(field: string, value: string) {
    this.formData.update(data => ({
      ...data,
      [field]: value
    }));
  }
}
```

```html
<form>
  <div class="field">
    <label>名前</label>
    <input 
      [value]="formData().name"
      (input)="updateField('name', $event.target.value)">
    @if (validationErrors()['name']) {
      <span class="error">{{validationErrors()['name']}}</span>
    }
  </div>
  
  <div class="field">
    <label>メールアドレス</label>
    <input 
      [value]="formData().email"
      (input)="updateField('email', $event.target.value)">
    @if (validationErrors()['email']) {
      <span class="error">{{validationErrors()['email']}}</span>
    }
  </div>
  
  <button 
    [disabled]="!isFormValid()"
    (click)="submitForm()">
    送信
  </button>
</form>
```

### 3. リアルタイム検索の最適化
```typescript
export class SearchComponent {
  allItems = signal<Item[]>([]);
  searchTerm = signal('');
  searchResults = signal<Item[]>([]);
  isLoading = signal(false);
  
  // 検索結果をcomputedで最適化
  filteredItems = computed(() => {
    const items = this.allItems();
    const term = this.searchTerm();
    
    if (!term.trim()) {
      return items;
    }
    
    return items.filter(item => 
      item.name.toLowerCase().includes(term.toLowerCase()) ||
      item.description.toLowerCase().includes(term.toLowerCase()) ||
      item.tags.some(tag => tag.toLowerCase().includes(term.toLowerCase()))
    );
  });
  
  // 検索結果の統計情報
  searchStats = computed(() => {
    const total = this.allItems().length;
    const filtered = this.filteredItems().length;
    return {
      total,
      filtered,
      percentage: total > 0 ? (filtered / total) * 100 : 0
    };
  });
  
  // デバウンス付き検索
  private searchTimeout?: number;
  
  onSearchInput(event: Event) {
    const target = event.target as HTMLInputElement;
    const value = target.value;
    
    // 既存のタイムアウトをクリア
    if (this.searchTimeout) {
      clearTimeout(this.searchTimeout);
    }
    
    // 新しいタイムアウトを設定
    this.searchTimeout = setTimeout(() => {
      this.searchTerm.set(value);
    }, 300); // 300ms後に実行
  }
}
```

```html
<div class="search-container">
  <input 
    type="text"
    placeholder="検索..."
    (input)="onSearchInput($event)">
  
  <div class="search-stats">
    全{{searchStats().total}}件中{{searchStats().filtered}}件表示
    ({{searchStats().percentage.toFixed(1)}}%)
  </div>
  
  @if (filteredItems().length > 0) {
    <div class="search-results">
      @for (item of filteredItems(); track item.id) {
        <div class="search-item">
          <h3>{{item.name}}</h3>
          <p>{{item.description}}</p>
          <div class="tags">
            @for (tag of item.tags; track tag) {
              <span class="tag">{{tag}}</span>
            }
          </div>
        </div>
      }
    </div>
  } @else {
    <div class="no-results">
      検索結果が見つかりませんでした
    </div>
  }
</div>
```

### 4. 仮想スクロールの実装
```typescript
export class VirtualScrollComponent {
  allItems = signal<Item[]>([]);
  containerHeight = 400;
  itemHeight = 50;
  scrollTop = signal(0);
  
  // 表示範囲の計算
  visibleRange = computed(() => {
    const scrollTop = this.scrollTop();
    const start = Math.floor(scrollTop / this.itemHeight);
    const end = Math.min(
      start + Math.ceil(this.containerHeight / this.itemHeight) + 1,
      this.allItems().length
    );
    return { start, end };
  });
  
  // 表示するアイテム
  visibleItems = computed(() => {
    const { start, end } = this.visibleRange();
    return this.allItems().slice(start, end).map((item, index) => ({
      ...item,
      index: start + index
    }));
  });
  
  // オフセット計算
  offsetY = computed(() => {
    return this.visibleRange().start * this.itemHeight;
  });
  
  onScroll(event: Event) {
    const target = event.target as HTMLElement;
    this.scrollTop.set(target.scrollTop);
  }
}
```

```html
<div 
  class="virtual-scroll-container"
  [style.height.px]="containerHeight"
  (scroll)="onScroll($event)">
  
  <div 
    class="virtual-scroll-content"
    [style.height.px]="allItems().length * itemHeight">
    
    <div 
      class="visible-items"
      [style.transform]="'translateY(' + offsetY() + 'px)'">
      
      @for (item of visibleItems(); track item.id) {
        <div 
          class="virtual-item"
          [style.height.px]="itemHeight">
          {{item.name}}
        </div>
      }
    </div>
  </div>
</div>
```

## パフォーマンス測定と監視

### 1. パフォーマンス測定
```typescript
export class PerformanceMonitoringComponent {
  private performanceObserver = new PerformanceObserver((list) => {
    for (const entry of list.getEntries()) {
      console.log('パフォーマンス測定:', entry.name, entry.duration);
    }
  });
  
  ngOnInit() {
    this.performanceObserver.observe({ entryTypes: ['measure'] });
  }
  
  measurePerformance(name: string, fn: () => void) {
    performance.mark(`${name}-start`);
    fn();
    performance.mark(`${name}-end`);
    performance.measure(name, `${name}-start`, `${name}-end`);
  }
  
  ngOnDestroy() {
    this.performanceObserver.disconnect();
  }
}
```

### 2. 変更検知の監視
```typescript
export class ChangeDetectionMonitoringComponent {
  private changeDetectionCount = 0;
  
  ngDoCheck() {
    this.changeDetectionCount++;
    console.log(`変更検知実行回数: ${this.changeDetectionCount}`);
  }
  
  resetCounter() {
    this.changeDetectionCount = 0;
  }
}
```

## ベストプラクティス

1. **OnPush戦略の活用**: 可能な限りOnPushを使用
2. **trackBy関数の実装**: リストアイテムには適切なtrackBy関数を実装
3. **computedの活用**: 重い計算はcomputedで最適化
4. **Signalベースの設計**: Angular v20のSignalを積極的に活用
5. **パフォーマンス測定**: 実際のパフォーマンスを測定して検証

## 注意点

- 過度な最適化は避ける
- 実際のユーザー体験を重視
- メモリ使用量も考慮
- ブラウザの開発者ツールで測定

## 関連技術
- OnPush戦略
- trackBy関数
- Angular v20のSignal
- computed
- 仮想スクロール
- パフォーマンス監視
