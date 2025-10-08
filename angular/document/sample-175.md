# #175 「動的スタイル変更」

## 概要
ユーザー操作やアプリケーション状態に応じてスタイルを動的に変更する方法をまとめ、`[ngClass]`/`[ngStyle]`やCSS変数を組み合わせた実装例を学びます。

## 学習目標
- Angularのバインディングでスタイルを動的に切り替える手順を理解する
- Renderer2やCSS変数を使った高度なスタイル変更を習得する
- 状態管理とスタイルロジックを整理して保守性を高める

## 技術ポイント
- **[ngClass]/[ngStyle]**: 状態に応じてクラスやスタイルを切り替える
- **CSS変数**: カラーテーマやサイズをランタイムに変更
- **Renderer2**: DOMレベルのstyle操作を安全に行う

## 📺 画面表示用コード（動画用）

```html
<div [ngClass]="{ 'is-active': active }"></div>
```

```html
<div [ngStyle]="{ 'font-size.px': fontSize }"></div>
```

```typescript
this.renderer.setStyle(el.nativeElement, '--card-radius', `${value}px`);
```

## 💻 詳細実装例（学習用）
```typescript
// dynamic-style.component.ts
import { Component, Renderer2 } from '@angular/core';

@Component({
  selector: 'app-dynamic-style',
  standalone: true,
  templateUrl: './dynamic-style.component.html',
  styleUrls: ['./dynamic-style.component.scss'],
})
export class DynamicStyleComponent {
  active = false;
  fontSize = 16;

  constructor(private readonly renderer: Renderer2) {}

  toggleActive(): void {
    this.active = !this.active;
  }

  increaseFont(): void {
    this.fontSize += 2;
  }
}
```

```html
<!-- dynamic-style.component.html -->
<div
  class="card"
  [ngClass]="{ 'card--active': active }"
  [ngStyle]="{ 'font-size.px': fontSize }"
>
  動的スタイルカード
</div>
<button (click)="toggleActive()">アクティブ切替</button>
<button (click)="increaseFont()">フォントサイズ +2</button>
```

```scss
/* dynamic-style.component.scss */
.card {
  transition: transform 0.3s ease, font-size 0.3s ease;
}
.card--active {
  transform: scale(1.05);
}
```

## ベストプラクティス
- 状態をSignalやComponentのプロパティで一元管理し、テンプレートから参照する
- 複雑な条件はコンポーネント側でクラスマップやスタイルオブジェクトにまとめて返す
- アニメーションを伴う場合はCSSトランジションやAngular Animationsを活用する

## 注意点
- 直接DOMを操作する場合はRenderer2を使い、SSR対応を考慮する
- 動的に生成されるスタイルが増えすぎるとパフォーマンスに影響することがあるため注意する
- クラス名やスタイルが散らばらないよう、命名と責務を明確にする

## 関連技術
- `[ngClass]` / `[ngStyle]`
- CSSカスタムプロパティ
- Angular Animations（`@angular/animations`）
