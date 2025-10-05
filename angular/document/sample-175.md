# #175 「動的スタイル変更」

## 概要
Angular v20における動的スタイル変更の実装方法。CSS変数とJavaScriptを組み合わせてリアルタイムなスタイル変更を実現し、インタラクティブなUIを構築する方法を学ぶ。

## 学習目標
- 動的スタイル変更の実装方法を理解する
- CSS変数とJavaScript連携を学ぶ
- リアルタイムなスタイル更新を把握する

## 技術ポイント
- CSS変数の動的変更
- JavaScript からのスタイル制御
- リアルタイムな更新
- ユーザーインタラクション

## 📺 画面表示用コード

### 動的スタイル変更の実装
```typescript
@Component({
  selector: 'app-dynamic-styles',
  template: `
    <div class="controls">
      <div class="control-group">
        <label>背景色:</label>
        <input type="color" [(ngModel)]="backgroundColor" (input)="updateBackgroundColor()">
      </div>
      
      <div class="control-group">
        <label>文字色:</label>
        <input type="color" [(ngModel)]="textColor" (input)="updateTextColor()">
      </div>
      
      <div class="control-group">
        <label>フォントサイズ: {{ fontSize }}px</label>
        <input type="range" [(ngModel)]="fontSize" (input)="updateFontSize()" min="12" max="32">
      </div>
      
      <div class="control-group">
        <label>角丸: {{ borderRadius }}px</label>
        <input type="range" [(ngModel)]="borderRadius" (input)="updateBorderRadius()" min="0" max="20">
      </div>
      
      <button (click)="resetStyles()">リセット</button>
    </div>
    
    <div class="dynamic-content">
      <h2>動的スタイル変更</h2>
      <p>コントロールを操作してスタイルを変更してください</p>
      <div class="sample-box">
        <h3>サンプルボックス</h3>
        <p>この要素のスタイルが動的に変わります</p>
      </div>
    </div>
  `,
  styles: [`
    :host {
      --dynamic-bg-color: #f8f9fa;
      --dynamic-text-color: #333333;
      --dynamic-font-size: 16px;
      --dynamic-border-radius: 8px;
    }
    
    .controls {
      background: #ffffff;
      padding: 20px;
      border-radius: 10px;
      box-shadow: 0 2px 10px rgba(0,0,0,0.1);
      margin-bottom: 20px;
    }
    
    .control-group {
      margin-bottom: 15px;
      display: flex;
      align-items: center;
      gap: 10px;
    }
    
    .control-group label {
      min-width: 120px;
      font-weight: 500;
    }
    
    .control-group input[type="color"] {
      width: 50px;
      height: 35px;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }
    
    .control-group input[type="range"] {
      flex: 1;
      margin: 0 10px;
    }
    
    button {
      background: #007bff;
      color: white;
      border: none;
      padding: 10px 20px;
      border-radius: 5px;
      cursor: pointer;
      margin-top: 10px;
    }
    
    button:hover {
      background: #0056b3;
    }
    
    .dynamic-content {
      background: var(--dynamic-bg-color);
      color: var(--dynamic-text-color);
      font-size: var(--dynamic-font-size);
      padding: 30px;
      border-radius: var(--dynamic-border-radius);
      box-shadow: 0 4px 15px rgba(0,0,0,0.1);
      transition: all 0.3s ease;
    }
    
    .dynamic-content h2 {
      margin-bottom: 20px;
      font-size: calc(var(--dynamic-font-size) * 1.5);
    }
    
    .sample-box {
      background: rgba(0,123,255,0.1);
      border: 2px solid var(--dynamic-text-color);
      padding: 20px;
      margin-top: 20px;
      border-radius: calc(var(--dynamic-border-radius) / 2);
      transition: all 0.3s ease;
    }
    
    .sample-box h3 {
      color: var(--dynamic-text-color);
      margin-bottom: 10px;
    }
  `]
})
export class DynamicStylesComponent {
  backgroundColor = '#f8f9fa';
  textColor = '#333333';
  fontSize = 16;
  borderRadius = 8;
  
  updateBackgroundColor() {
    document.documentElement.style.setProperty('--dynamic-bg-color', this.backgroundColor);
  }
  
  updateTextColor() {
    document.documentElement.style.setProperty('--dynamic-text-color', this.textColor);
  }
  
  updateFontSize() {
    document.documentElement.style.setProperty('--dynamic-font-size', this.fontSize + 'px');
  }
  
  updateBorderRadius() {
    document.documentElement.style.setProperty('--dynamic-border-radius', this.borderRadius + 'px');
  }
  
  resetStyles() {
    this.backgroundColor = '#f8f9fa';
    this.textColor = '#333333';
    this.fontSize = 16;
    this.borderRadius = 8;
    
    this.updateBackgroundColor();
    this.updateTextColor();
    this.updateFontSize();
    this.updateBorderRadius();
  }
}
```

## 実践的な活用例
- ユーザー設定によるスタイルカスタマイズ
- リアルタイムなプレビュー機能
- インタラクティブなデザインツール

## ベストプラクティス
- 適切なCSS変数の使用
- スムーズなトランジション
- ユーザビリティの考慮

## 注意点
- パフォーマンスの考慮
- アクセシビリティの維持
- ブラウザサポート

## 関連技術
- CSS 変数
- 動的スタイリング
- ユーザーインタラクション
