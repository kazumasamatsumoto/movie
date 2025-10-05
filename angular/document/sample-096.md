# #096 「@Input() 型定義とバリデーション」

## 概要
Angular v20における@Input()での型定義とバリデーションを学びます。TypeScriptの型システムを活用した型安全性の向上と、実行時バリデーションの実装方法について解説します。

## 学習目標
- 型定義の重要性を理解する
- カスタム型の定義と使用方法を習得する
- 型安全性とバリデーションの実装方法を身につける

## 📺 画面表示用コード

```typescript
// 型定義付き@Input()
interface User {
  id: number;
  name: string;
  email: string;
  role: 'admin' | 'user';
}

@Component({
  selector: 'app-typed-input',
  standalone: true,
  template: `
    <div class="user-card">
      <h3>{{user.name}}</h3>
      <p>{{user.email}}</p>
      <span class="role">{{user.role}}</span>
    </div>
  `
})
export class TypedInputComponent {
  @Input() user: User = {
    id: 0,
    name: '',
    email: '',
    role: 'user'
  };
}
```

```typescript
// 型ガード付きバリデーション
export class ValidatedInputComponent {
  @Input() data: any;
  
  ngOnInit() {
    if (this.isValidUser(this.data)) {
      this.processUser(this.data);
    }
  }
  
  private isValidUser(data: any): data is User {
    return data && 
           typeof data.id === 'number' && 
           typeof data.name === 'string' &&
           typeof data.email === 'string' &&
           (data.role === 'admin' || data.role === 'user');
  }
}
```

## 技術ポイント

### 1. 基本的な型定義
```typescript
// プリミティブ型
@Input() name: string;
@Input() age: number;
@Input() isActive: boolean;

// 配列型
@Input() items: string[];
@Input() users: User[];

// オブジェクト型
@Input() config: Config;
@Input() user: User;
```

### 2. カスタム型の定義
```typescript
// インターフェース
interface User {
  id: number;
  name: string;
  email: string;
}

// 型エイリアス
type Status = 'pending' | 'approved' | 'rejected';

// ユニオン型
type StringOrNumber = string | number;
```

### 3. 型ガード
```typescript
// 型ガード関数
function isString(value: any): value is string {
  return typeof value === 'string';
}

// 使用例
if (isString(this.inputValue)) {
  // ここでinputValueはstring型として扱われる
}
```

## 実践的な活用例

### 1. 型安全な設定コンポーネント
```typescript
// config.component.ts
interface ComponentConfig {
  theme: 'light' | 'dark';
  size: 'small' | 'medium' | 'large';
  animations: boolean;
  language: 'ja' | 'en';
}

@Component({
  selector: 'app-config',
  standalone: true,
  template: `
    <div class="config" [class]="config.theme">
      <h3>設定</h3>
      <div class="config-item">
        <label>テーマ:</label>
        <select [(ngModel)]="config.theme">
          <option value="light">ライト</option>
          <option value="dark">ダーク</option>
        </select>
      </div>
      <div class="config-item">
        <label>サイズ:</label>
        <select [(ngModel)]="config.size">
          <option value="small">小</option>
          <option value="medium">中</option>
          <option value="large">大</option>
        </select>
      </div>
    </div>
  `,
  imports: [FormsModule]
})
export class ConfigComponent {
  @Input() config: ComponentConfig = {
    theme: 'light',
    size: 'medium',
    animations: true,
    language: 'ja'
  };
  
  @Output() configChange = new EventEmitter<ComponentConfig>();
}
```

### 2. 型安全なフォームコンポーネント
```typescript
// typed-form.component.ts
interface FormData {
  name: string;
  email: string;
  age: number;
  interests: string[];
}

interface ValidationResult {
  isValid: boolean;
  errors: string[];
}

@Component({
  selector: 'app-typed-form',
  standalone: true,
  template: `
    <form (ngSubmit)="onSubmit()">
      <div class="form-group">
        <label>名前:</label>
        <input [(ngModel)]="formData.name" name="name" required>
      </div>
      <div class="form-group">
        <label>メール:</label>
        <input [(ngModel)]="formData.email" name="email" type="email" required>
      </div>
      <div class="form-group">
        <label>年齢:</label>
        <input [(ngModel)]="formData.age" name="age" type="number" required>
      </div>
      <button type="submit" [disabled]="!validation.isValid">送信</button>
    </form>
    <div *ngIf="!validation.isValid" class="errors">
      <div *ngFor="let error of validation.errors">{{error}}</div>
    </div>
  `,
  imports: [FormsModule]
})
export class TypedFormComponent {
  @Input() formData: FormData = {
    name: '',
    email: '',
    age: 0,
    interests: []
  };
  
  @Output() formSubmit = new EventEmitter<FormData>();
  
  get validation(): ValidationResult {
    const errors: string[] = [];
    
    if (!this.formData.name) {
      errors.push('名前は必須です');
    }
    
    if (!this.formData.email || !this.isValidEmail(this.formData.email)) {
      errors.push('有効なメールアドレスを入力してください');
    }
    
    if (!this.formData.age || this.formData.age < 0) {
      errors.push('有効な年齢を入力してください');
    }
    
    return {
      isValid: errors.length === 0,
      errors
    };
  }
  
  onSubmit() {
    if (this.validation.isValid) {
      this.formSubmit.emit(this.formData);
    }
  }
  
  private isValidEmail(email: string): boolean {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
  }
}
```

### 3. 型安全なAPIレスポンス処理
```typescript
// api-data.component.ts
interface ApiResponse<T> {
  data: T;
  status: 'success' | 'error';
  message?: string;
}

interface User {
  id: number;
  name: string;
  email: string;
  avatar?: string;
}

@Component({
  selector: 'app-api-data',
  standalone: true,
  template: `
    <div class="api-data">
      <div *ngIf="loading" class="loading">読み込み中...</div>
      <div *ngIf="error" class="error">{{error}}</div>
      <div *ngIf="users" class="users">
        <div *ngFor="let user of users" class="user-item">
          <img *ngIf="user.avatar" [src]="user.avatar" [alt]="user.name">
          <h4>{{user.name}}</h4>
          <p>{{user.email}}</p>
        </div>
      </div>
    </div>
  `
})
export class ApiDataComponent implements OnInit {
  @Input() apiUrl: string = '';
  
  users: User[] = [];
  loading = false;
  error: string | null = null;
  
  ngOnInit() {
    this.loadUsers();
  }
  
  private async loadUsers() {
    this.loading = true;
    this.error = null;
    
    try {
      const response = await fetch(this.apiUrl);
      const result: ApiResponse<User[]> = await response.json();
      
      if (this.isValidApiResponse(result)) {
        this.users = result.data;
      } else {
        this.error = '無効なAPIレスポンスです';
      }
    } catch (error) {
      this.error = 'データの読み込みに失敗しました';
    } finally {
      this.loading = false;
    }
  }
  
  private isValidApiResponse(response: any): response is ApiResponse<User[]> {
    return response &&
           typeof response.status === 'string' &&
           Array.isArray(response.data) &&
           response.data.every(this.isValidUser);
  }
  
  private isValidUser(user: any): user is User {
    return user &&
           typeof user.id === 'number' &&
           typeof user.name === 'string' &&
           typeof user.email === 'string';
  }
}
```

### 4. 型安全なイベント処理
```typescript
// typed-events.component.ts
interface CustomEvent {
  type: 'user_action' | 'data_change' | 'system_event';
  payload: any;
  timestamp: Date;
}

@Component({
  selector: 'app-typed-events',
  standalone: true,
  template: `
    <div class="typed-events">
      <button (click)="triggerUserAction()">ユーザーアクション</button>
      <button (click)="triggerDataChange()">データ変更</button>
      <button (click)="triggerSystemEvent()">システムイベント</button>
    </div>
  `
})
export class TypedEventsComponent {
  @Output() customEvent = new EventEmitter<CustomEvent>();
  
  triggerUserAction() {
    this.emitEvent('user_action', { action: 'button_click', userId: 123 });
  }
  
  triggerDataChange() {
    this.emitEvent('data_change', { field: 'name', value: '新しい値' });
  }
  
  triggerSystemEvent() {
    this.emitEvent('system_event', { level: 'info', message: 'システム正常' });
  }
  
  private emitEvent(type: CustomEvent['type'], payload: any) {
    const event: CustomEvent = {
      type,
      payload,
      timestamp: new Date()
    };
    
    this.customEvent.emit(event);
  }
}
```

## ベストプラクティス

1. **厳密な型定義**: 可能な限り厳密な型を定義する
2. **型ガードの活用**: 実行時バリデーションで型ガードを使用
3. **インターフェースの活用**: 複雑なオブジェクトにはインターフェースを定義
4. **ユニオン型の活用**: 複数の型を受け入れる場合はユニオン型を使用

## 注意点

- 型定義はコンパイル時のチェックであり、実行時のバリデーションではない
- 外部データ（APIレスポンスなど）は型ガードで検証する
- `any`型の使用は最小限に抑える

## 関連技術
- TypeScript型システム
- 型ガード
- インターフェース
- バリデーション
