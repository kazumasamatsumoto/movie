# #171 「CSS 変数の活用」

## 概要
Angular v20におけるCSS変数（カスタムプロパティ）の活用方法。動的なテーマ管理、リアルタイムなスタイル変更、保守性の高いスタイル設計を実現するためのCSS変数の実装方法を学ぶ。

## 学習目標
- CSS変数の基本的な使い方を理解する
- 動的テーマ管理を学ぶ
- JavaScript連携を把握する

## 技術ポイント
- :root での変数定義
- var() 関数での値参照
- JavaScript からの制御
- 動的な値変更

## 📺 画面表示用コード

### CSS変数の基本的な使用
```typescript
@Component({
  selector: 'app-css-variables',
  template: `
    <div class="theme-container">
      <h2>CSS変数の活用</h2>
      <div class="card">カード要素</div>
      <button (click)="changeTheme()">テーマ変更</button>
    </div>
  `,
  styles: [`
    :host {
      --primary-color: #007bff;
      --secondary-color: #6c757d;
      --background-color: #ffffff;
      --text-color: #333333;
    }
    
    .theme-container {
      padding: 20px;
      background-color: var(--background-color);
      color: var(--text-color);
      transition: all 0.3s ease;
    }
    
    .card {
      background: var(--primary-color);
      color: white;
      padding: 20px;
      border-radius: 8px;
      margin: 15px 0;
    }
    
    button {
      background: var(--secondary-color);
      color: white;
      border: none;
      padding: 10px 20px;
      border-radius: 4px;
      cursor: pointer;
    }
  `]
})
export class CssVariablesComponent {
  isDarkTheme = false;
  
  changeTheme() {
    this.isDarkTheme = !this.isDarkTheme;
    const root = document.documentElement;
    
    if (this.isDarkTheme) {
      root.style.setProperty('--primary-color', '#28a745');
      root.style.setProperty('--background-color', '#343a40');
      root.style.setProperty('--text-color', '#ffffff');
    } else {
      root.style.setProperty('--primary-color', '#007bff');
      root.style.setProperty('--background-color', '#ffffff');
      root.style.setProperty('--text-color', '#333333');
    }
  }
}
```

## 実践的な活用例
- テーマシステムの構築
- 動的なスタイル変更
- ユーザー設定に応じたスタイル

## ベストプラクティス
- 適切な変数命名
- スコープの考慮
- フォールバック値の設定

## 注意点
- ブラウザサポートの確認
- パフォーマンスの考慮
- 変数の継承関係

## 関連技術
- CSS カスタムプロパティ
- 動的スタイリング
- テーマシステム
