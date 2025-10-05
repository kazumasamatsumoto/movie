# #174 「ダークモード対応」

## 概要
Angular v20におけるダークモード対応の実装方法。prefers-color-schemeメディアクエリとCSS変数を活用し、システム設定に応じた自動的なテーマ切り替えを実現する。

## 学習目標
- ダークモードの実装方法を理解する
- メディアクエリの活用を学ぶ
- 自動的なテーマ切り替えを把握する

## 技術ポイント
- prefers-color-scheme メディアクエリ
- CSS変数でのテーマ定義
- 自動的なテーマ検知
- 手動切り替えとの組み合わせ

## 📺 画面表示用コード

### 自動ダークモード対応
```typescript
@Component({
  selector: 'app-dark-mode',
  template: `
    <div class="theme-toggle">
      <button (click)="toggleManualMode()">
        {{ isManualMode ? '自動モード' : '手動モード' }}
      </button>
      <button *ngIf="isManualMode" (click)="toggleDarkMode()">
        {{ isDarkMode ? 'ライトモード' : 'ダークモード' }}
      </button>
    </div>
    
    <div class="content">
      <h2>ダークモード対応</h2>
      <div class="card">
        <h3>カードタイトル</h3>
        <p>システム設定または手動でテーマが切り替わります</p>
        <div class="feature-list">
          <div class="feature-item">自動検知機能</div>
          <div class="feature-item">手動切り替え機能</div>
          <div class="feature-item">スムーズなトランジション</div>
        </div>
      </div>
    </div>
  `,
  styles: [`
    :host {
      --bg-primary: #ffffff;
      --bg-secondary: #f8f9fa;
      --text-primary: #333333;
      --text-secondary: #666666;
      --border-color: #dee2e6;
      --shadow: rgba(0,0,0,0.1);
      --accent-color: #007bff;
    }
    
    /* システムのダークモード設定を検知 */
    @media (prefers-color-scheme: dark) {
      :host {
        --bg-primary: #1a1a1a;
        --bg-secondary: #2d2d2d;
        --text-primary: #ffffff;
        --text-secondary: #cccccc;
        --border-color: #404040;
        --shadow: rgba(0,0,0,0.3);
        --accent-color: #0d6efd;
      }
    }
    
    /* 手動ダークモード */
    :host(.dark-mode) {
      --bg-primary: #1a1a1a;
      --bg-secondary: #2d2d2d;
      --text-primary: #ffffff;
      --text-secondary: #cccccc;
      --border-color: #404040;
      --shadow: rgba(0,0,0,0.3);
      --accent-color: #0d6efd;
    }
    
    .theme-toggle {
      display: flex;
      gap: 10px;
      margin-bottom: 20px;
      padding: 15px;
      background: var(--bg-secondary);
      border-radius: 8px;
    }
    
    .theme-toggle button {
      padding: 10px 20px;
      border: 1px solid var(--accent-color);
      background: transparent;
      color: var(--accent-color);
      border-radius: 5px;
      cursor: pointer;
      transition: all 0.3s ease;
    }
    
    .theme-toggle button:hover {
      background: var(--accent-color);
      color: var(--bg-primary);
    }
    
    .content {
      background: var(--bg-primary);
      color: var(--text-primary);
      padding: 20px;
      border-radius: 10px;
      box-shadow: 0 4px 6px var(--shadow);
      transition: all 0.3s ease;
    }
    
    .card {
      background: var(--bg-secondary);
      border: 1px solid var(--border-color);
      padding: 20px;
      border-radius: 8px;
      margin-top: 15px;
    }
    
    .feature-list {
      margin-top: 15px;
    }
    
    .feature-item {
      background: var(--bg-primary);
      border: 1px solid var(--border-color);
      padding: 10px;
      margin: 5px 0;
      border-radius: 4px;
      color: var(--text-secondary);
    }
  `]
})
export class DarkModeComponent implements OnInit {
  isDarkMode = false;
  isManualMode = false;
  
  ngOnInit() {
    // システムの設定を確認
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    this.isDarkMode = prefersDark;
    
    // システム設定の変更を監視
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
      if (!this.isManualMode) {
        this.isDarkMode = e.matches;
      }
    });
  }
  
  toggleManualMode() {
    this.isManualMode = !this.isManualMode;
    if (!this.isManualMode) {
      // 自動モードに戻す
      const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
      this.isDarkMode = prefersDark;
      this.applyDarkMode();
    }
  }
  
  toggleDarkMode() {
    if (this.isManualMode) {
      this.isDarkMode = !this.isDarkMode;
      this.applyDarkMode();
    }
  }
  
  private applyDarkMode() {
    const hostElement = document.querySelector('app-dark-mode');
    if (hostElement) {
      hostElement.classList.toggle('dark-mode', this.isDarkMode);
    }
  }
}
```

## 実践的な活用例
- システム設定に応じた自動テーマ切り替え
- ユーザー設定による手動切り替え
- アクセシビリティの向上

## ベストプラクティス
- システム設定の尊重
- 手動切り替えの提供
- スムーズなトランジション

## 注意点
- ブラウザサポートの確認
- パフォーマンスの考慮
- ユーザーエクスペリエンス

## 関連技術
- CSS メディアクエリ
- システム設定検知
- テーマシステム
