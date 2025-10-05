# #179 「[ngClass] 条件付きクラス」

## 概要
Angular v20における[ngClass]での条件付きクラス適用。三項演算子や論理演算子を活用し、複雑な条件に基づいた柔軟なクラス制御を実現する方法を学ぶ。

## 学習目標
- 条件付きクラスの実装方法を理解する
- 複雑な条件の組み合わせを学ぶ
- 効率的なクラス制御を把握する

## 技術ポイント
- 三項演算子の活用
- 論理演算子の使用
- 複数条件の組み合わせ
- 動的なクラス適用

## 📺 画面表示用コード

### 条件付きクラスの実装
```typescript
@Component({
  selector: 'app-conditional-classes',
  template: `
    <div class="container">
      <h2>条件付きクラス制御</h2>
      
      <div class="form-section">
        <h3>フォームバリデーション</h3>
        <input type="email" 
               [(ngModel)]="email"
               [ngClass]="{
                 'form-input': true,
                 'valid': isValidEmail && email.length > 0,
                 'invalid': !isValidEmail && email.length > 0,
                 'required': email.length === 0,
                 'focused': isEmailFocused
               }"
               (focus)="isEmailFocused = true"
               (blur)="isEmailFocused = false"
               placeholder="メールアドレスを入力">
        
        <div class="validation-feedback" 
             [ngClass]="{
               'feedback': true,
               'success': isValidEmail && email.length > 0,
               'error': !isValidEmail && email.length > 0,
               'hidden': email.length === 0
             }">
          {{ getValidationMessage() }}
        </div>
      </div>
      
      <div class="user-profile">
        <h3>ユーザープロファイル</h3>
        <div class="profile-card" 
             [ngClass]="{
               'profile': true,
               'premium': user.isPremium,
               'verified': user.isVerified,
               'active': user.isActive,
               'suspended': !user.isActive,
               'new-user': user.joinDate > getRecentDate()
             }">
          
          <div class="profile-header">
            <h4>{{ user.name }}</h4>
            <div class="status-badges">
              <span class="badge" 
                    [ngClass]="user.isPremium ? 'premium' : 'standard'">
                {{ user.isPremium ? 'Premium' : 'Standard' }}
              </span>
              <span class="badge" 
                    [ngClass]="user.isVerified ? 'verified' : 'unverified'">
                {{ user.isVerified ? 'Verified' : 'Unverified' }}
              </span>
            </div>
          </div>
          
          <div class="profile-info">
            <p>メール: {{ user.email }}</p>
            <p>参加日: {{ user.joinDate | date }}</p>
            <p>ステータス: {{ user.isActive ? 'アクティブ' : '停止中' }}</p>
          </div>
        </div>
      </div>
      
      <div class="notification-system">
        <h3>通知システム</h3>
        <div class="notification" 
             *ngFor="let notification of notifications"
             [ngClass]="{
               'notification': true,
               'info': notification.type === 'info',
               'warning': notification.type === 'warning',
               'error': notification.type === 'error',
               'success': notification.type === 'success',
               'urgent': notification.priority === 'high',
               'read': notification.isRead,
               'unread': !notification.isRead
             }">
          
          <div class="notification-content">
            <h5>{{ notification.title }}</h5>
            <p>{{ notification.message }}</p>
            <span class="timestamp">{{ notification.timestamp | date:'short' }}</span>
          </div>
          
          <div class="notification-actions">
            <button [ngClass]="{
                     'btn': true,
                     'btn-sm': true,
                     'mark-read': !notification.isRead,
                     'mark-unread': notification.isRead
                   }"
                    (click)="toggleReadStatus(notification)">
              {{ notification.isRead ? '未読にする' : '既読にする' }}
            </button>
          </div>
        </div>
      </div>
      
      <div class="controls">
        <button (click)="toggleUserPremium()">
          {{ user.isPremium ? 'Premium解除' : 'Premium有効化' }}
        </button>
        <button (click)="toggleUserVerification()">
          {{ user.isVerified ? '認証解除' : '認証有効化' }}
        </button>
        <button (click)="toggleUserStatus()">
          {{ user.isActive ? 'ユーザー停止' : 'ユーザー有効化' }}
        </button>
        <button (click)="addNotification()">通知追加</button>
      </div>
    </div>
  `,
  styles: [`
    .container {
      padding: 20px;
      max-width: 800px;
      margin: 0 auto;
    }
    
    .form-input {
      width: 100%;
      padding: 12px;
      border: 2px solid #ddd;
      border-radius: 6px;
      font-size: 16px;
      transition: all 0.3s ease;
      margin-bottom: 10px;
    }
    
    .form-input.valid {
      border-color: #28a745;
      background-color: rgba(40, 167, 69, 0.1);
    }
    
    .form-input.invalid {
      border-color: #dc3545;
      background-color: rgba(220, 53, 69, 0.1);
    }
    
    .form-input.required {
      border-left: 4px solid #ffc107;
    }
    
    .form-input.focused {
      box-shadow: 0 0 0 3px rgba(0, 123, 255, 0.1);
      border-color: #007bff;
    }
    
    .validation-feedback {
      padding: 8px 12px;
      border-radius: 4px;
      margin-bottom: 15px;
      font-size: 14px;
      transition: all 0.3s ease;
    }
    
    .validation-feedback.success {
      background-color: #d4edda;
      color: #155724;
      border: 1px solid #c3e6cb;
    }
    
    .validation-feedback.error {
      background-color: #f8d7da;
      color: #721c24;
      border: 1px solid #f5c6cb;
    }
    
    .validation-feedback.hidden {
      opacity: 0;
      height: 0;
      padding: 0;
      margin: 0;
      overflow: hidden;
    }
    
    .profile {
      border: 2px solid #ddd;
      border-radius: 10px;
      padding: 20px;
      margin: 15px 0;
      transition: all 0.3s ease;
    }
    
    .profile.premium {
      border-color: #ffc107;
      background: linear-gradient(135deg, #ffc107 0%, #ff8c00 100%);
      color: white;
    }
    
    .profile.verified {
      border-left: 4px solid #28a745;
    }
    
    .profile.active {
      box-shadow: 0 4px 12px rgba(0, 123, 255, 0.2);
    }
    
    .profile.suspended {
      opacity: 0.6;
      background-color: #f8f9fa;
    }
    
    .profile.new-user {
      border-color: #17a2b8;
      background: linear-gradient(135deg, #17a2b8 0%, #138496 100%);
      color: white;
    }
    
    .badge {
      padding: 4px 8px;
      border-radius: 12px;
      font-size: 12px;
      font-weight: bold;
      margin: 0 5px;
    }
    
    .badge.premium {
      background: #ffc107;
      color: #333;
    }
    
    .badge.standard {
      background: #6c757d;
      color: white;
    }
    
    .badge.verified {
      background: #28a745;
      color: white;
    }
    
    .badge.unverified {
      background: #dc3545;
      color: white;
    }
    
    .notification {
      border: 1px solid #ddd;
      border-radius: 8px;
      padding: 15px;
      margin: 10px 0;
      transition: all 0.3s ease;
    }
    
    .notification.info {
      border-left: 4px solid #17a2b8;
      background-color: #d1ecf1;
    }
    
    .notification.warning {
      border-left: 4px solid #ffc107;
      background-color: #fff3cd;
    }
    
    .notification.error {
      border-left: 4px solid #dc3545;
      background-color: #f8d7da;
    }
    
    .notification.success {
      border-left: 4px solid #28a745;
      background-color: #d4edda;
    }
    
    .notification.urgent {
      border: 2px solid #dc3545;
      box-shadow: 0 2px 8px rgba(220, 53, 69, 0.3);
    }
    
    .notification.unread {
      font-weight: bold;
      background-color: #f8f9fa;
    }
    
    .notification.read {
      opacity: 0.7;
    }
    
    .btn {
      padding: 8px 16px;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      font-size: 14px;
      transition: all 0.3s ease;
    }
    
    .btn-sm {
      padding: 6px 12px;
      font-size: 12px;
    }
    
    .btn.mark-read {
      background: #28a745;
      color: white;
    }
    
    .btn.mark-unread {
      background: #6c757d;
      color: white;
    }
    
    .controls {
      margin-top: 20px;
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
    }
    
    .controls button {
      padding: 10px 15px;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      background: #007bff;
      color: white;
      transition: all 0.3s ease;
    }
    
    .controls button:hover {
      background: #0056b3;
    }
  `]
})
export class ConditionalClassesComponent {
  email = '';
  isEmailFocused = false;
  
  user = {
    name: '田中太郎',
    email: 'tanaka@example.com',
    isPremium: false,
    isVerified: true,
    isActive: true,
    joinDate: new Date('2024-01-15')
  };
  
  notifications = [
    {
      id: 1,
      title: '新機能のお知らせ',
      message: '新しい機能が追加されました',
      type: 'info',
      priority: 'normal',
      isRead: false,
      timestamp: new Date()
    },
    {
      id: 2,
      title: '重要な更新',
      message: 'システムメンテナンスが予定されています',
      type: 'warning',
      priority: 'high',
      isRead: true,
      timestamp: new Date(Date.now() - 3600000)
    }
  ];
  
  get isValidEmail() {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(this.email);
  }
  
  getValidationMessage() {
    if (this.email.length === 0) return '';
    return this.isValidEmail ? '有効なメールアドレスです' : '無効なメールアドレスです';
  }
  
  getRecentDate() {
    const date = new Date();
    date.setMonth(date.getMonth() - 1);
    return date;
  }
  
  toggleUserPremium() {
    this.user.isPremium = !this.user.isPremium;
  }
  
  toggleUserVerification() {
    this.user.isVerified = !this.user.isVerified;
  }
  
  toggleUserStatus() {
    this.user.isActive = !this.user.isActive;
  }
  
  toggleReadStatus(notification: any) {
    notification.isRead = !notification.isRead;
  }
  
  addNotification() {
    const types = ['info', 'warning', 'error', 'success'];
    const priorities = ['normal', 'high'];
    
    const newNotification = {
      id: this.notifications.length + 1,
      title: '新しい通知',
      message: 'これは新しく追加された通知です',
      type: types[Math.floor(Math.random() * types.length)],
      priority: priorities[Math.floor(Math.random() * priorities.length)],
      isRead: false,
      timestamp: new Date()
    };
    
    this.notifications.unshift(newNotification);
  }
}
```

## 実践的な活用例
- フォームバリデーション
- ユーザーステータス表示
- 通知システム

## ベストプラクティス
- 明確な条件設定
- 適切なクラス命名
- パフォーマンスの考慮

## 注意点
- 条件の複雑さ管理
- クラスの競合回避
- 可読性の維持

## 関連技術
- 条件付きスタイリング
- 複雑な条件管理
- 動的クラス制御
