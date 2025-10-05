# #094 「@Input() デフォルト値の設定」

## 概要
Angular v20における@Input()でのデフォルト値の設定方法を学びます。適切なデフォルト値の設定により、より柔軟で使いやすいコンポーネントAPIを実現する方法について解説します。

## 学習目標
- デフォルト値の設定方法を理解する
- プリミティブ型とオブジェクト型でのデフォルト値設定を習得する
- 適切なデフォルト値の選択方法を身につける

## 📺 画面表示用コード

```typescript
// デフォルト値の設定
@Component({
  selector: 'app-default-values',
  standalone: true,
  template: `
    <h2>{{title}}</h2>
    <p>{{message}}</p>
    <div class="config">
      <p>サイズ: {{size}}</p>
      <p>有効: {{enabled}}</p>
    </div>
  `
})
export class DefaultValuesComponent {
  @Input() title: string = 'デフォルトタイトル';
  @Input() message: string = 'デフォルトメッセージ';
  @Input() size: 'small' | 'medium' | 'large' = 'medium';
  @Input() enabled: boolean = true;
}
```

```typescript
// オブジェクトのデフォルト値
export class ObjectDefaultsComponent {
  @Input() config: Config = {
    theme: 'light',
    language: 'ja',
    notifications: true
  };
}
```

## 技術ポイント

### 1. デフォルト値の基本構文
```typescript
@Input() propertyName: Type = defaultValue;
```
- **defaultValue**: 親から値が渡されない場合の初期値
- **型安全性**: デフォルト値は指定した型と一致する必要がある
- **実行時設定**: デフォルト値は実行時に設定される

### 2. プリミティブ型のデフォルト値
```typescript
@Input() name: string = '';
@Input() count: number = 0;
@Input() isActive: boolean = false;
@Input() items: string[] = [];
```

### 3. オブジェクト型のデフォルト値
```typescript
@Input() config: Config = { theme: 'light', size: 'medium' };
@Input() user: User = { id: 0, name: 'Guest', role: 'user' };
```

## 実践的な活用例

### 1. 設定可能なコンポーネント
```typescript
// configurable-button.component.ts
interface ButtonConfig {
  variant: 'primary' | 'secondary' | 'danger';
  size: 'small' | 'medium' | 'large';
  disabled: boolean;
  loading: boolean;
}

@Component({
  selector: 'app-configurable-button',
  standalone: true,
  template: `
    <button 
      [class]="buttonClasses"
      [disabled]="config.disabled || config.loading"
      (click)="onClick()">
      <span *ngIf="config.loading">読み込み中...</span>
      <span *ngIf="!config.loading">{{label}}</span>
    </button>
  `
})
export class ConfigurableButtonComponent {
  @Input() label: string = 'ボタン';
  @Input() config: ButtonConfig = {
    variant: 'primary',
    size: 'medium',
    disabled: false,
    loading: false
  };
  @Output() buttonClick = new EventEmitter<void>();
  
  get buttonClasses(): string {
    return `btn btn-${this.config.variant} btn-${this.config.size}`;
  }
  
  onClick() {
    if (!this.config.disabled && !this.config.loading) {
      this.buttonClick.emit();
    }
  }
}
```

### 2. フォームフィールドのデフォルト値
```typescript
// form-field.component.ts
interface FieldConfig {
  type: 'text' | 'email' | 'password' | 'number';
  placeholder: string;
  required: boolean;
  maxLength?: number;
  min?: number;
  max?: number;
}

@Component({
  selector: 'app-form-field',
  standalone: true,
  template: `
    <div class="form-field">
      <label *ngIf="label" [for]="fieldId">{{label}}</label>
      <input 
        [id]="fieldId"
        [type]="config.type"
        [placeholder]="config.placeholder"
        [required]="config.required"
        [maxlength]="config.maxLength"
        [min]="config.min"
        [max]="config.max"
        [value]="value"
        (input)="onInput($event)">
      <div *ngIf="errorMessage" class="error">{{errorMessage}}</div>
    </div>
  `
})
export class FormFieldComponent {
  @Input() fieldId: string = '';
  @Input() label: string = '';
  @Input() value: string = '';
  @Input() errorMessage: string = '';
  @Input() config: FieldConfig = {
    type: 'text',
    placeholder: '入力してください',
    required: false
  };
  
  @Output() valueChange = new EventEmitter<string>();
  
  onInput(event: Event) {
    const target = event.target as HTMLInputElement;
    this.value = target.value;
    this.valueChange.emit(this.value);
  }
}
```

### 3. データ表示コンポーネントのデフォルト値
```typescript
// data-display.component.ts
interface DisplayConfig {
  showHeader: boolean;
  showFooter: boolean;
  itemsPerPage: number;
  sortDirection: 'asc' | 'desc';
  filterEnabled: boolean;
}

@Component({
  selector: 'app-data-display',
  standalone: true,
  template: `
    <div class="data-display">
      <div *ngIf="config.showHeader" class="header">
        <h3>{{title}}</h3>
        <div *ngIf="config.filterEnabled" class="filter">
          <input [(ngModel)]="filterText" placeholder="フィルター">
        </div>
      </div>
      
      <div class="content">
        <div *ngFor="let item of filteredData" class="item">
          {{item | json}}
        </div>
      </div>
      
      <div *ngIf="config.showFooter" class="footer">
        <p>表示件数: {{filteredData.length}}</p>
      </div>
    </div>
  `
})
export class DataDisplayComponent {
  @Input() title: string = 'データ一覧';
  @Input() data: any[] = [];
  @Input() config: DisplayConfig = {
    showHeader: true,
    showFooter: true,
    itemsPerPage: 10,
    sortDirection: 'asc',
    filterEnabled: false
  };
  
  filterText: string = '';
  
  get filteredData(): any[] {
    if (!this.config.filterEnabled || !this.filterText) {
      return this.data;
    }
    
    return this.data.filter(item => 
      JSON.stringify(item).toLowerCase().includes(this.filterText.toLowerCase())
    );
  }
}
```

### 4. 複雑なオブジェクトのデフォルト値
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
  permissions: string[];
}

@Component({
  selector: 'app-user-profile',
  standalone: true,
  template: `
    <div class="user-profile">
      <img *ngIf="profile.avatar" [src]="profile.avatar" [alt]="profile.name">
      <h2>{{profile.name}}</h2>
      <p>{{profile.email}}</p>
      <span class="role">{{profile.role}}</span>
      
      <div class="preferences">
        <p>テーマ: {{profile.preferences.theme}}</p>
        <p>言語: {{profile.preferences.language}}</p>
        <p>通知: {{profile.preferences.notifications ? 'ON' : 'OFF'}}</p>
      </div>
      
      <div class="permissions">
        <span *ngFor="let permission of profile.permissions" class="permission">
          {{permission}}
        </span>
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
    },
    permissions: []
  };
}
```

## ベストプラクティス

1. **意味のあるデフォルト値**: 実際の使用ケースに適したデフォルト値を設定
2. **型安全性**: デフォルト値が指定した型と一致することを確認
3. **不変性**: オブジェクトのデフォルト値は不変であることが望ましい
4. **ドキュメント**: デフォルト値の意味と用途を明確に文書化

## 注意点

- デフォルト値は実行時に設定されるため、コンパイル時の型チェックとは別
- オブジェクトのデフォルト値は参照が共有される可能性がある
- 複雑なオブジェクトのデフォルト値は、不変性を考慮して設計する

## 関連技術
- デフォルト値
- 型安全性
- オブジェクト初期化
- コンポーネントAPI設計
