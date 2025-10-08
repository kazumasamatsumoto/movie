# #208 「投影されたコンテンツの操作」

## 概要
`ContentChild`や`ContentChildren`を用いて投影されたコンテンツ（要素・ディレクティブ）の参照を取得し、子コンポーネント側でスタイルや動作を制御する方法を学びます。

## 学習目標
- 投影コンテンツのDOM要素を取得して操作する手順を理解する
- ディレクティブインスタンス経由でメソッドを呼び出す例を習得する
- Renderer2を使って安全に投影コンテンツを変更する

## 技術ポイント
- **ElementRef操作**: 投影されたDOMへアクセスしてフォーカスやクラス操作を行う
- **ディレクティブ活用**: 投影元にディレクティブを付与し、子がAPIとして利用
- **Renderer2**: 直接DOMを触らず安全にスタイルや属性を変更

## 📺 画面表示用コード（動画用）

```typescript
@ContentChild('focusable', { read: ElementRef })
focusable?: ElementRef<HTMLInputElement>;
```

```typescript
this.renderer.addClass(this.focusable?.nativeElement, 'highlight');
```

```typescript
@ContentChild(MyDirective) directive?: MyDirective;
this.directive?.run();
```

## 💻 詳細実装例（学習用）
```typescript
// project-operator.component.ts
import { AfterContentInit, Component, ContentChild, ElementRef, Renderer2 } from '@angular/core';
import { HighlightDirective } from './highlight.directive';

@Component({
  selector: 'app-project-operator',
  standalone: true,
  imports: [HighlightDirective],
  templateUrl: './project-operator.component.html',
})
export class ProjectOperatorComponent implements AfterContentInit {
  @ContentChild('focusEl', { read: ElementRef })
  focusEl?: ElementRef<HTMLInputElement>;

  @ContentChild(HighlightDirective)
  highlight?: HighlightDirective;

  constructor(private readonly renderer: Renderer2) {}

  ngAfterContentInit(): void {
    if (this.focusEl) {
      this.focusEl.nativeElement.focus();
      this.renderer.addClass(this.focusEl.nativeElement, 'focused');
    }
    this.highlight?.activate();
  }
}
```

```typescript
// highlight.directive.ts
import { Directive, ElementRef, Renderer2 } from '@angular/core';

@Directive({
  selector: '[appHighlight]',
  standalone: true,
})
export class HighlightDirective {
  constructor(private readonly el: ElementRef<HTMLElement>, private readonly renderer: Renderer2) {}

  activate(): void {
    this.renderer.setStyle(this.el.nativeElement, 'background', '#fff9c4');
  }
}
```

```html
<!-- parent.component.html -->
<app-project-operator>
  <input #focusEl appHighlight placeholder="投影された入力" />
</app-project-operator>
```

## ベストプラクティス
- 投影コンテンツに付与するディレクティブをAPIとして設計し、子コンポーネントでメソッドを呼び出せるようにする
- DOM操作はRenderer2を経由し、SSRやセキュリティを意識する
- 投影要素の存在が前提の場合はフォールバックや警告を用意する

## 注意点
- 投影コンテンツを直接操作すると親の設計に依存するため、必要最小限の操作に留める
- `ContentChild`で取得できるのは最初の要素のみ。複数操作する場合は`ContentChildren`を使用する
- ElementRefを直接操作する際はプラットフォームによる影響を確認し、SSRでは防御的なコーディングを行う

## 関連技術
- `ContentChild` / `ContentChildren`
- Renderer2によるDOM操作
- 投影コンテンツのデバッグ (#216)

