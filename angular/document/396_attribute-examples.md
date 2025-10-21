# #396 「Attribute Directive の実用例」

## 概要
Attribute Directiveはボタンのローディング状態、ツールチップ、ドラッグ操作など局所的なUI振る舞いを再利用できる形で提供するのに適している。

## 学習目標
- Attribute Directiveの代表的なユースケースを理解する
- 実務でよく使われる振る舞いをディレクティブとして切り出す方法を学ぶ
- コンポーネントとディレクティブの役割分担を意識する

## 技術ポイント
- ホスト要素へクラス・属性付与で状態を表現
- Renderer2でイベントに応じたDOM操作
- DIを利用してサービスと連携（例: Tooltipサービス）

## 📺 画面表示用コード（動画用）
```typescript
@Directive({ selector: '[appLoadingButton]', standalone: true })
export class LoadingButtonDirective {
  @Input() set appLoadingButton(loading: boolean) { this.renderer.setProperty(this.el.nativeElement, 'disabled', loading); }
  constructor(private readonly el: ElementRef<HTMLButtonElement>, private readonly renderer: Renderer2) {}
}
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appLoadingButton]',
  standalone: true
})
export class LoadingButtonDirective implements OnChanges {
  @Input() appLoadingButton = false;

  constructor(private readonly el: ElementRef<HTMLButtonElement>, private readonly renderer: Renderer2) {}

  ngOnChanges(): void {
    this.renderer.setProperty(this.el.nativeElement, 'disabled', this.appLoadingButton);
    this.renderer[this.appLoadingButton ? 'addClass' : 'removeClass'](this.el.nativeElement, 'is-loading');
  }
}

@Component({
  selector: 'app-loading-button-demo',
  standalone: true,
  imports: [CommonModule, LoadingButtonDirective],
  template: `
    <button type="button" [appLoadingButton]="loading" (click)="simulate()">送信</button>
  `
})
export class LoadingButtonDemoComponent {
  protected loading = false;
  protected simulate(): void {
    this.loading = true;
    setTimeout(() => (this.loading = false), 1200);
  }
}
```

## ベストプラクティス
- 小さな責務ごとにディレクティブ化し、組み合わせてUIを構築する
- 状態はInputsで受け取り外部管理し、副作用はディレクティブ内で完結
- Storybookなどで使い方を共有し、デザインシステムへ統合する

## 注意点
- 操作対象の要素型を明確にし、`ElementRef<HTMLButtonElement>`のように型付け
- ビジュアルのみならクラス付与にとどめ、直接DOMプロパティを変更しすぎない
- 複数ディレクティブが同じプロパティを制御する場合の競合に注意

## 関連技術
- Renderer2
- Storybook
- Design System実装
