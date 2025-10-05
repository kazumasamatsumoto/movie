# #103 「@Input() とngOnChanges の連携」

## 概要
Angular v20における@Input()とngOnChangesの連携を学びます。入力プロパティの変更を適切に監視し、効率的な変更処理を実装する方法について解説します。

## 学習目標
- @Input()とngOnChangesの連携方法を理解する
- 効率的な変更監視の実装を習得する
- パフォーマンスを考慮した変更処理を身につける

## 📺 画面表示用コード

```typescript
// @Input()とngOnChangesの連携
@Component({
  selector: 'app-input-changes',
  standalone: true,
  template: `
    <div class="input-changes">
      <h3>{{title}}</h3>
      <p>データ: {{data}}</p>
      <p>変更回数: {{changeCount}}</p>
    </div>
  `
})
export class InputChangesComponent implements OnChanges {
  @Input() title: string = '';
  @Input() data: any;
  
  changeCount = 0;
  
  ngOnChanges(changes: SimpleChanges) {
    if (changes['data']) {
      this.changeCount++;
      this.handleDataChange(changes['data']);
    }
  }
  
  private handleDataChange(change: SimpleChange) {
    console.log('データ変更:', change);
  }
}
```

```typescript
// 特定プロパティの監視
export class SpecificPropertyComponent implements OnChanges {
  @Input() userId: string = '';
  @Input() userData: any;
  
  ngOnChanges(changes: SimpleChanges) {
    if (changes['userId'] && !changes['userId'].firstChange) {
      this.loadUserData(changes['userId'].currentValue);
    }
  }
}
```

```typescript
// 複数プロパティの連携監視
export class MultiPropertyComponent implements OnChanges {
  @Input() filter: string = '';
  @Input() sortBy: string = '';
  @Input() pageSize: number = 10;
  
  ngOnChanges(changes: SimpleChanges) {
    const hasRelevantChange = ['filter', 'sortBy', 'pageSize'].some(
      prop => changes[prop] && !changes[prop].firstChange
    );
    
    if (hasRelevantChange) {
      this.refreshData();
    }
  }
}
```

## 技術ポイント

### 1. ngOnChangesの基本
- **SimpleChanges**: 変更の詳細情報を含むオブジェクト
- **firstChange**: 初回変更かどうかの判定
- **previousValue/currentValue**: 変更前後の値

### 2. 効率的な変更監視
- **特定プロパティの監視**: 必要なプロパティのみを監視
- **初回変更の除外**: firstChangeフラグの活用
- **条件付き処理**: 変更の種類に応じた処理

### 3. パフォーマンス考慮
- **軽量な処理**: ngOnChangesでの重い処理を避ける
- **デバウンス**: 頻繁な変更の制御
- **メモ化**: 計算結果のキャッシュ

## 実践的な活用例

### 1. データフィルタリングコンポーネント
```typescript
// data-filter.component.ts
@Component({
  selector: 'app-data-filter',
  standalone: true,
  template: `
    <div class="data-filter">
      <h3>{{title}}</h3>
      
      <div class="filter-info">
        <p>フィルター: {{filter}}</p>
        <p>並び順: {{sortBy}}</p>
        <p>ページサイズ: {{pageSize}}</p>
        <p>結果数: {{filteredData.length}}</p>
        <p>変更回数: {{changeCount}}</p>
      </div>
      
      <div class="filtered-data">
        <div *ngFor="let item of filteredData" class="data-item">
          {{item.name}} - {{item.value}}
        </div>
      </div>
    </div>
  `
})
export class DataFilterComponent implements OnChanges {
  @Input() title: string = 'データフィルター';
  @Input() data: Array<{ name: string; value: number; category: string }> = [];
  @Input() filter: string = '';
  @Input() sortBy: string = 'name';
  @Input() pageSize: number = 10;
  
  filteredData: Array<{ name: string; value: number; category: string }> = [];
  changeCount = 0;
  
  ngOnChanges(changes: SimpleChanges) {
    this.changeCount++;
    
    // データ、フィルター、ソートの変更を監視
    const dataChanged = changes['data'];
    const filterChanged = changes['filter'];
    const sortChanged = changes['sortBy'];
    const pageSizeChanged = changes['pageSize'];
    
    if (dataChanged || filterChanged || sortChanged || pageSizeChanged) {
      this.applyFilters();
    }
    
    // 初回変更でない場合の特別な処理
    if (filterChanged && !filterChanged.firstChange) {
      console.log('フィルター変更:', filterChanged.previousValue, '→', filterChanged.currentValue);
    }
  }
  
  private applyFilters() {
    let result = [...this.data];
    
    // フィルタリング
    if (this.filter) {
      result = result.filter(item =>
        item.name.toLowerCase().includes(this.filter.toLowerCase())
      );
    }
    
    // ソート
    result.sort((a, b) => {
      if (this.sortBy === 'name') {
        return a.name.localeCompare(b.name);
      } else if (this.sortBy === 'value') {
        return a.value - b.value;
      }
      return 0;
    });
    
    // ページサイズ制限
    this.filteredData = result.slice(0, this.pageSize);
  }
}
```

### 2. ユーザープロフィール更新コンポーネント
```typescript
// user-profile-update.component.ts
interface User {
  id: string;
  name: string;
  email: string;
  role: string;
  lastModified: Date;
}

@Component({
  selector: 'app-user-profile-update',
  standalone: true,
  template: `
    <div class="user-profile-update">
      <h3>{{title}}</h3>
      
      <div class="user-info">
        <p>ユーザーID: {{user.id}}</p>
        <p>名前: {{user.name}}</p>
        <p>メール: {{user.email}}</p>
        <p>ロール: {{user.role}}</p>
        <p>最終更新: {{user.lastModified | date:'medium'}}</p>
      </div>
      
      <div class="update-log">
        <h4>更新履歴</h4>
        <div *ngFor="let log of updateLogs" class="log-entry">
          {{log.timestamp | date:'short'}} - {{log.message}}
        </div>
      </div>
      
      <div class="actions">
        <button (click)="refreshUser()">ユーザー情報更新</button>
        <button (click)="clearLogs()">ログクリア</button>
      </div>
    </div>
  `
})
export class UserProfileUpdateComponent implements OnChanges {
  @Input() title: string = 'ユーザープロフィール';
  @Input() userId: string = '';
  @Input() user: User = {
    id: '',
    name: '',
    email: '',
    role: '',
    lastModified: new Date()
  };
  
  updateLogs: Array<{ timestamp: Date; message: string }> = [];
  
  ngOnChanges(changes: SimpleChanges) {
    // ユーザーIDの変更を監視
    if (changes['userId']) {
      const userIdChange = changes['userId'];
      if (!userIdChange.firstChange) {
        this.handleUserIdChange(userIdChange.previousValue, userIdChange.currentValue);
      }
    }
    
    // ユーザーデータの変更を監視
    if (changes['user']) {
      const userChange = changes['user'];
      if (!userChange.firstChange) {
        this.handleUserDataChange(userChange.previousValue, userChange.currentValue);
      }
    }
  }
  
  private handleUserIdChange(oldUserId: string, newUserId: string) {
    this.addLog(`ユーザーID変更: ${oldUserId} → ${newUserId}`);
    
    if (newUserId) {
      this.loadUserData(newUserId);
    }
  }
  
  private handleUserDataChange(oldUser: User, newUser: User) {
    const changes = this.detectUserChanges(oldUser, newUser);
    
    if (changes.length > 0) {
      this.addLog(`ユーザーデータ変更: ${changes.join(', ')}`);
    }
  }
  
  private detectUserChanges(oldUser: User, newUser: User): string[] {
    const changes: string[] = [];
    
    if (oldUser.name !== newUser.name) {
      changes.push(`名前: ${oldUser.name} → ${newUser.name}`);
    }
    
    if (oldUser.email !== newUser.email) {
      changes.push(`メール: ${oldUser.email} → ${newUser.email}`);
    }
    
    if (oldUser.role !== newUser.role) {
      changes.push(`ロール: ${oldUser.role} → ${newUser.role}`);
    }
    
    return changes;
  }
  
  private loadUserData(userId: string) {
    // 実際の実装では、ここでAPIからユーザーデータを取得
    console.log(`ユーザーデータを読み込み中: ${userId}`);
    this.addLog(`ユーザーデータ読み込み: ${userId}`);
  }
  
  private addLog(message: string) {
    this.updateLogs.push({
      timestamp: new Date(),
      message
    });
    
    // ログの最大数を制限
    if (this.updateLogs.length > 10) {
      this.updateLogs.shift();
    }
  }
  
  refreshUser() {
    if (this.userId) {
      this.loadUserData(this.userId);
    }
  }
  
  clearLogs() {
    this.updateLogs = [];
  }
}
```

### 3. パフォーマンス監視コンポーネント
```typescript
// performance-monitor.component.ts
@Component({
  selector: 'app-performance-monitor',
  standalone: true,
  template: `
    <div class="performance-monitor">
      <h3>{{title}}</h3>
      
      <div class="performance-stats">
        <p>変更検知回数: {{detectionCount}}</p>
        <p>平均処理時間: {{averageProcessingTime}}ms</p>
        <p>最大処理時間: {{maxProcessingTime}}ms</p>
        <p>データサイズ: {{dataSize}}</p>
      </div>
      
      <div class="recent-changes">
        <h4>最近の変更</h4>
        <div *ngFor="let change of recentChanges" class="change-entry">
          {{change.timestamp | date:'HH:mm:ss'}} - {{change.message}}
        </div>
      </div>
      
      <div class="actions">
        <button (click)="resetStats()">統計リセット</button>
        <button (click)="simulateHeavyChange()">重い変更シミュレート</button>
      </div>
    </div>
  `
})
export class PerformanceMonitorComponent implements OnChanges {
  @Input() title: string = 'パフォーマンス監視';
  @Input() data: any;
  
  detectionCount = 0;
  processingTimes: number[] = [];
  recentChanges: Array<{ timestamp: Date; message: string }> = [];
  
  get averageProcessingTime(): number {
    if (this.processingTimes.length === 0) return 0;
    return this.processingTimes.reduce((sum, time) => sum + time, 0) / this.processingTimes.length;
  }
  
  get maxProcessingTime(): number {
    return Math.max(...this.processingTimes, 0);
  }
  
  get dataSize(): number {
    return JSON.stringify(this.data).length;
  }
  
  ngOnChanges(changes: SimpleChanges) {
    const startTime = performance.now();
    
    this.detectionCount++;
    
    if (changes['data']) {
      this.handleDataChange(changes['data']);
    }
    
    const endTime = performance.now();
    const processingTime = endTime - startTime;
    
    this.processingTimes.push(processingTime);
    
    // 処理時間の履歴を制限
    if (this.processingTimes.length > 100) {
      this.processingTimes.shift();
    }
    
    // 重い処理の警告
    if (processingTime > 10) {
      this.addChange(`⚠️ 重い処理検出: ${processingTime.toFixed(2)}ms`);
    } else {
      this.addChange(`変更検知: ${processingTime.toFixed(2)}ms`);
    }
  }
  
  private handleDataChange(change: SimpleChange) {
    const dataSize = JSON.stringify(change.currentValue).length;
    const previousSize = JSON.stringify(change.previousValue || {}).length;
    
    this.addChange(`データサイズ変更: ${previousSize} → ${dataSize} bytes`);
    
    // データサイズが大きすぎる場合の警告
    if (dataSize > 10000) {
      this.addChange(`⚠️ 大きなデータサイズ: ${dataSize} bytes`);
    }
  }
  
  private addChange(message: string) {
    this.recentChanges.push({
      timestamp: new Date(),
      message
    });
    
    // 履歴の最大数を制限
    if (this.recentChanges.length > 20) {
      this.recentChanges.shift();
    }
  }
  
  resetStats() {
    this.detectionCount = 0;
    this.processingTimes = [];
    this.recentChanges = [];
  }
  
  simulateHeavyChange() {
    // 重い処理をシミュレート
    const startTime = performance.now();
    
    // 大量のデータ処理をシミュレート
    for (let i = 0; i < 100000; i++) {
      Math.random();
    }
    
    const endTime = performance.now();
    this.addChange(`重い処理完了: ${(endTime - startTime).toFixed(2)}ms`);
  }
}
```

### 4. デバウンス付き変更処理
```typescript
// debounced-changes.component.ts
@Component({
  selector: 'app-debounced-changes',
  standalone: true,
  template: `
    <div class="debounced-changes">
      <h3>{{title}}</h3>
      
      <div class="input-data">
        <p>検索クエリ: {{searchQuery}}</p>
        <p>フィルター: {{filter}}</p>
        <p>並び順: {{sortBy}}</p>
      </div>
      
      <div class="debounce-info">
        <p>即座の変更回数: {{immediateChanges}}</p>
        <p>デバウンス後の処理回数: {{debouncedChanges}}</p>
        <p>最終処理時刻: {{lastProcessedTime | date:'HH:mm:ss'}}</p>
      </div>
      
      <div class="results">
        <p>検索結果数: {{searchResults.length}}</p>
        <div *ngFor="let result of searchResults" class="result-item">
          {{result}}
        </div>
      </div>
    </div>
  `
})
export class DebouncedChangesComponent implements OnChanges, OnDestroy {
  @Input() title: string = 'デバウンス変更処理';
  @Input() searchQuery: string = '';
  @Input() filter: string = '';
  @Input() sortBy: string = 'name';
  
  searchResults: string[] = [];
  immediateChanges = 0;
  debouncedChanges = 0;
  lastProcessedTime: Date = new Date();
  
  private debounceTimer?: number;
  private readonly debounceDelay = 300; // 300ms
  
  ngOnChanges(changes: SimpleChanges) {
    this.immediateChanges++;
    
    // 検索関連のプロパティの変更を監視
    const hasSearchChange = ['searchQuery', 'filter', 'sortBy'].some(
      prop => changes[prop] && !changes[prop].firstChange
    );
    
    if (hasSearchChange) {
      this.debounceSearch();
    }
  }
  
  ngOnDestroy() {
    if (this.debounceTimer) {
      clearTimeout(this.debounceTimer);
    }
  }
  
  private debounceSearch() {
    // 既存のタイマーをクリア
    if (this.debounceTimer) {
      clearTimeout(this.debounceTimer);
    }
    
    // 新しいタイマーを設定
    this.debounceTimer = setTimeout(() => {
      this.performSearch();
    }, this.debounceDelay);
  }
  
  private performSearch() {
    this.debouncedChanges++;
    this.lastProcessedTime = new Date();
    
    // 実際の検索処理をシミュレート
    const mockData = [
      'Angular', 'TypeScript', 'JavaScript', 'React', 'Vue',
      'Node.js', 'Express', 'MongoDB', 'PostgreSQL', 'Redis'
    ];
    
    let results = mockData;
    
    // 検索クエリでフィルタリング
    if (this.searchQuery) {
      results = results.filter(item =>
        item.toLowerCase().includes(this.searchQuery.toLowerCase())
      );
    }
    
    // フィルターでフィルタリング
    if (this.filter) {
      results = results.filter(item =>
        item.toLowerCase().includes(this.filter.toLowerCase())
      );
    }
    
    // ソート
    results.sort((a, b) => {
      if (this.sortBy === 'name') {
        return a.localeCompare(b);
      }
      return 0;
    });
    
    this.searchResults = results;
  }
}
```

## ベストプラクティス

1. **効率的な監視**: 必要なプロパティのみを監視
2. **初回変更の考慮**: firstChangeフラグの適切な使用
3. **軽量な処理**: ngOnChangesでの重い処理を避ける
4. **デバウンス**: 頻繁な変更の制御

## 注意点

- ngOnChangesは頻繁に実行されるため、軽量な処理を心がける
- 初回変更（firstChange = true）の適切な処理
- 深いオブジェクトの変更は検知されない場合がある

## 関連技術
- ngOnChanges
- SimpleChanges
- 変更検知
- パフォーマンス最適化
