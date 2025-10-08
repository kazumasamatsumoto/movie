# #156 「Renderer2 での安全な DOM 操作」

## 概要
`Renderer2`を活用して、プラットフォーム非依存かつ安全にDOMを操作する方法を学びます。ElementRefよりも抽象化されたAPIで、SSRやWeb Worker環境でも動作します。

## 学習目標
- Renderer2の主要メソッド（`setStyle`, `addClass`, `listen`など）を理解する
- ElementRefとRenderer2の組み合わせ方を習得する
- SSR対応を考慮したDOM操作の基本を身につける

## 技術ポイント
- **安全な操作**: Renderer2はプラットフォームに合わせてDOM操作を抽象化
- **イベントハンドリング**: `renderer.listen(element, 'click', handler)`
- **スタイル操作**: `renderer.setStyle(element, 'color', '#fff')`

## 📺 画面表示用コード（動画用）

```typescript
constructor(private renderer: Renderer2) {}
```

```typescript
this.renderer.addClass(element, 'active');
```

```typescript
const unlisten = this.renderer.listen(element, 'click', handler);
```

## 💻 詳細実装例（学習用）
```typescript
// highlight.directive.ts
import { Directive, ElementRef, Input, OnDestroy, OnInit, Renderer2 } from '@angular/core';

@Directive({
  selector: '[appHighlight]',
  standalone: true,
})
export class HighlightDirective implements OnInit, OnDestroy {
  @Input() appHighlight = '#ffeb3b';

  private unlisten: (() => void) | null = null;

  constructor(
    private readonly elementRef: ElementRef<HTMLElement>,
    private readonly renderer: Renderer2,
  ) {}

  ngOnInit(): void {
    const el = this.elementRef.nativeElement;
    this.renderer.setStyle(el, 'transition', 'background-color .4s');
    this.renderer.listen(el, 'mouseenter', () =>
      this.renderer.setStyle(el, 'background-color', this.appHighlight),
    );
    this.unlisten = this.renderer.listen(el, 'mouseleave', () =>
      this.renderer.removeStyle(el, 'background-color'),
    );
  }

  ngOnDestroy(): void {
    this.unlisten?.();
  }
}
```

```html
<!-- app.component.html -->
<p appHighlight="#b2dfdb">Renderer2で安全にハイライト</p>
```

## ベストプラクティス
- DOM操作はRenderer2を通して行い、直接nativeElementを書き換えない
- 追加したイベントリスナーは`ngOnDestroy`で解除しメモリリークを防ぐ
- 複雑なDOM操作はディレクティブに切り出し、再利用しやすい形にする

## 注意点
- Renderer2でも生成する要素が多いとパフォーマンスに影響するため、必要な操作に留める
- SSR環境ではレンダラーがDOM APIを提供しない場合もあるため、操作が安全か確認する
- listenで登録したイベントは戻り値の関数を呼び出して解除することを忘れない

## 関連技術
- RendererFactory2でカスタムRendererを生成
- Angular CDKのDomPortal
- HostBinding/HostListenerでのクラス・スタイル操作
