# #199 「select ディレクティブでの選択」

## 概要
`select`属性にディレクティブセレクタを指定し、特定のディレクティブが付与された要素だけをコンテンツ投影で振り分ける方法を解説します。

## 学習目標
- ディレクティブセレクタを使ったスロット構成を理解する
- APIとしてディレクティブを提供し、役割を明示する設計を習得する
- `ContentChild`でディレクティブインスタンスを取得し、追加処理を行う例を把握する

## 技術ポイント
- **ディレクティブ指定**: `<ng-content select="appHighlight"></ng-content>` のように書く
- **役割分担**: ディレクティブを付けるだけでセレクタがマッチし、親は利用しやすい
- **拡張性**: ディレクティブにロジックを持たせ、投影先で追加機能を提供できる

## 📺 画面表示用コード（動画用）

```html
<ng-content select="appHighlightHeader"></ng-content>
<ng-content></ng-content>
```

```html
<app-card>
  <h3 appHighlightHeader>ヘッダー</h3>
  <p>本文</p>
</app-card>
```

```typescript
@Directive({ selector: '[appHighlightHeader]' })
```

## 💻 詳細実装例（学習用）
```typescript
// highlight-header.directive.ts
import { Directive } from '@angular/core';

@Directive({
  selector: '[appHighlightHeader]',
  standalone: true,
})
export class HighlightHeaderDirective {}
```

```typescript
// card.component.ts
import { Component } from '@angular/core';
import { HighlightHeaderDirective } from './highlight-header.directive';

@Component({
  selector: 'app-card',
  standalone: true,
  imports: [HighlightHeaderDirective],
  templateUrl: './card.component.html',
  styleUrls: ['./card.component.scss'],
})
export class CardComponent {}
```

```html
<!-- card.component.html -->
<article class="card">
  <header class="card__header">
    <ng-content select="appHighlightHeader"></ng-content>
  </header>
  <section class="card__body">
    <ng-content></ng-content>
  </section>
</article>
```

## ベストプラクティス
- ディレクティブ名は役割を示す形（`appModalHeader`, `appCardFooter`など）にして直感的にする
- ディレクティブに追加機能（スタイル適用、アクセシビリティ補助など）を実装すると利便性が高まる
- APIとしてディレクティブを提供する場合はドキュメントに使用例を記載する

## 注意点
- ディレクティブがスタンドアロンでない場合は`imports`に追加忘れがないか確認する
- 複数のディレクティブを対象にしたい場合、複数の`ng-content`を用意するか、selectに複合セレクタを使用する
- 親がディレクティブを付け忘れるとデフォルトスロットへ回ってしまうため、フォールバックを用意する

## 関連技術
- `ContentChild` / `ContentChildren`でディレクティブインスタンスを取得
- 属性セレクタ / クラスセレクタと組み合わせたAPI設計
- Angular Materialなどのライブラリでのスロット用ディレクティブ

