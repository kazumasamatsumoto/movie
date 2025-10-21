# #320 「Renderer2 - 安全なDOM操作」

## 概要
Renderer2はAngularが提供する抽象化されたDOM操作APIで、ブラウザやSSR、Web Workerなど環境差を吸収しながら安全に操作できる。

## 学習目標
- Renderer2の役割とメリットを理解する
- 主なメソッドの用途を把握する
- ElementRefと組み合わせた実践的な使用方法を学ぶ

## 技術ポイント
- 依存注入で`Renderer2`を取得
- スタイル、属性、クラス、リスナーを環境依存なく操作
- 解除関数を保持してクリーンアップする

## 📺 画面表示用コード（動画用）
```typescript
@Directive({ selector: '[appElevate]', standalone: true })
export class ElevateDirective implements OnInit {
  constructor(private readonly el: ElementRef<HTMLElement>, private readonly r: Renderer2) {}
  ngOnInit(): void {
    const host = this.el.nativeElement;
    this.r.setStyle(host, 'transition', 'box-shadow .2s');
    this.r.listen(host, 'mouseenter', () => this.r.setStyle(host, 'boxShadow', '0 8px 24px rgba(15,23,42,.25)'));
  }
}
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appElevate]',
  standalone: true
})
export class ElevateDirective implements OnInit, OnDestroy {
  private removeEnter?: () => void;
  private removeLeave?: () => void;

  constructor(private readonly el: ElementRef<HTMLElement>, private readonly renderer: Renderer2) {}

  ngOnInit(): void {
    const host = this.el.nativeElement;
    this.renderer.setStyle(host, 'transition', 'box-shadow .2s');
    this.removeEnter = this.renderer.listen(host, 'mouseenter', () =>
      this.renderer.setStyle(host, 'boxShadow', '0 8px 24px rgba(15,23,42,.25)')
    );
    this.removeLeave = this.renderer.listen(host, 'mouseleave', () =>
      this.renderer.removeStyle(host, 'boxShadow')
    );
  }

  ngOnDestroy(): void {
    this.removeEnter?.();
    this.removeLeave?.();
  }
}
```

## ベストプラクティス
- 直接DOM操作ではなくRenderer2に委譲し、プラットフォーム互換性を確保する
- 解除関数をプロパティに保持し、`ngOnDestroy`で必ず呼び出す
- 繰り返し適用されるスタイルはクラス付与へ切り替え、余計なinlineスタイルを減らす

## 注意点
- Renderer2は同期APIなので重い処理をリスナー内で行うとUIが固まる
- SSRではリスナーが無視されるため、ブラウザ初期化時の挙動を確認する
- Renderer2はブラウザAPIではないため、直接アクセスできる機能には限りがある

## 関連技術
- ElementRef
- HostBinding / HostListener
- Angular SSR
