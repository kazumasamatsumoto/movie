# #182 「[ngStyle] 複数スタイル指定」

## 概要
`[ngStyle]`を使って複数のスタイルをまとめて指定・更新するパターンを紹介し、オブジェクト構文によるスタイル管理のベストプラクティスを学びます。

## 学習目標
- `[ngStyle]`のオブジェクト構文で複数プロパティを設定する手順を理解する
- スタイルオブジェクトをコンポーネント側で生成し、テンプレートを簡潔にする方法を習得する
- 状態に応じた複数スタイルの切り替えを整理する

## 技術ポイント
- **複数指定**: `[ngStyle]="{ background: bg, color: fg, 'border-radius.px': radius }"`
- **動的生成**: `get styleMap()`で状態に応じた値を返す
- **CSS変数**: `--spacing`などの変数をまとめて設定可能

```html
<div [ngStyle]="{ background: bgColor, color: textColor, 'padding.px': padding }"></div>
```

```typescript
get styleMap() {
  return {
    background: this.theme.background,
    color: this.theme.text,
    '--card-gap': `${this.theme.gap}px`,
  };
}
```

```html
<article [ngStyle]="styleMap"></article>
```

## 💻 詳細実装例（学習用）
```typescript
// card.component.ts
import { Component, Input } from '@angular/core';

type CardTheme = {
  background: string;
  text: string;
  gap: number;
};

@Component({
  selector: 'app-themed-card',
  standalone: true,
  templateUrl: './themed-card.component.html',
  styleUrls: ['./themed-card.component.scss'],
})
export class ThemedCardComponent {
  @Input() theme: CardTheme = {
    background: '#ffffff',
    text: '#263238',
    gap: 16,
  };

  get styleMap(): Record<string, string> {
    return {
      background: this.theme.background,
      color: this.theme.text,
      '--card-gap': `${this.theme.gap}px`,
    };
  }
}
```

```html
<!-- themed-card.component.html -->
<article class="card" [ngStyle]="styleMap">
  <ng-content></ng-content>
</article>
```

```scss
/* themed-card.component.scss */
.card {
  padding: var(--card-gap, 16px);
  border-radius: 12px;
  transition: background 0.3s ease;
}
```

## ベストプラクティス
- `styleMap`のようなgetterを用意し、テンプレートからは1行で参照する
- CSS変数を併用して子要素やShadow DOMにも値を伝播させる
- スタイルを計算するロジックはコンポーネント側に集約し、テンプレートに複雑な式を書かない

## 注意点
- `[ngStyle]`で設定されたスタイルはインラインスタイルになるため、優先度が高くなる点を意識する
- 変化が激しいスタイル（毎フレーム更新など）はCSSアニメーションやGPUアクセラレーションを検討する
- スタイルオブジェクトが大きくなる場合は型定義を用意し、IntelliSenseと可読性を向上させる

## 関連技術
- `[ngClass]` や Renderer2
- CSSカスタムプロパティ
- Angular Animations
