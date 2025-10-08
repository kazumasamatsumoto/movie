# #068 「ngAfterContentInit - コンテンツ投影後」

## 概要
`ng-content`で投影された外部コンテンツが初期化されるタイミングで処理を行う`ngAfterContentInit`の使いどころを学びます。

## 学習目標
- Content projection後に呼ばれるフックの役割を理解する
- `ContentChild` / `ContentChildren`で取得した要素を初期化する
- 初回と以後の更新でフックを使い分ける

## 技術ポイント
- **Content projection**: 親が提供するテンプレートを子が受け入れる仕組み
- **ngAfterContentInit**: 投影コンテンツがDOMに挿入された直後に1度だけ呼ばれる
- **ContentChild**: 投影された要素への参照を取得しプロパティを操作

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```typescript
@ContentChild('label', { static: true }) label?: ElementRef;
```

```typescript
ngAfterContentInit(): void {
  console.log(this.label?.nativeElement.textContent);
}
```

```html
<ng-content></ng-content>
```

## 💻 詳細実装例（学習用）
```typescript
import { AfterContentInit, Component, ContentChild, ElementRef } from '@angular/core';

@Component({
  selector: 'app-card',
  standalone: true,
  templateUrl: './card.component.html',
  styleUrls: ['./card.component.css'],
})
export class CardComponent implements AfterContentInit {
  @ContentChild('title', { static: true }) title?: ElementRef<HTMLSpanElement>;

  ngAfterContentInit(): void {
    if (this.title) {
      const text = this.title.nativeElement.textContent?.trim();
      console.log(`カードタイトル: ${text}`);
    }
  }
}
```

```html
<!-- card.component.html -->
<article class="card">
  <header>
    <ng-content select="[card-title]"></ng-content>
  </header>
  <section>
    <ng-content></ng-content>
  </section>
</article>
```

```html
<!-- host.component.html -->
<app-card>
  <span card-title #title>Lifecycleガイド</span>
  <p>投影されたコンテンツを初期化できます。</p>
</app-card>
```

## ベストプラクティス
- `static: true`を指定すると`ngOnInit`以前に参照できるが、基本は`ngAfterContentInit`で使用する
- 投影内容によって処理が変わる場合は、適切な属性セレクタで`select`を活用する
- `ngAfterContentChecked`で内容の更新を監視し、初期化は`ngAfterContentInit`に限定する

## 注意点
- コンテンツが非同期に変わる場合、`ngAfterContentInit`だけでは追跡できない
- `ElementRef`を直接操作するとXSSリスクがあるためRenderer2を検討する
- SSRではDOM操作ができないため、プラットフォームを考慮する

## 関連技術
- Content projection (`ng-content`)
- `ContentChildren`と`QueryList`
- Renderer2による安全なDOM操作
