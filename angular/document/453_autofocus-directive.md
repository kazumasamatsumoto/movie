# #453 「AutoFocus Directive - 自動フォーカス」

## 概要
AutoFocusディレクティブは要素が表示されたタイミングで自動的にフォーカスを当てる機能を提供し、フォームやモーダルのユーザビリティを向上させる。

## 学習目標
- 自動フォーカス処理の基本を理解する
- 表示直後にフォーカスを当てるライフサイクルフックを学ぶ
- ブラウザ環境に限定してフォーカスを実行する方法を把握する

## 技術ポイント
- `ngAfterViewInit`または`ngOnInit`で`nativeElement.focus()`
- SSRではフォーカスを実行しない
- Inputで遅延時間や条件を設定可能

## 📺 画面表示用コード（動画用）
```typescript
ngAfterViewInit(): void { queueMicrotask(() => this.el.nativeElement.focus()); }
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appAutoFocus]',
  standalone: true
})
export class AutoFocusDirective implements AfterViewInit {
  @Input() appAutoFocus = true;
  @Input() focusDelay = 0;

  constructor(
    private readonly el: ElementRef<HTMLElement>,
    @Inject(PLATFORM_ID) private readonly platformId: Object
  ) {}

  ngAfterViewInit(): void {
    if (!this.appAutoFocus || !isPlatformBrowser(this.platformId)) return;
    window.setTimeout(() => this.el.nativeElement.focus(), this.focusDelay);
  }
}
```

## ベストプラクティス
- Inputでフォーカス有無や遅延時間を制御し、柔軟性を持たせる
- `isPlatformBrowser`でブラウザ環境に限定
- モーダル表示など非同期レンダリングでは適切な遅延を付与

## 注意点
- 強制フォーカスはユーザー制御を奪うため、必要な場面に限定
- iOSの入力要素ではフォーカスが動作しない場合がある
- SSRではDOMが存在しないため必ず環境判定を行う

## 関連技術
- AfterViewInit
- PLATFORM_ID / isPlatformBrowser
- FocusTrap
