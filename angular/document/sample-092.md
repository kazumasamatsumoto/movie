# #092 「@Input() の基本構文」

## 概要
Angular v20における@Input()デコレータの基本構文を学びます。型指定、デフォルト値の設定、エイリアスの使用方法など、@Input()の詳細な使用方法について解説します。

## 学習目標
- @Input()の基本構文を理解する
- 型指定とデフォルト値の設定方法を習得する
- エイリアス指定の使用方法を身につける

## 📺 画面表示用コード

```typescript
// 基本的な@Input()の定義
@Component({
  selector: 'app-example',
  standalone: true,
  template: `<p>{{value}}</p>`
})
export class ExampleComponent {
  @Input() value: string = 'デフォルト値';
  @Input() count: number = 0;
  @Input() isActive: boolean = false;
}
```

```typescript
// 型指定付きの@Input()
export class TypedInputComponent {
  @Input() name: string;
  @Input() age: number;
  @Input() email: string;
  @Input() isVerified: boolean = false;
}
```

```typescript
// エイリアス指定
export class AliasInputComponent {
  @Input('external-name') internalName: string = '';
  @Input('user-data') userData: User = {};
}
```

## 技術ポイント

### 1. 基本的な構文パターン
```typescript
// パターン1: 型のみ指定
@Input() propertyName: Type;

// パターン2: デフォルト値付き
@Input() propertyName: Type = defaultValue;

// パターン3: エイリアス指定
@Input('alias-name') propertyName: Type;
```

### 2. 型指定の重要性
- **型安全性**: TypeScriptの型チェックを活用
- **IDE支援**: 自動補完やエラー検出
- **ドキュメント効果**: コードの意図が明確になる

### 3. デフォルト値の設定
- **フォールバック**: 親から値が渡されない場合の安全策
- **オプショナル**: 必須でないプロパティの適切な処理
- **初期化**: コンポーネントの初期状態の設定

## 実践的な活用例

### 1. 基本的な型指定
```typescript
// button.component.ts
@Component({
  selector: 'app-button',
  standalone: true,
  template: `
    <button 
      [type]="buttonType"
      [disabled]="disabled"
      [class]="buttonClass">
      {{label}}
    </button>
  `
})
export class ButtonComponent {
  @Input() label: string = 'ボタン';
  @Input() buttonType: 'button' | 'submit' | 'reset' = 'button';
  @Input() disabled: boolean = false;
  @Input() variant: 'primary' | 'secondary' | 'danger' = 'primary';
  
  get buttonClass(): string {
    return `btn btn-${this.variant}`;
  }
}
```

### 2. 複雑なオブジェクトの型指定
```typescript
// user-profile.component.ts
interface UserProfile {
  id: number;
  name: string;
  email: string;
  avatar?: string;
  role: 'admin' | 'user' | 'guest';
  lastLogin?: Date;
}

@Component({
  selector: 'app-user-profile',
  standalone: true,
  template: `
    <div class="user-profile">
      <img *ngIf="profile.avatar" [src]="profile.avatar" [alt]="profile.name">
      <h2>{{profile.name}}</h2>
      <p>{{profile.email}}</p>
      <span class="role-badge">{{profile.role}}</span>
      <p *ngIf="profile.lastLogin">
        最終ログイン: {{profile.lastLogin | date}}
      </p>
    </div>
  `
})
export class UserProfileComponent {
  @Input() profile: UserProfile = {
    id: 0,
    name: 'ゲストユーザー',
    email: '',
    role: 'guest'
  };
}
```

### 3. エイリアス指定の活用
```typescript
// data-table.component.ts
@Component({
  selector: 'app-data-table',
  standalone: true,
  template: `
    <table>
      <thead>
        <tr>
          <th *ngFor="let column of columns">{{column.title}}</th>
        </tr>
      </thead>
      <tbody>
        <tr *ngFor="let row of data">
          <td *ngFor="let column of columns">
            {{row[column.key]}}
          </td>
        </tr>
      </tbody>
    </table>
  `
})
export class DataTableComponent {
  // エイリアスを使用してAPIの一貫性を保持
  @Input('table-data') data: any[] = [];
  @Input('table-columns') columns: TableColumn[] = [];
  @Input('table-config') config: TableConfig = {
    sortable: true,
    filterable: false,
    pageSize: 10
  };
}
```

### 4. 条件付きデフォルト値
```typescript
// modal.component.ts
@Component({
  selector: 'app-modal',
  standalone: true,
  template: `
    <div *ngIf="isOpen" class="modal-overlay" (click)="close()">
      <div class="modal-content" (click)="$event.stopPropagation()">
        <h2>{{title}}</h2>
        <div class="modal-body">
          <ng-content></ng-content>
        </div>
        <div class="modal-footer">
          <button (click)="close()">{{closeButtonText}}</button>
        </div>
      </div>
    </div>
  `
})
export class ModalComponent {
  @Input() isOpen: boolean = false;
  @Input() title: string = 'モーダル';
  @Input() closeButtonText: string = '閉じる';
  @Input() closable: boolean = true;
  
  close() {
    if (this.closable) {
      this.isOpen = false;
    }
  }
}
```

## ベストプラクティス

1. **明確な型定義**: 適切な型を指定して型安全性を確保
2. **意味のあるデフォルト値**: 適切なデフォルト値を設定
3. **一貫した命名**: プロパティ名の一貫性を保つ
4. **エイリアスの活用**: 必要に応じてエイリアスを使用

## 注意点

- 型定義を省略すると`any`型になり、型安全性が失われる
- デフォルト値は実行時のフォールバックであり、コンパイル時のチェックではない
- エイリアスは外部APIと内部実装の分離に使用する

## 関連技術
- TypeScript型定義
- プロパティバインディング
- デフォルト値
- エイリアス指定
