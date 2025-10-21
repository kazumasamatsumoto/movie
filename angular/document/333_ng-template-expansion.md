# #333 「<ng-template> への展開」

## 概要
構造ディレクティブはコンパイル時に`<ng-template>`へ展開され、テンプレートを遅延生成する仕組みでDOM構造を制御する。

## 学習目標
- `<ng-template>`の役割と生成タイミングを理解する
- EmbeddedViewRefの仕組みを把握する
- カスタムディレクティブ実装でテンプレート展開を応用する

## 技術ポイント
- `<ng-template>`はレンダリング時にDOMへ直接出力されない
- ViewContainerRefが`createEmbeddedView`でテンプレートを実体化
- コンテキストオブジェクトでテンプレートに値を渡す

## 📺 画面表示用コード（動画用）
```html
<ng-template #emptyState>
  <p>データがありません。</p>
</ng-template>
```

## 💻 詳細実装例（学習用）
```typescript
interface EmptyContext {
  $implicit: number;
}

@Directive({
  selector: '[appEmptyState]',
  standalone: true
})
export class EmptyStateDirective implements OnChanges {
  @Input({ alias: 'appEmptyState', required: true }) count!: number;
  @Input() appEmptyStateTemplate?: TemplateRef<EmptyContext>;

  constructor(private readonly view: ViewContainerRef, private readonly defaultTpl: TemplateRef<EmptyContext>) {}

  ngOnChanges(): void {
    this.view.clear();
    if (this.count === 0) {
      const tpl = this.appEmptyStateTemplate ?? this.defaultTpl;
      this.view.createEmbeddedView(tpl, { $implicit: this.count });
    }
  }
}

@Component({
  selector: 'app-empty-demo',
  standalone: true,
  imports: [CommonModule, EmptyStateDirective],
  template: `
    <ul *appEmptyState="items.length; template: emptyTpl">
      <li *ngFor="let item of items">{{ item }}</li>
    </ul>
    <ng-template #emptyTpl let-count>
      <p>0件でした ({{ count }})</p>
    </ng-template>
  `
})
export class EmptyDemoComponent {
  protected items: string[] = [];
}
```

## ベストプラクティス
- `let-`構文でコンテキスト値をテンプレートへ受け渡し、再利用性を高める
- デフォルトテンプレートとカスタムテンプレートを切り替えられるAPIを用意する
- テンプレート内で複雑なロジックを避け、表示ロジックに専念させる

## 注意点
- `<ng-template>`はブラウザで直接見えないため、デバッグ時はAngular DevToolsなどを活用する
- EmbeddedViewを生成しっぱなしにするとメモリリークを招く
- テンプレート参照を渡すときは型を明示してIDE補完を活かす

## 関連技術
- EmbeddedViewRef
- TemplateRef
- Angular DevTools
