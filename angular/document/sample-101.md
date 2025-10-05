# #101 「@Input() での不変性の考慮」

## 概要
Angular v20における@Input()での不変性の考慮を学びます。オブジェクトや配列の不変性を維持し、予期しない副作用を防ぐ方法について解説します。

## 学習目標
- 不変性の重要性を理解する
- 不変性を維持する実装方法を習得する
- 副作用を防ぐベストプラクティスを身につける

## 📺 画面表示用コード

```typescript
// 不変性を考慮した実装
@Component({
  selector: 'app-immutable-input',
  standalone: true,
  template: `
    <div class="immutable-display">
      <h3>{{data.title}}</h3>
      <p>{{data.content}}</p>
      <button (click)="updateData()">データ更新</button>
    </div>
  `
})
export class ImmutableInputComponent {
  @Input() data: { title: string; content: string } = { title: '', content: '' };
  
  updateData() {
    // 不変性を維持してデータを更新
    this.data = { ...this.data, content: '更新されたコンテンツ' };
  }
}
```

```typescript
// Readonly型の使用
export class ReadonlyInputComponent {
  @Input() readonlyData: Readonly<{ id: number; name: string }[]> = [];
  
  processData() {
    // readonlyDataは変更できない
    const newData = [...this.readonlyData, { id: 3, name: '新しいアイテム' }];
    // this.readonlyData = newData; // エラー: readonly
  }
}
```

```typescript
// Object.freezeの使用
export class FreezeInputComponent {
  @Input() frozenData: any = {};
  
  ngOnInit() {
    // オブジェクトを凍結して不変性を保つ
    Object.freeze(this.frozenData);
  }
}
```

## 技術ポイント

### 1. 不変性の基本概念
- **不変性**: データが作成後に変更されない性質
- **副作用の防止**: 予期しない変更を防ぐ
- **予測可能性**: データの状態が予測可能

### 2. 不変性を維持する方法
```typescript
// スプレッド演算子
const newObject = { ...oldObject, newProperty: value };

// 配列の不変操作
const newArray = [...oldArray, newItem];
const filteredArray = oldArray.filter(item => condition);

// Object.freeze
const frozenObject = Object.freeze({ ...object });

// Readonly型
const readonlyData: Readonly<DataType> = data;
```

### 3. TypeScriptの不変性サポート
- **Readonly**: 読み取り専用プロパティ
- **ReadonlyArray**: 読み取り専用配列
- **as const**: リテラル型の不変性

## 実践的な活用例

### 1. 不変な設定管理
```typescript
// immutable-config.component.ts
interface AppConfig {
  theme: 'light' | 'dark';
  language: 'ja' | 'en';
  features: {
    notifications: boolean;
    analytics: boolean;
  };
}

@Component({
  selector: 'app-immutable-config',
  standalone: true,
  template: `
    <div class="config-manager">
      <h3>{{title}}</h3>
      
      <div class="config-display">
        <p>テーマ: {{config.theme}}</p>
        <p>言語: {{config.language}}</p>
        <p>通知: {{config.features.notifications ? 'ON' : 'OFF'}}</p>
        <p>分析: {{config.features.analytics ? 'ON' : 'OFF'}}</p>
      </div>
      
      <div class="config-actions">
        <button (click)="toggleTheme()">テーマ切り替え</button>
        <button (click)="toggleNotifications()">通知切り替え</button>
        <button (click)="resetConfig()">設定リセット</button>
      </div>
    </div>
  `
})
export class ImmutableConfigComponent {
  @Input() title: string = '設定管理';
  @Input() config: Readonly<AppConfig> = Object.freeze({
    theme: 'light',
    language: 'ja',
    features: {
      notifications: true,
      analytics: false
    }
  });
  
  @Output() configChange = new EventEmitter<AppConfig>();
  
  toggleTheme() {
    const newConfig: AppConfig = {
      ...this.config,
      theme: this.config.theme === 'light' ? 'dark' : 'light'
    };
    this.configChange.emit(newConfig);
  }
  
  toggleNotifications() {
    const newConfig: AppConfig = {
      ...this.config,
      features: {
        ...this.config.features,
        notifications: !this.config.features.notifications
      }
    };
    this.configChange.emit(newConfig);
  }
  
  resetConfig() {
    const defaultConfig: AppConfig = {
      theme: 'light',
      language: 'ja',
      features: {
        notifications: true,
        analytics: false
      }
    };
    this.configChange.emit(defaultConfig);
  }
}
```

### 2. 不変なデータリスト管理
```typescript
// immutable-list.component.ts
interface ListItem {
  id: number;
  name: string;
  completed: boolean;
}

@Component({
  selector: 'app-immutable-list',
  standalone: true,
  template: `
    <div class="list-manager">
      <h3>{{title}}</h3>
      
      <div class="list-controls">
        <input 
          [(ngModel)]="newItemName" 
          placeholder="新しいアイテム"
          (keyup.enter)="addItem()">
        <button (click)="addItem()">追加</button>
        <button (click)="clearCompleted()">完了済みクリア</button>
      </div>
      
      <div class="list-stats">
        <p>総数: {{items.length}}</p>
        <p>完了: {{completedCount}}</p>
        <p>未完了: {{pendingCount}}</p>
      </div>
      
      <div class="list-items">
        <div *ngFor="let item of items" class="list-item" [class.completed]="item.completed">
          <span>{{item.name}}</span>
          <button (click)="toggleItem(item.id)">完了切り替え</button>
          <button (click)="removeItem(item.id)">削除</button>
        </div>
      </div>
    </div>
  `,
  imports: [FormsModule]
})
export class ImmutableListComponent {
  @Input() title: string = 'アイテム管理';
  @Input() items: ReadonlyArray<ListItem> = [];
  
  @Output() itemsChange = new EventEmitter<ReadonlyArray<ListItem>>();
  
  newItemName: string = '';
  
  get completedCount(): number {
    return this.items.filter(item => item.completed).length;
  }
  
  get pendingCount(): number {
    return this.items.filter(item => !item.completed).length;
  }
  
  addItem() {
    if (!this.newItemName.trim()) return;
    
    const newItem: ListItem = {
      id: Math.max(...this.items.map(item => item.id), 0) + 1,
      name: this.newItemName.trim(),
      completed: false
    };
    
    // 不変性を維持してアイテムを追加
    const newItems = [...this.items, newItem];
    this.itemsChange.emit(newItems);
    this.newItemName = '';
  }
  
  toggleItem(itemId: number) {
    // 不変性を維持してアイテムを更新
    const newItems = this.items.map(item => 
      item.id === itemId 
        ? { ...item, completed: !item.completed }
        : item
    );
    this.itemsChange.emit(newItems);
  }
  
  removeItem(itemId: number) {
    // 不変性を維持してアイテムを削除
    const newItems = this.items.filter(item => item.id !== itemId);
    this.itemsChange.emit(newItems);
  }
  
  clearCompleted() {
    // 不変性を維持して完了済みアイテムを削除
    const newItems = this.items.filter(item => !item.completed);
    this.itemsChange.emit(newItems);
  }
}
```

### 3. 深いオブジェクトの不変性管理
```typescript
// deep-immutable.component.ts
interface DeepData {
  user: {
    profile: {
      name: string;
      settings: {
        theme: string;
        notifications: boolean;
      };
    };
    permissions: string[];
  };
}

@Component({
  selector: 'app-deep-immutable',
  standalone: true,
  template: `
    <div class="deep-data">
      <h3>{{title}}</h3>
      
      <div class="data-display">
        <p>ユーザー名: {{data.user.profile.name}}</p>
        <p>テーマ: {{data.user.profile.settings.theme}}</p>
        <p>通知: {{data.user.profile.settings.notifications ? 'ON' : 'OFF'}}</p>
        <p>権限: {{data.user.permissions.join(', ')}}</p>
      </div>
      
      <div class="data-actions">
        <button (click)="updateUserName()">名前更新</button>
        <button (click)="toggleTheme()">テーマ切り替え</button>
        <button (click)="toggleNotifications()">通知切り替え</button>
        <button (click)="addPermission()">権限追加</button>
      </div>
    </div>
  `
})
export class DeepImmutableComponent {
  @Input() title: string = '深いデータ管理';
  @Input() data: DeepData = {
    user: {
      profile: {
        name: 'デフォルトユーザー',
        settings: {
          theme: 'light',
          notifications: true
        }
      },
      permissions: ['read']
    }
  };
  
  @Output() dataChange = new EventEmitter<DeepData>();
  
  updateUserName() {
    const newData: DeepData = {
      ...this.data,
      user: {
        ...this.data.user,
        profile: {
          ...this.data.user.profile,
          name: '更新された名前'
        }
      }
    };
    this.dataChange.emit(newData);
  }
  
  toggleTheme() {
    const newData: DeepData = {
      ...this.data,
      user: {
        ...this.data.user,
        profile: {
          ...this.data.user.profile,
          settings: {
            ...this.data.user.profile.settings,
            theme: this.data.user.profile.settings.theme === 'light' ? 'dark' : 'light'
          }
        }
      }
    };
    this.dataChange.emit(newData);
  }
  
  toggleNotifications() {
    const newData: DeepData = {
      ...this.data,
      user: {
        ...this.data.user,
        profile: {
          ...this.data.user.profile,
          settings: {
            ...this.data.user.profile.settings,
            notifications: !this.data.user.profile.settings.notifications
          }
        }
      }
    };
    this.dataChange.emit(newData);
  }
  
  addPermission() {
    const newPermission = 'write';
    const newData: DeepData = {
      ...this.data,
      user: {
        ...this.data.user,
        permissions: [...this.data.user.permissions, newPermission]
      }
    };
    this.dataChange.emit(newData);
  }
}
```

### 4. 不変性ユーティリティの活用
```typescript
// immutable-utils.component.ts
class ImmutableUtils {
  static updateObject<T extends object>(obj: T, updates: Partial<T>): T {
    return { ...obj, ...updates };
  }
  
  static updateNestedObject<T extends object>(
    obj: T, 
    path: string[], 
    value: any
  ): T {
    if (path.length === 0) return obj;
    if (path.length === 1) {
      return { ...obj, [path[0]]: value };
    }
    
    const [first, ...rest] = path;
    return {
      ...obj,
      [first]: this.updateNestedObject(obj[first as keyof T], rest, value)
    };
  }
  
  static addToArray<T>(arr: readonly T[], item: T): readonly T[] {
    return [...arr, item];
  }
  
  static removeFromArray<T>(arr: readonly T[], predicate: (item: T) => boolean): readonly T[] {
    return arr.filter(predicate);
  }
  
  static updateArrayItem<T>(arr: readonly T[], index: number, updates: Partial<T>): readonly T[] {
    return arr.map((item, i) => 
      i === index ? { ...item, ...updates } : item
    );
  }
}

interface ComplexData {
  id: number;
  name: string;
  metadata: {
    tags: string[];
    created: Date;
    updated: Date;
  };
}

@Component({
  selector: 'app-immutable-utils',
  standalone: true,
  template: `
    <div class="immutable-utils">
      <h3>{{title}}</h3>
      
      <div class="data-display">
        <p>ID: {{data.id}}</p>
        <p>名前: {{data.name}}</p>
        <p>タグ: {{data.metadata.tags.join(', ')}}</p>
        <p>作成日: {{data.metadata.created | date}}</p>
        <p>更新日: {{data.metadata.updated | date}}</p>
      </div>
      
      <div class="actions">
        <button (click)="updateName()">名前更新</button>
        <button (click)="addTag()">タグ追加</button>
        <button (click)="removeTag()">タグ削除</button>
        <button (click)="updateTimestamp()">タイムスタンプ更新</button>
      </div>
    </div>
  `
})
export class ImmutableUtilsComponent {
  @Input() title: string = '不変性ユーティリティ';
  @Input() data: ComplexData = {
    id: 1,
    name: 'サンプルデータ',
    metadata: {
      tags: ['angular', 'typescript'],
      created: new Date(),
      updated: new Date()
    }
  };
  
  @Output() dataChange = new EventEmitter<ComplexData>();
  
  updateName() {
    const newData = ImmutableUtils.updateObject(this.data, {
      name: '更新された名前'
    });
    this.dataChange.emit(newData);
  }
  
  addTag() {
    const newTag = 'immutable';
    const newData = ImmutableUtils.updateNestedObject(
      this.data,
      ['metadata', 'tags'],
      ImmutableUtils.addToArray(this.data.metadata.tags, newTag)
    );
    this.dataChange.emit(newData);
  }
  
  removeTag() {
    if (this.data.metadata.tags.length === 0) return;
    
    const newData = ImmutableUtils.updateNestedObject(
      this.data,
      ['metadata', 'tags'],
      this.data.metadata.tags.slice(0, -1)
    );
    this.dataChange.emit(newData);
  }
  
  updateTimestamp() {
    const newData = ImmutableUtils.updateNestedObject(
      this.data,
      ['metadata', 'updated'],
      new Date()
    );
    this.dataChange.emit(newData);
  }
}
```

## ベストプラクティス

1. **Readonly型の活用**: TypeScriptの型システムを活用
2. **スプレッド演算子**: オブジェクトや配列の不変操作
3. **Object.freeze**: 実行時の不変性保証
4. **ユーティリティ関数**: 複雑な不変操作の抽象化

## 注意点

- 深いオブジェクトの不変操作は複雑になる場合がある
- パフォーマンスを考慮して適切な不変操作を選択
- 不変性を維持するためのコストと利益のバランスを考慮

## 関連技術
- 不変性
- 関数型プログラミング
- TypeScript型システム
- 副作用の管理
