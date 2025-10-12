# #220 「Web Components との比較」

## 概要
Angularのコンテンツ投影（`ng-content`）とWeb Componentsの`<slot>`との違い・共通点を整理し、どちらを採用すべきかの判断材料を提供します。

## 学習目標
- Angularコンテンツ投影とWeb Components slotの仕組みを比較する
- ViewEncapsulation設定によるShadow DOM利用時の挙動を理解する
- プロジェクト要件に応じた選択基準を把握する

## 技術ポイント
- **Angular投影**: `ViewEncapsulation.Emulated`のもとでフレームワークが疑似的にスロットを処理
- **Web Components slot**: Shadow DOMを利用し、`<slot name="header">`などで完全に隔離されたスコープを提供
- **互換性**: Angularでも`ViewEncapsulation.ShadowDom`を指定すればネイティブslotが使用可能

## 📺 画面表示用コード（動画用）

```html
<!-- Angular -->
<ng-content select="[card-header]"></ng-content>
```

```html
<!-- Web Components -->
<slot name="header"></slot>
```

```typescript
encapsulation: ViewEncapsulation.ShadowDom
```

## 💻 詳細実装例（学習用）
```typescript
// shadow-card.component.ts
import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'app-shadow-card',
  standalone: true,
  template: `
    <article class="card">
      <header><slot name="header"></slot></header>
      <section><slot></slot></section>
    </article>
  `,
  styleUrls: ['./shadow-card.component.scss'],
  encapsulation: ViewEncapsulation.ShadowDom,
})
export class ShadowCardComponent {}
```

```html
<!-- Web Component利用例 -->
<app-shadow-card>
  <h3 slot="header">Web Components スロット</h3>
  <p>本文コンテンツ</p>
</app-shadow-card>
```

```html
<!-- Angularコンテンツ投影例 -->
<app-card>
  <h3 card-header>Angular コンテンツ投影</h3>
  <p>本文コンテンツ</p>
</app-card>
```

## ベストプラクティス
- Angularアプリ内で完結する場合は`ng-content`を利用し、Angularのライフサイクルと統合する
- Web Componentsとして外部配布する場合は`ViewEncapsulation.ShadowDom`とslotを利用し、フレームワークに依存しないAPIを提供する
- CSSカスタムプロパティやイベントインターフェースを揃え、どちらの方式でも一貫した体験を提供する

## 注意点
- Shadow DOMではグローバルスタイルが届かないため、必要なスタイルを内部に読み込むかCSS変数で渡す
- Angularコンテンツ投影はShadow DOMほど厳密に隔離されていないため、グローバルスタイルの影響を受ける
- Web Components化する際はバンドルサイズやポリフィル、ブラウザサポートを検討する

## 関連技術
- ViewEncapsulation（#162〜#165）
- CSSカスタムプロパティによるテーマ共有
- Angular ElementsでのWeb Componentsエクスポート


