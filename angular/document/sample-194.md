# #194 「Multi Slot Projection - 複数スロット」

## 概要
複数の`ng-content`と`select`属性を使って、親コンポーネントから渡されたコンテンツを複数のスロットに振り分ける「Multi Slot Projection」を実装します。

## 学習目標
- 複数スロットにコンテンツを投影する基本構造を理解する
- `select`属性でセレクタを指定し、コンテンツを適切な場所へ挿入する
- 未マッチコンテンツの扱いとフォールバック戦略を把握する

## 技術ポイント
- **select属性**: CSSセレクタで投影対象を絞り込む
- **順序**: `ng-content`の宣言順にセレクタが評価され、マッチした要素が差し込まれる
- **フォールバック**: マッチしなかった要素は最後の`ng-content`（selectなし）へ送られる

## 📺 画面表示用コード（動画用）

```html
<ng-content select="[card-header]"></ng-content>
<ng-content></ng-content>
<ng-content select="[card-footer]"></ng-content>
```

```html
<app-card>
  <div card-header>ヘッダー</div>
  <p>本文</p>
  <div card-footer>フッター</div>
</app-card>
```

```scss
.card__header { font-weight: 600; }
.card__footer { text-align: right; }
```

## 💻 詳細実装例（学習用）
```typescript
// card.component.ts
import { Component } from '@angular/core';

@Component({
  selector: 'app-card',
  standalone: true,
  templateUrl: './card.component.html',
  styleUrls: ['./card.component.scss'],
})
export class CardComponent {}
```

```html
<!-- card.component.html -->
<article class="card">
  <header class="card__header">
    <ng-content select="[card-header]"></ng-content>
  </header>
  <section class="card__body">
    <ng-content></ng-content>
  </section>
  <footer class="card__footer">
    <ng-content select="[card-footer]"></ng-content>
  </footer>
</article>
```

```html
<!-- parent.component.html -->
<app-card>
  <h3 card-header>複数スロットカード</h3>
  <p>本文コンテンツをここに差し込みます。</p>
  <button card-footer>閉じる</button>
</app-card>
```

## ベストプラクティス
- スロットの名前（セレクタ）はAPIとして命名し、利用者が直感的に理解できるものにする
- 未指定の場合に備えてデフォルトコンテンツやメッセージを用意する
- スロット数が多い場合は責務を分割し、シンプルなコンポーネント構造を保つ

## 注意点
- セレクタが複雑だと意図せずマッチしない場合があるため、クラスや属性ベースのシンプルな指定が望ましい
- 画面リーダーなどアクセシビリティを考慮し、構造的なHTMLタグを使う
- 投影コンテンツが重い場合は`@defer`や`*ngIf`で必要なタイミングだけ描画する

## 関連技術
- `select`でのタグ・クラス・属性指定（#195〜#199）
- `ContentChild`/`ContentChildren`
- `ngTemplateOutlet`でのテンプレート切り替え

