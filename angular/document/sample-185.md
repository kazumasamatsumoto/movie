# #185 「レスポンシブデザイン実装」

## 概要
Angularアプリでレスポンシブデザインを実装する基本戦略を整理し、CSSメディアクエリやAngular CDKのレイアウトツールを組み合わせた例を紹介します。

## 学習目標
- CSSメディアクエリを用いたレスポンシブレイアウトの構築方法を理解する
- Angular CDKのBreakPointObserverを使ってTypeScript側でレイアウトを切り替える方法を習得する
- コンポーネント構造とスタイル設計を連携させるベストプラクティスを把握する

## 技術ポイント
- **CSSメディアクエリ**: `@media (max-width: 600px) { ... }`
- **Flexbox/Grid**: モバイルファーストでレイアウトを構築
- **BreakPointObserver**: TypeScriptでブレークポイントを検知し、状態を切り替え

## 📺 画面表示用コード（動画用）

```scss
@media (max-width: 600px) {
  .layout {
    grid-template-columns: 1fr;
  }
}
```

```typescript
breakpointObserver.observe('(max-width: 600px)').subscribe(...);
```

```html
<div [class.is-mobile]="isMobile"></div>
```

## 💻 詳細実装例（学習用）
```scss
/* dashboard.component.scss */
.dashboard {
  display: grid;
  grid-template-columns: 240px 1fr;
  gap: 24px;
}

@media (max-width: 768px) {
  .dashboard {
    grid-template-columns: 1fr;
    gap: 16px;
  }
}
```

```typescript
// dashboard.component.ts
import { BreakpointObserver, Breakpoints } from '@angular/cdk/layout';
import { Component } from '@angular/core';
import { map } from 'rxjs/operators';

@Component({
  selector: 'app-dashboard',
  standalone: true,
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.scss'],
})
export class DashboardComponent {
  readonly isHandset$ = this.breakpointObserver
    .observe(Breakpoints.Handset)
    .pipe(map((state) => state.matches));

  constructor(private readonly breakpointObserver: BreakpointObserver) {}
}
```

```html
<!-- dashboard.component.html -->
<div class="dashboard" [class.dashboard--mobile]="(isHandset$ | async) ?? false">
  <aside class="dashboard__sidebar">サイドバー</aside>
  <main class="dashboard__main">メインコンテンツ</main>
</div>
```

## ベストプラクティス
- モバイルファーストでスタイルを記述し、ブレークポイントで上書きする
- 共通のブレークポイント変数をSCSSまたはTypeScriptで管理し、コンポーネント間で統一する
- BreakPointObserverを使ってTypeScript側でレイアウトやデータを切り替える場合は、可能な限り`async`パイプでテンプレートにバインドする

## 注意点
- 過剰なブレークポイントは保守が難しくなるため、デザインシステムのガイドラインに従う
- Flexbox/Gridを使う際、古いブラウザ対応が必要な場合はポリフィルやフォールバックを検討する
- BreakPointObserverの購読解除を忘れない（`takeUntilDestroyed`や`async`パイプで対応）

## 関連技術
- Angular CDK Layout (BreakPointObserver)
- CSS Grid/Flexbox
- Tailwind CSS や Bootstrap のレスポンシブユーティリティ
