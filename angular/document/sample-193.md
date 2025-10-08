# #193 「Single Slot Projection - 単一スロット」

## 概要
単一の`ng-content`を用いた基本的なコンテンツ投影（シングルスロット）を理解し、親が渡す任意のHTMLをそのまま表示するラッパーコンポーネントを実装します。

## 学習目標
- `ng-content`を1つだけ用いた単一スロット投影の構造を理解する
- シンプルなラッパーコンポーネントで投影を活用する
- 親コンポーネントからのコンテンツ注入例を把握する

## 技術ポイント
- **単一スロット**: `select`属性を持たない`ng-content`は投影内容をそのまま挿入
- **汎用コンポーネント**: 親が自由に内容を差し込めるカード・ラッパーに適用しやすい
- **スコープ**: 投影されたテンプレートは親コンポーネントのスコープで評価

## 📺 画面表示用コード（動画用）

```html
<section class="wrapper">
  <ng-content></ng-content>
</section>
```

```html
<app-wrapper>
  <p>ここに任意のHTMLを差し込めます</p>
</app-wrapper>
```

```scss
.wrapper { padding: 16px; border: 1px solid #ddd; }
```

## 💻 詳細実装例（学習用）
```typescript
// wrapper.component.ts
import { Component } from '@angular/core';

@Component({
  selector: 'app-wrapper',
  standalone: true,
  templateUrl: './wrapper.component.html',
  styleUrls: ['./wrapper.component.scss'],
})
export class WrapperComponent {}
```

```html
<!-- wrapper.component.html -->
<section class="wrapper">
  <ng-content></ng-content>
</section>
```

```scss
/* wrapper.component.scss */
.wrapper {
  padding: 16px;
  border-radius: 8px;
  background: #fafafa;
}
```

```html
<!-- parent.component.html -->
<app-wrapper>
  <h3>単一スロット投影</h3>
  <p>親から渡した要素がそのまま表示されます。</p>
</app-wrapper>
```

## ベストプラクティス
- 単一スロットでは構造を制限しないため、ドキュメントで期待する使用例を示す
- 見た目だけを提供し、コンテンツは親側に委ねる「ラッパー」コンポーネントに適している
- 投影がないケースに備え、デフォルトメッセージや空状態スタイルを用意しておく

## 注意点
- 子コンポーネントから投影コンテンツの内部に直接バインディングはできない（親スコープで実行）
- 表示切り替えには`*ngIf`を親側で使うか、子で`ContentChild`を検査して条件分岐する
- 複数領域が必要になったらMulti Slot Projectionへ拡張する

## 関連技術
- Multi Slot Projection（#194）
- `ContentChild`で投影要素の存在チェック
- `ngTemplateOutlet`によるテンプレート再描画

