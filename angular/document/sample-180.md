# #180 「[ngStyle] 動的スタイル制御」

## 概要
`[ngStyle]`を用いてCSSプロパティを動的に変更する基本パターンを学び、コンポーネントの状態とスタイルを柔軟に連動させる方法を理解します。

## 学習目標
- `[ngStyle]`のオブジェクト構文で複数スタイルを変更する手順を理解する
- 単位指定（`.px`, `.em`など）やCSS変数への代入を習得する
- コンポーネントの状態ロジックとスタイルを整理して再利用性を高める

## 技術ポイント
- **基本構文**: `[ngStyle]="{ width: width + 'px', color: textColor }"`
- **ユニット指定**: `[ngStyle]="{ 'font-size.px': fontSize }"`
- **スタイルオブジェクト**: `get styleMap()`でまとめて返す

## 📺 画面表示用コード（動画用）

```html
<div [ngStyle]="{ 'font-size.px': fontSize, color: textColor }"></div>
```

```typescript
get styleMap() {
  return { width: `${progress}%`, background: color };
}
```

```html
<div [ngStyle]="styleMap"></div>
```

## 💻 詳細実装例（学習用）
```typescript
// progress-bar.component.ts
import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-progress-bar',
  standalone: true,
  templateUrl: './progress-bar.component.html',
  styleUrls: ['./progress-bar.component.scss'],
})
export class ProgressBarComponent {
  @Input() progress = 0;
  @Input() color = '#42a5f5';

  get styleMap(): Record<string, string> {
    return {
      width: `${this.progress}%`,
      background: this.color,
    };
  }
}
```

```html
<!-- progress-bar.component.html -->
<div class="progress-bar">
  <div class="progress-bar__inner" [ngStyle]="styleMap"></div>
</div>
```

```scss
/* progress-bar.component.scss */
.progress-bar {
  width: 100%;
  height: 8px;
  background: rgba(0, 0, 0, 0.1);
  border-radius: 999px;
  overflow: hidden;
}
.progress-bar__inner {
  height: 100%;
  transition: width 0.3s ease;
}
```

## ベストプラクティス
- スタイルロジックはコンポーネント側で計算し、テンプレートには`[ngStyle]="styleMap"`のように記述する
- CSS変数を`setProperty`で操作する場合はRenderer2を利用して安全性を確保する
- アニメーションや変化量が大きい場合はCSSトランジションを併用する

## 注意点
- スタイルオブジェクトはChange Detectionごとに再計算されるため、パフォーマンスに注意する
- `[ngStyle]`で頻繁に直接数値連結を行うより、getterで一度まとめた方が可読性が高い
- スタイルが複雑になった場合は専用コンポーネントやディレクティブに抽出する

## 関連技術
- `[ngClass]`によるクラス制御
- Renderer2/RendererFactory2
- Angular Animationsでのスタイル制御
