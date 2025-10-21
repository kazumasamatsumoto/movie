# #500 「Defer Directive - 遅延表示」

## 概要
Deferディレクティブは条件が満たされるまでテンプレートの表示を遅延し、必要なタイミングだけコンテンツをレンダリングしてパフォーマンスやUXを向上させる。

## 学習目標
- 遅延表示ディレクティブの構造を理解する
- 条件が整ったときにビューを生成する仕組みを学ぶ
- 解除条件や再表示の管理方法を把握する

## 技術ポイント
- Inputでboolean/Promise/Observableを受け取る
- 条件がtrueになったら`createEmbeddedView`
- 再度非表示にするかどうかを設計で決める

## 📺 画面表示用コード（動画用）
```html
<app-heavy *appDefer="isReady"></app-heavy>
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appDefer]',
  standalone: true
})
export class DeferDirective implements OnChanges {
  @Input('appDefer') condition: boolean | Promise<unknown> | Observable<unknown> = false;
  private viewCreated = false;
  private destroyRef = inject(DestroyRef);

  constructor(
    private readonly template: TemplateRef<unknown>,
    private readonly viewContainer: ViewContainerRef
  ) {}

  ngOnChanges(): void {
    this.viewContainer.clear();
    this.viewCreated = false;
    this.resolveCondition(this.condition);
  }

  private resolveCondition(value: boolean | Promise<unknown> | Observable<unknown>): void {
    if (value instanceof Promise) {
      value.then(() => this.show());
    } else if (isObservable(value)) {
      value.pipe(takeUntilDestroyed(this.destroyRef)).subscribe(() => this.show());
    } else if (value) {
      this.show();
    }
  }

  private show(): void {
    if (!this.viewCreated) {
      this.viewContainer.createEmbeddedView(this.template);
      this.viewCreated = true;
    }
  }
}
```

## ベストプラクティス
- boolean/Promise/Observableの三種類をサポートし柔軟性を高める
- ビュー生成が一度だけなら`viewCreated`フラグで制御
- 非同期解除時のキャンセルに`takeUntilDestroyed`を利用

## 注意点
- Promise/Observableがエラーの場合の対応を実装
- 再表示が必要な場合は`clear`するかどうか仕様を明確にする
- SSRでは非同期結果が遅れるため初期状態も考慮

## 関連技術
- Promise/Observable
- DestroyRef / takeUntilDestroyed
- Structural Directive実装
