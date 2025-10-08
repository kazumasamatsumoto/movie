# #212 「アコーディオン での活用例」

## 概要
コンテンツ投影を利用してアコーディオン（折りたたみ）コンポーネントを実装し、ヘッダーと本文を柔軟に差し替える方法を紹介します。

## 学習目標
- アコーディオン構造で投影スロットを設計する
- 親コンポーネントが任意のコンテンツを差し込めるアコーディオンを実装する
- コンテンツの開閉状態をコンポーネントが管理するパターンを学ぶ

## 技術ポイント
- **スロット**: `[accordion-header]`と`[accordion-body]`などの属性セレクタを使用
- **開閉制御**: Inputや内部状態で展開状態を管理し、CSS/アニメーションを適用
- **複数項目**: `@ContentChildren`で複数のアコーディオンアイテムを扱う場合もある

## 📺 画面表示用コード（動画用）

```html
<header (click)="toggle()">
  <ng-content select="[accordion-header]"></ng-content>
</header>
<section *ngIf="expanded">
  <ng-content select="[accordion-body]"></ng-content>
</section>
```

```html
<app-accordion>
  <h3 accordion-header>ヘッダー</h3>
  <p accordion-body>本文</p>
</app-accordion>
```

```scss
.accordion__body { transition: height 0.3s ease; }
```

## 💻 詳細実装例（学習用）
```typescript
// accordion.component.ts
import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-accordion',
  standalone: true,
  templateUrl: './accordion.component.html',
  styleUrls: ['./accordion.component.scss'],
})
export class AccordionComponent {
  @Input() expanded = false;

  toggle(): void {
    this.expanded = !this.expanded;
  }
}
```

```html
<!-- accordion.component.html -->
<section class="accordion">
  <header class="accordion__header" (click)="toggle()">
    <ng-content select="[accordion-header]"></ng-content>
  </header>
  <section class="accordion__body" *ngIf="expanded">
    <ng-content select="[accordion-body]"></ng-content>
  </section>
</section>
```

```scss
/* accordion.component.scss */
.accordion {
  border: 1px solid #e0e0e0;
  border-radius: 8px;
}
.accordion__header {
  padding: 12px;
  cursor: pointer;
  font-weight: 600;
}
.accordion__body {
  padding: 12px;
  border-top: 1px solid #e0e0e0;
}
```

```html
<!-- parent.component.html -->
<app-accordion>
  <h3 accordion-header>セクション1</h3>
  <p accordion-body>折りたたみ本文です。</p>
</app-accordion>
```

## ベストプラクティス
- アコーディオン全体を管理するコンテナ（複数の`app-accordion`）を用意し、`ContentChildren`でトグル制御を行うと便利
- アクセシビリティのため、`role="button"`や`aria-expanded`を付与する
- 投影スロットに複数要素を含める場合は`ng-container`でグルーピングする

## 注意点
- `*ngIf`で本文を切り替えると再描画コストが発生するため、アニメーションが必要なら`@angular/animations`を検討
- 投影コンテンツ内でフォームやインタラクションがある場合、閉じたときの状態保持に注意
- 状態を親と同期させたい場合は@Outputイベントを発火し、親が制御する

## 関連技術
- Multi Slot Projection
- `ContentChildren`による複数アコーディオンの管理
- Angular Animationsでの開閉アニメーション

