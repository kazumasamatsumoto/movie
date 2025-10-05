# #164 「ViewEncapsulation.None - グローバル」

## 概要
Angular v20におけるViewEncapsulation.Noneの使用方法と注意点。スタイルのカプセル化を無効化し、グローバルスコープでスタイルを適用する際の適切な実装方法を学ぶ。

## 学習目標
- ViewEncapsulation.Noneの特徴を理解する
- グローバルスタイルの適用方法を学ぶ
- 使用時の注意点を把握する

## 技術ポイント
- カプセル化の無効化
- グローバルスコープでの適用
- スタイルの競合リスク
- 適切な命名規則

## 📺 画面表示用コード

### Noneの基本的な使用
```typescript
@Component({
  selector: 'app-global-example',
  template: `
    <div class="global-container">
      <h2 class="global-title">グローバルスタイル</h2>
      <p class="global-content">このスタイルはグローバルに適用されます</p>
    </div>
  `,
  styles: [`
    .global-container {
      background: #f0f8ff;
      padding: 25px;
      border: 3px solid #4169e1;
      border-radius: 15px;
      margin: 20px 0;
    }
    
    .global-title {
      color: #4169e1;
      font-size: 24px;
      font-weight: bold;
      margin-bottom: 15px;
    }
    
    .global-content {
      color: #333;
      line-height: 1.7;
      font-size: 16px;
    }
  `],
  encapsulation: ViewEncapsulation.None
})
export class GlobalExampleComponent {}
```

### グローバルスタイルの影響例
```typescript
@Component({
  selector: 'app-affected-component',
  template: `
    <div class="global-container">
      <!-- 上記のグローバルスタイルが適用される -->
      <p>この要素も同じスタイルが適用されます</p>
    </div>
  `
})
export class AffectedComponent {}
```

## 実践的な活用例
- ライブラリスタイルの適用
- グローバルテーマの実装
- レガシーCSSとの統合

## ベストプラクティス
- 明確な命名規則の使用
- スタイルの競合回避
- 限定的な使用

## 注意点
- スタイルの競合リスク
- 予期しない副作用
- デバッグの複雑さ

## 関連技術
- グローバルスタイル
- CSS 競合回避
- スタイル管理
