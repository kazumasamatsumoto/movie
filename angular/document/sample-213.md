# #213 「レイアウト Component での活用例」

## 概要
コンテンツ投影を利用して、アプリ全体のレイアウト（ヘッダー・サイドバー・メインコンテンツなど）を共通化しつつ、ページごとに差し替え可能なレイアウトコンポーネントを構築する方法を学びます。

## 学習目標
- レイアウト領域を複数スロットに分ける設計を理解する
- 親コンポーネントが最小限のマークアップでページを構築できるレイアウトを実装する
- フォールバックコンテンツや可変領域を設計する方法を習得する

## 技術ポイント
- **スロット構成**: `[layout-header]`, `[layout-sidebar]`, `[layout-footer]` などで領域を定義
- **レスポンシブ対応**: CSS GridやFlexboxでレイアウトを調整
- **Optionalスロット**: サイドバーなど省略可能な領域はデフォルト表示を用意

## 📺 画面表示用コード（動画用）

```html
<ng-content select="[layout-header]"></ng-content>
<ng-content select="[layout-sidebar]"></ng-content>
<ng-content></ng-content>
<ng-content select="[layout-footer]"></ng-content>
```

```html
<app-layout>
  <header layout-header>ヘッダー</header>
  <aside layout-sidebar>サイドバー</aside>
  <main>本文</main>
  <footer layout-footer>フッター</footer>
</app-layout>
```

```scss
.layout { display: grid; grid-template-columns: 200px 1fr; }
```

## 💻 詳細実装例（学習用）
```typescript
// layout.component.ts
import { Component } from '@angular/core';

@Component({
  selector: 'app-layout',
  standalone: true,
  templateUrl: './layout.component.html',
  styleUrls: ['./layout.component.scss'],
})
export class LayoutComponent {}
```

```html
<!-- layout.component.html -->
<div class="layout">
  <header class="layout__header">
    <ng-content select="[layout-header]"></ng-content>
  </header>
  <aside class="layout__sidebar">
    <ng-content select="[layout-sidebar]"></ng-content>
  </aside>
  <main class="layout__content">
    <ng-content></ng-content>
  </main>
  <footer class="layout__footer">
    <ng-content select="[layout-footer]"></ng-content>
  </footer>
</div>
```

```scss
/* layout.component.scss */
.layout {
  display: grid;
  grid-template-columns: 240px 1fr;
  grid-template-rows: auto 1fr auto;
  grid-template-areas:
    'header header'
    'sidebar content'
    'footer footer';
  min-height: 100vh;
}
.layout__header {
  grid-area: header;
}
.layout__sidebar {
  grid-area: sidebar;
}
.layout__content {
  grid-area: content;
  padding: 24px;
}
.layout__footer {
  grid-area: footer;
}

@media (max-width: 768px) {
  .layout {
    grid-template-columns: 1fr;
    grid-template-areas:
      'header'
      'content'
      'footer';
  }
  .layout__sidebar {
    display: none;
  }
}
```

```html
<!-- parent.component.html -->
<app-layout>
  <header layout-header>
    <h1>アプリタイトル</h1>
  </header>
  <aside layout-sidebar>
    <nav>サイドメニュー</nav>
  </aside>
  <div>
    <p>ページごとの本文コンテンツをここに投影します。</p>
  </div>
  <footer layout-footer>
    <p>&copy; 2024 My Company</p>
  </footer>
</app-layout>
```

## ベストプラクティス
- レイアウトスロットの属性名を明確に定義し、ドキュメント化して他ページでも再利用しやすくする
- サイドバーなど省略可能な領域にはデフォルト表示（空状態）を用意する
- レイアウトCSSをGridやFlexboxで設計し、レスポンシブブレークポイントを統一する

## 注意点
- 投影領域が多すぎると利用者が分かりづらくなるため、必要最低限にとどめる
- レイアウトコンポーネントはスタイル依存が高いので、命名規則とスタイルガイドを整備する
- コンテンツ量が多いとスクロール挙動が変わるため、overflowなどの設定を適切に行う

## 関連技術
- CSS Grid / Flexboxレイアウト（#187, #188）
- `ContentChild`でスロット存在確認（#207）
- 再利用可能なコンポーネント設計（#214）

