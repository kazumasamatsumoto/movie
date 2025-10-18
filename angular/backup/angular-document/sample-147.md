# #147 「ContentChild と ng-content」

## 概要
`ng-content`によるコンテンツプロジェクションと`@ContentChild`を組み合わせ、親から渡された要素やテンプレートを制御する方法を学びます。

## 学習目標
- `ng-content`のselect属性とContentChildの対応関係を理解する
- 投影されたテンプレートを内部で再描画する手順を習得する
- 複数スロット構成でのContentChildの扱い方を把握する

## 技術ポイント
- **ng-content**: 親が提供するコンテンツを配置
- **ContentChild**: 特定スロットのテンプレート参照を取得
- **ViewContainerRef**: 取得したテンプレートを任意の位置に挿入

```html
<ng-content select="[card-header]"></ng-content>
```

```typescript
@ContentChild('cardHeader')
header?: TemplateRef<unknown>;
```

```typescript
this.vcr.createEmbeddedView(this.header);
```

## 💻 詳細実装例（学習用）
```typescript
// layout-card.component.ts
import { AfterContentInit, Component, ContentChild, TemplateRef, ViewContainerRef } from '@angular/core';

@Component({
  selector: 'app-layout-card',
  standalone: true,
  templateUrl: './layout-card.component.html',
})
export class LayoutCardComponent implements AfterContentInit {
  @ContentChild('cardHeader')
  headerTemplate?: TemplateRef<unknown>;

  constructor(private readonly headerVcr: ViewContainerRef) {}

  ngAfterContentInit(): void {
    if (this.headerTemplate) {
      this.headerVcr.createEmbeddedView(this.headerTemplate);
    }
  }
}
```

```html
<!-- layout-card.component.html -->
<article class="layout-card">
  <header>
    <ng-container></ng-container>
  </header>
  <section>
    <ng-content></ng-content>
  </section>
</article>
```

```html
<!-- parent.component.html -->
<app-layout-card>
  <ng-template #cardHeader>
    <h3 card-header>親から渡したヘッダー</h3>
  </ng-template>
  <p>カード本文コンテンツ</p>
</app-layout-card>
```

## ベストプラクティス
- select属性でスロットを区別し、親は該当属性や参照名を付けてコンテンツを渡す
- ContentChildでテンプレートを取り出した後は`ngTemplateOutlet`や`ViewContainerRef`で描画する
- fallbackコンテンツを用意し、親が投影しない場合の表示を確保する

## 注意点
- `ng-content`の位置にそのままレンダリングする場合は、ContentChildで制御せずに`ng-content`を使用するだけで十分なケースもある
- ViewContainerRefを使ってテンプレートを挿入する際は、再描画で重複しないようにクリアする
- 複雑なスロット構成ではAPIドキュメントを整備し、親に渡してもらう要素を明示する

## 関連技術
- 多スロット構成（`<ng-content select="...">`）
- `@ContentChildren`による複数スロットの参照
- Angular Materialのコンテンツプロジェクションパターン
