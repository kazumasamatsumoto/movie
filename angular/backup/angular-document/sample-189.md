# #189 「スタイリングのパフォーマンス」

## 概要
スタイルがレンダリングパフォーマンスへ与える影響を理解し、Angularアプリで快適な描画を維持するための最適化手法を整理します。

## 学習目標
- CSSセレクタの複雑さやアニメーションがパフォーマンスへ与える影響を理解する
- Angular特有の変更検知とスタイル適用の関係を把握する
- Lighthouseなどでパフォーマンスを測定し、改善サイクルを回す方法を学ぶ

## 技術ポイント
- **セレクタ最適化**: クラスセレクタ中心にし、深いネストやユニバーサルセレクタを避ける
- **アニメーション最適化**: GPUアクセラレーションが効く`transform`や`opacity`を利用
- **レンダリング抑制**: `@defer`, `*ngIf`で不要なDOMを描画しない

```scss
/* ✅ クラスセレクタ */
.card__title { font-weight: 600; }
```

```scss
/* ❌ 非推奨: 子孫セレクタの深いネスト */
.layout .sidebar .menu li a { ... }
```

```scss
/* アニメーションはtransform/opacityを使用 */
.fade { transition: opacity 0.3s; }
```

## 💻 詳細実装例（学習用）
```scss
/* bad-example.scss */
div ul li a {
  color: #fff;
}
```

```scss
/* optimized.scss */
.nav__link {
  color: #fff;
}
```

```typescript
// heavy-list.component.ts
import { Component, signal } from '@angular/core';

@Component({
  selector: 'app-heavy-list',
  standalone: true,
  templateUrl: './heavy-list.component.html',
  styleUrls: ['./heavy-list.component.scss'],
})
export class HeavyListComponent {
  readonly items = signal(Array.from({ length: 1000 }, (_, i) => `Item ${i}`));
}
```

```html
<!-- heavy-list.component.html -->
<ul class="list">
  <li class="list__item" @for (item of items(); track item)>{{ item }}</li>
</ul>
```

```scss
/* heavy-list.component.scss */
.list {
  padding: 0;
  margin: 0;
}
.list__item {
  list-style: none;
  padding: 8px 12px;
}
```

## ベストプラクティス
- セレクタはクラス中心とし、子孫セレクタを最小限にする
- `will-change`, `transform`, `opacity`を利用してアニメーションのリフローを避け、`transition`も必要なプロパティだけに限定する
- 大量要素のレンダリングでは`trackBy`（`@for`や`*ngFor`のtrack句）を利用し、不要なDOM更新を防ぐ
- LighthouseやChrome DevTools Performanceパネルでパフォーマンスを計測し、スタイルの影響を検証する

## 注意点
- インラインスタイル（`[ngStyle]`）を多用すると優先度が高くなり、後で上書きが難しくなる
- アニメーションとAngularの変更検知が同時に走ると、パフォーマンスが低下することがある
- `ViewEncapsulation.None`を多用するとカスケードが複雑化し、レンダリングのコストが増える可能性がある

## 関連技術
- Angular ChangeDetectionStrategy.OnPush
- DevTools Performance/Renderingパネル
- CSS Containment、GPUアクセラレーション
