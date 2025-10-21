# #308 「Directive の作成方法」

## 概要
Angular CLIを使えばDirectiveの雛形を即座に生成でき、selectorやAPIを整えるだけで再利用可能な振る舞いを追加できる。

## 学習目標
- `ng g directive`コマンドの使い方を理解する
- 生成されたファイルの主要構成を把握する
- Standaloneディレクティブの登録方法を習得する

## 技術ポイント
- CLIで生成する際は`--standalone`オプションを付与
- selectorと`@Input`を用途に合わせて調整
- 利用側で`imports`に追加すれば即座に使用できる

## 📺 画面表示用コード（動画用）
```bash
ng g directive shared/highlight --standalone
# create src/app/shared/highlight.directive.ts
# create src/app/shared/highlight.directive.spec.ts
```

## 💻 詳細実装例（学習用）
```typescript
// CLIで生成された雛形を編集
@Directive({
  selector: '[appHighlight]',
  standalone: true
})
export class HighlightDirective implements OnInit {
  @Input() appHighlight = '#ffe066';

  constructor(private readonly renderer: Renderer2, private readonly el: ElementRef<HTMLElement>) {}

  ngOnInit(): void {
    this.renderer.setStyle(this.el.nativeElement, 'backgroundColor', this.appHighlight);
  }
}

@Component({
  selector: 'app-highlight-demo',
  standalone: true,
  imports: [CommonModule, HighlightDirective],
  template: `
    <p appHighlight="#fef08a">CLIで作成したディレクティブが背景色を変えます。</p>
  `
})
export class HighlightDemoComponent {}
```

## ベストプラクティス
- 生成直後に`standalone: true`が付いているか確認し、不要なNgModule依存を排除する
- テストファイルも自動生成されるので、振る舞いの期待値を早期に記述する
- ディレクトリ構造は`shared/directives`など用途別に整理し、保守性を高める

## 注意点
- CLIのselector命名は`app`プレフィックスになるため、プロジェクトの規約に合わせて変更する
- 生成後に不要な`common`インポート等があれば整理する
- スタンドアロンでない環境に追加する場合はモジュールの`declarations`/`exports`も忘れない

## 関連技術
- Angular CLI
- Standalone APIs
- Schematics
