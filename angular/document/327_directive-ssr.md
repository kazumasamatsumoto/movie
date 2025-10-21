# #327 「SSR対応のDOM操作」

## 概要
SSR環境ではDOMが存在しないため、ディレクティブはブラウザでのみ実行するようガードし、Hydration時の差異を避ける必要がある。

## 学習目標
- SSRで直面するDOM操作の制約を理解する
- SSRとブラウザで分岐する実装パターンを学ぶ
- Hydrationと組み合わせて副作用を最小化する

## 技術ポイント
- `isPlatformBrowser`でブラウザ判定
- `APP_ID`や`TransferState`でSSRとのデータ共有
- 初期レンダリングとブラウザ初期化の副作用を揃える

## 📺 画面表示用コード（動画用）
```typescript
@Directive({ selector: '[appHydrateSafe]', standalone: true })
export class HydrateSafeDirective implements OnInit {
  private readonly platformId = inject(PLATFORM_ID);
  constructor(private readonly el: ElementRef<HTMLElement>, private readonly r: Renderer2) {}
  ngOnInit(): void {
    if (!isPlatformBrowser(this.platformId)) return;
    this.r.addClass(this.el.nativeElement, 'hydrated');
  }
}
```

## 💻 詳細実装例（学習用）
```typescript
@Injectable({ providedIn: 'root' })
export class HydrationStateService {
  private readonly key = makeStateKey<boolean>('hydrated-flag');
  constructor(private readonly state: TransferState) {}
  hasHydrated(): boolean {
    return this.state.get(this.key, false);
  }
  markHydrated(): void {
    this.state.set(this.key, true);
  }
}

@Directive({
  selector: '[appHydrateSafe]',
  standalone: true
})
export class HydrateSafeDirective implements OnInit {
  private readonly platformId = inject(PLATFORM_ID);

  constructor(
    private readonly el: ElementRef<HTMLElement>,
    private readonly renderer: Renderer2,
    private readonly hydrationState: HydrationStateService
  ) {}

  ngOnInit(): void {
    if (!isPlatformBrowser(this.platformId)) return;
    if (!this.hydrationState.hasHydrated()) {
      this.renderer.addClass(this.el.nativeElement, 'hydrated');
      this.hydrationState.markHydrated();
    }
  }
}
```

## ベストプラクティス
- SSR時は副作用を発生させず、ブラウザ初期化時に最小限の変更だけ行う
- Hydrationエラーを避けるため、HTML構造と属性をSSR時と一致させる
- 状態共有が必要な場合は`TransferState`でデータを受け渡す

## 注意点
- SSRで`requestAnimationFrame`や`window`を呼ぶと例外が発生する
- ハイドレーション前にDOMを変更すると差分が生じFlashが発生する
- Lazy loadされたディレクティブがクライアント側でのみ動く場合のフォールバックを検討する

## 関連技術
- Angular Universal
- TransferState
- Hydration
