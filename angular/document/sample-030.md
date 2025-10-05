# #030 「Component 設計の基本原則」台本

四国めたん「Component 設計の基本原則について学びましょう！」
ずんだもん「設計の基本原則って何？」
四国めたん「高品質なComponentを作るための、設計時に守るべき重要な原則です」
ずんだもん「どんな原則があるの？」
四国めたん「単一責任の原則、開放閉鎖の原則、依存性逆転の原則、インターフェース分離の原則などがあります」
ずんだもん「なぜ重要なの？」
四国めたん「保守性、拡張性、テスタビリティ、再利用性の向上に繋がります」

---

## 📺 画面表示用コード

// 原則1: 単一責任の原則（Single Responsibility Principle）
```typescript
// ❌ 悪い例：複数の責任を持つComponent
@Component({
  selector: 'app-user-management',
  standalone: true,
  template: `
    <div>
      <h2>ユーザー管理</h2>
      <form (ngSubmit)="addUser()">
        <input [(ngModel)]="newUser.name" placeholder="名前">
        <input [(ngModel)]="newUser.email" placeholder="メール">
        <button type="submit">追加</button>
      </form>
      <div *ngFor="let user of users">
        <span>{{user.name}} - {{user.email}}</span>
        <button (click)="editUser(user)">編集</button>
        <button (click)="deleteUser(user)">削除</button>
      </div>
      <div *ngIf="selectedUser">
        <h3>ユーザー詳細</h3>
        <p>名前: {{selectedUser.name}}</p>
        <p>メール: {{selectedUser.email}}</p>
        <p>作成日: {{selectedUser.createdAt | date}}</p>
      </div>
    </div>
  `
})
export class UserManagementComponent {
  // ユーザー追加、一覧表示、詳細表示、編集、削除の複数責任
}

// ✅ 良い例：単一責任の原則に従ったComponent
@Component({
  selector: 'app-user-form',
  standalone: true,
  template: `
    <form (ngSubmit)="onSubmit()" class="user-form">
      <input [(ngModel)]="user.name" placeholder="名前" required>
      <input [(ngModel)]="user.email" placeholder="メール" required>
      <button type="submit">送信</button>
    </form>
  `
})
export class UserFormComponent {
  @Input() user: User = { id: 0, name: '', email: '', age: 0 };
  @Output() userSubmit = new EventEmitter<User>();
  
  onSubmit() {
    if (this.isValid()) {
      this.userSubmit.emit(this.user);
    }
  }
  
  private isValid(): boolean {
    return !!(this.user.name && this.user.email);
  }
}

@Component({
  selector: 'app-user-list',
  standalone: true,
  template: `
    <div class="user-list">
      <div *ngFor="let user of users" class="user-item">
        <span>{{user.name}} - {{user.email}}</span>
        <button (click)="onEdit(user)">編集</button>
        <button (click)="onDelete(user)">削除</button>
      </div>
    </div>
  `
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

// 原則2: 開放閉鎖の原則（Open-Closed Principle）
```typescript
// 基底となる抽象クラス
abstract class BaseNotificationComponent {
  abstract show(message: string): void;
  abstract hide(): void;
}

// 具体的な実装
@Component({
  selector: 'app-toast-notification',
  standalone: true,
  template: `
    <div class="toast" [class.show]="isVisible">
      <span>{{message}}</span>
      <button (click)="hide()">×</button>
    </div>
  `,
  styles: [`
    .toast {
      position: fixed;
      top: 20px;
      right: 20px;
      background-color: #333;
      color: white;
      padding: 15px;
      border-radius: 4px;
      opacity: 0;
      transition: opacity 0.3s;
    }
    .toast.show {
      opacity: 1;
    }
  `]
})
export class ToastNotificationComponent extends BaseNotificationComponent {
  message = '';
  isVisible = false;
  
  show(message: string): void {
    this.message = message;
    this.isVisible = true;
    setTimeout(() => this.hide(), 3000);
  }
  
  hide(): void {
    this.isVisible = false;
  }
}

// 新しい通知タイプの追加（既存コードを変更せずに拡張）
@Component({
  selector: 'app-modal-notification',
  standalone: true,
  template: `
    <div class="modal-overlay" *ngIf="isVisible" (click)="hide()">
      <div class="modal-content" (click)="$event.stopPropagation()">
        <h3>通知</h3>
        <p>{{message}}</p>
        <button (click)="hide()">閉じる</button>
      </div>
    </div>
  `,
  styles: [`
    .modal-overlay {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background-color: rgba(0,0,0,0.5);
      display: flex;
      justify-content: center;
      align-items: center;
    }
    .modal-content {
      background: white;
      padding: 20px;
      border-radius: 8px;
      max-width: 400px;
    }
  `]
})
export class ModalNotificationComponent extends BaseNotificationComponent {
  message = '';
  isVisible = false;
  
  show(message: string): void {
    this.message = message;
    this.isVisible = true;
  }
  
  hide(): void {
    this.isVisible = false;
  }
}
```

// 原則3: 依存性逆転の原則（Dependency Inversion Principle）
```typescript
// 抽象化されたインターフェース
interface UserRepository {
  getUsers(): Observable<User[]>;
  createUser(user: User): Observable<User>;
  updateUser(user: User): Observable<User>;
  deleteUser(id: number): Observable<void>;
}

// 具体的な実装
@Injectable()
export class ApiUserRepository implements UserRepository {
  constructor(private http: HttpClient) {}
  
  getUsers(): Observable<User[]> {
    return this.http.get<User[]>('/api/users');
  }
  
  createUser(user: User): Observable<User> {
    return this.http.post<User>('/api/users', user);
  }
  
  updateUser(user: User): Observable<User> {
    return this.http.put<User>(`/api/users/${user.id}`, user);
  }
  
  deleteUser(id: number): Observable<void> {
    return this.http.delete<void>(`/api/users/${id}`);
  }
}

// モック実装（テスト用）
@Injectable()
export class MockUserRepository implements UserRepository {
  private users: User[] = [
    { id: 1, name: 'テストユーザー1', email: 'test1@example.com', age: 25 },
    { id: 2, name: 'テストユーザー2', email: 'test2@example.com', age: 30 }
  ];
  
  getUsers(): Observable<User[]> {
    return of(this.users);
  }
  
  createUser(user: User): Observable<User> {
    const newUser = { ...user, id: Date.now() };
    this.users.push(newUser);
    return of(newUser);
  }
  
  updateUser(user: User): Observable<User> {
    const index = this.users.findIndex(u => u.id === user.id);
    if (index !== -1) {
      this.users[index] = user;
    }
    return of(user);
  }
  
  deleteUser(id: number): Observable<void> {
    this.users = this.users.filter(u => u.id !== id);
    return of(void 0);
  }
}

// 依存性逆転の原則に従ったComponent
@Component({
  selector: 'app-user-management',
  standalone: true,
  template: `
    <div class="user-management">
      <h2>ユーザー管理</h2>
      <app-user-form (userSubmit)="addUser($event)"></app-user-form>
      <app-user-list 
        [users]="users" 
        (edit)="editUser($event)"
        (delete)="deleteUser($event)">
      </app-user-list>
    </div>
  `
})
export class UserManagementComponent implements OnInit {
  users: User[] = [];
  
  constructor(
    @Inject('UserRepository') private userRepository: UserRepository
  ) {}
  
  ngOnInit() {
    this.loadUsers();
  }
  
  private loadUsers() {
    this.userRepository.getUsers().subscribe(users => {
      this.users = users;
    });
  }
  
  addUser(user: User) {
    this.userRepository.createUser(user).subscribe(newUser => {
      this.users.push(newUser);
    });
  }
  
  editUser(user: User) {
    this.userRepository.updateUser(user).subscribe(updatedUser => {
      const index = this.users.findIndex(u => u.id === updatedUser.id);
      if (index !== -1) {
        this.users[index] = updatedUser;
      }
    });
  }
  
  deleteUser(user: User) {
    this.userRepository.deleteUser(user.id).subscribe(() => {
      this.users = this.users.filter(u => u.id !== user.id);
    });
  }
}
```

// 原則4: インターフェース分離の原則（Interface Segregation Principle）
```typescript
// ❌ 悪い例：大きなインターフェース
interface UserOperations {
  createUser(user: User): Observable<User>;
  updateUser(user: User): Observable<User>;
  deleteUser(id: number): Observable<void>;
  getUser(id: number): Observable<User>;
  getUsers(): Observable<User[]>;
  validateUser(user: User): boolean;
  formatUser(user: User): string;
  exportUsers(): Observable<Blob>;
  importUsers(file: File): Observable<User[]>;
}

// ✅ 良い例：分離されたインターフェース
interface UserRepository {
  createUser(user: User): Observable<User>;
  updateUser(user: User): Observable<User>;
  deleteUser(id: number): Observable<void>;
  getUser(id: number): Observable<User>;
  getUsers(): Observable<User[]>;
}

interface UserValidator {
  validateUser(user: User): boolean;
  validateEmail(email: string): boolean;
  validateAge(age: number): boolean;
}

interface UserFormatter {
  formatUser(user: User): string;
  formatUserList(users: User[]): string;
}

interface UserExporter {
  exportUsers(): Observable<Blob>;
  exportUsersToCSV(): Observable<Blob>;
  exportUsersToJSON(): Observable<Blob>;
}

interface UserImporter {
  importUsers(file: File): Observable<User[]>;
  importUsersFromCSV(file: File): Observable<User[]>;
  importUsersFromJSON(file: File): Observable<User[]>;
}

// 分離されたインターフェースを使用するComponent
@Component({
  selector: 'app-user-management',
  standalone: true,
  template: `
    <div class="user-management">
      <h2>ユーザー管理</h2>
      <app-user-form (userSubmit)="addUser($event)"></app-user-form>
      <app-user-list 
        [users]="users" 
        (edit)="editUser($event)"
        (delete)="deleteUser($event)">
      </app-user-list>
    </div>
  `
})
export class UserManagementComponent implements OnInit {
  users: User[] = [];
  
  constructor(
    private userRepository: UserRepository,
    private userValidator: UserValidator,
    private userFormatter: UserFormatter
  ) {}
  
  ngOnInit() {
    this.loadUsers();
  }
  
  private loadUsers() {
    this.userRepository.getUsers().subscribe(users => {
      this.users = users;
    });
  }
  
  addUser(user: User) {
    if (this.userValidator.validateUser(user)) {
      this.userRepository.createUser(user).subscribe(newUser => {
        this.users.push(newUser);
        console.log('ユーザー追加:', this.userFormatter.formatUser(newUser));
      });
    } else {
      console.error('無効なユーザー情報です');
    }
  }
  
  editUser(user: User) {
    if (this.userValidator.validateUser(user)) {
      this.userRepository.updateUser(user).subscribe(updatedUser => {
        const index = this.users.findIndex(u => u.id === updatedUser.id);
        if (index !== -1) {
          this.users[index] = updatedUser;
        }
      });
    }
  }
  
  deleteUser(user: User) {
    this.userRepository.deleteUser(user.id).subscribe(() => {
      this.users = this.users.filter(u => u.id !== user.id);
    });
  }
}
```

// 設計原則のまとめ
```typescript
@Component({
  selector: 'app-design-principles-summary',
  standalone: true,
  template: `
    <div class="principles-summary">
      <h2>Component設計の基本原則</h2>
      <div class="principle-item">
        <h3>1. 単一責任の原則（SRP）</h3>
        <p>一つのComponentは一つの責任のみを持つ</p>
        <ul>
          <li>保守性の向上</li>
          <li>テスタビリティの向上</li>
          <li>再利用性の向上</li>
        </ul>
      </div>
      <div class="principle-item">
        <h3>2. 開放閉鎖の原則（OCP）</h3>
        <p>拡張に対して開いており、修正に対して閉じている</p>
        <ul>
          <li>新機能の追加が容易</li>
          <li>既存コードの安定性</li>
          <li>プラグインアーキテクチャの実現</li>
        </ul>
      </div>
      <div class="principle-item">
        <h3>3. 依存性逆転の原則（DIP）</h3>
        <p>抽象に依存し、具象に依存しない</p>
        <ul>
          <li>テスタビリティの向上</li>
          <li>柔軟性の向上</li>
          <li>疎結合の実現</li>
        </ul>
      </div>
      <div class="principle-item">
        <h3>4. インターフェース分離の原則（ISP）</h3>
        <p>クライアントは使用しないインターフェースに依存すべきでない</p>
        <ul>
          <li>不要な依存関係の排除</li>
          <li>インターフェースの明確化</li>
          <li>保守性の向上</li>
        </ul>
      </div>
    </div>
  `,
  styles: [`
    .principles-summary {
      padding: 20px;
      max-width: 800px;
      margin: 0 auto;
    }
    .principle-item {
      margin-bottom: 20px;
      padding: 15px;
      border: 1px solid #007bff;
      border-radius: 8px;
      background-color: #e7f3ff;
    }
    .principle-item h3 {
      color: #004085;
      margin-top: 0;
    }
    .principle-item ul {
      margin-bottom: 0;
    }
  `]
})
export class DesignPrinciplesSummaryComponent {
  // Component設計の基本原則を説明
}
```
