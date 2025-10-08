# #146 「ContentChild の基本構文」

## 概要
`@ContentChild`の基本構文を確認し、テンプレート参照変数や型指定による投影コンテンツの取得方法を整理します。

## 学習目標
- ContentChildデコレータの書式を理解する
- テンプレート参照変数・コンポーネント・ディレクティブを取得する方法を習得する
- 取得結果を利用するタイミングを把握する

## 技術ポイント
- **基本構文**: `@ContentChild('slot') slot?: ElementRef<HTMLDivElement>;`
- **型指定**: `@ContentChild(HeaderComponent) header?: HeaderComponent;`
- **ライフサイクル**: `ngAfterContentInit`で参照が利用可能

## 📺 画面表示用コード（動画用）

```html
<ng-content select="[slot=header]"></ng-content>
```

```typescript
@ContentChild('header')
header?: TemplateRef<unknown>;
```

```typescript
ngAfterContentInit() {
  console.log(this.header);
}
```

## 💻 詳細実装例（学習用）
```typescript
// wrapper.component.ts
import { AfterContentInit, Component, ContentChild, TemplateRef } from '@angular/core';

@Component({
  selector: 'app-wrapper',
  standalone: true,
  templateUrl: './wrapper.component.html',
})
export class WrapperComponent implements AfterContentInit {
  @ContentChild('header')
  headerTemplate?: TemplateRef<unknown>;

  ngAfterContentInit(): void {
    if (!this.headerTemplate) {
      console.warn('ヘッダーが提供されていません');
    }
  }
}
```

```html
<!-- wrapper.component.html -->
<article class="wrapper">
  <header>
    <ng-template
      [ngTemplateOutlet]="headerTemplate"
    ></ng-template>
  </header>
  <section>
    <ng-content></ng-content>
  </section>
</article>
```

```html
<!-- parent.component.html -->
<app-wrapper>
  <ng-template #header>
    <h2>投影ヘッダー</h2>
  </ng-template>
  <p>投影された本文</p>
</app-wrapper>
```

## ベストプラクティス
- 親にテンプレート参照を要求する場合は、参照名や必要な構造をドキュメント化する
- fallbackヘッダーを用意して、未提供時でもレイアウトが崩れないようにする
- TemplateRefをレンダリングする際は`ngTemplateOutlet`を利用すると柔軟

## 注意点
- ContentChildにアクセスできるのは投影が確定した`ngAfterContentInit`以降
- select属性で分岐した複数スロットの場合、ContentChildは指定された要素のみ取得する
- 親のテンプレート変更により参照が変わる可能性があるため、`ngAfterContentChecked`で再確認することもある

## 関連技術
- `@ContentChildren`
- `ngAfterContentInit` / `ngAfterContentChecked`
- `TemplateRef` と `ViewContainerRef`
