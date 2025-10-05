# #102 「@Input() の変更検知」

## 概要
Angular v20における@Input()の変更検知を学びます。Angularの変更検知システム、OnPush戦略、効率的な変更検知の実装方法について解説します。

## 学習目標
- Angularの変更検知システムを理解する
- @Input()の変更検知メカニズムを把握する
- 効率的な変更検知の実装方法を習得する

## 📺 画面表示用コード

```typescript
// 基本的な変更検知
@Component({
  selector: 'app-change-detection',
  standalone: true,
  template: `
    <div class="change-detection">
      <h3>{{data.title}}</h3>
      <p>{{data.content}}</p>
      <p>更新回数: {{updateCount}}</p>
    </div>
  `
})
export class ChangeDetectionComponent implements OnChanges {
  @Input() data: { title: string; content: string } = { title: '', content: '' };
  updateCount = 0;
  
  ngOnChanges(changes: SimpleChanges) {
    this.updateCount++;
    console.log('データが変更されました:', changes);
  }
}
```

```typescript
// OnPush戦略の使用
@Component({
  selector: 'app-onpush-detection',
  standalone: true,
  changeDetection: ChangeDetectionStrategy.OnPush,
  template: `<p>{{message}}</p>`
})
export class OnPushDetectionComponent {
  @Input() message: string = '';
}
```

```typescript
// 手動での変更検知
export class ManualDetectionComponent {
  @Input() data: any;
  private cdr = inject(ChangeDetectorRef);
  
  updateData() {
    this.cdr.detectChanges();
  }
}
```

## 技術ポイント

### 1. Angularの変更検知システム
- **デフォルト戦略**: すべてのコンポーネントで変更検知を実行
- **OnPush戦略**: 入力プロパティの変更時のみ検知
- **手動検知**: ChangeDetectorRefを使用した手動制御

### 2. @Input()の変更検知
- **参照比較**: オブジェクトの参照を比較
- **プリミティブ比較**: 値の比較
- **SimpleChanges**: 変更の詳細情報

### 3. パフォーマンス最適化
- **OnPush戦略**: 不要な変更検知を回避
- **trackBy関数**: リストの効率的な更新
- **不変性**: 参照の変更による確実な検知

## 実践的な活用例

### 1. 基本的な変更検知コンポーネント
```typescript
// basic-change-detection.component.ts
@Component({
  selector: 'app-basic-change-detection',
  standalone: true,
  template: `
    <div class="basic-detection">
      <h3>{{title}}</h3>
      
      <div class="input-data">
        <p>受信データ: {{inputData | json}}</p>
        <p>データタイプ: {{typeof inputData}}</p>
        <p>データ長: {{getDataLength()}}</p>
      </div>
      
      <div class="change-info">
        <p>変更回数: {{changeCount}}</p>
        <p>最終変更時刻: {{lastChangeTime | date:'medium'}}</p>
        <p>変更されたプロパティ: {{changedProperties.join(', ')}}</p>
      </div>
    </div>
  `
})
export class BasicChangeDetectionComponent implements OnChanges {
  @Input() title: string = '変更検知';
  @Input() inputData: any;
  
  changeCount = 0;
  lastChangeTime: Date = new Date();
  changedProperties: string[] = [];
  
  ngOnChanges(changes: SimpleChanges) {
    this.changeCount++;
    this.lastChangeTime = new Date();
    this.changedProperties = Object.keys(changes);
    
    console.log('変更検知:', changes);
    
    // 特定のプロパティの変更を処理
    if (changes['inputData']) {
      this.handleDataChange(changes['inputData']);
    }
  }
  
  getDataLength(): number {
    if (Array.isArray(this.inputData)) {
      return this.inputData.length;
    } else if (typeof this.inputData === 'string') {
      return this.inputData.length;
    } else if (typeof this.inputData === 'object') {
      return Object.keys(this.inputData).length;
    }
    return 0;
  }
  
  private handleDataChange(change: SimpleChange) {
    console.log('データ変更:', {
      previousValue: change.previousValue,
      currentValue: change.currentValue,
      firstChange: change.firstChange
    });
  }
}
```

### 2. OnPush戦略を使用したコンポーネント
```typescript
// onpush-detection.component.ts
@Component({
  selector: 'app-onpush-detection',
  standalone: true,
  changeDetection: ChangeDetectionStrategy.OnPush,
  template: `
    <div class="onpush-detection">
      <h3>{{title}}</h3>
      
      <div class="data-display">
        <p>ユーザー名: {{user.name}}</p>
        <p>メール: {{user.email}}</p>
        <p>ロール: {{user.role}}</p>
        <p>最終更新: {{user.lastUpdated | date:'medium'}}</p>
      </div>
      
      <div class="actions">
        <button (click)="updateUser()">ユーザー更新</button>
        <button (click)="refreshData()">データ更新</button>
      </div>
      
      <div class="change-stats">
        <p>変更検知回数: {{detectionCount}}</p>
        <p>手動更新回数: {{manualUpdateCount}}</p>
      </div>
    </div>
  `
})
export class OnPushDetectionComponent implements OnChanges {
  @Input() title: string = 'OnPush検知';
  @Input() user: { name: string; email: string; role: string; lastUpdated: Date } = {
    name: '',
    email: '',
    role: '',
    lastUpdated: new Date()
  };
  
  detectionCount = 0;
  manualUpdateCount = 0;
  
  private cdr = inject(ChangeDetectorRef);
  
  ngOnChanges(changes: SimpleChanges) {
    this.detectionCount++;
    console.log('OnPush変更検知:', changes);
  }
  
  updateUser() {
    // 手動でデータを更新
    this.user = {
      ...this.user,
      name: '更新されたユーザー',
      lastUpdated: new Date()
    };
    
    // 手動で変更検知を実行
    this.cdr.detectChanges();
    this.manualUpdateCount++;
  }
  
  refreshData() {
    // データを再読み込み（例：APIから）
    this.user = {
      name: 'リフレッシュユーザー',
      email: 'refresh@example.com',
      role: 'admin',
      lastUpdated: new Date()
    };
    
    // マークして変更検知を実行
    this.cdr.markForCheck();
  }
}
```

### 3. 効率的なリスト変更検知
```typescript
// efficient-list-detection.component.ts
@Component({
  selector: 'app-efficient-list-detection',
  standalone: true,
  template: `
    <div class="efficient-list">
      <h3>{{title}}</h3>
      
      <div class="list-controls">
        <button (click)="addItem()">アイテム追加</button>
        <button (click)="updateItem()">アイテム更新</button>
        <button (click)="removeItem()">アイテム削除</button>
        <button (click)="shuffleItems()">シャッフル</button>
      </div>
      
      <div class="performance-info">
        <p>アイテム数: {{items.length}}</p>
        <p>レンダリング時間: {{renderTime}}ms</p>
        <p>変更検知回数: {{detectionCount}}</p>
      </div>
      
      <div class="item-list">
        <div 
          *ngFor="let item of items; trackBy: trackByFn" 
          class="item"
          [class.updated]="item.updated">
          {{item.id}}: {{item.name}} ({{item.value}})
        </div>
      </div>
    </div>
  `
})
export class EfficientListDetectionComponent implements OnChanges {
  @Input() title: string = '効率的リスト検知';
  @Input() items: Array<{ id: number; name: string; value: number; updated: boolean }> = [];
  
  detectionCount = 0;
  renderTime = 0;
  
  ngOnChanges(changes: SimpleChanges) {
    this.detectionCount++;
    
    if (changes['items']) {
      const startTime = performance.now();
      
      // レンダリング時間の測定
      setTimeout(() => {
        this.renderTime = performance.now() - startTime;
      }, 0);
    }
  }
  
  // 効率的な変更検知のためのtrackBy関数
  trackByFn(index: number, item: any): number {
    return item.id;
  }
  
  addItem() {
    const newItem = {
      id: Math.max(...this.items.map(item => item.id), 0) + 1,
      name: `アイテム ${this.items.length + 1}`,
      value: Math.floor(Math.random() * 100),
      updated: false
    };
    
    this.items = [...this.items, newItem];
  }
  
  updateItem() {
    if (this.items.length === 0) return;
    
    const randomIndex = Math.floor(Math.random() * this.items.length);
    this.items = this.items.map((item, index) => 
      index === randomIndex 
        ? { ...item, value: Math.floor(Math.random() * 100), updated: true }
        : item
    );
  }
  
  removeItem() {
    if (this.items.length === 0) return;
    
    const randomIndex = Math.floor(Math.random() * this.items.length);
    this.items = this.items.filter((_, index) => index !== randomIndex);
  }
  
  shuffleItems() {
    this.items = [...this.items].sort(() => Math.random() - 0.5);
  }
}
```

### 4. カスタム変更検知ロジック
```typescript
// custom-detection.component.ts
@Component({
  selector: 'app-custom-detection',
  standalone: true,
  template: `
    <div class="custom-detection">
      <h3>{{title}}</h3>
      
      <div class="data-comparison">
        <div class="previous-data">
          <h4>前回のデータ</h4>
          <pre>{{previousData | json}}</pre>
        </div>
        
        <div class="current-data">
          <h4>現在のデータ</h4>
          <pre>{{currentData | json}}</pre>
        </div>
      </div>
      
      <div class="change-analysis">
        <h4>変更分析</h4>
        <p>変更検知: {{hasChanges ? 'あり' : 'なし'}}</p>
        <p>変更されたフィールド: {{changedFields.join(', ')}}</p>
        <p>変更の種類: {{changeTypes.join(', ')}}</p>
      </div>
      
      <div class="actions">
        <button (click)="forceUpdate()">強制更新</button>
        <button (click)="resetData()">データリセット</button>
      </div>
    </div>
  `
})
export class CustomDetectionComponent implements OnChanges {
  @Input() title: string = 'カスタム検知';
  @Input() data: any = {};
  
  previousData: any = {};
  currentData: any = {};
  hasChanges = false;
  changedFields: string[] = [];
  changeTypes: string[] = [];
  
  private cdr = inject(ChangeDetectorRef);
  
  ngOnChanges(changes: SimpleChanges) {
    this.previousData = changes['data']?.previousValue || {};
    this.currentData = changes['data']?.currentValue || {};
    
    this.analyzeChanges();
  }
  
  private analyzeChanges() {
    this.changedFields = [];
    this.changeTypes = [];
    this.hasChanges = false;
    
    if (this.previousData && this.currentData) {
      this.hasChanges = this.detectChanges(this.previousData, this.currentData);
    }
  }
  
  private detectChanges(oldData: any, newData: any, path: string = ''): boolean {
    let hasChanges = false;
    
    // オブジェクトの変更検知
    if (typeof oldData === 'object' && typeof newData === 'object') {
      const allKeys = new Set([...Object.keys(oldData), ...Object.keys(newData)]);
      
      for (const key of allKeys) {
        const currentPath = path ? `${path}.${key}` : key;
        
        if (!(key in oldData)) {
          // 新しいプロパティ
          this.changedFields.push(currentPath);
          this.changeTypes.push('追加');
          hasChanges = true;
        } else if (!(key in newData)) {
          // 削除されたプロパティ
          this.changedFields.push(currentPath);
          this.changeTypes.push('削除');
          hasChanges = true;
        } else if (oldData[key] !== newData[key]) {
          // 値の変更
          if (typeof oldData[key] === 'object' && typeof newData[key] === 'object') {
            hasChanges = this.detectChanges(oldData[key], newData[key], currentPath) || hasChanges;
          } else {
            this.changedFields.push(currentPath);
            this.changeTypes.push('変更');
            hasChanges = true;
          }
        }
      }
    } else if (oldData !== newData) {
      // プリミティブ値の変更
      this.changedFields.push(path || 'root');
      this.changeTypes.push('変更');
      hasChanges = true;
    }
    
    return hasChanges;
  }
  
  forceUpdate() {
    this.cdr.detectChanges();
  }
  
  resetData() {
    this.previousData = {};
    this.currentData = {};
    this.hasChanges = false;
    this.changedFields = [];
    this.changeTypes = [];
  }
}
```

## ベストプラクティス

1. **OnPush戦略**: パフォーマンス向上のための活用
2. **trackBy関数**: リストの効率的な更新
3. **不変性**: 確実な変更検知のための参照変更
4. **手動制御**: 必要に応じた手動変更検知

## 注意点

- 深いオブジェクトの変更は検知されない場合がある
- OnPush戦略使用時は手動での変更検知が必要
- パフォーマンスと機能のバランスを考慮

## 関連技術
- 変更検知
- OnPush戦略
- ChangeDetectorRef
- パフォーマンス最適化
