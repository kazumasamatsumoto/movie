# #502 「非同期条件の処理」

## 概要
非同期条件を扱う構造ディレクティブはObservableやPromiseの完了を待ってテンプレートを表示し、成功・失敗をハンドリングする必要がある。

## 学習目標
- Observable/Promiseの完了待ちロジックを理解する
- 購読解除とエラーハンドリングの実装を学ぶ
- Loading/成功/失敗の各状態をテンプレートに渡す方法を把握する

## 技術ポイント
- `takeUntilDestroyed`や`Subscription`で購読管理
- Promiseは`await`/`then`/`catch`
- Contextに`loading`, `error`, `data`などを渡す

## 📺 画面表示用コード（動画用）
```typescript
value.pipe(takeUntilDestroyed(this.destroyRef)).subscribe({ next: () => this.show(), error: err => this.handleError(err) });
```

## 💻 詳細実装例（学習用）
```typescript
interface AsyncContext<T> {
  $implicit: T | null;
  loading: boolean;
  error: unknown;
}

@Directive({
  selector: '[appDeferAsync]',
  standalone: true
})
export class DeferAsyncDirective<T> implements OnChanges {
  @Input('appDeferAsync') source?: Observable<T> | Promise<T>;
  private readonly destroyRef = inject(DestroyRef);

  constructor(
    private readonly template: TemplateRef<AsyncContext<T>>,
    private readonly viewContainer: ViewContainerRef
  ) {}

  ngOnChanges(): void {
    this.viewContainer.clear();
    if (!this.source) return;
    const context: AsyncContext<T> = { $implicit: null, loading: true, error: null };
    const view = this.viewContainer.createEmbeddedView(this.template, context);

    const onSuccess = (value: T) => {
      context.$implicit = value;
      context.loading = false;
      view.markForCheck();
    };
    const onError = (error: unknown) => {
      context.error = error;
      context.loading = false;
      view.markForCheck();
    };

    if (this.source instanceof Promise) {
      this.source.then(onSuccess).catch(onError);
    } else {
      this.source.pipe(takeUntilDestroyed(this.destroyRef)).subscribe({ next: onSuccess, error: onError });
    }
  }
}
```

## ベストプラクティス
- Contextでloadingとerrorを提供し、テンプレート側で分岐
- Observableは購読解除を確実に行いメモリリークを防ぐ
- 非同期処理中に条件が再変更された場合は既存ビューをクリアしてリセット

## 注意点
- Promise/Observableが同時に設定される場合の優先順位を決める
- long-running Observableは初回イベントで表示するか最後まで待つか仕様を明確に
- markForCheckを忘れるとOnPush環境で変更が反映されない

## 関連技術
- takeUntilDestroyed
- AsyncPipe
- Contextオブジェクト
