# #143 「ViewChildren での反復処理」

## 概要
`@ViewChildren`で取得した`QueryList`を使い、要素を順番に処理したりインデックス付きで操作する実践的なパターンを紹介します。

## 学習目標
- QueryListを反復処理する手法（forEach/配列化）を理解する
- インデックスや条件付き処理を組み合わせるテクニックを習得する
- ViewChildrenを利用したUI更新ロジックの組み立て方を学ぶ

## 技術ポイント
- **forEach**: QueryList自体に備わる反復処理
- **配列化**: `[...queryList].forEach((item, index) => ...)`
- **条件処理**: filterやfindで特定要素を抽出

```typescript
this.items.forEach((item, i) => item.nativeElement.dataset.index = `${i}`);
```

```typescript
const active = this.items.find((item) => item.nativeElement.classList.contains('active'));
```

```typescript
[...this.items].forEach((item, idx) => item.highlight(idx === 0));
```

## 💻 詳細実装例（学習用）
```typescript
// carousel.component.ts
import { AfterViewInit, Component, ElementRef, QueryList, ViewChildren } from '@angular/core';

@Component({
  selector: 'app-carousel',
  standalone: true,
  templateUrl: './carousel.component.html',
  styleUrls: ['./carousel.component.css'],
})
export class CarouselComponent implements AfterViewInit {
  @ViewChildren('slide')
  slides!: QueryList<ElementRef<HTMLDivElement>>;

  ngAfterViewInit(): void {
    [...this.slides].forEach((slide, index) => {
      slide.nativeElement.setAttribute('data-slide', `${index}`);
    });
    this.activate(0);
  }

  activate(index: number): void {
    this.slides.forEach((slide, idx) => {
      slide.nativeElement.classList.toggle('active', idx === index);
    });
  }
}
```

```html
<!-- carousel.component.html -->
<div class="carousel">
  <div #slide class="slide">スライド1</div>
  <div #slide class="slide">スライド2</div>
  <div #slide class="slide">スライド3</div>
</div>
<div class="controls">
  <button type="button" (click)="activate(0)">1</button>
  <button type="button" (click)="activate(1)">2</button>
  <button type="button" (click)="activate(2)">3</button>
</div>
```

```css
/* carousel.component.css */
.slide {
  display: none;
}
.slide.active {
  display: block;
}
```

## ベストプラクティス
- QueryListを配列化する場合は最新状態が必要なタイミングで行い、キャッシュしすぎない
- DOM操作はRenderer2を介して行うと安全性が高まる
- 大量の要素を操作するときは処理をバッチ化し、パフォーマンスを確保する

## 注意点
- QueryListを配列化した後に要素数が変わっても自動更新されない
- DOM操作が多い場合はコンポーネント分割やディレクティブ化を検討する
- 異なるテンプレート構造で参照名を再利用すると複雑化するため、明確な命名を行う

## 関連技術
- QueryListの`map`・`filter`メソッド
- `@ContentChildren`での反復処理
- Renderer2によるクラス付与/削除
