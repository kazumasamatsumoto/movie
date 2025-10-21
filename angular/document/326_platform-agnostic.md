# #326 「プラットフォーム非依存の実装」

## 概要
ディレクティブをプラットフォーム非依存に実装することで、ブラウザ以外の環境（SSRやWeb Worker）でも安全に動作させられる。

## 学習目標
- プラットフォームごとの制約を理解する
- `PLATFORM_ID`や`isPlatformBrowser`で分岐する方法を学ぶ
- 依存サービスで環境別実装を切り替える

## 技術ポイント
- `inject(PLATFORM_ID)`またはコンストラクタで受け取る
- Renderer2を使いDOM依存コードを抽象化
- サービスに環境ごとの戦略を委譲

## 📺 画面表示用コード（動画用）
```typescript
@Directive({ selector: '[appPlatformSafe]', standalone: true })
export class PlatformSafeDirective implements OnInit {
  private readonly platformId = inject(PLATFORM_ID);
  constructor(private readonly el: ElementRef<HTMLElement>, private readonly r: Renderer2) {}
  ngOnInit(): void {
    if (!isPlatformBrowser(this.platformId)) return;
    this.r.setStyle(this.el.nativeElement, 'outline', '1px solid #0ea5e9');
  }
}
```

## 💻 詳細実装例（学習用）
```typescript
@Injectable({ providedIn: 'root' })
export class ClipboardPort {
  constructor(@Inject(PLATFORM_ID) private readonly platformId: Object) {}
  copy(text: string): Promise<void> {
    if (isPlatformBrowser(this.platformId)) {
      return navigator.clipboard.writeText(text);
    }
    return Promise.reject(new Error('Clipboard not available'));
  }
}

@Directive({
  selector: '[appClipboardButton]',
  standalone: true
})
export class ClipboardButtonDirective {
  @Input({ alias: 'appClipboardButton', required: true }) text!: string;
  private readonly platformId = inject(PLATFORM_ID);

  constructor(private readonly clipboard: ClipboardPort, private readonly el: ElementRef<HTMLButtonElement>) {}

  @HostListener('click')
  async handleClick(): Promise<void> {
    if (!isPlatformBrowser(this.platformId)) return;
    await this.clipboard.copy(this.text);
    this.el.nativeElement.setAttribute('data-copied', 'true');
  }
}
```

## ベストプラクティス
- ブラウザ限定APIを呼ぶ前に`isPlatformBrowser`でチェックする
- サービス層で環境別実装を用意し、Directiveからは抽象化されたAPIだけ使う
- 非ブラウザ環境では安全にスキップし、明示的なエラーメッセージを返す

## 注意点
- Hydration時に初期化するとSSRとのDOM差異が発生する可能性がある
- `window`や`document`を直接参照しないようにする
- Web WorkerではRenderer2も限定的に動作するため、利用メソッドを絞る

## 関連技術
- PLATFORM_ID
- isPlatformBrowser / isPlatformServer
- Angular Universal
