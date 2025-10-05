# #181 「[ngStyle] オブジェクト構文」

## 概要
Angular v20における[ngStyle]のオブジェクト構文の使用方法。{プロパティ名: 値}の形式で複数のスタイルプロパティを効率的に制御し、動的で柔軟なスタイル適用を実現する方法を学ぶ。

## 学習目標
- [ngStyle]オブジェクト構文の使い方を理解する
- 複数スタイルの同時制御を学ぶ
- 効率的なスタイル管理を把握する

## 技術ポイント
- オブジェクト構文の基本形式
- 複数プロパティの同時指定
- 動的な値の適用
- 効率的なスタイル制御

## 📺 画面表示用コード

### オブジェクト構文の基本的な使用
```typescript
@Component({
  selector: 'app-ngstyle-object',
  template: `
    <div class="container">
      <h2>オブジェクト構文によるスタイル制御</h2>
      
      <div class="controls">
        <input type="color" [(ngModel)]="primaryColor" placeholder="プライマリ色">
        <input type="color" [(ngModel)]="secondaryColor" placeholder="セカンダリ色">
        <input type="range" [(ngModel)]="fontSize" min="12" max="32">
        <input type="range" [(ngModel)]="spacing" min="10" max="50">
      </div>
      
      <div class="styled-element" 
           [ngStyle]="{
             'background-color': primaryColor,
             'color': secondaryColor,
             'font-size': fontSize + 'px',
             'padding': spacing + 'px',
             'border-radius': '8px',
             'box-shadow': '0 4px 8px rgba(0,0,0,0.1)',
             'transition': 'all 0.3s ease'
           }">
        <h3>動的スタイル要素</h3>
        <p>オブジェクト構文でスタイルが制御されます</p>
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
      margin-bottom: 20px;
      flex-wrap: wrap;
    }
    
    .controls input {
      padding: 8px;
      border: 1px solid #ddd;
      border-radius: 4px;
    }
    
    .styled-element {
      text-align: center;
      margin: 20px 0;
    }
    
    .styled-element h3 {
      margin-bottom: 15px;
    }
  `]
})
export class NgStyleObjectComponent {
  primaryColor = '#f8f9fa';
  secondaryColor = '#333333';
  fontSize = 16;
  spacing = 20;
}
```

## 実践的な活用例
- 複数スタイルの同時制御
- 動的なスタイル変更
- 効率的なスタイル管理

## ベストプラクティス
- 適切なプロパティ設定
- パフォーマンスの考慮
- 可読性の維持

## 注意点
- スタイル値の妥当性
- パフォーマンスへの影響
- ブラウザサポート

## 関連技術
- オブジェクト構文
- 動的スタイリング
- 効率的な制御
