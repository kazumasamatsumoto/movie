# #180 「[ngStyle] 動的スタイル制御」

## 概要
Angular v20における[ngStyle]ディレクティブを使った動的スタイル制御。JavaScriptの値に基づいたリアルタイムなスタイル変更により、インタラクティブで動的なUIを実現する方法を学ぶ。

## 学習目標
- [ngStyle]の基本的な使い方を理解する
- 動的スタイル変更を学ぶ
- データバインディングとの連携を把握する

## 技術ポイント
- [ngStyle] ディレクティブの使用
- オブジェクト形式でのスタイル指定
- データバインディングとの連携
- リアルタイムなスタイル更新

## 📺 画面表示用コード

### 基本的な[ngStyle]の使用
```typescript
@Component({
  selector: 'app-ngstyle-basic',
  template: `
    <div class="container">
      <h2>動的スタイル制御</h2>
      
      <div class="controls">
        <div class="control-group">
          <label>背景色:</label>
          <input type="color" [(ngModel)]="backgroundColor" (input)="updateStyles()">
        </div>
        
        <div class="control-group">
          <label>文字色:</label>
          <input type="color" [(ngModel)]="textColor" (input)="updateStyles()">
        </div>
        
        <div class="control-group">
          <label>フォントサイズ: {{ fontSize }}px</label>
          <input type="range" [(ngModel)]="fontSize" (input)="updateStyles()" min="12" max="32">
        </div>
        
        <div class="control-group">
          <label>角丸: {{ borderRadius }}px</label>
          <input type="range" [(ngModel)]="borderRadius" (input)="updateStyles()" min="0" max="20">
        </div>
        
        <div class="control-group">
          <label>透明度: {{ opacity }}%</label>
          <input type="range" [(ngModel)]="opacity" (input)="updateStyles()" min="10" max="100">
        </div>
      </div>
      
      <div class="dynamic-element" 
           [ngStyle]="{
             'background-color': backgroundColor,
             'color': textColor,
             'font-size': fontSize + 'px',
             'border-radius': borderRadius + 'px',
             'opacity': opacity / 100,
             'padding': '20px',
             'margin': '15px 0',
             'border': '2px solid ' + borderColor,
             'box-shadow': '0 4px 8px rgba(0,0,0,' + (opacity / 200) + ')',
             'transition': 'all 0.3s ease'
           }">
        <h3>動的スタイル要素</h3>
        <p>コントロールを操作してスタイルを変更してください</p>
        <p>フォントサイズ: {{ fontSize }}px</p>
        <p>角丸: {{ borderRadius }}px</p>
        <p>透明度: {{ opacity }}%</p>
      </div>
      
      <div class="progress-section">
        <h3>プログレス表示</h3>
        <div class="progress-bar" 
             [ngStyle]="{
               'width': progress + '%',
               'background-color': getProgressColor(),
               'height': '20px',
               'border-radius': '10px',
               'transition': 'all 0.5s ease'
             }">
        </div>
        <p>進捗: {{ progress }}%</p>
        <button (click)="updateProgress()">進捗更新</button>
      </div>
      
      <div class="animation-section">
        <h3>アニメーション制御</h3>
        <div class="animated-box" 
             [ngStyle]="{
               'transform': 'translateX(' + translateX + 'px) rotate(' + rotation + 'deg)',
               'background': getGradientBackground(),
               'width': boxSize + 'px',
               'height': boxSize + 'px',
               'border-radius': boxSize / 2 + 'px',
               'transition': 'all 0.5s ease'
             }">
        </div>
        
        <div class="animation-controls">
          <button (click)="moveLeft()">左に移動</button>
          <button (click)="moveRight()">右に移動</button>
          <button (click)="rotate()">回転</button>
          <button (click)="resize()">サイズ変更</button>
        </div>
      </div>
      
      <div class="reset-section">
        <button (click)="resetStyles()">スタイルリセット</button>
      </div>
    </div>
  `,
  styles: [`
    .container {
      padding: 20px;
      max-width: 800px;
      margin: 0 auto;
    }
    
    .controls {
      background: #f8f9fa;
      padding: 20px;
      border-radius: 8px;
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
    
    .dynamic-element {
      text-align: center;
      font-family: Arial, sans-serif;
    }
    
    .dynamic-element h3 {
      margin-bottom: 15px;
    }
    
    .dynamic-element p {
      margin: 8px 0;
    }
    
    .progress-section {
      margin: 20px 0;
    }
    
    .progress-bar {
      background: #e9ecef;
      border-radius: 10px;
      margin: 10px 0;
      position: relative;
    }
    
    .progress-section button {
      padding: 8px 16px;
      border: none;
      border-radius: 4px;
      background: #007bff;
      color: white;
      cursor: pointer;
      margin-top: 10px;
    }
    
    .animated-box {
      background: linear-gradient(45deg, #ff6b6b, #4ecdc4);
      margin: 20px auto;
      position: relative;
    }
    
    .animation-controls {
      display: flex;
      gap: 10px;
      justify-content: center;
      margin-top: 15px;
    }
    
    .animation-controls button {
      padding: 8px 16px;
      border: none;
      border-radius: 4px;
      background: #28a745;
      color: white;
      cursor: pointer;
      transition: all 0.3s ease;
    }
    
    .animation-controls button:hover {
      background: #218838;
    }
    
    .reset-section {
      text-align: center;
      margin-top: 30px;
    }
    
    .reset-section button {
      padding: 12px 24px;
      border: none;
      border-radius: 6px;
      background: #dc3545;
      color: white;
      cursor: pointer;
      font-size: 16px;
      transition: all 0.3s ease;
    }
    
    .reset-section button:hover {
      background: #c82333;
    }
  `]
})
export class NgStyleBasicComponent {
  backgroundColor = '#f8f9fa';
  textColor = '#333333';
  fontSize = 16;
  borderRadius = 8;
  opacity = 100;
  borderColor = '#007bff';
  progress = 0;
  translateX = 0;
  rotation = 0;
  boxSize = 100;
  
  updateStyles() {
    // スタイル更新のトリガー（実際の更新はngStyleが自動で行う）
  }
  
  getProgressColor() {
    if (this.progress < 30) return '#dc3545';
    if (this.progress < 70) return '#ffc107';
    return '#28a745';
  }
  
  getGradientBackground() {
    const hue1 = (this.translateX + 200) % 360;
    const hue2 = (this.rotation + 180) % 360;
    return `linear-gradient(${this.rotation}deg, hsl(${hue1}, 70%, 60%), hsl(${hue2}, 70%, 60%))`;
  }
  
  updateProgress() {
    this.progress = Math.floor(Math.random() * 101);
  }
  
  moveLeft() {
    this.translateX = Math.max(this.translateX - 50, -200);
  }
  
  moveRight() {
    this.translateX = Math.min(this.translateX + 50, 200);
  }
  
  rotate() {
    this.rotation = (this.rotation + 45) % 360;
  }
  
  resize() {
    this.boxSize = this.boxSize === 100 ? 150 : 100;
  }
  
  resetStyles() {
    this.backgroundColor = '#f8f9fa';
    this.textColor = '#333333';
    this.fontSize = 16;
    this.borderRadius = 8;
    this.opacity = 100;
    this.borderColor = '#007bff';
    this.progress = 0;
    this.translateX = 0;
    this.rotation = 0;
    this.boxSize = 100;
  }
}
```

## 実践的な活用例
- リアルタイムなスタイル変更
- プログレスバーの動的表示
- アニメーション制御
- ユーザー設定に応じたスタイル

## ベストプラクティス
- 適切なスタイル値の設定
- パフォーマンスの考慮
- アクセシビリティの維持

## 注意点
- スタイル値の妥当性確認
- パフォーマンスへの影響
- ブラウザサポート

## 関連技術
- 動的スタイリング
- データバインディング
- リアルタイム更新
