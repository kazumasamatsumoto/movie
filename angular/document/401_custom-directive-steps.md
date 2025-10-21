# #401 「カスタム Directive の作成手順」

## 概要
カスタムDirectiveはCLIで雛形を生成し、Host要素に対する振る舞いを実装してテスト・ドキュメント化する一連の手順で構築する。

## 学習目標
- カスタムDirective作成の全体フローを把握する
- CLI生成から登録・テストまでのステップを理解する
- ドキュメント化まで含めた完成プロセスを説明できる

## 技術ポイント
- `ng generate directive`で雛形生成
- Standaloneディレクティブは`imports`で利用側へ登録
- テスト/ドキュメントをセットで整備し再利用性を高める

## 📺 画面表示用コード（動画用）
```bash
ng g directive shared/highlight --standalone
```

## 💻 詳細実装例（学習用）
```typescript
// 1. 生成
// ng g directive shared/highlight --standalone

// 2. 実装
@Directive({
  selector: '[appHighlight]',
  standalone: true
})
export class HighlightDirective {
  constructor(private readonly el: ElementRef<HTMLElement>, private readonly renderer: Renderer2) {}
  ngOnInit(): void {
    this.renderer.setStyle(this.el.nativeElement, 'backgroundColor', '#fef08a');
  }
}

// 3. 利用
@Component({
  selector: 'app-highlight-demo',
  standalone: true,
  imports: [CommonModule, HighlightDirective],
  template: `<p appHighlight>Directive作成手順デモ</p>`
})
export class HighlightDemoComponent {}

// 4. テスト生成: highlight.directive.spec.ts
```

## ベストプラクティス
- 雛形生成直後にスタンドアロン設定やselectorを整える
- 利用側コンポーネントで早期に挙動確認し、テストケースを追加
- ドキュメントで目的・使い方・Input/Outputを共有する

## 注意点
- selectorやプレフィックスの統一を怠ると衝突しやすい
- スタンドアロンでない場合は忘れずにNgModuleへ登録
- テストやドキュメントを後回しにすると再利用が難しくなる

## 関連技術
- Angular CLI
- Standalone API
- Storybook
