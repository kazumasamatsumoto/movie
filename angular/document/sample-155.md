# #155 「ElementRef の注意点とリスク」

## 概要
`ElementRef`を使用する際のセキュリティリスクやプラットフォーム依存性を理解し、安全な代替手段を検討するためのポイントを整理します。

## 学習目標
- ElementRefが抱えるリスク（XSS、SSR非対応等）を理解する
- DOM操作をRenderer2へ委譲するメリットを把握する
- ElementRef利用時の防御策を身につける

## 技術ポイント
- **XSSリスク**: `innerHTML`の直接書き換えは危険
- **SSRとの相性**: サーバーではDOMがないため`nativeElement`が利用できない
- **代替案**: Renderer2、Angular CDK、TemplateRefを活用

## 📺 画面表示用コード（動画用）

```typescript
this.element.nativeElement.innerHTML = userInput; // ❌ 危険
```

```typescript
if (isPlatformBrowser(this.platformId)) { ... }
```

```typescript
this.renderer.setProperty(element.nativeElement, 'textContent', safeText);
```

## 💻 詳細実装例（学習用）
```typescript
// safe-text.directive.ts
import { Directive, ElementRef, Inject, Input, PLATFORM_ID, Renderer2 } from '@angular/core';
import { isPlatformBrowser } from '@angular/common';

@Directive({
  selector: '[appSafeText]',
  standalone: true,
})
export class SafeTextDirective {
  @Input({ required: true }) appSafeText = '';

  constructor(
    private readonly elementRef: ElementRef<HTMLElement>,
    private readonly renderer: Renderer2,
    @Inject(PLATFORM_ID) private readonly platformId: object,
  ) {}

  ngOnChanges(): void {
    if (isPlatformBrowser(this.platformId)) {
      this.renderer.setProperty(
        this.elementRef.nativeElement,
        'textContent',
        this.appSafeText,
      );
    }
  }
}
```

```html
<!-- host.component.html -->
<p [appSafeText]="userInput"></p>
```

## ベストプラクティス
- 直接DOMを書き換える必要がある場合でもRenderer2やAngular CDKを優先する
- `innerHTML`のような危険なAPIを使う場合はDomSanitizerでサニタイズする
- SSR対応が必要なアプリでは、ElementRefを使用する前に`isPlatformBrowser`で環境を確認する

## 注意点
- ElementRefを注入しただけではテストしづらく、モックもしにくい
- ネイティブAPIに依存するとブラウザ差異が出る可能性がある
- イベントリスナーを直接追加するとAngularのゾーン外で実行されるため、change detectionと同期できないケースがある

## 関連技術
- Renderer2とRendererFactory2
- DomSanitizer
- Angular CDK（Overlay、Portal）による高度なDOM処理
