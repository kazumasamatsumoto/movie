# #203 「ng-container との組み合わせ」

## 概要
`ng-container`を使って余分なDOMを生成せずにコンテンツ投影を整理する方法を学び、条件分岐やグルーピングをシンプルに記述します。

## 学習目標
- `ng-container`の役割とコンテンツ投影との併用パターンを理解する
- `*ngIf`/`*ngFor`など構造ディレクティブを用いた投影制御を習得する
- DOMに不要なラッパーを生成せずにテンプレート制御を行う

## 技術ポイント
- **非表示ラッパー**: `ng-container`はDOMに出力されず、子要素のみ描画される
- **条件制御**: `ng-container *ngIf="condition"`で投影の有無を制御
- **複数要素まとめ**: selectにマッチさせる要素群をひとまとめにできる

## 📺 画面表示用コード（動画用）

```html
<ng-container *ngIf="hasHeader">
  <ng-content select="[panel-header]"></ng-content>
</ng-container>
```

```html
<ng-container [ngSwitch]="variant">
  <ng-content *ngSwitchCase="'primary'" select="[primary]"></ng-content>
  <ng-content *ngSwitchDefault></ng-content>
</ng-container>
```

```html
<ng-container select="[card-body]"></ng-container>
```

## 💻 詳細実装例（学習用）
```html
<!-- accordion.component.html -->
<section class="accordion">
  <header class="accordion__header">
    <ng-content select="[accordion-header]"></ng-content>
  </header>
  <ng-container *ngIf="expanded; else collapsed">
    <section class="accordion__body">
      <ng-content select="[accordion-body]"></ng-content>
    </section>
  </ng-container>
  <ng-template #collapsed>
    <p class="accordion__placeholder">内容は折りたたまれています</p>
  </ng-template>
</section>
```

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
}
```

## ベストプラクティス
- DOM構造を汚さず条件分岐したい場合は`ng-container`を優先的に利用する
- 投影スロットの有無を`ng-container`と`*ngIf`で制御し、HTMLの階層を浅く保つ
- `ngSwitch`などと組み合わせ、複数の投影パターンを読みやすく記述する

## 注意点
- `ng-container`自体には属性を付与できないため、必要に応じて`div`など実要素を使う
- 多数の`ng-container`をネストすると読みづらくなるため、責務を分割する
- `select`にマッチさせる場合は、`ng-container`がセレクタ対象にならない点を理解する（中の要素が対象）

## 関連技術
- `ng-template`によるテンプレート管理
- `ContentChild`で投影判定
- `ngTemplateOutlet`による描画切り替え


