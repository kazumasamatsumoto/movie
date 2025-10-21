# #323 「addClass() / removeClass()」

## 概要
`addClass`と`removeClass`はRenderer2でクラスを安全に付け替えるためのメソッドで、スタイルの管理をCSSに委ねられる。

## 学習目標
- クラス操作の基本パターンを習得する
- 条件付きでクラスを切り替える実装を理解する
- 差分適用で無駄なDOM操作を避ける

## 技術ポイント
- 複数クラスはループで個別に操作
- 前回状態を保持して不要な呼び出しを減らす
- teardown時に必要ならクラスを外す

## 📺 画面表示用コード（動画用）
```typescript
@Directive({ selector: '[appActiveClass]', standalone: true })
export class ActiveClassDirective implements OnChanges {
  @Input({ alias: 'appActiveClass' }) active = false;
  constructor(private readonly el: ElementRef<HTMLElement>, private readonly r: Renderer2) {}
  ngOnChanges(): void {
    if (this.active) this.r.addClass(this.el.nativeElement, 'is-active');
    else this.r.removeClass(this.el.nativeElement, 'is-active');
  }
}
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appStateClasses]',
  standalone: true
})
export class StateClassesDirective implements OnChanges, OnDestroy {
  @Input() states: string[] = [];
  private applied = new Set<string>();

  constructor(private readonly el: ElementRef<HTMLElement>, private readonly renderer: Renderer2) {}

  ngOnChanges(): void {
    const host = this.el.nativeElement;
    const next = new Set(this.states);
    for (const name of this.applied) {
      if (!next.has(name)) {
        this.renderer.removeClass(host, name);
        this.applied.delete(name);
      }
    }
    for (const name of next) {
      if (!this.applied.has(name)) {
        this.renderer.addClass(host, name);
        this.applied.add(name);
      }
    }
  }

  ngOnDestroy(): void {
    const host = this.el.nativeElement;
    for (const name of this.applied) {
      this.renderer.removeClass(host, name);
    }
    this.applied.clear();
  }
}
```

## ベストプラクティス
- クラス名はプレフィックス付きにして責務を明確にする
- 付け外しの差分を追跡し、不要なDOM操作を防ぐ
- 状態をInputで受け取り、テンプレート側から真偽値を管理する

## 注意点
- 既存クラスと衝突しないよう命名規則をドキュメント化する
- Tailwindなどのユーティリティクラスは大量になるため、取り扱うクラスを事前に限定する
- SSRでは初期状態とブラウザ初期化時の状態が一致するか検証する

## 関連技術
- Renderer2
- CSS Utilityクラス
- Signalsによる状態管理
