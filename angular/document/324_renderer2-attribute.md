# #324 「setAttribute() / removeAttribute()」

## 概要
`setAttribute`と`removeAttribute`はアクセシビリティやデータ属性を動的に制御する際に利用し、HTML仕様に従った値設定を可能にする。

## 学習目標
- 属性操作の仕組みと用途を理解する
- Boolean属性やARIA属性の扱い方を学ぶ
- 解除タイミングを管理する

## 技術ポイント
- Boolean属性は空文字で有効化、`removeAttribute`で解除
- `setAttribute`は文字列値を想定するため型変換する
- ARIA属性はアクセシビリティ向上に有効

## 📺 画面表示用コード（動画用）
```typescript
@Directive({ selector: '[appBusy]', standalone: true })
export class BusyDirective implements OnChanges {
  @Input({ alias: 'appBusy' }) busy = false;
  constructor(private readonly el: ElementRef<HTMLElement>, private readonly r: Renderer2) {}
  ngOnChanges(): void {
    if (this.busy) this.r.setAttribute(this.el.nativeElement, 'aria-busy', 'true');
    else this.r.removeAttribute(this.el.nativeElement, 'aria-busy');
  }
}
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appBusy]',
  standalone: true
})
export class BusyDirective implements OnChanges, OnDestroy {
  @Input({ alias: 'appBusy' }) busy = false;
  @Input() label?: string;

  constructor(private readonly el: ElementRef<HTMLElement>, private readonly renderer: Renderer2) {}

  ngOnChanges(): void {
    const host = this.el.nativeElement;
    if (this.busy) {
      this.renderer.setAttribute(host, 'aria-busy', 'true');
      this.renderer.setAttribute(host, 'aria-live', 'polite');
      if (this.label) {
        this.renderer.setAttribute(host, 'aria-label', this.label);
      }
    } else {
      this.renderer.removeAttribute(host, 'aria-busy');
      this.renderer.removeAttribute(host, 'aria-live');
      if (this.label) {
        this.renderer.removeAttribute(host, 'aria-label');
      }
    }
  }

  ngOnDestroy(): void {
    const host = this.el.nativeElement;
    this.renderer.removeAttribute(host, 'aria-busy');
    this.renderer.removeAttribute(host, 'aria-live');
    this.renderer.removeAttribute(host, 'aria-label');
  }
}
```

## ベストプラクティス
- ARIA属性を積極的に補完し、ユーザーの状況を支援する
- Boolean属性は`setAttribute`で空文字を渡し、解除時に`removeAttribute`する
- 変更前の値をキャッシュして差分更新を行うとDOM操作が最小化される

## 注意点
- ミススペルした属性名はHTMLにそのまま出力されるためレビューで検知する
- カスタム属性は`data-`プレフィックスを付けて仕様に従う
- attribute→propertyの違いを理解し、必要なら`setProperty`を使う

## 関連技術
- ARIA
- Renderer2
- Web Accessibility
