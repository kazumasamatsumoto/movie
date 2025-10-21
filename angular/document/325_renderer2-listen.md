# #325 「listen() でのイベント監視」

## 概要
`Renderer2.listen`はイベントを環境非依存に監視できるAPIで、解除関数を通じてクリーンアップを簡単に行える。

## 学習目標
- `listen`の呼び出し方と戻り値を理解する
- グローバルターゲット（document/window）への適用方法を学ぶ
- 解除忘れを防ぐパターンを習得する

## 技術ポイント
- 第1引数に`'document'`, `'window'`, または要素参照を指定
- 戻り値の解除関数を`ngOnDestroy`で呼び出す
- コールバック内でChangeDetectionやSignalを適切に更新する

## 📺 画面表示用コード（動画用）
```typescript
@Directive({ selector: '[appHoverLog]', standalone: true })
export class HoverLogDirective implements OnInit, OnDestroy {
  private detach?: () => void;
  constructor(private readonly el: ElementRef<HTMLElement>, private readonly r: Renderer2) {}
  ngOnInit(): void {
    this.detach = this.r.listen(this.el.nativeElement, 'mouseenter', () => console.log('hover'));
  }
  ngOnDestroy(): void { this.detach?.(); }
}
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appOutsideClick]',
  standalone: true
})
export class OutsideClickDirective implements OnInit, OnDestroy {
  @Output() outside = new EventEmitter<void>();
  private detach?: () => void;

  constructor(private readonly el: ElementRef<HTMLElement>, private readonly renderer: Renderer2) {}

  ngOnInit(): void {
    this.detach = this.renderer.listen('document', 'click', event => {
      if (!this.el.nativeElement.contains(event.target as Node)) {
        this.outside.emit();
      }
    });
  }

  ngOnDestroy(): void {
    this.detach?.();
  }
}
```

## ベストプラクティス
- 解除関数はプロパティに保持し、`ngOnDestroy`で必ず実行する
- ChangeDetectionが必要な場合は`NgZone.run`やSignalsを利用しUI更新と同期する
- グローバルリスナーは一括管理して、重複登録やメモリリークを避ける

## 注意点
- SSRではイベントが発火しないため、ブラウザ初期化時の安全な処理を用意する
- 多数のリスナーを登録するとパフォーマンスに影響するのでまとめる
- コールバック内で長時間処理を行うとUIスレッドをブロックする

## 関連技術
- NgZone
- takeUntilDestroyed
- Renderer2
