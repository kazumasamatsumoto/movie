# #173 「テーマの実装方法」

## 概要
Angular v20におけるテーマシステムの実装方法。CSS変数とクラスベースのアプローチを組み合わせ、効率的で保守性の高いテーマシステムを構築する方法を学ぶ。

## 学習目標
- テーマシステムの設計方法を理解する
- CSS変数を使ったテーマ実装を学ぶ
- 動的テーマ切り替えを把握する

## 技術ポイント
- CSS変数でのテーマ値定義
- クラスベースのテーマ切り替え
- テーマの構造設計
- 動的なテーマ変更

## 📺 画面表示用コード

### 基本的なテーマシステム
```typescript
@Component({
  selector: 'app-theme-system',
  template: `
    <div class="theme-controls">
      <button (click)="setTheme('light')" [class.active]="currentTheme === 'light'">
        ライトテーマ
      </button>
      <button (click)="setTheme('dark')" [class.active]="currentTheme === 'dark'">
        ダークテーマ
      </button>
      <button (click)="setTheme('colorful')" [class.active]="currentTheme === 'colorful'">
        カラフルテーマ
      </button>
    </div>
    
    <div class="theme-content">
      <h2>テーマシステム</h2>
      <div class="card">
        <h3>カードタイトル</h3>
        <p>テーマに応じてスタイルが変わります</p>
      </div>
      <div class="button-group">
        <button class="btn primary">プライマリボタン</button>
        <button class="btn secondary">セカンダリボタン</button>
      </div>
    </div>
  `,
  styles: [`
    :host {
      --primary-color: #007bff;
      --secondary-color: #6c757d;
      --background-color: #ffffff;
      --text-color: #333333;
      --border-color: #dee2e6;
      --shadow-color: rgba(0,0,0,0.1);
    }
    
    /* ライトテーマ */
    :host(.light-theme) {
      --primary-color: #007bff;
      --secondary-color: #6c757d;
      --background-color: #ffffff;
      --text-color: #333333;
      --border-color: #dee2e6;
      --shadow-color: rgba(0,0,0,0.1);
    }
    
    /* ダークテーマ */
    :host(.dark-theme) {
      --primary-color: #0d6efd;
      --secondary-color: #6c757d;
      --background-color: #212529;
      --text-color: #ffffff;
      --border-color: #495057;
      --shadow-color: rgba(255,255,255,0.1);
    }
    
    /* カラフルテーマ */
    :host(.colorful-theme) {
      --primary-color: #ff6b6b;
      --secondary-color: #4ecdc4;
      --background-color: #f8f9fa;
      --text-color: #2c3e50;
      --border-color: #ff6b6b;
      --shadow-color: rgba(255,107,107,0.2);
    }
    
    .theme-controls {
      display: flex;
      gap: 10px;
      margin-bottom: 20px;
    }
    
    .theme-controls button {
      padding: 10px 20px;
      border: 2px solid var(--primary-color);
      background: transparent;
      color: var(--primary-color);
      border-radius: 5px;
      cursor: pointer;
      transition: all 0.3s ease;
    }
    
    .theme-controls button.active {
      background: var(--primary-color);
      color: white;
    }
    
    .theme-content {
      background: var(--background-color);
      color: var(--text-color);
      padding: 20px;
      border-radius: 10px;
      box-shadow: 0 4px 6px var(--shadow-color);
      transition: all 0.3s ease;
    }
    
    .card {
      background: var(--background-color);
      border: 1px solid var(--border-color);
      padding: 20px;
      border-radius: 8px;
      margin: 15px 0;
    }
    
    .btn {
      padding: 12px 24px;
      border: none;
      border-radius: 6px;
      cursor: pointer;
      margin: 5px;
      transition: all 0.3s ease;
    }
    
    .btn.primary {
      background: var(--primary-color);
      color: white;
    }
    
    .btn.secondary {
      background: var(--secondary-color);
      color: white;
    }
  `]
})
export class ThemeSystemComponent {
  currentTheme = 'light';
  
  setTheme(theme: string) {
    this.currentTheme = theme;
    const hostElement = document.querySelector('app-theme-system');
    if (hostElement) {
      // 既存のテーマクラスを削除
      hostElement.classList.remove('light-theme', 'dark-theme', 'colorful-theme');
      // 新しいテーマクラスを追加
      hostElement.classList.add(`${theme}-theme`);
    }
  }
}
```

## 実践的な活用例
- アプリケーション全体のテーマ管理
- ユーザー設定によるテーマ切り替え
- ブランドカラーの動的適用

## ベストプラクティス
- 一貫したテーマ構造
- 適切な変数命名
- パフォーマンスの考慮

## 注意点
- テーマの一貫性
- アクセシビリティの考慮
- ブラウザサポート

## 関連技術
- CSS 変数
- テーマシステム
- 動的スタイリング
