# #024 「Component のリファクタリング」台本

四国めたん「Component のリファクタリングについて学びましょう！」
ずんだもん「リファクタリングって何？」
四国めたん「外部の動作を変えずに、内部のコードを改善する作業です」
ずんだもん「どんな時にリファクタリングするの？」
四国めたん「コードの重複、複雑なロジック、保守性の向上が必要な時です」
ずんだもん「どんな方法があるの？」
四国めたん「メソッドの抽出、Componentの分割、命名の改善、構造の整理などがあります」

---

## 📺 画面表示用コード

// リファクタリング前のComponent（問題のあるコード）
```typescript
// ❌ リファクタリング前：複雑で長いComponent
@Component({
  selector: 'app-user-management',
  standalone: true,
  template: `
    <div>
      <h2>ユーザー管理</h2>
      <div>
        <input [(ngModel)]="name" placeholder="名前">
        <input [(ngModel)]="email" placeholder="メール">
        <input [(ngModel)]="age" placeholder="年齢">
        <button (click)="addUser()">追加</button>
      </div>
      <div>
        <h3>ユーザー一覧</h3>
        <div *ngFor="let user of users">
          <span>{{user.name}} - {{user.email}} - {{user.age}}歳</span>
          <button (click)="editUser(user)">編集</button>
          <button (click)="deleteUser(user)">削除</button>
        </div>
      </div>
      <div *ngIf="editingUser">
        <h3>ユーザー編集</h3>
        <input [(ngModel)]="editingUser.name">
        <input [(ngModel)]="editingUser.email">
        <input [(ngModel)]="editingUser.age">
        <button (click)="saveUser()">保存</button>
        <button (click)="cancelEdit()">キャンセル</button>
      </div>
    </div>
  `
})
export class UserManagementComponent {
  name = '';
  email = '';
  age = '';
  users: any[] = [];
  editingUser: any = null;
  
  addUser() {
    if (this.name && this.email && this.age) {
      this.users.push({
        id: Date.now(),
        name: this.name,
        email: this.email,
        age: parseInt(this.age)
      });
      this.name = '';
      this.email = '';
      this.age = '';
    }
  }
  
  editUser(user: any) {
    this.editingUser = { ...user };
  }
  
  deleteUser(user: any) {
    this.users = this.users.filter(u => u.id !== user.id);
  }
  
  saveUser() {
    const index = this.users.findIndex(u => u.id === this.editingUser.id);
    if (index !== -1) {
      this.users[index] = { ...this.editingUser };
    }
    this.editingUser = null;
  }
  
  cancelEdit() {
    this.editingUser = null;
  }
}
```

// リファクタリング後：Componentの分割
```typescript
// ✅ リファクタリング後：ユーザー追加フォーム
@Component({
  selector: 'app-user-form',
  standalone: true,
  imports: [FormsModule],
  template: `
    <form (ngSubmit)="onSubmit()" class="user-form">
      <div class="form-group">
        <label>名前:</label>
        <input [(ngModel)]="user.name" name="name" required>
      </div>
      <div class="form-group">
        <label>メール:</label>
        <input [(ngModel)]="user.email" name="email" type="email" required>
      </div>
      <div class="form-group">
        <label>年齢:</label>
        <input [(ngModel)]="user.age" name="age" type="number" required>
      </div>
      <button type="submit" [disabled]="!isValid()">
        {{isEditing ? '更新' : '追加'}}
      </button>
      <button type="button" (click)="onCancel()" *ngIf="isEditing">
        キャンセル
      </button>
    </form>
  `,
  styles: [`
    .user-form {
      padding: 20px;
      border: 1px solid #ddd;
      border-radius: 8px;
      margin-bottom: 20px;
    }
    .form-group {
      margin-bottom: 15px;
    }
    .form-group label {
      display: block;
      margin-bottom: 5px;
      font-weight: bold;
    }
    .form-group input {
      width: 100%;
      padding: 8px;
      border: 1px solid #ccc;
      border-radius: 4px;
    }
    button {
      margin-right: 10px;
      padding: 8px 16px;
    }
  `]
})
export class UserFormComponent {
  @Input() user: User = { id: 0, name: '', email: '', age: 0 };
  @Input() isEditing = false;
  @Output() userSubmit = new EventEmitter<User>();
  @Output() cancel = new EventEmitter<void>();
  
  onSubmit() {
    if (this.isValid()) {
      this.userSubmit.emit({ ...this.user });
      if (!this.isEditing) {
        this.resetForm();
      }
    }
  }
  
  onCancel() {
    this.cancel.emit();
  }
  
  private isValid(): boolean {
    return !!(this.user.name && this.user.email && this.user.age > 0);
  }
  
  private resetForm() {
    this.user = { id: 0, name: '', email: '', age: 0 };
  }
}
```

// ユーザー一覧Component
```typescript
@Component({
  selector: 'app-user-list',
  standalone: true,
  template: `
    <div class="user-list">
      <h3>ユーザー一覧</h3>
      <div *ngFor="let user of users" class="user-item">
        <div class="user-info">
          <span class="user-name">{{user.name}}</span>
          <span class="user-email">{{user.email}}</span>
          <span class="user-age">{{user.age}}歳</span>
        </div>
        <div class="user-actions">
          <button (click)="onEdit(user)" class="edit-btn">編集</button>
          <button (click)="onDelete(user)" class="delete-btn">削除</button>
        </div>
      </div>
    </div>
  `,
  styles: [`
    .user-list {
      margin-top: 20px;
    }
    .user-item {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 15px;
      border: 1px solid #ddd;
      border-radius: 8px;
      margin-bottom: 10px;
    }
    .user-info {
      display: flex;
      gap: 20px;
    }
    .user-name {
      font-weight: bold;
    }
    .user-email {
      color: #666;
    }
    .user-age {
      color: #888;
    }
    .user-actions {
      display: flex;
      gap: 10px;
    }
    .edit-btn {
      background-color: #007bff;
      color: white;
    }
    .delete-btn {
      background-color: #dc3545;
      color: white;
    }
  `]
})
export class UserListComponent {
  @Input() users: User[] = [];
  @Output() edit = new EventEmitter<User>();
  @Output() delete = new EventEmitter<User>();
  
  onEdit(user: User) {
    this.edit.emit(user);
  }
  
  onDelete(user: User) {
    this.delete.emit(user);
  }
}
```

// リファクタリング後のメインComponent
```typescript
// ✅ リファクタリング後：シンプルで責任が明確
@Component({
  selector: 'app-user-management-refactored',
  standalone: true,
  imports: [UserFormComponent, UserListComponent],
  template: `
    <div class="user-management">
      <h2>ユーザー管理</h2>
      <app-user-form
        [user]="editingUser"
        [isEditing]="isEditing"
        (userSubmit)="handleUserSubmit($event)"
        (cancel)="handleCancel()">
      </app-user-form>
      <app-user-list
        [users]="users"
        (edit)="handleEdit($event)"
        (delete)="handleDelete($event)">
      </app-user-list>
    </div>
  `,
  styles: [`
    .user-management {
      max-width: 800px;
      margin: 0 auto;
      padding: 20px;
    }
  `]
})
export class UserManagementRefactoredComponent {
  users: User[] = [];
  editingUser: User = { id: 0, name: '', email: '', age: 0 };
  isEditing = false;
  
  handleUserSubmit(user: User) {
    if (this.isEditing) {
      this.updateUser(user);
    } else {
      this.addUser(user);
    }
    this.resetEditing();
  }
  
  handleEdit(user: User) {
    this.editingUser = { ...user };
    this.isEditing = true;
  }
  
  handleDelete(user: User) {
    this.users = this.users.filter(u => u.id !== user.id);
  }
  
  handleCancel() {
    this.resetEditing();
  }
  
  private addUser(user: User) {
    const newUser = { ...user, id: Date.now() };
    this.users.push(newUser);
  }
  
  private updateUser(user: User) {
    const index = this.users.findIndex(u => u.id === user.id);
    if (index !== -1) {
      this.users[index] = { ...user };
    }
  }
  
  private resetEditing() {
    this.editingUser = { id: 0, name: '', email: '', age: 0 };
    this.isEditing = false;
  }
}
```

// 型定義の改善
```typescript
// リファクタリング：型定義の改善
interface User {
  id: number;
  name: string;
  email: string;
  age: number;
}

// リファクタリング：定数の抽出
const USER_FORM_LABELS = {
  NAME: '名前',
  EMAIL: 'メール',
  AGE: '年齢'
} as const;

const USER_ACTIONS = {
  ADD: '追加',
  EDIT: '編集',
  DELETE: '削除',
  SAVE: '保存',
  CANCEL: 'キャンセル'
} as const;
```

// リファクタリング：サービスの抽出
```typescript
@Injectable({
  providedIn: 'root'
})
export class UserService {
  private users: User[] = [];
  
  getUsers(): User[] {
    return [...this.users];
  }
  
  addUser(user: Omit<User, 'id'>): User {
    const newUser: User = {
      ...user,
      id: Date.now()
    };
    this.users.push(newUser);
    return newUser;
  }
  
  updateUser(user: User): User | null {
    const index = this.users.findIndex(u => u.id === user.id);
    if (index !== -1) {
      this.users[index] = { ...user };
      return this.users[index];
    }
    return null;
  }
  
  deleteUser(id: number): boolean {
    const index = this.users.findIndex(u => u.id === id);
    if (index !== -1) {
      this.users.splice(index, 1);
      return true;
    }
    return false;
  }
}
```

// リファクタリングのベストプラクティス
```typescript
@Component({
  selector: 'app-refactoring-best-practices',
  standalone: true,
  template: `
    <div class="best-practices">
      <h2>リファクタリングのベストプラクティス</h2>
      <div class="practice-item">
        <h3>1. 小さなステップで実行</h3>
        <p>一度に大きな変更をせず、小さなステップで実行</p>
      </div>
      <div class="practice-item">
        <h3>2. テストを書く</h3>
        <p>リファクタリング前にテストを書いて動作を保証</p>
      </div>
      <div class="practice-item">
        <h3>3. 単一責任の原則</h3>
        <p>各Componentは一つの責任のみを持つ</p>
      </div>
      <div class="practice-item">
        <h3>4. 命名の改善</h3>
        <p>意味のある名前を付けて可読性を向上</p>
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
export class RefactoringBestPracticesComponent {
  // リファクタリングのベストプラクティスを説明
}
```
