# #028 「Component のコメント規約」台本

四国めたん「Component のコメント規約について学びましょう！」
ずんだもん「コメント規約って何？」
四国めたん「コードの可読性と保守性を向上させるための、コメントの書き方のルールです」
ずんだもん「どんなコメントを書くの？」
四国めたん「JSDoc、インラインコメント、TODOコメント、説明コメントなどがあります」
ずんだもん「なぜ重要なの？」
四国めたん「チーム開発での理解促進、将来の自分への説明、コードの意図を明確にします」

---

## 📺 画面表示用コード

// JSDocコメントの例
```typescript
/**
 * ユーザー管理を行うComponent
 * 
 * このComponentはユーザーの一覧表示、追加、編集、削除機能を提供します。
 * 管理者権限に応じて表示内容が変わります。
 * 
 * @example
 * ```html
 * <app-user-management 
 *   [isAdmin]="true"
 *   (userAdded)="onUserAdded($event)">
 * </app-user-management>
 * ```
 * 
 * @since 1.0.0
 * @version 2.1.0
 * @author 開発チーム
 */
@Component({
  selector: 'app-user-management',
  standalone: true,
  template: `
    <div class="user-management">
      <h2>ユーザー管理</h2>
      <div class="user-form">
        <input [(ngModel)]="newUser.name" placeholder="名前">
        <input [(ngModel)]="newUser.email" placeholder="メール">
        <button (click)="addUser()">追加</button>
      </div>
      <div class="user-list">
        <div *ngFor="let user of users" class="user-item">
          <span>{{user.name}} - {{user.email}}</span>
          <button (click)="editUser(user)">編集</button>
          <button (click)="deleteUser(user)">削除</button>
        </div>
      </div>
    </div>
  `,
  styles: [`
    .user-management {
      padding: 20px;
      max-width: 800px;
      margin: 0 auto;
    }
    .user-form {
      margin-bottom: 20px;
      padding: 15px;
      border: 1px solid #ddd;
      border-radius: 8px;
    }
    .user-form input {
      margin-right: 10px;
      padding: 8px;
    }
    .user-item {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 10px;
      border: 1px solid #eee;
      margin-bottom: 5px;
    }
  `]
})
export class UserManagementComponent {
  /**
   * 管理者権限フラグ
   * trueの場合、すべてのユーザー操作が可能
   * falseの場合、読み取り専用モード
   */
  @Input() isAdmin = false;
  
  /**
   * ユーザー追加時のイベント
   * 新しく追加されたユーザー情報を親Componentに通知
   */
  @Output() userAdded = new EventEmitter<User>();
  
  /**
   * 新規ユーザー情報
   * フォームで入力される一時的なデータ
   */
  newUser: Partial<User> = {};
  
  /**
   * ユーザー一覧
   * 表示対象のユーザー情報を保持
   */
  users: User[] = [];
  
  /**
   * ユーザーを追加する
   * 
   * フォームの入力値を検証し、有効な場合のみユーザーを追加します。
   * 管理者権限がない場合は追加処理を実行しません。
   * 
   * @returns {void}
   * @throws {Error} 管理者権限がない場合
   */
  addUser(): void {
    // 管理者権限のチェック
    if (!this.isAdmin) {
      console.warn('管理者権限が必要です');
      return;
    }
    
    // 入力値の検証
    if (!this.isValidUser(this.newUser)) {
      console.error('無効なユーザー情報です');
      return;
    }
    
    // ユーザー追加処理
    const user: User = {
      id: this.generateUserId(),
      name: this.newUser.name!,
      email: this.newUser.email!,
      age: this.newUser.age || 0
    };
    
    this.users.push(user);
    this.userAdded.emit(user);
    
    // フォームのリセット
    this.resetForm();
  }
  
  /**
   * ユーザーを編集する
   * 
   * @param {User} user - 編集対象のユーザー
   * @returns {void}
   */
  editUser(user: User): void {
    // TODO: 編集機能の実装
    console.log('編集機能は未実装です:', user);
  }
  
  /**
   * ユーザーを削除する
   * 
   * @param {User} user - 削除対象のユーザー
   * @returns {void}
   */
  deleteUser(user: User): void {
    // 管理者権限のチェック
    if (!this.isAdmin) {
      console.warn('管理者権限が必要です');
      return;
    }
    
    // 削除確認
    if (confirm(`${user.name}を削除しますか？`)) {
      this.users = this.users.filter(u => u.id !== user.id);
    }
  }
  
  /**
   * ユーザー情報の妥当性を検証する
   * 
   * @private
   * @param {Partial<User>} user - 検証対象のユーザー情報
   * @returns {boolean} 妥当性の結果
   */
  private isValidUser(user: Partial<User>): boolean {
    return !!(user.name && user.email);
  }
  
  /**
   * 新しいユーザーIDを生成する
   * 
   * @private
   * @returns {number} 生成されたユーザーID
   */
  private generateUserId(): number {
    // 現在の最大ID + 1を返す
    const maxId = Math.max(...this.users.map(u => u.id), 0);
    return maxId + 1;
  }
  
  /**
   * フォームをリセットする
   * 
   * @private
   * @returns {void}
   */
  private resetForm(): void {
    this.newUser = {};
  }
}
```

// インラインコメントの例
```typescript
@Component({
  selector: 'app-comment-examples',
  standalone: true,
  template: `
    <div class="comment-examples">
      <h2>コメント例</h2>
      <div class="example-section">
        <h3>計算処理の例</h3>
        <p>結果: {{calculateResult()}}</p>
      </div>
    </div>
  `
})
export class CommentExamplesComponent {
  private data: number[] = [1, 2, 3, 4, 5];
  
  /**
   * データの平均値を計算する
   * 
   * @returns {number} 計算結果の平均値
   */
  calculateResult(): number {
    // データが空の場合は0を返す
    if (this.data.length === 0) {
      return 0;
    }
    
    // 合計値を計算
    const sum = this.data.reduce((acc, value) => acc + value, 0);
    
    // 平均値を計算して返す
    // 小数点以下2桁で四捨五入
    return Math.round((sum / this.data.length) * 100) / 100;
  }
  
  /**
   * 複雑な条件分岐の例
   */
  processUser(user: User): string {
    // 管理者の場合は特別な処理
    if (user.role === 'admin') {
      return '管理者権限で処理しました';
    }
    
    // 一般ユーザーの場合
    if (user.role === 'user') {
      // 年齢による分岐処理
      if (user.age >= 18) {
        return '成人ユーザーとして処理しました';
      } else {
        return '未成年ユーザーとして処理しました';
      }
    }
    
    // その他の場合（デフォルト）
    return '不明なユーザータイプです';
  }
}
```

// TODOコメントの例
```typescript
@Component({
  selector: 'app-todo-comments',
  standalone: true,
  template: `
    <div class="todo-examples">
      <h2>TODOコメント例</h2>
      <button (click)="processData()">データ処理</button>
    </div>
  `
})
export class TodoCommentsComponent {
  /**
   * データ処理メソッド
   * 
   * TODO: エラーハンドリングを追加する
   * TODO: ローディング状態の表示を実装する
   * TODO: キャンセル機能を追加する
   */
  processData(): void {
    // FIXME: この処理は非効率なので最適化が必要
    const result = this.expensiveCalculation();
    
    // HACK: 一時的な解決策、本来は別の方法で実装すべき
    setTimeout(() => {
      console.log('処理完了:', result);
    }, 1000);
  }
  
  /**
   * 高コストな計算処理
   * 
   * @private
   * @returns {number} 計算結果
   */
  private expensiveCalculation(): number {
    // NOTE: この計算はO(n²)の複雑度を持つ
    // 大量のデータではパフォーマンス問題が発生する可能性がある
    let result = 0;
    for (let i = 0; i < 1000; i++) {
      for (let j = 0; j < 1000; j++) {
        result += i * j;
      }
    }
    return result;
  }
}
```

// コメント規約のベストプラクティス
```typescript
@Component({
  selector: 'app-comment-best-practices',
  standalone: true,
  template: `
    <div class="best-practices">
      <h2>コメント規約のベストプラクティス</h2>
      <div class="practice-item">
        <h3>1. 目的を明確にする</h3>
        <p>なぜそのコードが必要なのかを説明</p>
      </div>
      <div class="practice-item">
        <h3>2. 簡潔で分かりやすく</h3>
        <p>冗長な説明は避け、要点を簡潔に</p>
      </div>
      <div class="practice-item">
        <h3>3. 定期的な見直し</h3>
        <p>コードの変更に合わせてコメントも更新</p>
      </div>
      <div class="practice-item">
        <h3>4. 統一された形式</h3>
        <p>チームでコメントの形式を統一</p>
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
      border: 1px solid #007bff;
      border-radius: 8px;
      background-color: #e7f3ff;
    }
    .practice-item h3 {
      color: #004085;
      margin-top: 0;
    }
  `]
})
export class CommentBestPracticesComponent {
  // コメント規約のベストプラクティスを説明
}
```
