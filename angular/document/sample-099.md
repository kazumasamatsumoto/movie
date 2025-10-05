# #099 「@Input() 配列の受け渡し」

## 概要
Angular v20における@Input()での配列の受け渡しを学びます。配列の参照渡し、変更検知、不変性の維持、効率的な配列操作など、配列を安全に扱う方法について解説します。

## 学習目標
- 配列の受け渡し方法を理解する
- 配列の変更検知を把握する
- 不変性を考慮した配列操作を習得する

## 📺 画面表示用コード

```typescript
// 配列の受け渡し
@Component({
  selector: 'app-array-input',
  standalone: true,
  template: `
    <div class="array-display">
      <h3>{{title}}</h3>
      <ul>
        <li *ngFor="let item of items">{{item}}</li>
      </ul>
      <p>配列の長さ: {{items.length}}</p>
    </div>
  `
})
export class ArrayInputComponent {
  @Input() title: string = '配列表示';
  @Input() items: string[] = [];
}
```

```typescript
// 配列の参照渡し
export class ArrayReferenceComponent {
  @Input() data: any[] = [];
  
  addItem() {
    // 子で変更すると親にも影響する（参照渡し）
    this.data.push('新しいアイテム');
  }
}
```

```typescript
// 不変性を維持した配列操作
export class ImmutableArrayComponent {
  @Input() items: string[] = [];
  
  addItem(newItem: string) {
    // 新しい配列を作成して不変性を維持
    this.items = [...this.items, newItem];
  }
}
```

## 技術ポイント

### 1. 配列の参照渡し
- **参照共有**: 配列の参照が渡される
- **変更の影響**: 子で変更すると親にも影響する
- **メモリ効率**: 配列のコピーは作成されない

### 2. 配列の変更検知
- **参照比較**: Angularは配列の参照を比較
- **要素の変更**: 配列内の要素の変更は検知されない場合がある
- **OnPush戦略**: 変更検知の最適化

### 3. 不変性を考慮した配列操作
- **スプレッド演算子**: `[...array]`で新しい配列を作成
- **配列メソッド**: `map()`, `filter()`, `reduce()`などの使用
- **ReadonlyArray**: TypeScriptの型システムを活用

## 実践的な活用例

### 1. アイテムリストコンポーネント
```typescript
// item-list.component.ts
interface ListItem {
  id: number;
  name: string;
  description: string;
  completed: boolean;
}

@Component({
  selector: 'app-item-list',
  standalone: true,
  template: `
    <div class="item-list">
      <h3>{{title}}</h3>
      <div class="list-stats">
        <p>総数: {{items.length}}</p>
        <p>完了: {{completedCount}}</p>
        <p>未完了: {{pendingCount}}</p>
      </div>
      
      <div class="list-items">
        <div *ngFor="let item of items" class="list-item" [class.completed]="item.completed">
          <h4>{{item.name}}</h4>
          <p>{{item.description}}</p>
          <button (click)="toggleItem(item.id)">完了切り替え</button>
          <button (click)="removeItem(item.id)">削除</button>
        </div>
      </div>
    </div>
  `
})
export class ItemListComponent {
  @Input() title: string = 'アイテム一覧';
  @Input() items: ListItem[] = [];
  
  @Output() itemUpdate = new EventEmitter<ListItem>();
  @Output() itemRemove = new EventEmitter<number>();
  
  get completedCount(): number {
    return this.items.filter(item => item.completed).length;
  }
  
  get pendingCount(): number {
    return this.items.filter(item => !item.completed).length;
  }
  
  toggleItem(itemId: number) {
    // 不変性を維持してアイテムを更新
    this.items = this.items.map(item => {
      if (item.id === itemId) {
        const updatedItem = { ...item, completed: !item.completed };
        this.itemUpdate.emit(updatedItem);
        return updatedItem;
      }
      return item;
    });
  }
  
  removeItem(itemId: number) {
    // 不変性を維持してアイテムを削除
    this.items = this.items.filter(item => item.id !== itemId);
    this.itemRemove.emit(itemId);
  }
}
```

### 2. データテーブルコンポーネント
```typescript
// data-table.component.ts
interface TableColumn {
  key: string;
  title: string;
  sortable: boolean;
  filterable: boolean;
}

interface TableRow {
  [key: string]: any;
}

@Component({
  selector: 'app-data-table',
  standalone: true,
  template: `
    <div class="data-table">
      <h3>{{title}}</h3>
      
      <div class="table-controls">
        <input 
          [(ngModel)]="searchTerm" 
          placeholder="検索..."
          (input)="onSearch()">
        <select [(ngModel)]="pageSize" (change)="onPageSizeChange()">
          <option value="10">10件</option>
          <option value="25">25件</option>
          <option value="50">50件</option>
        </select>
      </div>
      
      <table>
        <thead>
          <tr>
            <th 
              *ngFor="let column of columns" 
              [class.sortable]="column.sortable"
              (click)="sort(column)">
              {{column.title}}
              <span *ngIf="sortColumn === column.key" class="sort-indicator">
                {{sortDirection === 'asc' ? '↑' : '↓'}}
              </span>
            </th>
          </tr>
        </thead>
        <tbody>
          <tr *ngFor="let row of paginatedData; let i = index">
            <td *ngFor="let column of columns">
              {{row[column.key]}}
            </td>
          </tr>
        </tbody>
      </table>
      
      <div class="pagination">
        <button (click)="previousPage()" [disabled]="currentPage === 0">前へ</button>
        <span>ページ {{currentPage + 1}} / {{totalPages}}</span>
        <button (click)="nextPage()" [disabled]="currentPage >= totalPages - 1">次へ</button>
      </div>
    </div>
  `,
  imports: [FormsModule]
})
export class DataTableComponent {
  @Input() title: string = 'データテーブル';
  @Input() data: TableRow[] = [];
  @Input() columns: TableColumn[] = [];
  @Input() pageSize: number = 10;
  
  searchTerm: string = '';
  currentPage: number = 0;
  sortColumn: string = '';
  sortDirection: 'asc' | 'desc' = 'asc';
  
  get filteredData(): TableRow[] {
    if (!this.searchTerm) return this.data;
    
    return this.data.filter(row =>
      this.columns.some(column =>
        String(row[column.key]).toLowerCase().includes(this.searchTerm.toLowerCase())
      )
    );
  }
  
  get sortedData(): TableRow[] {
    if (!this.sortColumn) return this.filteredData;
    
    return [...this.filteredData].sort((a, b) => {
      const aVal = a[this.sortColumn];
      const bVal = b[this.sortColumn];
      
      if (aVal < bVal) return this.sortDirection === 'asc' ? -1 : 1;
      if (aVal > bVal) return this.sortDirection === 'asc' ? 1 : -1;
      return 0;
    });
  }
  
  get paginatedData(): TableRow[] {
    const start = this.currentPage * this.pageSize;
    const end = start + this.pageSize;
    return this.sortedData.slice(start, end);
  }
  
  get totalPages(): number {
    return Math.ceil(this.sortedData.length / this.pageSize);
  }
  
  sort(column: TableColumn) {
    if (!column.sortable) return;
    
    if (this.sortColumn === column.key) {
      this.sortDirection = this.sortDirection === 'asc' ? 'desc' : 'asc';
    } else {
      this.sortColumn = column.key;
      this.sortDirection = 'asc';
    }
    
    this.currentPage = 0; // ソート時に最初のページに戻る
  }
  
  onSearch() {
    this.currentPage = 0; // 検索時に最初のページに戻る
  }
  
  onPageSizeChange() {
    this.currentPage = 0; // ページサイズ変更時に最初のページに戻る
  }
  
  previousPage() {
    if (this.currentPage > 0) {
      this.currentPage--;
    }
  }
  
  nextPage() {
    if (this.currentPage < this.totalPages - 1) {
      this.currentPage++;
    }
  }
}
```

### 3. タグ管理コンポーネント
```typescript
// tag-manager.component.ts
interface Tag {
  id: number;
  name: string;
  color: string;
  count: number;
}

@Component({
  selector: 'app-tag-manager',
  standalone: true,
  template: `
    <div class="tag-manager">
      <h3>{{title}}</h3>
      
      <div class="tag-input">
        <input 
          [(ngModel)]="newTagName" 
          placeholder="新しいタグ名"
          (keyup.enter)="addTag()">
        <button (click)="addTag()" [disabled]="!newTagName.trim()">追加</button>
      </div>
      
      <div class="tag-list">
        <div *ngFor="let tag of tags" class="tag-item" [style.background-color]="tag.color">
          <span class="tag-name">{{tag.name}}</span>
          <span class="tag-count">({{tag.count}})</span>
          <button (click)="removeTag(tag.id)" class="remove-btn">×</button>
        </div>
      </div>
      
      <div class="tag-actions">
        <button (click)="clearAllTags()">全てクリア</button>
        <button (click)="sortTagsByName()">名前でソート</button>
        <button (click)="sortTagsByCount()">件数でソート</button>
      </div>
    </div>
  `,
  imports: [FormsModule]
})
export class TagManagerComponent {
  @Input() title: string = 'タグ管理';
  @Input() tags: Tag[] = [];
  
  @Output() tagAdd = new EventEmitter<Tag>();
  @Output() tagRemove = new EventEmitter<number>();
  @Output() tagsClear = new EventEmitter<void>();
  
  newTagName: string = '';
  
  private readonly colors = ['#ff6b6b', '#4ecdc4', '#45b7d1', '#96ceb4', '#feca57', '#ff9ff3'];
  
  addTag() {
    const name = this.newTagName.trim();
    if (!name) return;
    
    // 重複チェック
    if (this.tags.some(tag => tag.name.toLowerCase() === name.toLowerCase())) {
      alert('同じ名前のタグが既に存在します');
      return;
    }
    
    const newTag: Tag = {
      id: Math.max(...this.tags.map(t => t.id), 0) + 1,
      name,
      color: this.colors[Math.floor(Math.random() * this.colors.length)],
      count: 0
    };
    
    // 不変性を維持してタグを追加
    this.tags = [...this.tags, newTag];
    this.tagAdd.emit(newTag);
    this.newTagName = '';
  }
  
  removeTag(tagId: number) {
    // 不変性を維持してタグを削除
    this.tags = this.tags.filter(tag => tag.id !== tagId);
    this.tagRemove.emit(tagId);
  }
  
  clearAllTags() {
    this.tags = [];
    this.tagsClear.emit();
  }
  
  sortTagsByName() {
    // 不変性を維持してソート
    this.tags = [...this.tags].sort((a, b) => a.name.localeCompare(b.name));
  }
  
  sortTagsByCount() {
    // 不変性を維持してソート
    this.tags = [...this.tags].sort((a, b) => b.count - a.count);
  }
}
```

### 4. 配列の変更検知とパフォーマンス最適化
```typescript
// performance-array.component.ts
@Component({
  selector: 'app-performance-array',
  standalone: true,
  template: `
    <div class="performance-array">
      <h3>{{title}}</h3>
      
      <div class="controls">
        <button (click)="addRandomItems(100)">100件追加</button>
        <button (click)="addRandomItems(1000)">1000件追加</button>
        <button (click)="clearItems()">クリア</button>
        <button (click)="shuffleItems()">シャッフル</button>
      </div>
      
      <div class="stats">
        <p>アイテム数: {{items.length}}</p>
        <p>表示時間: {{renderTime}}ms</p>
      </div>
      
      <div class="item-list">
        <div *ngFor="let item of items; trackBy: trackByFn" class="item">
          {{item.id}}: {{item.name}}
        </div>
      </div>
    </div>
  `
})
export class PerformanceArrayComponent implements OnChanges {
  @Input() title: string = 'パフォーマンス配列';
  @Input() items: Array<{id: number, name: string}> = [];
  
  renderTime: number = 0;
  
  ngOnChanges(changes: SimpleChanges) {
    if (changes['items']) {
      const startTime = performance.now();
      // 仮想的な処理時間をシミュレート
      setTimeout(() => {
        this.renderTime = performance.now() - startTime;
      }, 0);
    }
  }
  
  addRandomItems(count: number) {
    const newItems = Array.from({ length: count }, (_, i) => ({
      id: this.items.length + i + 1,
      name: `アイテム ${this.items.length + i + 1}`
    }));
    
    // 不変性を維持してアイテムを追加
    this.items = [...this.items, ...newItems];
  }
  
  clearItems() {
    this.items = [];
  }
  
  shuffleItems() {
    // 不変性を維持してシャッフル
    this.items = [...this.items].sort(() => Math.random() - 0.5);
  }
  
  trackByFn(index: number, item: any): number {
    return item.id; // 効率的な変更検知のためのtrackBy関数
  }
}
```

## ベストプラクティス

1. **不変性の維持**: スプレッド演算子や配列メソッドを使用
2. **効率的な変更検知**: trackBy関数の活用
3. **型安全性**: 明確な型定義
4. **パフォーマンス**: 大量データの処理時の最適化

## 注意点

- 配列は参照渡しなので、子で変更すると親にも影響する
- 配列内の要素の変更は変更検知されない場合がある
- 大量のデータを扱う場合はtrackBy関数を使用してパフォーマンスを向上

## 関連技術
- 配列操作
- 不変性
- 変更検知
- パフォーマンス最適化
