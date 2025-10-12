# #204 「ng-template での投影」

## 概要
`ng-template`を使って親コンポーネントからテンプレートを投影し、子コンポーネント内で任意の場所・タイミングにレンダリングする方法を学びます。

## 学習目標
- 親が`ng-template`に参照名を付けて子へ渡す実装を理解する
- 子コンポーネントで`TemplateRef`を受け取り、`ViewContainerRef`や`ngTemplateOutlet`で描画する方法を習得する
- 動的なテンプレート差し込みによる柔軟なUI構築を身につける

## 技術ポイント
- **テンプレート定義**: 親側で`<ng-template #header>...</ng-template>`を用意
- **テンプレート受取**: 子で`@ContentChild('header', { read: TemplateRef })`を利用
- **描画**: `ViewContainerRef.createEmbeddedView(templateRef)`または`[ngTemplateOutlet]`

## 📺 画面表示用コード（動画用）

```html
<ng-template #header>
  <h3>テンプレートヘッダー</h3>
</ng-template>
```

```typescript
@ContentChild('header', { read: TemplateRef })
headerTemplate?: TemplateRef<unknown>;
```

```html
<ng-container *ngIf="headerTemplate" [ngTemplateOutlet]="headerTemplate"></ng-container>
```

## 💻 詳細実装例（学習用）
```typescript
// templated-card.component.ts
import { AfterContentInit, Component, ContentChild, TemplateRef, ViewContainerRef } from '@angular/core';

@Component({
  selector: 'app-templated-card',
  standalone: true,
  templateUrl: './templated-card.component.html',
  styleUrls: ['./templated-card.component.scss'],
})
export class TemplatedCardComponent implements AfterContentInit {
  @ContentChild('cardHeader', { read: TemplateRef })
  cardHeader?: TemplateRef<unknown>;

  constructor(private readonly vcr: ViewContainerRef) {}

  ngAfterContentInit(): void {
    if (this.cardHeader) {
      this.vcr.createEmbeddedView(this.cardHeader);
    }
  }
}
```

```html
<!-- templated-card.component.html -->
<article class="card">
  <header class="card__header">
    <ng-content select="[card-header]"></ng-content>
  </header>
  <section class="card__body">
    <ng-content></ng-content>
  </section>
</article>
```

```html
<!-- parent.component.html -->
<ng-template #customHeader>
  <h2 card-header>テンプレートで渡したヘッダー</h2>
</ng-template>

<app-templated-card>
  <ng-container *ngTemplateOutlet="customHeader"></ng-container>
  <p>本文コンテンツ</p>
</app-templated-card>
```

## ベストプラクティス
- TemplateRefの参照名（`#cardHeader`など）をAPIとして明確にし、使用方法を共有する
- `ngTemplateOutletContext`を使うことでテンプレートにデータを渡しやすくなる
- TemplateRefを複数受け取る場合はMulti Slot Projectionと組み合わせて構造を整理する

## 注意点
- TemplateRefは`ngAfterContentInit`以降で利用可能。早いタイミングで参照するとundefinedになる
- 動的レンダリングはViewContainerRefを直接使うと柔軟だが、描画位置を誤るとDOMが乱れるので注意
- TemplateRefが頻繁に切り替わる場合は再描画コストを測定し、必要に応じてキャッシュする

## 関連技術
- `ngTemplateOutlet`の詳細（#205）
- `ContentChild` で TemplateRef を取得
- `ViewContainerRef.createEmbeddedView`


