# #187 「Flexbox レイアウト」

## 概要
CSS Flexboxを利用してシンプルかつ柔軟なレイアウトを構築する基本パターンを紹介し、Angularコンポーネントのスタイルに適用する方法を整理します。

## 学習目標
- Flexboxの主要プロパティ（`display: flex`, `justify-content`, `align-items`など）を理解する
- 横並びレイアウトや縦並びレイアウトをFlexboxで実装する
- ギャップやレスポンシブ対応を取り入れたFlexbox設計を学ぶ

## 技術ポイント
- **基本設定**: `display: flex; flex-direction: row;`
- **アライメント**: `justify-content: space-between; align-items: center;`
- **ギャップ**: `gap: 16px;`（Flexboxでも利用可能）

## 📺 画面表示用コード（動画用）

```scss
.toolbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
}
```

```scss
.layout {
  display: flex;
  flex-direction: column;
  gap: 24px;
}
```

```scss
@media (max-width: 600px) {
  .toolbar {
    flex-direction: column;
  }
}
```

## 💻 詳細実装例（学習用）
```typescript
// toolbar.component.ts
import { Component } from '@angular/core';

@Component({
  selector: 'app-toolbar',
  standalone: true,
  templateUrl: './toolbar.component.html',
  styleUrls: ['./toolbar.component.scss'],
})
export class ToolbarComponent {}
```

```html
<!-- toolbar.component.html -->
<div class="toolbar">
  <div class="toolbar__left">
    <h3>Flexbox Toolbar</h3>
  </div>
  <div class="toolbar__right">
    <button>アクション1</button>
    <button>アクション2</button>
  </div>
></div>
```

```scss
/* toolbar.component.scss */
.toolbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 12px 20px;
  background: #fafafa;
  border-radius: 12px;
  gap: 16px;
}

.toolbar__right {
  display: flex;
  gap: 12px;
}

@media (max-width: 600px) {
  .toolbar {
    flex-direction: column;
    align-items: stretch;
  }
  .toolbar__right {
    justify-content: stretch;
  }
}
```

## ベストプラクティス
- ユーティリティクラス（`flex`, `flex-center`）をグローバルに定義して再利用性を高める
- `gap`プロパティを使うと余白調整がシンプルになる（Flexbox/ Grid共通）
- Flexboxは一方向レイアウトに最適。複雑な2次元レイアウトにはCSS Gridを検討する

## 注意点
- 古いブラウザでは`gap`がサポートされない場合があるため、フォールバックを検討する
- `flex: 1`など、余白の伸縮設定を適切に行わないと意図しないレイアウトになる
- ネストが深いFlexboxは可読性が下がるためコンポーネントに分割する

## 関連技術
- CSS Grid
- Tailwind CSSのFlexユーティリティ
- Angular CDK Layout
