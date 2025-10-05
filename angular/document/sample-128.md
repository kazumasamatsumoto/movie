# #128 「Component 境界の設計」

## 概要
Angular v20におけるコンポーネント境界の設計原則。明確な責任分離とインターフェース設計により、疎結合で保守性の高いコンポーネントアーキテクチャを構築し、チーム開発でも効率的な開発を実現する。

## 学習目標
- コンポーネント境界の設計原則を理解する
- 責任分離の重要性を学ぶ
- 適切な抽象化レベルを把握する

## 技術ポイント
- 単一責任の原則
- 疎結合設計
- 明確なInput/Outputインターフェース
- 適切な抽象化レベル

## 📺 画面表示用コード

### 明確な境界設計
```typescript
// ビジネスロジックの分離
@Injectable()
export class UserService {
  private _users = signal<User[]>([]);
  users = this._users.asReadonly();
  
  addUser(user: User) {
    this._users.update(users => [...users, user]);
  }
  
  removeUser(userId: number) {
    this._users.update(users => 
      users.filter(user => user.id !== userId)
    );
  }
}

// プレゼンテーション層
@Component({
  selector: 'app-user-list',
  template: `
    <div *ngFor="let user of users()">
      {{ user.name }}
      <button (click)="removeUser(user.id)">削除</button>
    </div>
  `
})
export class UserListComponent {
  private userService = inject(UserService);
  users = this.userService.users;
  
  removeUser(userId: number) {
    this.userService.removeUser(userId);
  }
}
```

### 明確なインターフェース設計
```typescript
interface UserCardConfig {
  user: User;
  showActions: boolean;
  theme: 'light' | 'dark';
}

@Component({
  selector: 'app-user-card',
  template: `
    <div [class]="'user-card ' + config.theme">
      <h3>{{ config.user.name }}</h3>
      <p>{{ config.user.email }}</p>
      <div *ngIf="config.showActions">
        <button (click)="editUser()">編集</button>
        <button (click)="deleteUser()">削除</button>
      </div>
    </div>
  `
})
export class UserCardComponent {
  @Input() config!: UserCardConfig;
  @Output() userEdit = new EventEmitter<User>();
  @Output() userDelete = new EventEmitter<User>();
  
  editUser() {
    this.userEdit.emit(this.config.user);
  }
  
  deleteUser() {
    this.userDelete.emit(this.config.user);
  }
}
```

## 実践的な活用例
- 大規模アプリケーションの設計
- チーム開発でのコンポーネント分割
- 再利用可能なUIライブラリ

## ベストプラクティス
- 単一責任の原則に従う
- 明確なインターフェースを定義する
- 適切な抽象化レベルを維持する
- テストしやすい設計を行う

## 注意点
- 過度な分割を避ける
- パフォーマンスを考慮する
- チームでの理解を深める

## 関連技術
- コンポーネント設計
- アーキテクチャパターン
- インターフェース設計
- ソフトウェア設計原則
