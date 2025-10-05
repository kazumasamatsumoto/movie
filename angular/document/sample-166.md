# #166 「:host セレクタ - ホスト要素」

## 概要
Angular v20における:hostセレクタの使用方法。コンポーネントのホスト要素（カスタムタグ）にスタイルを適用し、コンポーネント自体の見た目を制御する方法を学ぶ。

## 学習目標
- :hostセレクタの基本的な使い方を理解する
- ホスト要素へのスタイル適用を学ぶ
- コンポーネント自体のスタイリングを把握する

## 技術ポイント
- :host セレクタの使用
- ホスト要素のスタイリング
- コンポーネント自体の制御
- 動的なホストスタイル

## 📺 画面表示用コード

### :hostの基本的な使用
```typescript
@Component({
  selector: 'app-host-styling',
  template: `
    <div class="content">
      <h2>ホスト要素のスタイリング</h2>
      <p>このコンポーネント自体にスタイルが適用されます</p>
    </div>
  `,
  styles: [`
    :host {
      display: block;
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
      padding: 20px;
      border-radius: 15px;
      box-shadow: 0 8px 25px rgba(0,0,0,0.15);
      margin: 20px 0;
    }
    
    .content {
      color: white;
      text-align: center;
    }
    
    .content h2 {
      margin-bottom: 15px;
      font-size: 24px;
    }
    
    .content p {
      font-size: 16px;
      opacity: 0.9;
    }
  `]
})
export class HostStylingComponent {}
```

### 動的な:hostスタイル
```typescript
@Component({
  selector: 'app-dynamic-host',
  template: `
    <div class="container">
      <button (click)="toggleStyle()">スタイル切り替え</button>
      <p>ホスト要素のスタイルが動的に変わります</p>
    </div>
  `,
  styles: [`
    :host {
      display: block;
      padding: 20px;
      border-radius: 10px;
      transition: all 0.3s ease;
    }
    
    :host(.active) {
      background: linear-gradient(45deg, #ff6b6b, #4ecdc4);
      color: white;
      transform: scale(1.02);
    }
    
    :host(.inactive) {
      background: #f0f0f0;
      color: #333;
    }
    
    .container {
      text-align: center;
    }
    
    button {
      padding: 10px 20px;
      margin-bottom: 15px;
      border: none;
      border-radius: 5px;
      cursor: pointer;
      font-size: 16px;
    }
  `]
})
export class DynamicHostComponent {
  isActive = false;
  
  toggleStyle() {
    this.isActive = !this.isActive;
    const hostElement = document.querySelector('app-dynamic-host');
    if (hostElement) {
      hostElement.classList.toggle('active', this.isActive);
      hostElement.classList.toggle('inactive', !this.isActive);
    }
  }
}
```

## 実践的な活用例
- コンポーネントの境界線設定
- 背景色やパディングの制御
- ホスト要素のレイアウト制御

## ベストプラクティス
- 適切なホストスタイルの設計
- 動的スタイルの効率的な実装
- レスポンシブデザインの考慮

## 注意点
- ホスト要素の表示方法
- 動的スタイルの適用タイミング
- パフォーマンスの考慮

## 関連技術
- CSS セレクタ
- ホスト要素
- 動的スタイリング
