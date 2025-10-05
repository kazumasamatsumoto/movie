# #165 「ViewEncapsulation.ShadowDom - Shadow DOM」

## 概要
Angular v20におけるViewEncapsulation.ShadowDomの実装方法と特徴。ブラウザネイティブのShadow DOM機能を活用し、完全なスタイル分離と真のカプセル化を実現する方法を学ぶ。

## 学習目標
- ViewEncapsulation.ShadowDomの特徴を理解する
- Shadow DOMの利点を学ぶ
- ブラウザサポートを把握する

## 技術ポイント
- 完全なスタイル分離
- 真のカプセル化
- ブラウザネイティブ機能
- 外部スタイルからの隔離

## 📺 画面表示用コード

### ShadowDomの基本的な使用
```typescript
@Component({
  selector: 'app-shadow-dom-example',
  template: `
    <div class="shadow-container">
      <h2 class="shadow-title">Shadow DOM</h2>
      <p class="shadow-content">完全に分離されたスタイル</p>
      <button class="shadow-button">ボタン</button>
    </div>
  `,
  styles: [`
    .shadow-container {
      background: linear-gradient(45deg, #ff6b6b, #4ecdc4);
      padding: 30px;
      border-radius: 20px;
      box-shadow: 0 10px 30px rgba(0,0,0,0.3);
      color: white;
    }
    
    .shadow-title {
      font-size: 28px;
      margin-bottom: 20px;
      text-align: center;
      text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }
    
    .shadow-content {
      font-size: 16px;
      line-height: 1.6;
      margin-bottom: 20px;
      text-align: center;
    }
    
    .shadow-button {
      background: rgba(255,255,255,0.2);
      border: 2px solid white;
      color: white;
      padding: 12px 24px;
      border-radius: 25px;
      cursor: pointer;
      font-size: 16px;
      transition: all 0.3s ease;
      display: block;
      margin: 0 auto;
    }
    
    .shadow-button:hover {
      background: rgba(255,255,255,0.3);
      transform: translateY(-2px);
    }
  `],
  encapsulation: ViewEncapsulation.ShadowDom
})
export class ShadowDomExampleComponent {}
```

### Shadow DOMの特徴確認
```typescript
@Component({
  selector: 'app-shadow-test',
  template: `
    <div class="global-style">
      グローバルスタイルの影響を受ける要素
    </div>
    <app-shadow-dom-example></app-shadow-dom-example>
    <div class="global-style">
      グローバルスタイルの影響を受ける要素
    </div>
  `,
  styles: [`
    .global-style {
      background: red;
      padding: 10px;
      margin: 10px 0;
    }
  `]
})
export class ShadowTestComponent {}
```

## 実践的な活用例
- 完全分離が必要なコンポーネント
- ライブラリコンポーネント
- 外部スタイルの影響を受けない設計

## ベストプラクティス
- ブラウザサポートの確認
- 適切な使用場面の選択
- パフォーマンスの考慮

## 注意点
- ブラウザサポートの制限
- デバッグの複雑さ
- 外部スタイルの適用制限

## 関連技術
- Shadow DOM
- 完全スタイル分離
- ブラウザネイティブ機能
