# #162 「ViewEncapsulation - カプセル化戦略」

## 概要
Angular v20におけるViewEncapsulationの仕組みと戦略。コンポーネントスタイルの適用範囲を制御し、スタイルの競合を防ぎ、予測可能なスタイリングを実現する方法を学ぶ。

## 学習目標
- ViewEncapsulationの概念を理解する
- 3つのカプセル化戦略を学ぶ
- 適切な戦略の選択方法を把握する

## 技術ポイント
- ViewEncapsulation.Emulated（デフォルト）
- ViewEncapsulation.None（グローバル）
- ViewEncapsulation.ShadowDom（Shadow DOM）
- カプセル化戦略の使い分け

## 📺 画面表示用コード

### Emulated（デフォルト）
```typescript
@Component({
  selector: 'app-emulated',
  template: `
    <div class="box">Emulated カプセル化</div>
  `,
  styles: [`
    .box {
      background: lightblue;
      padding: 20px;
      border: 2px solid blue;
    }
  `],
  encapsulation: ViewEncapsulation.Emulated
})
export class EmulatedComponent {}
```

### None（グローバル）
```typescript
@Component({
  selector: 'app-global',
  template: `
    <div class="global-box">Global スタイル</div>
  `,
  styles: [`
    .global-box {
      background: lightgreen;
      padding: 20px;
      border: 2px solid green;
    }
  `],
  encapsulation: ViewEncapsulation.None
})
export class GlobalComponent {}
```

### ShadowDom
```typescript
@Component({
  selector: 'app-shadow-dom',
  template: `
    <div class="shadow-box">Shadow DOM</div>
  `,
  styles: [`
    .shadow-box {
      background: lightcoral;
      padding: 20px;
      border: 2px solid red;
    }
  `],
  encapsulation: ViewEncapsulation.ShadowDom
})
export class ShadowDomComponent {}
```

## 実践的な活用例
- ライブラリコンポーネントのスタイリング
- グローバルテーマの適用
- 完全分離が必要なコンポーネント

## ベストプラクティス
- 用途に応じた戦略選択
- スタイルの競合回避
- パフォーマンスの考慮

## 注意点
- ブラウザサポートの確認
- スタイルの予期しない影響
- デバッグの複雑さ

## 関連技術
- Shadow DOM
- CSS カプセル化
- コンポーネント設計
