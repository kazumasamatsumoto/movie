# #176 「[ngClass] 動的クラス制御」

## 概要
Angular v20における[ngClass]ディレクティブを使った動的クラス制御。条件に応じたクラス適用により、インタラクティブで状態に応じたスタイル制御を実現する方法を学ぶ。

## 学習目標
- [ngClass]の基本的な使い方を理解する
- 条件付きクラス適用を学ぶ
- 動的スタイル制御を把握する

## 技術ポイント
- [ngClass] ディレクティブの使用
- 条件付きクラス適用
- 動的なクラス制御
- 状態に応じたスタイル

## 📺 画面表示用コード

### 基本的な[ngClass]の使用
```typescript
@Component({
  selector: 'app-ngclass-basic',
  template: `
    <div class="container">
      <h2>動的クラス制御</h2>
      
      <div class="controls">
        <button (click)="toggleActive()" [ngClass]="{'btn': true, 'active': isActive}">
          {{ isActive ? 'アクティブ' : '非アクティブ' }}
        </button>
        
        <button (click)="toggleDisabled()" [ngClass]="{'btn': true, 'disabled': isDisabled}">
          {{ isDisabled ? '無効' : '有効' }}
        </button>
      </div>
      
      <div class="status-indicator" 
           [ngClass]="{
             'status': true,
             'success': status === 'success',
             'warning': status === 'warning',
             'error': status === 'error'
           }">
        {{ status | uppercase }}
      </div>
      
      <div class="theme-toggle">
        <button (click)="toggleTheme()" [ngClass]="'theme-btn ' + currentTheme">
          テーマ切り替え
        </button>
      </div>
    </div>
  `,
  styles: [`
    .container {
      padding: 20px;
      max-width: 600px;
      margin: 0 auto;
    }
    
    .btn {
      padding: 12px 24px;
      border: none;
      border-radius: 6px;
      cursor: pointer;
      margin: 5px;
      transition: all 0.3s ease;
      background: #6c757d;
      color: white;
    }
    
    .btn.active {
      background: #28a745;
      transform: scale(1.05);
      box-shadow: 0 4px 8px rgba(40, 167, 69, 0.3);
    }
    
    .btn.disabled {
      background: #dc3545;
      opacity: 0.6;
      cursor: not-allowed;
    }
    
    .status-indicator {
      padding: 15px;
      margin: 20px 0;
      border-radius: 8px;
      text-align: center;
      font-weight: bold;
      font-size: 18px;
      transition: all 0.3s ease;
    }
    
    .status.success {
      background: #d4edda;
      color: #155724;
      border: 1px solid #c3e6cb;
    }
    
    .status.warning {
      background: #fff3cd;
      color: #856404;
      border: 1px solid #ffeaa7;
    }
    
    .status.error {
      background: #f8d7da;
      color: #721c24;
      border: 1px solid #f5c6cb;
    }
    
    .theme-toggle {
      margin-top: 20px;
    }
    
    .theme-btn {
      padding: 15px 30px;
      border: none;
      border-radius: 8px;
      cursor: pointer;
      font-size: 16px;
      transition: all 0.3s ease;
    }
    
    .theme-btn.light {
      background: #ffffff;
      color: #333333;
      border: 2px solid #333333;
    }
    
    .theme-btn.dark {
      background: #333333;
      color: #ffffff;
      border: 2px solid #ffffff;
    }
  `]
})
export class NgClassBasicComponent {
  isActive = false;
  isDisabled = false;
  status = 'success';
  currentTheme = 'light';
  
  toggleActive() {
    this.isActive = !this.isActive;
  }
  
  toggleDisabled() {
    this.isDisabled = !this.isDisabled;
  }
  
  toggleTheme() {
    this.currentTheme = this.currentTheme === 'light' ? 'dark' : 'light';
  }
}
```

## 実践的な活用例
- ボタンの状態管理
- ステータス表示
- テーマ切り替え

## ベストプラクティス
- 明確な条件設定
- 適切なクラス命名
- パフォーマンスの考慮

## 注意点
- 条件の複雑さ管理
- クラスの競合回避
- 可読性の維持

## 関連技術
- 動的クラス制御
- 条件付きスタイリング
- 状態管理
