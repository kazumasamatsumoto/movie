# #316 「ngOnDestroy でのクリーンアップ」

## 概要
`ngOnDestroy`はディレクティブ破棄時に呼ばれ、イベントリスナーやタイマー、Observable購読を解除して副作用を片付ける最後のチャンスとなる。

## 学習目標
- `ngOnDestroy`で解放すべきリソースを識別する
- Renderer2リスナーやSignal効果の解除方法を学ぶ
- クリーンアップをテストで検証する手法を把握する

## 技術ポイント
- `listen`が返す解除関数や`setInterval`のIDを保持
- `takeUntilDestroyed`や`destroyRef.onDestroy`を活用
- クリーンアップ後にDOMを元の状態へ戻す

## 📺 画面表示用コード（動画用）
```typescript
@Directive({ selector: '[appHoverIntent]', standalone: true })
export class HoverIntentDirective implements OnDestroy {
  private remove?: () => void;
  constructor(private readonly renderer: Renderer2, private readonly el: ElementRef<HTMLElement>) {
    this.remove = this.renderer.listen(this.el.nativeElement, 'mouseenter', () => {});
  }
  ngOnDestroy(): void { this.remove?.(); }
}
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appHoverIntent]',
  standalone: true
})
export class HoverIntentDirective implements OnInit, OnDestroy {
  private removeEnter?: () => void;
  private removeLeave?: () => void;
  private timer?: number;

  constructor(private readonly renderer: Renderer2, private readonly el: ElementRef<HTMLElement>) {}

  ngOnInit(): void {
    const element = this.el.nativeElement;
    this.removeEnter = this.renderer.listen(element, 'mouseenter', () => {
      this.timer = window.setTimeout(() => this.renderer.addClass(element, 'is-hover'), 150);
    });
    this.removeLeave = this.renderer.listen(element, 'mouseleave', () => {
      if (this.timer) clearTimeout(this.timer);
      this.renderer.removeClass(element, 'is-hover');
    });
  }

  ngOnDestroy(): void {
    this.removeEnter?.();
    this.removeLeave?.();
    if (this.timer) {
      clearTimeout(this.timer);
      this.timer = undefined;
    }
  }
}
```

## ベストプラクティス
- すべての解除関数やタイマーIDをプロパティとして保持し、`ngOnDestroy`でまとめて解放する
- `DestroyRef`を利用してクリーンアップ登録を一元化する
- ユニットテストで`ngOnDestroy`呼び出し後にリスナーが解除されたことをSpyで確認する

## 注意点
- `ngOnDestroy`が呼ばれないケース（アプリ強制終了等）も想定し、副作用がシステムに影響しないようにする
- DOM状態を変更した場合は必要に応じて元の状態へ戻す
- サービスへ登録したハンドラを取り除かないとメモリリークに繋がる

## 関連技術
- Renderer2.listen
- DestroyRef
- takeUntilDestroyed
