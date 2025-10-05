# #120 「Input/Output のよくあるエラー」

## 概要
Angular v20におけるInput/Outputの実装で発生する典型的なエラーとその解決方法。型安全性の向上により、多くのエラーがコンパイル時に検出され、実行時エラーを大幅に削減できる。

## 学習目標
- Input/Outputの典型的なエラーパターンを理解する
- エラーの原因と解決方法を学ぶ
- 型安全性を活用したエラー回避を把握する

## 技術ポイント
- 型不一致エラーの解決
- 未定義プロパティエラーの回避
- 循環参照エラーの解決
- コンパイル時エラー検出

## 📺 画面表示用コード

### 型安全性の実装
```typescript
// 型定義の明確化
interface UserData {
  id: number;
  name: string;
  email: string;
}

@Component({
  selector: 'app-user-card',
  template: `
    <div *ngIf="user">
      <h3>{{ user.name }}</h3>
      <p>{{ user.email }}</p>
      <button (click)="onEdit()">編集</button>
    </div>
  `
})
export class UserCardComponent {
  // 型を明確に定義
  @Input() user: UserData | null = null;
  @Output() userEdit = new EventEmitter<UserData>();

  onEdit() {
    if (this.user) {
      this.userEdit.emit(this.user);
    }
  }
}
```

### エラー回避のパターン
```typescript
@Component({
  template: `
    <app-user-card 
      [user]="selectedUser"
      (userEdit)="onUserEdit($event)">
    </app-user-card>
  `
})
export class UserListComponent {
  selectedUser: UserData | null = null;

  onUserEdit(user: UserData) {
    // 型安全性により、userの型が保証される
    console.log('編集対象:', user.name);
  }
}
```

### よくあるエラーの例
```typescript
// ❌ 型不一致エラー
@Input() user: string = '';  // 実際はオブジェクト

// ✅ 正しい型定義
@Input() user: UserData | null = null;

// ❌ 未定義プロパティアクセス
{{ user.name }}  // userがnullの場合エラー

// ✅ 安全なアクセス
{{ user?.name }}

// ❌ 循環参照
@Input() parent: ParentComponent;  // 循環依存

// ✅ 適切な設計
@Input() parentData: ParentData;
```

## 実践的な活用例
- 型安全なコンポーネント設計
- エラーハンドリングの実装
- デバッグ効率の向上

## ベストプラクティス
- 明確な型定義を使用する
- オプショナルチェーニングを活用する
- コンパイル時エラーを活用する
- 適切なエラーハンドリングを実装する

## 注意点
- 型定義を適切に行う
- null/undefinedチェックを忘れない
- 循環依存を避ける
- 本番環境でのエラーを考慮する

## 関連技術
- TypeScript型システム
- エラーハンドリング
- デバッグ手法
- コンパイル時検証
