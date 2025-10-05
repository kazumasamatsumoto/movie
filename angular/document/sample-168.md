# #168 「::ng-deep - 子孫セレクタ（非推奨）」

## 概要
Angular v20における::ng-deepセレクタの使用と非推奨について。子コンポーネントのスタイルを強制的に適用する機能と、その問題点と代替手段について学ぶ。

## 学習目標
- ::ng-deepの基本的な使い方を理解する
- 非推奨の理由を学ぶ
- 代替手段を把握する

## 技術ポイント
- ::ng-deep セレクタの使用
- カプセル化の破綻
- スタイルの競合リスク
- 代替手段の実装

## 📺 画面表示用コード

### ::ng-deepの使用例（非推奨）
```typescript
@Component({
  selector: 'app-parent-component',
  template: `
    <div class="parent-container">
      <h2>親コンポーネント</h2>
      <app-child-component></app-child-component>
    </div>
  `,
  styles: [`
    .parent-container {
      padding: 20px;
      background: #f5f5f5;
    }
    
    /* ❌ 非推奨: 子コンポーネントのスタイルを強制変更 */
    ::ng-deep app-child-component .child-content {
      background: red !important;
      color: white !important;
    }
  `]
})
export class ParentComponent {}

@Component({
  selector: 'app-child-component',
  template: `
    <div class="child-content">
      子コンポーネントの内容
    </div>
  `,
  styles: [`
    .child-content {
      background: blue;
      color: white;
      padding: 15px;
      border-radius: 5px;
    }
  `]
})
export class ChildComponent {}
```

### 推奨される代替手段
```typescript
// 方法1: ViewEncapsulation.Noneの使用
@Component({
  selector: 'app-recommended-parent',
  template: `
    <div class="parent-container">
      <h2>推奨される実装</h2>
      <app-styled-child></app-styled-child>
    </div>
  `,
  styles: [`
    .parent-container {
      padding: 20px;
      background: #f5f5f5;
    }
    
    /* 特定のクラス名を使用 */
    .parent-container .custom-child-style {
      background: green;
      color: white;
      padding: 15px;
      border-radius: 5px;
    }
  `],
  encapsulation: ViewEncapsulation.None
})
export class RecommendedParentComponent {}

// 方法2: グローバルスタイルの使用
@Component({
  selector: 'app-global-style-parent',
  template: `
    <div class="global-parent">
      <h2>グローバルスタイル実装</h2>
      <div class="custom-child-wrapper">
        <app-child-component></app-child-component>
      </div>
    </div>
  `,
  styles: [`
    .global-parent {
      padding: 20px;
    }
    
    .custom-child-wrapper {
      /* グローバルスタイルで制御 */
    }
  `]
})
export class GlobalStyleParentComponent {}
```

## 実践的な活用例
- ライブラリスタイルの上書き
- グローバルテーマの適用
- レガシーシステムとの統合

## ベストプラクティス
- ::ng-deepの使用を避ける
- 適切な代替手段の選択
- スタイル設計の見直し

## 注意点
- カプセル化の破綻
- スタイルの競合リスク
- 保守性の低下
- 将来の互換性問題

## 関連技術
- CSS カプセル化
- スタイル設計
- 代替手段
