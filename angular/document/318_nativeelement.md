# #318 「nativeElement の使用」

## 概要
`ElementRef.nativeElement`は実際のDOMノードを指し、直接操作するとパフォーマンスを最適化できるが、プラットフォーム依存や安全性の問題が伴う。

## 学習目標
- `nativeElement`を直接扱うリスクとメリットを理解する
- アクセス前に環境を確認する方法を学ぶ
- Renderer2などの代替手段と比較する

## 技術ポイント
- SSRやWeb Workerでは`nativeElement`が利用できない可能性がある
- 型キャストで要素の種類を明確にする
- 必要に応じて`isPlatformBrowser`で環境を分岐

## 📺 画面表示用コード（動画用）
```typescript
@Directive({ selector: '[appNativeSelect]', standalone: true })
export class NativeSelectDirective {
  constructor(private readonly el: ElementRef<HTMLSelectElement>) {}
  ngOnInit(): void {
    const select = this.el.nativeElement;
    if (select.options.length === 0) select.disabled = true;
  }
}
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appNativeSelect]',
  standalone: true
})
export class NativeSelectDirective implements OnInit {
  constructor(
    private readonly el: ElementRef<HTMLSelectElement>,
    @Inject(PLATFORM_ID) private readonly platformId: Object
  ) {}

  ngOnInit(): void {
    if (!isPlatformBrowser(this.platformId)) return;
    const select = this.el.nativeElement;
    if (select.options.length === 0) {
      select.disabled = true;
      select.title = '選択肢がありません';
    }
  }
}
```

## ベストプラクティス
- `nativeElement`に触れる前に`isPlatformBrowser`で確認し、SSR崩壊を防ぐ
- 可能ならRenderer2を利用し、`nativeElement`はどうしても必要な最小限の場面に限定する
- DOM変化に伴う副作用は`ngOnDestroy`で元に戻す

## 注意点
- 直接代入はXSSリスクを高めるため、ユーザー入力を埋め込まない
- ViewEncapsulationなしでスタイルを操作すると副作用が広がる
- テスト環境ではJSDOM等でAPIが異なる場合があるのでガードを設ける

## 関連技術
- PLATFORM_ID
- isPlatformBrowser
- Renderer2
