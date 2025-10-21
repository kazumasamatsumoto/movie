# #321 「Renderer2 のメソッド」

## 概要
Renderer2はDOM操作のための多様なメソッドを提供し、スタイルやクラス、属性、イベントリスナーなどを環境非依存に扱える。

## 学習目標
- Renderer2の代表的なメソッドと役割を整理する
- 各メソッドの使いどころを理解する
- メソッドの戻り値（解除関数など）を活用する

## 技術ポイント
- `setStyle`, `removeStyle`でスタイル変更
- `addClass`, `removeClass`でクラス切り替え
- `setAttribute`, `removeAttribute`, `listen`で属性とイベントを制御

## 📺 画面表示用コード（動画用）
```typescript
@Directive({ selector: '[appRendererGuide]', standalone: true })
export class RendererGuideDirective implements OnInit {
  constructor(private readonly el: ElementRef<HTMLElement>, private readonly r: Renderer2) {}
  ngOnInit(): void {
    const host = this.el.nativeElement;
    this.r.setStyle(host, 'color', '#1f2937');
    this.r.addClass(host, 'is-ready');
    this.r.setAttribute(host, 'data-state', 'ready');
    this.r.listen(host, 'click', () => this.r.removeClass(host, 'is-ready'));
  }
}
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appRendererGuide]',
  standalone: true
})
export class RendererGuideDirective implements OnInit, OnDestroy {
  private removeClick?: () => void;

  constructor(private readonly el: ElementRef<HTMLElement>, private readonly renderer: Renderer2) {}

  ngOnInit(): void {
    const host = this.el.nativeElement;
    this.renderer.setStyle(host, 'padding', '0.75rem 1rem');
    this.renderer.addClass(host, 'btn');
    this.renderer.addClass(host, 'btn--primary');
    this.renderer.setAttribute(host, 'role', 'button');
    this.removeClick = this.renderer.listen(host, 'click', () => {
      this.renderer.setStyle(host, 'opacity', '0.7');
      window.setTimeout(() => this.renderer.removeStyle(host, 'opacity'), 200);
    });
  }

  ngOnDestroy(): void {
    this.removeClick?.();
  }
}
```

## ベストプラクティス
- 同じメソッドを連続で呼ぶ場合は前回値を記録して差分だけ更新する
- `listen`の戻り値は必ず保持し、`ngOnDestroy`で解除する
- メソッド選択で責務を分離し、スタイルは`setStyle`よりクラス付与を優先する

## 注意点
- Renderer2は同期APIのため、重い処理をリスナー内で行わない
- 同一プロパティを複数ディレクティブで操作すると競合する恐れがある
- SSRで`listen`は実行されない点を想定しブラウザ初期化時の挙動を確認する

## 関連技術
- RendererStyleFlags2
- HostBinding / HostListener
- ChangeDetectorRef
