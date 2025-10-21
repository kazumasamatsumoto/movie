# #319 「直接DOM操作の注意点」

## 概要
直接DOMを操作すると高速だが、プラットフォーム依存やセキュリティ問題、変更検知の破綻を招く恐れがあるため慎重な扱いが必要。

## 学習目標
- 直接DOM操作が引き起こすリスクを列挙できる
- 安全にDOMを扱うためのガード方法を習得する
- Renderer2やSignalsとの併用による代替策を理解する

## 技術ポイント
- SSR/Web WorkerではDOM APIが存在しない
- XSS対策としてサニタイズや`innerText`利用を検討
- ChangeDetectorRefを使ってUI更新を同期させる

## 📺 画面表示用コード（動画用）
```typescript
@Directive({ selector: '[appUnsafeDom]', standalone: true })
export class UnsafeDomDirective {
  constructor(private readonly el: ElementRef<HTMLElement>) {}
  ngOnInit(): void {
    if (typeof window === 'undefined') return;
    this.el.nativeElement.innerHTML = '<strong>危険</strong>';
  }
}
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appSafeDom]',
  standalone: true
})
export class SafeDomDirective implements OnInit {
  @Input({ alias: 'appSafeDom', required: true }) content!: string;

  constructor(
    private readonly renderer: Renderer2,
    private readonly el: ElementRef<HTMLElement>,
    @Inject(PLATFORM_ID) private readonly platformId: Object,
    private readonly sanitizer: DomSanitizer
  ) {}

  ngOnInit(): void {
    if (!isPlatformBrowser(this.platformId)) return;
    const safe = this.sanitizer.sanitize(SecurityContext.HTML, this.content) ?? '';
    this.renderer.setProperty(this.el.nativeElement, 'innerHTML', safe);
  }
}
```

## ベストプラクティス
- Renderer2やAngularのテンプレート構文で表現できる場合は直接DOM操作を避ける
- 必要な場合も環境チェックとサニタイズを行い、安全性を担保する
- 変更検知が必要なときは`NgZone.run`やSignalsを使ってUIと同期させる

## 注意点
- 外部ライブラリがDOMを書き換える場合はラッパーを用意し制御する
- innerHTMLやinsertAdjacentHTMLのようなAPIはXSSリスクが高い
- モバイルWebViewなど一部環境ではDOM APIの挙動が異なる

## 関連技術
- DomSanitizer
- PLATFORM_ID
- ChangeDetectorRef
