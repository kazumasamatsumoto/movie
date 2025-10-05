# #182 「[ngStyle] 複数スタイル指定」

## 概要
Angular v20における[ngStyle]での複数スタイル指定方法。オブジェクト構文を活用して複数のスタイルプロパティを同時に制御し、効率的で保守性の高いスタイル管理を実現する。

## 学習目標
- 複数スタイルの同時指定を理解する
- 効率的なスタイル制御を学ぶ
- 動的なスタイル管理を把握する

## 技術ポイント
- 複数プロパティの同時制御
- 条件付きスタイル適用
- 効率的なスタイル管理
- 動的な値の組み合わせ

## 📺 画面表示用コード

### 複数スタイルの同時指定
```typescript
@Component({
  selector: 'app-multiple-styles',
  template: `
    <div class="container">
      <h2>複数スタイル指定</h2>
      
      <div class="card" 
           [ngStyle]="{
             'background': getCardBackground(),
             'color': getCardColor(),
             'border': getCardBorder(),
             'box-shadow': getCardShadow(),
             'transform': getCardTransform(),
             'transition': 'all 0.3s ease',
             'padding': '20px',
             'border-radius': '10px',
             'margin': '15px 0'
           }">
        <h3>複数スタイルカード</h3>
        <p>複数のスタイルプロパティが同時に制御されます</p>
      </div>
      
      <div class="controls">
        <button (click)="toggleTheme()">テーマ切り替え</button>
        <button (click)="toggleSize()">サイズ切り替え</button>
        <button (click)="toggleAnimation()">アニメーション切り替え</button>
      </div>
    </div>
  `,
  styles: [`
    .container {
      padding: 20px;
      max-width: 600px;
      margin: 0 auto;
    }
    
    .controls {
      display: flex;
      gap: 10px;
      margin-top: 20px;
    }
    
    .controls button {
      padding: 10px 20px;
      border: none;
      border-radius: 5px;
      background: #007bff;
      color: white;
      cursor: pointer;
      transition: all 0.3s ease;
    }
    
    .controls button:hover {
      background: #0056b3;
    }
  `]
})
export class MultipleStylesComponent {
  isDarkTheme = false;
  isLargeSize = false;
  isAnimated = false;
  
  getCardBackground() {
    return this.isDarkTheme 
      ? 'linear-gradient(135deg, #2c3e50 0%, #34495e 100%)'
      : 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)';
  }
  
  getCardColor() {
    return this.isDarkTheme ? '#ffffff' : '#ffffff';
  }
  
  getCardBorder() {
    return this.isLargeSize ? '3px solid #ffc107' : '2px solid #007bff';
  }
  
  getCardShadow() {
    const intensity = this.isLargeSize ? '0.3' : '0.1';
    return `0 8px 25px rgba(0,0,0,${intensity})`;
  }
  
  getCardTransform() {
    return this.isAnimated ? 'scale(1.05)' : 'scale(1)';
  }
  
  toggleTheme() {
    this.isDarkTheme = !this.isDarkTheme;
  }
  
  toggleSize() {
    this.isLargeSize = !this.isLargeSize;
  }
  
  toggleAnimation() {
    this.isAnimated = !this.isAnimated;
  }
}
```

## 実践的な活用例
- 複雑なスタイル制御
- テーマシステム
- 動的なスタイル変更

## ベストプラクティス
- 効率的なスタイル管理
- 適切なプロパティ設定
- パフォーマンスの考慮

## 注意点
- スタイルの競合回避
- パフォーマンスへの影響
- 可読性の維持

## 関連技術
- 複数スタイル制御
- 動的スタイリング
- 効率的な管理
