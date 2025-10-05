# #091 「@Input() - 親から子へデータを渡す」

## 概要
Angular v20における@Input()デコレータの基本概念を学びます。親コンポーネントから子コンポーネントへのデータ渡しの仕組みと、単方向データフローの重要性について解説します。

## 学習目標
- @Input()デコレータの基本的な使用方法を理解する
- 親から子へのデータ渡しの仕組みを把握する
- 単方向データフローの重要性を理解する

## 📺 画面表示用コード

```typescript
// 子コンポーネント
@Component({
  selector: 'app-child',
  standalone: true,
  template: `
    <h2>{{title}}</h2>
    <p>{{message}}</p>
  `
})
export class ChildComponent {
  @Input() title: string = '';
  @Input() message: string = '';
}
```

```html
<!-- 親コンポーネント -->
<app-child 
  [title]="'こんにちは'"
  [message]="'Angular v20です'">
</app-child>
```

```typescript
// 親コンポーネント
@Component({
  selector: 'app-parent',
  standalone: true,
  imports: [ChildComponent],
  template: `
    <app-child 
      [title]="pageTitle"
      [message]="pageMessage">
    </app-child>
  `
})
export class ParentComponent {
  pageTitle = 'ウェルカムページ';
  pageMessage = 'Angular v20へようこそ';
}
```

## 技術ポイント

### 1. @Input()デコレータの基本
@Input()デコレータは、親コンポーネントから子コンポーネントにデータを渡すためのAngularの機能です。これにより、コンポーネント間の単方向データフローを実現できます。

### 2. 基本的な構文
```typescript
@Input() propertyName: Type = defaultValue;
```
- `propertyName`: プロパティ名
- `Type`: TypeScriptの型
- `defaultValue`: デフォルト値（オプション）

### 3. 親コンポーネントでの使用方法
```html
<child-component [propertyName]="value"></child-component>
```
角括弧`[]`を使用してプロパティバインディングを行います。

## 実践的な活用例

### 1. 基本的なデータ渡し
```typescript
// user-card.component.ts
@Component({
  selector: 'app-user-card',
  standalone: true,
  template: `
    <div class="user-card">
      <img [src]="avatarUrl" [alt]="name">
      <h3>{{name}}</h3>
      <p>{{email}}</p>
      <span class="role">{{role}}</span>
    </div>
  `
})
export class UserCardComponent {
  @Input() name: string = '';
  @Input() email: string = '';
  @Input() avatarUrl: string = '';
  @Input() role: string = 'user';
}
```

```typescript
// user-list.component.ts
@Component({
  selector: 'app-user-list',
  standalone: true,
  imports: [UserCardComponent],
  template: `
    <div class="user-list">
      <app-user-card
        *ngFor="let user of users"
        [name]="user.name"
        [email]="user.email"
        [avatarUrl]="user.avatarUrl"
        [role]="user.role">
      </app-user-card>
    </div>
  `
})
export class UserListComponent {
  users = [
    { name: '田中太郎', email: 'tanaka@example.com', avatarUrl: '/avatar1.jpg', role: 'admin' },
    { name: '佐藤花子', email: 'sato@example.com', avatarUrl: '/avatar2.jpg', role: 'user' }
  ];
}
```

### 2. オブジェクトの受け渡し
```typescript
// product-card.component.ts
@Component({
  selector: 'app-product-card',
  standalone: true,
  template: `
    <div class="product-card">
      <h3>{{product.name}}</h3>
      <p class="price">{{product.price | currency:'JPY'}}</p>
      <p>{{product.description}}</p>
      <button [disabled]="!product.inStock">購入</button>
    </div>
  `
})
export class ProductCardComponent {
  @Input() product: Product = {
    id: 0,
    name: '',
    price: 0,
    description: '',
    inStock: false
  };
}
```

### 3. 条件付きの表示
```typescript
// notification.component.ts
@Component({
  selector: 'app-notification',
  standalone: true,
  template: `
    <div *ngIf="show" class="notification" [class]="type">
      <span>{{message}}</span>
      <button (click)="dismiss()">×</button>
    </div>
  `
})
export class NotificationComponent {
  @Input() message: string = '';
  @Input() type: 'success' | 'error' | 'warning' | 'info' = 'info';
  @Input() show: boolean = false;
  
  dismiss() {
    this.show = false;
  }
}
```

## ベストプラクティス

1. **型安全性**: 適切な型定義を使用する
2. **デフォルト値**: 適切なデフォルト値を設定する
3. **不変性**: 可能な限り不変なデータを渡す
4. **単方向フロー**: 親から子への単方向データフローを維持する

## 注意点

- 子コンポーネントで@Input()プロパティを変更しても親に影響しない（プリミティブ型の場合）
- オブジェクトや配列は参照渡しなので、子で変更すると親にも影響する
- 適切な型定義により、コンパイル時にエラーを検出できる

## 関連技術
- プロパティバインディング
- 単方向データフロー
- コンポーネント通信
- TypeScript型定義
