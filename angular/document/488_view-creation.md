# #488 「ビューの生成」

## 概要
ビュー生成は条件に応じて`createEmbeddedView`を呼び、テンプレートからDOMツリーを生成するプロセスで、生成したビューを保持することで再利用や状態管理が可能になる。

## 学習目標
- ビュー生成のタイミングとロジックを理解する
- 生成したEmbeddedViewRefの管理方法を学ぶ
- 条件に応じてビューを切り替える構造を把握する

## 技術ポイント
- ビュー生成前に`clear`で既存ビューを整理
- EmbeddedViewRefをプロパティで保持
- 再利用する際は`detach`/`attach`の利用も検討

## 📺 画面表示用コード（動画用）
```typescript
if (!this.viewRef) this.viewRef = this.viewContainer.createEmbeddedView(this.template);
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appDefer]',
  standalone: true
})
export class DeferDirective implements OnChanges {
  @Input('appDefer') condition = false;
  private viewRef?: EmbeddedViewRef<unknown>;

  constructor(
    private readonly template: TemplateRef<unknown>,
    private readonly viewContainer: ViewContainerRef
  ) {}

  ngOnChanges(): void {
    if (this.condition) {
      if (!this.viewRef) {
        this.viewRef = this.viewContainer.createEmbeddedView(this.template);
      }
    } else {
      this.viewContainer.clear();
      this.viewRef = undefined;
    }
  }
}
```

## ベストプラクティス
- ビュー生成状態をフラグやプロパティで持って重複生成を避ける
- 再利用したい場合はViewRefを保持し、必要に応じて`clear`と`create`を使い分ける
- 複数テンプレートを切り替える場合は`ViewContainerRef`のインデックスを活用

## 注意点
- 条件が頻繁に変わる場合は生成・破棄コストが高くなるためキャッシュを検討
- ViewRef保持時は破棄忘れに注意しメモリリークを防ぐ
- Deferなど非同期で生成する際は競合を防ぐため状態管理を丁寧に

## 関連技術
- EmbeddedViewRef
- ViewContainerRef
- Structural Directiveパターン
