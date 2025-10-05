# #025 「Component の複製と再利用」台本

四国めたん「Component の複製と再利用について解説します！」
ずんだもん「Componentを複製する時って何に注意すればいいの？」
四国めたん「コピー&ペーストではなく、再利用可能な設計を心がけることが重要です」
ずんだもん「どんな方法で再利用するの？」
四国めたん「Input/Output、コンテンツ投影、サービスの活用などがあります」
ずんだもん「複製のデメリットは？」
四国めたん「コードの重複、保守性の低下、バグの増加などの問題があります」

---

## 📺 画面表示用コード

// ❌ 悪い例：Componentの複製
```typescript
// user-card.component.ts
@Component({
  selector: 'app-user-card',
  standalone: true,
  template: `
    <div class="user-card">
      <h3>田中太郎</h3>
      <p>tanaka@example.com</p>
      <p>30歳</p>
    </div>
  `,
  styles: [`
    .user-card {
      border: 1px solid #ccc;
      padding: 15px;
      border-radius: 8px;
    }
  `]
})
export class UserCardComponent { }

// user-card-admin.component.ts（複製）
@Component({
  selector: 'app-user-card-admin',
  standalone: true,
  template: `
    <div class="user-card">
      <h3>佐藤花子</h3>
      <p>sato@example.com</p>
      <p>25歳</p>
    </div>
  `,
  styles: [`
    .user-card {
      border: 1px solid #ccc;
      padding: 15px;
      border-radius: 8px;
    }
  `]
})
export class UserCardAdminComponent { }
```

// ✅ 良い例：再利用可能なComponent
```typescript
// reusable-user-card.component.ts
@Component({
  selector: 'app-reusable-user-card',
  standalone: true,
  template: `
    <div class="user-card" [class.admin]="isAdmin">
      <div class="user-header">
        <h3>{{user.name}}</h3>
        <span *ngIf="isAdmin" class="admin-badge">管理者</span>
      </div>
      <div class="user-info">
        <p class="email">{{user.email}}</p>
        <p class="age">{{user.age}}歳</p>
        <p *ngIf="user.department" class="department">{{user.department}}</p>
      </div>
      <div class="user-actions" *ngIf="showActions">
        <button (click)="onEdit()" class="edit-btn">編集</button>
        <button (click)="onDelete()" class="delete-btn">削除</button>
      </div>
    </div>
  `,
  styles: [`
    .user-card {
      border: 1px solid #ccc;
      padding: 15px;
      border-radius: 8px;
      margin-bottom: 10px;
    }
    .user-card.admin {
      border-color: #007bff;
      background-color: #f8f9fa;
    }
    .user-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 10px;
    }
    .admin-badge {
      background-color: #007bff;
      color: white;
      padding: 2px 8px;
      border-radius: 12px;
      font-size: 12px;
    }
    .user-info p {
      margin: 5px 0;
    }
    .email {
      color: #666;
    }
    .age {
      color: #888;
    }
    .department {
      color: #28a745;
      font-weight: bold;
    }
    .user-actions {
      margin-top: 10px;
    }
    .edit-btn, .delete-btn {
      margin-right: 10px;
      padding: 4px 8px;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }
    .edit-btn {
      background-color: #28a745;
      color: white;
    }
    .delete-btn {
      background-color: #dc3545;
      color: white;
    }
  `]
})
export class ReusableUserCardComponent {
  @Input() user!: User;
  @Input() isAdmin = false;
  @Input() showActions = false;
  @Output() edit = new EventEmitter<User>();
  @Output() delete = new EventEmitter<User>();
  
  onEdit() {
    this.edit.emit(this.user);
  }
  
  onDelete() {
    this.delete.emit(this.user);
  }
}
```

// 再利用可能なComponentの使用例
```typescript
// user-list.component.ts
@Component({
  selector: 'app-user-list',
  standalone: true,
  imports: [ReusableUserCardComponent],
  template: `
    <div class="user-list">
      <h2>ユーザー一覧</h2>
      <app-reusable-user-card
        *ngFor="let user of users"
        [user]="user"
        [showActions]="true"
        (edit)="handleEdit($event)"
        (delete)="handleDelete($event)">
      </app-reusable-user-card>
    </div>
  `
})
export class UserListComponent {
  users: User[] = [
    { id: 1, name: '田中太郎', email: 'tanaka@example.com', age: 30, department: '開発部' },
    { id: 2, name: '佐藤花子', email: 'sato@example.com', age: 25, department: '営業部' }
  ];
  
  handleEdit(user: User) {
    console.log('編集:', user);
  }
  
  handleDelete(user: User) {
    this.users = this.users.filter(u => u.id !== user.id);
  }
}
```

// 管理者用の使用例
```typescript
// admin-user-list.component.ts
@Component({
  selector: 'app-admin-user-list',
  standalone: true,
  imports: [ReusableUserCardComponent],
  template: `
    <div class="admin-user-list">
      <h2>管理者用ユーザー一覧</h2>
      <app-reusable-user-card
        *ngFor="let user of adminUsers"
        [user]="user"
        [isAdmin]="user.role === 'admin'"
        [showActions]="true"
        (edit)="handleAdminEdit($event)"
        (delete)="handleAdminDelete($event)">
      </app-reusable-user-card>
    </div>
  `
})
export class AdminUserListComponent {
  adminUsers: User[] = [
    { id: 1, name: '管理者太郎', email: 'admin@example.com', age: 35, department: '管理部', role: 'admin' },
    { id: 2, name: '一般ユーザー', email: 'user@example.com', age: 28, department: '開発部', role: 'user' }
  ];
  
  handleAdminEdit(user: User) {
    console.log('管理者編集:', user);
  }
  
  handleAdminDelete(user: User) {
    console.log('管理者削除:', user);
  }
}
```

// コンテンツ投影を使った再利用
```typescript
// generic-card.component.ts
@Component({
  selector: 'app-generic-card',
  standalone: true,
  template: `
    <div class="generic-card" [class]="cardClass">
      <div class="card-header" *ngIf="title">
        <h3>{{title}}</h3>
        <button *ngIf="showClose" (click)="onClose()" class="close-btn">×</button>
      </div>
      <div class="card-body">
        <ng-content></ng-content>
      </div>
      <div class="card-footer" *ngIf="showFooter">
        <ng-content select="[slot=footer]"></ng-content>
      </div>
    </div>
  `,
  styles: [`
    .generic-card {
      border: 1px solid #ddd;
      border-radius: 8px;
      box-shadow: 0 2px 4px rgba(0,0,0,0.1);
      margin-bottom: 15px;
    }
    .card-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 15px;
      background-color: #f8f9fa;
      border-bottom: 1px solid #ddd;
    }
    .card-body {
      padding: 15px;
    }
    .card-footer {
      padding: 15px;
      background-color: #f8f9fa;
      border-top: 1px solid #ddd;
    }
    .close-btn {
      background: none;
      border: none;
      font-size: 20px;
      cursor: pointer;
    }
  `]
})
export class GenericCardComponent {
  @Input() title?: string;
  @Input() cardClass?: string;
  @Input() showClose = false;
  @Input() showFooter = false;
  @Output() close = new EventEmitter<void>();
  
  onClose() {
    this.close.emit();
  }
}
```

// 汎用カードの使用例
```typescript
// product-card.component.ts
@Component({
  selector: 'app-product-card',
  standalone: true,
  imports: [GenericCardComponent],
  template: `
    <app-generic-card title="商品情報" cardClass="product-card">
      <div class="product-info">
        <h4>{{product.name}}</h4>
        <p class="price">¥{{product.price | number}}</p>
        <p class="description">{{product.description}}</p>
      </div>
      <div slot="footer">
        <button (click)="addToCart()">カートに追加</button>
        <button (click)="viewDetails()">詳細を見る</button>
      </div>
    </app-generic-card>
  `,
  styles: [`
    .product-info h4 {
      color: #333;
      margin-bottom: 10px;
    }
    .price {
      font-size: 18px;
      font-weight: bold;
      color: #007bff;
    }
    .description {
      color: #666;
      margin-bottom: 15px;
    }
  `]
})
export class ProductCardComponent {
  @Input() product!: Product;
  @Output() addToCart = new EventEmitter<Product>();
  @Output() viewDetails = new EventEmitter<Product>();
  
  addToCart() {
    this.addToCart.emit(this.product);
  }
  
  viewDetails() {
    this.viewDetails.emit(this.product);
  }
}
```

// サービスの活用による再利用
```typescript
// data-display.component.ts
@Component({
  selector: 'app-data-display',
  standalone: true,
  template: `
    <div class="data-display">
      <h3>{{title}}</h3>
      <div *ngIf="isLoading" class="loading">
        読み込み中...
      </div>
      <div *ngIf="!isLoading && data" class="data-content">
        <ng-content></ng-content>
      </div>
      <div *ngIf="!isLoading && !data" class="no-data">
        データがありません
      </div>
    </div>
  `,
  styles: [`
    .data-display {
      border: 1px solid #ddd;
      border-radius: 8px;
      padding: 15px;
      margin-bottom: 15px;
    }
    .loading {
      text-align: center;
      color: #666;
    }
    .no-data {
      text-align: center;
      color: #999;
    }
  `]
})
export class DataDisplayComponent {
  @Input() title!: string;
  @Input() data: any;
  @Input() isLoading = false;
}
```

// 再利用のベストプラクティス
```typescript
@Component({
  selector: 'app-reuse-best-practices',
  standalone: true,
  template: `
    <div class="best-practices">
      <h2>再利用のベストプラクティス</h2>
      <div class="practice-item">
        <h3>1. 単一責任の原則</h3>
        <p>各Componentは一つの責任のみを持つ</p>
      </div>
      <div class="practice-item">
        <h3>2. 適切な抽象化</h3>
        <p>共通の機能を抽象化して再利用</p>
      </div>
      <div class="practice-item">
        <h3>3. 柔軟な設計</h3>
        <p>Input/Outputで柔軟性を確保</p>
      </div>
      <div class="practice-item">
        <h3>4. ドキュメント化</h3>
        <p>再利用方法をドキュメント化</p>
      </div>
    </div>
  `,
  styles: [`
    .best-practices {
      padding: 20px;
      max-width: 600px;
      margin: 0 auto;
    }
    .practice-item {
      margin-bottom: 15px;
      padding: 15px;
      border: 1px solid #28a745;
      border-radius: 8px;
      background-color: #d4edda;
    }
    .practice-item h3 {
      color: #155724;
      margin-top: 0;
    }
  `]
})
export class ReuseBestPracticesComponent {
  // 再利用のベストプラクティスを説明
}
```
