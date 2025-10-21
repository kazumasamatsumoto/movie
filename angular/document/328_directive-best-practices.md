# #328 「Directive のベストプラクティス」

## 概要
Directiveは責務を小さく保ち、DOM操作を抽象化し、クリーンなライフサイクル管理を行うことで再利用性と安全性が向上する。

## 学習目標
- Directive設計で重視すべき原則を体系的に理解する
- クリーンなライフサイクル管理の実装を学ぶ
- テストやドキュメントを通じた品質維持の手法を知る

## 技術ポイント
- Renderer2とDestroyRefで副作用管理
- Input/Outputで明確な契約を定義
- プラットフォーム判定やサニタイズで安全性を確保

## 📺 画面表示用コード（動画用）
```typescript
@Directive({ selector: '[appBestDirective]', standalone: true })
export class BestDirective {
  constructor(private readonly el: ElementRef<HTMLElement>, private readonly renderer: Renderer2, destroyRef: DestroyRef) {
    const off = this.renderer.listen(this.el.nativeElement, 'focus', () => {});
    destroyRef.onDestroy(off);
  }
}
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appAccessibleTooltip]',
  standalone: true
})
export class AccessibleTooltipDirective implements OnInit {
  @Input({ alias: 'appAccessibleTooltip', required: true }) message!: string;
  @Input() placement: 'top' | 'bottom' = 'top';
  private readonly platformId = inject(PLATFORM_ID);
  private cleanup: VoidFunction[] = [];

  constructor(private readonly el: ElementRef<HTMLElement>, private readonly renderer: Renderer2, destroyRef: DestroyRef) {
    destroyRef.onDestroy(() => this.cleanup.forEach(fn => fn()));
  }

  ngOnInit(): void {
    if (!isPlatformBrowser(this.platformId)) return;
    const host = this.el.nativeElement;
    this.renderer.setAttribute(host, 'role', 'tooltip');
    this.renderer.setAttribute(host, 'data-placement', this.placement);
    this.cleanup.push(this.renderer.listen(host, 'focus', () => this.renderer.addClass(host, 'is-active')));
    this.cleanup.push(this.renderer.listen(host, 'blur', () => this.renderer.removeClass(host, 'is-active')));
  }
}
```

## ベストプラクティス
- 責務をUIの振る舞いに限定し、ビジネスロジックはサービスやSignalsへ委譲する
- DestroyRefや解除関数を活用して副作用を確実にクリーンアップする
- 入力値には型とデフォルトを与え、APIの契約をドキュメント化する
- Renderer2とプラットフォーム判定で環境依存コードを排除する

## 注意点
- Directiveが肥大化したらコンポーネント分割やサービス抽出を検討する
- イベントリスナーやタイマーの解除漏れはメモリリークに直結する
- 利用ルールを共有しないと他チームが誤用するため、サンプルコードやStorybookで周知する

## 関連技術
- DestroyRef
- Angular Style Guide
- Storybook / ドキュメント整備
