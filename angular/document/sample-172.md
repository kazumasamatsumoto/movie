# #172 「CSS カスタムプロパティ」

## 概要
Angular v20におけるCSSカスタムプロパティの詳細な活用方法。値の継承、動的変更、JavaScript連携など、CSS変数の高度な機能を使用した効率的なスタイル管理を学ぶ。

## 学習目標
- CSSカスタムプロパティの特徴を理解する
- 継承とスコープを学ぶ
- 高度な活用方法を把握する

## 技術ポイント
- カスタムプロパティの定義
- 値の継承とスコープ
- JavaScript からの制御
- フォールバック値

## 📺 画面表示用コード

### カスタムプロパティの継承
```typescript
@Component({
  selector: 'app-custom-properties',
  template: `
    <div class="parent">
      <h3>親要素</h3>
      <div class="child">
        <h4>子要素</h4>
        <div class="grandchild">孫要素</div>
      </div>
    </div>
  `,
  styles: [`
    :host {
      --base-font-size: 16px;
      --base-color: #333;
      --base-spacing: 20px;
    }
    
    .parent {
      --parent-color: #007bff;
      --parent-font-size: calc(var(--base-font-size) * 1.2);
      font-size: var(--parent-font-size);
      color: var(--parent-color);
      padding: var(--base-spacing);
      border: 2px solid var(--parent-color);
    }
    
    .child {
      --child-color: #28a745;
      color: var(--child-color);
      margin: var(--base-spacing);
      font-size: calc(var(--base-font-size) * 1.1);
    }
    
    .grandchild {
      --grandchild-color: #dc3545;
      color: var(--grandchild-color);
      font-size: var(--base-font-size);
      background: rgba(220, 53, 69, 0.1);
      padding: 10px;
      border-radius: 4px;
    }
  `]
})
export class CustomPropertiesComponent {}
```

### 動的な値変更
```typescript
@Component({
  selector: 'app-dynamic-properties',
  template: `
    <div class="controls">
      <input type="range" [(ngModel)]="fontSize" (input)="updateFontSize()" min="12" max="24">
      <input type="color" [(ngModel)]="primaryColor" (input)="updateColor()">
    </div>
    <div class="dynamic-content">
      <h2>動的スタイル</h2>
      <p>フォントサイズと色が動的に変わります</p>
    </div>
  `,
  styles: [`
    :host {
      --dynamic-font-size: 16px;
      --dynamic-color: #007bff;
    }
    
    .controls {
      margin-bottom: 20px;
      padding: 15px;
      background: #f8f9fa;
      border-radius: 8px;
    }
    
    .controls input {
      margin: 0 10px;
    }
    
    .dynamic-content {
      font-size: var(--dynamic-font-size);
      color: var(--dynamic-color);
      padding: 20px;
      border: 2px solid var(--dynamic-color);
      border-radius: 8px;
      transition: all 0.3s ease;
    }
    
    .dynamic-content h2 {
      margin-bottom: 15px;
    }
  `]
})
export class DynamicPropertiesComponent {
  fontSize = 16;
  primaryColor = '#007bff';
  
  updateFontSize() {
    document.documentElement.style.setProperty('--dynamic-font-size', this.fontSize + 'px');
  }
  
  updateColor() {
    document.documentElement.style.setProperty('--dynamic-color', this.primaryColor);
  }
}
```

## 実践的な活用例
- 継承を活用したスタイル設計
- 動的なテーマ切り替え
- ユーザー設定に応じたスタイル

## ベストプラクティス
- 適切なスコープの設計
- 意味のある変数名
- フォールバック値の設定

## 注意点
- 継承関係の理解
- パフォーマンスの考慮
- ブラウザサポート

## 関連技術
- CSS 継承
- 動的スタイリング
- JavaScript連携
