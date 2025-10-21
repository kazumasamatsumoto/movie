# #403 「Directive クラスの基本構造」

## 概要
Directiveクラスは`@Directive`デコレータでメタデータを宣言し、クラス内で依存注入・ライフサイクルフック・HostBinding/HostListenerを実装する。

## 学習目標
- Directiveクラスの構成要素を理解する
- `@Directive`デコレータで指定できるプロパティを把握する
- ライフサイクルフックの活用方法を学ぶ

## 技術ポイント
- `selector`, `standalone`, `providers`, `exportAs`
- DIでElementRef, Renderer2, DestroyRefなどを注入
- `OnInit`, `OnDestroy`, `OnChanges`などを実装可能

## 📺 画面表示用コード（動画用）
```typescript
@Directive({ selector: '[appFocus]', standalone: true })
export class FocusDirective implements OnInit, OnDestroy {
  constructor(private readonly el: ElementRef<HTMLInputElement>) {}
  ngOnInit(): void { this.el.nativeElement.focus(); }
  ngOnDestroy(): void { this.el.nativeElement.blur(); }
}
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appAutoFocus]',
  standalone: true,
  exportAs: 'appAutoFocus'
})
export class AutoFocusDirective implements OnInit, OnDestroy {
  @Input() focusDelay = 0;
  private timeoutId?: number;

  constructor(private readonly el: ElementRef<HTMLElement>) {}

  ngOnInit(): void {
    this.timeoutId = window.setTimeout(() => this.el.nativeElement.focus(), this.focusDelay);
  }

  ngOnDestroy(): void {
    if (this.timeoutId) {
      clearTimeout(this.timeoutId);
    }
  }
}
```

## ベストプラクティス
- DIは`private readonly`で宣言し、ホスト要素操作を安全に行う
- フックを使って副作用の開始・終了を明示する
- `exportAs`でテンプレート参照を提供すると可視性が向上

## 注意点
- `constructor`ではDOM操作を行わず、`ngOnInit`まで待つ
- フックを実装したらインターフェースを忘れずに追加
- `@Directive`でprovidersを指定するとスコープがホスト要素に限定されることを理解する

## 関連技術
- ElementRef / Renderer2
- DestroyRef
- Angular Lifecycle Hooks
