# #163 「ViewEncapsulation.Emulated - デフォルト」

## 概要
Angular v20におけるViewEncapsulation.Emulatedの仕組みと特徴。CSSクラスを自動生成してスタイルのカプセル化を実現し、安全で予測可能なスタイル適用を実現する方法を学ぶ。

## 学習目標
- ViewEncapsulation.Emulatedの仕組みを理解する
- 自動カプセル化の特徴を学ぶ
- デフォルト設定の利点を把握する

## 技術ポイント
- 自動生成されるCSS属性
- スタイルのスコープ制限
- デフォルトの動作
- カプセル化の仕組み

## 📺 画面表示用コード

### Emulatedの基本的な使用
```typescript
@Component({
  selector: 'app-emulated-example',
  template: `
    <div class="container">
      <h2 class="title">Emulated カプセル化</h2>
      <p class="description">このスタイルは自動でカプセル化されます</p>
    </div>
  `,
  styles: [`
    .container {
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
      padding: 30px;
      border-radius: 10px;
      color: white;
    }
    
    .title {
      font-size: 28px;
      margin-bottom: 15px;
      text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .description {
      font-size: 16px;
      line-height: 1.6;
      opacity: 0.9;
    }
  `],
  encapsulation: ViewEncapsulation.Emulated
})
export class EmulatedExampleComponent {}
```

### 生成されるHTML（自動属性付与）
```html
<!-- 実際に生成されるHTML -->
<app-emulated-example _ngcontent-c0>
  <div class="container" _ngcontent-c0>
    <h2 class="title" _ngcontent-c0>Emulated カプセル化</h2>
    <p class="description" _ngcontent-c0>このスタイルは自動でカプセル化されます</p>
  </div>
</app-emulated-example>
```

## 実践的な活用例
- 一般的なコンポーネントスタイリング
- スタイルの競合回避
- 予測可能なスタイル適用

## ベストプラクティス
- デフォルト設定の活用
- 適切なクラス命名
- スタイルの整理

## 注意点
- 自動生成される属性の理解
- デバッグ時の考慮
- パフォーマンスの影響

## 関連技術
- CSS カプセル化
- 自動属性生成
- スタイル分離
