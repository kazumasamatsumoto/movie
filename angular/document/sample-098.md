# #098 「@Input() オブジェクトの受け渡し」

## 概要
Angular v20における@Input()でのオブジェクトの受け渡しを学びます。参照渡しの特性、オブジェクトの変更検知、不変性の維持など、オブジェクトを安全に扱う方法について解説します。

## 学習目標
- オブジェクトの受け渡し方法を理解する
- 参照渡しの特性を把握する
- オブジェクトの変更検知と不変性維持を習得する

## 📺 画面表示用コード

```typescript
// オブジェクトの受け渡し
interface User {
  id: number;
  name: string;
  email: string;
  role: string;
}

@Component({
  selector: 'app-object-input',
  standalone: true,
  template: `
    <div class="user-card">
      <h3>{{user.name}}</h3>
      <p>{{user.email}}</p>
      <span class="role">{{user.role}}</span>
    </div>
  `
})
export class ObjectInputComponent {
  @Input() user: User = {
    id: 0,
    name: '',
    email: '',
    role: 'user'
  };
}
```

```typescript
// 参照渡しの特性
export class ReferenceExampleComponent {
  @Input() data: any = {};
  
  modifyData() {
    // 子で変更すると親にも影響する（参照渡し）
    this.data.name = '変更された名前';
  }
}
```

```typescript
// 不変性の維持
export class ImmutableComponent {
  @Input() user: User = {};
  
  updateUser() {
    // 新しいオブジェクトを作成して不変性を維持
    this.user = { ...this.user, name: '新しい名前' };
  }
}
```

## 技術ポイント

### 1. 参照渡しの特性
- **参照共有**: オブジェクトの参照が渡される
- **変更の影響**: 子で変更すると親にも影響する
- **メモリ効率**: オブジェクトのコピーは作成されない

### 2. オブジェクトの変更検知
- **浅い比較**: Angularは参照の比較のみ行う
- **深い変更**: オブジェクト内部の変更は検知されない場合がある
- **OnPush戦略**: 変更検知の最適化

### 3. 不変性の維持
- **スプレッド演算子**: `{...obj}`で新しいオブジェクトを作成
- **Object.freeze()**: オブジェクトを凍結
- **Readonly型**: TypeScriptの型システムを活用

## 実践的な活用例

### 1. ユーザープロフィールコンポーネント
```typescript
// user-profile.component.ts
interface UserProfile {
  id: number;
  name: string;
  email: string;
  avatar?: string;
  role: 'admin' | 'user' | 'guest';
  preferences: {
    theme: 'light' | 'dark';
    language: 'ja' | 'en';
    notifications: boolean;
  };
  lastLogin?: Date;
}

@Component({
  selector: 'app-user-profile',
  standalone: true,
  template: `
    <div class="user-profile">
      <div class="profile-header">
        <img *ngIf="profile.avatar" [src]="profile.avatar" [alt]="profile.name">
        <h2>{{profile.name}}</h2>
        <span class="role-badge">{{profile.role}}</span>
      </div>
      
      <div class="profile-details">
        <p><strong>メール:</strong> {{profile.email}}</p>
        <p *ngIf="profile.lastLogin">
          <strong>最終ログイン:</strong> {{profile.lastLogin | date:'medium'}}
        </p>
      </div>
      
      <div class="preferences">
        <h4>設定</h4>
        <p>テーマ: {{profile.preferences.theme}}</p>
        <p>言語: {{profile.preferences.language}}</p>
        <p>通知: {{profile.preferences.notifications ? 'ON' : 'OFF'}}</p>
      </div>
    </div>
  `
})
export class UserProfileComponent {
  @Input() profile: UserProfile = {
    id: 0,
    name: 'ゲストユーザー',
    email: '',
    role: 'guest',
    preferences: {
      theme: 'light',
      language: 'ja',
      notifications: true
    }
  };
  
  ngOnInit() {
    this.validateProfile();
  }
  
  private validateProfile() {
    if (!this.profile.id) {
      console.warn('ユーザーIDが設定されていません');
    }
    
    if (!this.profile.email) {
      console.warn('メールアドレスが設定されていません');
    }
  }
}
```

### 2. 設定オブジェクトの管理
```typescript
// config-manager.component.ts
interface AppConfig {
  api: {
    baseUrl: string;
    timeout: number;
    retries: number;
  };
  ui: {
    theme: 'light' | 'dark';
    language: 'ja' | 'en';
    animations: boolean;
  };
  features: {
    notifications: boolean;
    analytics: boolean;
    debug: boolean;
  };
}

@Component({
  selector: 'app-config-manager',
  standalone: true,
  template: `
    <div class="config-manager">
      <h3>{{title}}</h3>
      
      <div class="config-section">
        <h4>API設定</h4>
        <p>ベースURL: {{config.api.baseUrl}}</p>
        <p>タイムアウト: {{config.api.timeout}}ms</p>
        <p>リトライ回数: {{config.api.retries}}</p>
      </div>
      
      <div class="config-section">
        <h4>UI設定</h4>
        <p>テーマ: {{config.ui.theme}}</p>
        <p>言語: {{config.ui.language}}</p>
        <p>アニメーション: {{config.ui.animations ? 'ON' : 'OFF'}}</p>
      </div>
      
      <div class="config-section">
        <h4>機能設定</h4>
        <p>通知: {{config.features.notifications ? 'ON' : 'OFF'}}</p>
        <p>分析: {{config.features.analytics ? 'ON' : 'OFF'}}</p>
        <p>デバッグ: {{config.features.debug ? 'ON' : 'OFF'}}</p>
      </div>
    </div>
  `
})
export class ConfigManagerComponent {
  @Input() title: string = '設定';
  @Input() config: AppConfig = {
    api: {
      baseUrl: 'https://api.example.com',
      timeout: 5000,
      retries: 3
    },
    ui: {
      theme: 'light',
      language: 'ja',
      animations: true
    },
    features: {
      notifications: true,
      analytics: false,
      debug: false
    }
  };
}
```

### 3. 不変性を考慮したデータ管理
```typescript
// immutable-data.component.ts
interface Task {
  id: number;
  title: string;
  description: string;
  completed: boolean;
  priority: 'low' | 'medium' | 'high';
  createdAt: Date;
  updatedAt: Date;
}

@Component({
  selector: 'app-immutable-data',
  standalone: true,
  template: `
    <div class="task-manager">
      <h3>{{title}}</h3>
      
      <div class="task-list">
        <div *ngFor="let task of tasks" class="task-item" [class.completed]="task.completed">
          <h4>{{task.title}}</h4>
          <p>{{task.description}}</p>
          <div class="task-meta">
            <span class="priority priority-{{task.priority}}">{{task.priority}}</span>
            <span class="date">{{task.createdAt | date:'short'}}</span>
          </div>
          <button (click)="toggleTask(task.id)">完了切り替え</button>
        </div>
      </div>
    </div>
  `
})
export class ImmutableDataComponent {
  @Input() title: string = 'タスク管理';
  @Input() tasks: Task[] = [];
  
  @Output() taskUpdate = new EventEmitter<Task>();
  
  toggleTask(taskId: number) {
    // 不変性を維持してタスクを更新
    this.tasks = this.tasks.map(task => {
      if (task.id === taskId) {
        const updatedTask: Task = {
          ...task,
          completed: !task.completed,
          updatedAt: new Date()
        };
        this.taskUpdate.emit(updatedTask);
        return updatedTask;
      }
      return task;
    });
  }
  
  // 新しいタスクを追加（不変性を維持）
  addTask(newTask: Omit<Task, 'id' | 'createdAt' | 'updatedAt'>) {
    const task: Task = {
      ...newTask,
      id: Math.max(...this.tasks.map(t => t.id), 0) + 1,
      createdAt: new Date(),
      updatedAt: new Date()
    };
    
    this.tasks = [...this.tasks, task];
  }
  
  // タスクを削除（不変性を維持）
  removeTask(taskId: number) {
    this.tasks = this.tasks.filter(task => task.id !== taskId);
  }
}
```

### 4. 深いオブジェクトの変更検知
```typescript
// deep-object.component.ts
interface NestedData {
  level1: {
    level2: {
      level3: {
        value: string;
        count: number;
      };
    };
  };
}

@Component({
  selector: 'app-deep-object',
  standalone: true,
  template: `
    <div class="deep-object">
      <h3>{{title}}</h3>
      <p>深い値: {{data.level1.level2.level3.value}}</p>
      <p>カウント: {{data.level1.level2.level3.count}}</p>
      
      <button (click)="updateDeepValue()">深い値を更新</button>
      <button (click)="updateShallowValue()">浅い値を更新</button>
    </div>
  `
})
export class DeepObjectComponent implements OnChanges {
  @Input() title: string = '深いオブジェクト';
  @Input() data: NestedData = {
    level1: {
      level2: {
        level3: {
          value: '初期値',
          count: 0
        }
      }
    }
  };
  
  ngOnChanges(changes: SimpleChanges) {
    if (changes['data']) {
      console.log('データが変更されました:', changes['data']);
      
      // 深い変更の検知は困難な場合がある
      this.checkForDeepChanges();
    }
  }
  
  updateDeepValue() {
    // 深い値を更新（参照は同じなので変更検知されない可能性がある）
    this.data.level1.level2.level3.value = '更新された値';
    this.data.level1.level2.level3.count++;
  }
  
  updateShallowValue() {
    // 新しいオブジェクトを作成して変更検知を確実にする
    this.data = {
      ...this.data,
      level1: {
        ...this.data.level1,
        level2: {
          ...this.data.level1.level2,
          level3: {
            ...this.data.level1.level2.level3,
            value: '新しい値',
            count: this.data.level1.level2.level3.count + 1
          }
        }
      }
    };
  }
  
  private checkForDeepChanges() {
    // 深い変更を検知するためのカスタムロジック
    console.log('現在のデータ:', JSON.stringify(this.data));
  }
}
```

## ベストプラクティス

1. **不変性の維持**: スプレッド演算子やObject.freeze()を使用
2. **型安全性**: 明確なインターフェース定義
3. **変更検知**: OnPush戦略やカスタム変更検知の活用
4. **メモリ管理**: 不要なオブジェクト参照の解放

## 注意点

- オブジェクトは参照渡しなので、子で変更すると親にも影響する
- 深いオブジェクトの変更は変更検知されない場合がある
- 不変性を維持することで予期しない副作用を防ぐ

## 関連技術
- 参照渡し
- 不変性
- 変更検知
- OnPush戦略
