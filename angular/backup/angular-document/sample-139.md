# #139 「ViewChild で DOM 操作」

## 概要
`@ViewChild`で取得したDOM要素を操作する際の実践例と、安全なアプローチを整理します。

## 学習目標
- ElementRefを介した基本的なDOM操作を理解する
- Renderer2を使ってプラットフォームに依存しない操作を行う
- 操作タイミングとライフサイクルの関係を把握する

## 技術ポイント
- **ElementRef**: `nativeElement`経由でDOMアクセス
- **Renderer2**: `addClass`, `setStyle`, `listen`など安全な操作API
- **プラットフォーム判定**: SSR対応のため`isPlatformBrowser`を利用

```typescript
@ViewChild('panel') panel?: ElementRef<HTMLDivElement>;
```

```typescript
this.panel?.nativeElement.scrollIntoView();
```

```typescript
this.renderer.addClass(this.panel?.nativeElement, 'active');
```

## 💻 詳細実装例（学習用）
```typescript
// panel.component.ts
import { AfterViewInit, Component, ElementRef, Inject, PLATFORM_ID, Renderer2, ViewChild } from '@angular/core';
import { isPlatformBrowser } from '@angular/common';

@Component({
  selector: 'app-panel',
  standalone: true,
  templateUrl: './panel.component.html',
})
export class PanelComponent implements AfterViewInit {
  @ViewChild('panel') panel?: ElementRef<HTMLDivElement>;

  constructor(
    private readonly renderer: Renderer2,
    @Inject(PLATFORM_ID) private readonly platformId: object,
  ) {}

  ngAfterViewInit(): void {
    if (!isPlatformBrowser(this.platformId) || !this.panel) {
      return;
    }
    const element = this.panel.nativeElement;
    this.renderer.addClass(element, 'mounted');
    element.scrollIntoView({ behavior: 'smooth' });
  }
}
```

```html
<!-- panel.component.html -->
<div #panel class="panel">
  ViewChildでDOMを操作するデモ
}</div>
```

```css
/* panel.component.css */
.panel {
  border: 1px solid #ccc;
  padding: 16px;
}
.panel.mounted {
  border-color: #26a69a;
}
```

## ベストプラクティス
- 可能な限りRenderer2を利用し、直接のDOM操作を減らす
- SSR対応アプリではElementRefを使用する前に`isPlatformBrowser`でチェックする
- DOM操作を行うメソッドをコンポーネント内に閉じ、外部から繰り返し呼ばれるようにしない

## 注意点
- `nativeElement`を直接操作するとXSSなどのリスクが高まるため、信頼できるデータのみを扱う
- Angularの変更検知と競合しないよう、DOM操作後に状態変更が必要ならChangeDetectorRefを活用する
- CSSクラスやスタイルの付与はRenderer2の`addClass`や`setStyle`を使うことでブラウザ依存を減らす

## 関連技術
- Renderer2とRendererFactory2
- HostBinding/HostListenerでの装飾
- Angular CDKによるDOMユーティリティ
