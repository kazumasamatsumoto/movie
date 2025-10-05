# #178 「[ngClass] 配列構文」

## 概要
Angular v20における[ngClass]の配列構文の使用方法。配列形式で複数のクラス名を組み合わせ、動的で柔軟なクラス適用を実現する方法を学ぶ。

## 学習目標
- [ngClass]配列構文の使い方を理解する
- 動的なクラス組み合わせを学ぶ
- 柔軟なクラス制御を把握する

## 技術ポイント
- 配列構文の基本形式
- 動的なクラス組み合わせ
- 条件付きクラス追加
- 効率的なクラス管理

## 📺 画面表示用コード

### 配列構文の基本的な使用
```typescript
@Component({
  selector: 'app-ngclass-array',
  template: `
    <div class="container">
      <h2>配列構文によるクラス制御</h2>
      
      <div class="component-grid">
        <div class="component-card" 
             [ngClass]="[
               'base-card',
               getCardSize(),
               getCardTheme(),
               getCardState(),
               isAnimated ? 'animated' : ''
             ]">
          <h3>動的カード</h3>
          <p>配列構文でクラスが組み合わされます</p>
        </div>
        
        <div class="button-group">
          <button [ngClass]="['btn', getButtonVariant(), getButtonSize()]"
                  (click)="toggleVariant()">
            ボタンバリアント変更
          </button>
          
          <button [ngClass]="['btn', 'primary', isDisabled ? 'disabled' : '']"
                  (click)="toggleDisabled()">
            {{ isDisabled ? '有効化' : '無効化' }}
          </button>
        </div>
        
        <div class="navigation" 
             [ngClass]="[
               'nav',
               'horizontal',
               isCollapsed ? 'collapsed' : 'expanded',
               currentPage === 'home' ? 'home-active' : ''
             ]">
          <div class="nav-item" [ngClass]="['nav-link', currentPage === 'home' ? 'active' : '']">
            ホーム
          </div>
          <div class="nav-item" [ngClass]="['nav-link', currentPage === 'about' ? 'active' : '']">
            について
          </div>
          <div class="nav-item" [ngClass]="['nav-link', currentPage === 'contact' ? 'active' : '']">
            お問い合わせ
          </div>
        </div>
      </div>
      
      <div class="controls">
        <button (click)="cycleCardSize()">カードサイズ変更</button>
        <button (click)="cycleCardTheme()">テーマ変更</button>
        <button (click)="cycleCardState()">状態変更</button>
        <button (click)="toggleAnimation()">アニメーション切り替え</button>
        <button (click)="cyclePage()">ページ切り替え</button>
      </div>
    </div>
  `,
  styles: [`
    .container {
      padding: 20px;
      max-width: 1000px;
      margin: 0 auto;
    }
    
    .base-card {
      padding: 20px;
      border-radius: 8px;
      margin: 15px 0;
      transition: all 0.3s ease;
      border: 2px solid transparent;
    }
    
    /* サイズクラス */
    .small { width: 200px; padding: 15px; }
    .medium { width: 300px; padding: 20px; }
    .large { width: 400px; padding: 25px; }
    
    /* テーマクラス */
    .theme-primary { 
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
      color: white;
    }
    .theme-secondary { 
      background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
      color: white;
    }
    .theme-success { 
      background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
      color: white;
    }
    
    /* 状態クラス */
    .state-normal { border-color: #ddd; }
    .state-highlighted { 
      border-color: #ffc107;
      box-shadow: 0 4px 12px rgba(255, 193, 7, 0.3);
    }
    .state-selected { 
      border-color: #007bff;
      box-shadow: 0 4px 12px rgba(0, 123, 255, 0.3);
    }
    
    /* アニメーションクラス */
    .animated {
      animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
      0% { transform: scale(1); }
      50% { transform: scale(1.05); }
      100% { transform: scale(1); }
    }
    
    .btn {
      padding: 12px 24px;
      border: none;
      border-radius: 6px;
      cursor: pointer;
      margin: 5px;
      transition: all 0.3s ease;
      font-weight: 500;
    }
    
    /* ボタンバリアント */
    .btn-primary { background: #007bff; color: white; }
    .btn-secondary { background: #6c757d; color: white; }
    .btn-success { background: #28a745; color: white; }
    .btn-danger { background: #dc3545; color: white; }
    
    /* ボタンサイズ */
    .btn-sm { padding: 8px 16px; font-size: 14px; }
    .btn-md { padding: 12px 24px; font-size: 16px; }
    .btn-lg { padding: 16px 32px; font-size: 18px; }
    
    .btn.disabled {
      opacity: 0.6;
      cursor: not-allowed;
    }
    
    .nav {
      display: flex;
      background: #f8f9fa;
      border-radius: 8px;
      padding: 10px;
      margin: 15px 0;
      transition: all 0.3s ease;
    }
    
    .nav.horizontal { flex-direction: row; }
    .nav.collapsed { opacity: 0.7; }
    .nav.expanded { opacity: 1; }
    
    .nav-item {
      padding: 10px 15px;
      margin: 0 5px;
      border-radius: 4px;
      cursor: pointer;
      transition: all 0.3s ease;
    }
    
    .nav-link {
      color: #6c757d;
    }
    
    .nav-link.active {
      background: #007bff;
      color: white;
    }
    
    .nav.home-active .nav-link {
      border-left: 3px solid #28a745;
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
      background: #6c757d;
      color: white;
      transition: all 0.3s ease;
    }
    
    .controls button:hover {
      background: #5a6268;
    }
  `]
})
export class NgClassArrayComponent {
  cardSizeIndex = 0;
  cardThemeIndex = 0;
  cardStateIndex = 0;
  buttonVariantIndex = 0;
  buttonSizeIndex = 0;
  isAnimated = false;
  isDisabled = false;
  currentPage = 'home';
  
  private sizes = ['small', 'medium', 'large'];
  private themes = ['theme-primary', 'theme-secondary', 'theme-success'];
  private states = ['state-normal', 'state-highlighted', 'state-selected'];
  private buttonVariants = ['btn-primary', 'btn-secondary', 'btn-success', 'btn-danger'];
  private buttonSizes = ['btn-sm', 'btn-md', 'btn-lg'];
  private pages = ['home', 'about', 'contact'];
  
  getCardSize() {
    return this.sizes[this.cardSizeIndex];
  }
  
  getCardTheme() {
    return this.themes[this.cardThemeIndex];
  }
  
  getCardState() {
    return this.states[this.cardStateIndex];
  }
  
  getButtonVariant() {
    return this.buttonVariants[this.buttonVariantIndex];
  }
  
  getButtonSize() {
    return this.buttonSizes[this.buttonSizeIndex];
  }
  
  cycleCardSize() {
    this.cardSizeIndex = (this.cardSizeIndex + 1) % this.sizes.length;
  }
  
  cycleCardTheme() {
    this.cardThemeIndex = (this.cardThemeIndex + 1) % this.themes.length;
  }
  
  cycleCardState() {
    this.cardStateIndex = (this.cardStateIndex + 1) % this.states.length;
  }
  
  toggleVariant() {
    this.buttonVariantIndex = (this.buttonVariantIndex + 1) % this.buttonVariants.length;
  }
  
  toggleAnimation() {
    this.isAnimated = !this.isAnimated;
  }
  
  toggleDisabled() {
    this.isDisabled = !this.isDisabled;
  }
  
  cyclePage() {
    const currentIndex = this.pages.indexOf(this.currentPage);
    this.currentPage = this.pages[(currentIndex + 1) % this.pages.length];
  }
}
```

## 実践的な活用例
- 動的なコンポーネントスタイリング
- 条件付きクラス組み合わせ
- 柔軟なUI制御

## ベストプラクティス
- 明確なクラス命名規則
- 効率的な配列管理
- 可読性の維持

## 注意点
- 配列の複雑さ管理
- パフォーマンスの考慮
- クラスの競合回避

## 関連技術
- 配列構文
- 動的クラス組み合わせ
- 柔軟なスタイル制御
