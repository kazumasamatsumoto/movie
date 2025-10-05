# #093 「@Input() 必須プロパティ - required」

## 概要
Angular v20における@Input()の必須プロパティ機能を学びます。`required: true`オプションを使用して、コンパイル時に必須プロパティを強制する方法について解説します。

## 学習目標
- 必須プロパティの設定方法を理解する
- コンパイル時の型安全性向上を把握する
- 適切な必須プロパティの使い分けを習得する

## 📺 画面表示用コード

```typescript
// 必須プロパティの定義
@Component({
  selector: 'app-required-input',
  standalone: true,
  template: `
    <h2>{{title}}</h2>
    <p>{{content}}</p>
  `
})
export class RequiredInputComponent {
  @Input({ required: true }) title!: string;
  @Input({ required: true }) content!: string;
  @Input() optionalField: string = '';
}
```

```html
<!-- 必須プロパティの使用 -->
<app-required-input 
  [title]="'必須タイトル'"
  [content]="'必須コンテンツ'">
</app-required-input>
```

```typescript
// コンパイルエラーの例
@Component({
  template: `
    <!-- エラー: 必須プロパティが不足 -->
    <app-required-input [title]="'タイトルのみ'">
    </app-required-input>
  `
})
export class ErrorComponent {
  // コンパイル時にエラーが発生
}
```

## 技術ポイント

### 1. 必須プロパティの基本構文
```typescript
@Input({ required: true }) propertyName!: Type;
```
- `required: true`: 必須プロパティの指定
- `!`: 非nullアサーション演算子（必須プロパティでは必須）

### 2. コンパイル時の型チェック
- **厳密な型チェック**: 親コンポーネントで値が渡されていない場合にコンパイルエラー
- **実行時安全性**: 必須プロパティが確実に設定される
- **開発効率**: 早期のエラー検出により開発効率が向上

### 3. 必須プロパティの特徴
- **コンパイル時チェック**: TypeScriptコンパイラによる静的チェック
- **実行時保証**: 値が確実に設定される
- **IDE支援**: エディタでのエラー表示

## 実践的な活用例

### 1. フォームコンポーネントでの必須プロパティ
```typescript
// form-field.component.ts
@Component({
  selector: 'app-form-field',
  standalone: true,
  template: `
    <div class="form-field">
      <label [for]="fieldId">{{label}}</label>
      <input 
        [id]="fieldId"
        [type]="inputType"
        [placeholder]="placeholder"
        [value]="value"
        (input)="onInput($event)">
      <div *ngIf="errorMessage" class="error">{{errorMessage}}</div>
    </div>
  `
})
export class FormFieldComponent {
  @Input({ required: true }) fieldId!: string;
  @Input({ required: true }) label!: string;
  @Input({ required: true }) inputType!: string;
  @Input() placeholder: string = '';
  @Input() value: string = '';
  @Input() errorMessage: string = '';
  
  onInput(event: Event) {
    const target = event.target as HTMLInputElement;
    this.value = target.value;
  }
}
```

### 2. データ表示コンポーネントでの必須プロパティ
```typescript
// data-card.component.ts
interface DataCardConfig {
  id: string;
  title: string;
  data: any[];
  displayFields: string[];
}

@Component({
  selector: 'app-data-card',
  standalone: true,
  template: `
    <div class="data-card">
      <h3>{{config.title}}</h3>
      <div class="data-list">
        <div *ngFor="let item of config.data" class="data-item">
          <span *ngFor="let field of config.displayFields">
            {{item[field]}}
          </span>
        </div>
      </div>
    </div>
  `
})
export class DataCardComponent {
  @Input({ required: true }) config!: DataCardConfig;
  @Input() theme: 'light' | 'dark' = 'light';
  @Input() maxItems: number = 10;
}
```

### 3. 必須プロパティとオプショナルプロパティの組み合わせ
```typescript
// user-card.component.ts
interface User {
  id: number;
  name: string;
  email: string;
  avatar?: string;
  role: string;
}

@Component({
  selector: 'app-user-card',
  standalone: true,
  template: `
    <div class="user-card">
      <img *ngIf="user.avatar" [src]="user.avatar" [alt]="user.name">
      <h3>{{user.name}}</h3>
      <p>{{user.email}}</p>
      <span class="role">{{user.role}}</span>
      <div *ngIf="showActions" class="actions">
        <button (click)="onEdit()">編集</button>
        <button (click)="onDelete()">削除</button>
      </div>
    </div>
  `
})
export class UserCardComponent {
  @Input({ required: true }) user!: User;
  @Input({ required: true }) onEdit!: () => void;
  @Input({ required: true }) onDelete!: () => void;
  @Input() showActions: boolean = true;
  @Input() cardSize: 'small' | 'medium' | 'large' = 'medium';
}
```

### 4. エラーハンドリング付き必須プロパティ
```typescript
// api-data.component.ts
@Component({
  selector: 'app-api-data',
  standalone: true,
  template: `
    <div class="api-data">
      <div *ngIf="loading" class="loading">読み込み中...</div>
      <div *ngIf="error" class="error">{{error}}</div>
      <div *ngIf="data" class="data">
        <h3>{{title}}</h3>
        <pre>{{data | json}}</pre>
      </div>
    </div>
  `
})
export class ApiDataComponent implements OnInit {
  @Input({ required: true }) apiUrl!: string;
  @Input({ required: true }) title!: string;
  @Input() refreshInterval: number = 0;
  
  data: any = null;
  loading = false;
  error: string | null = null;
  
  ngOnInit() {
    this.loadData();
    if (this.refreshInterval > 0) {
      setInterval(() => this.loadData(), this.refreshInterval);
    }
  }
  
  private loadData() {
    this.loading = true;
    this.error = null;
    
    // API呼び出しの実装
    fetch(this.apiUrl)
      .then(response => response.json())
      .then(data => {
        this.data = data;
        this.loading = false;
      })
      .catch(error => {
        this.error = 'データの読み込みに失敗しました';
        this.loading = false;
      });
  }
}
```

## ベストプラクティス

1. **適切な使用**: 本当に必須なプロパティのみに適用
2. **型安全性**: 非nullアサーション演算子`!`の適切な使用
3. **ドキュメント**: 必須プロパティの明確な文書化
4. **テスト**: 必須プロパティのテストケース

## 注意点

- 必須プロパティはコンパイル時のチェックであり、実行時のバリデーションではない
- 非nullアサーション演算子`!`は必須プロパティでは必須
- 過度な必須プロパティはコンポーネントの柔軟性を損なう可能性がある

## 関連技術
- TypeScript型チェック
- コンパイル時検証
- 非nullアサーション
- コンポーネントAPI設計
