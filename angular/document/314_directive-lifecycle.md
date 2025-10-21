# #314 「Directive のライフサイクル」

## 概要
Directiveはコンポーネントと同様にライフサイクルフックを備えており、初期化、入力値の変化、クリーンアップのタイミングで安全に処理を行える。

## 学習目標
- Directiveで利用可能な主要ライフサイクルフックを理解する
- フックごとの責務と使い分けを学ぶ
- ライフサイクルに沿ったリソース管理を実践する

## 技術ポイント
- `OnInit`, `OnChanges`, `OnDestroy`, `AfterViewInit`などを実装可能
- Input処理は`ngOnChanges`、DOM操作の初期化は`ngOnInit`
- クリーンアップは`ngOnDestroy`で実施しリークを防ぐ

## 📺 画面表示用コード（動画用）
```typescript
@Directive({ selector: '[appAutoFocus]', standalone: true })
export class AutoFocusDirective implements OnInit, OnChanges, OnDestroy {
  @Input({ alias: 'appAutoFocus' }) enabled = true;
  constructor(private readonly el: ElementRef<HTMLInputElement>) {}
  ngOnInit(): void { if (this.enabled) this.el.nativeElement.focus(); }
  ngOnChanges(): void { if (this.enabled) this.el.nativeElement.focus(); }
  ngOnDestroy(): void { this.el.nativeElement.blur(); }
}
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appAutoFocus]',
  standalone: true
})
export class AutoFocusDirective implements OnInit, OnChanges, OnDestroy {
  @Input({ alias: 'appAutoFocus' }) enabled = true;
  @Input() focusDelay = 0;
  private timeoutId?: number;

  constructor(private readonly el: ElementRef<HTMLElement>) {}

  ngOnInit(): void {
    this.tryFocus();
  }

  ngOnChanges(): void {
    this.tryFocus();
  }

  ngOnDestroy(): void {
    if (this.timeoutId) {
      clearTimeout(this.timeoutId);
    }
  }

  private tryFocus(): void {
    if (!this.enabled) return;
    if (this.timeoutId) clearTimeout(this.timeoutId);
    this.timeoutId = window.setTimeout(() => this.el.nativeElement.focus(), this.focusDelay);
  }
}
```

## ベストプラクティス
- DOM準備が必要な処理は`ngOnInit`または`ngAfterViewInit`で実行する
- Inputの変化に応じた処理は`ngOnChanges`で直列化し、差分更新を意識する
- リスナー解除やタイマー停止を`ngOnDestroy`で徹底し、リークを防ぐ

## 注意点
- `OnChanges`は`SimpleChanges`を利用して前回値を参照すること
- SSRではブラウザAPIがないため、フック内での使用をガードする
- フックの呼び出し順序を理解し、同期/非同期の混在に注意する

## 関連技術
- OnInit / OnDestroy
- ChangeDetection
- Angular Signals
