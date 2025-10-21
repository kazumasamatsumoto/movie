# #503 「LoadingIf Directive - ローディング制御」

## 概要
LoadingIfディレクティブは読み込み中はスケルトンテンプレートを表示し、ロード完了後に本来のテンプレートへ切り替える構造ディレクティブである。

## 学習目標
- ローディング状態を切り替える構造ディレクティブの設計を理解する
- MainテンプレートとFallbackテンプレートの切り替え方法を学ぶ
- コンテキストで`loading`などの状態を提供する

## 技術ポイント
- Inputでローディング状態(booleanやObservable)を受け取る
- `appLoadingIfElse`でスケルトンテンプレートを指定
- Contextに`loading`/`error`を提供

## 📺 画面表示用コード（動画用）
```html
<section *appLoadingIf="isLoading; else skeleton">コンテンツ</section>
<ng-template #skeleton>...</ng-template>
```

## 💻 詳細実装例（学習用）
```typescript
interface LoadingContext<T> {
  $implicit: T | null;
  loading: boolean;
  error: unknown;
}

@Directive({
  selector: '[appLoadingIf]',
  standalone: true
})
export class LoadingIfDirective<T> implements OnChanges {
  @Input('appLoadingIf') condition: boolean | Observable<T> = false;
  @Input('appLoadingIfElse') loadingTemplate?: TemplateRef<LoadingContext<T>>;
  private currentView?: EmbeddedViewRef<LoadingContext<T>>;

  constructor(
    private readonly template: TemplateRef<LoadingContext<T>>,
    private readonly viewContainer: ViewContainerRef,
    private readonly destroyRef: DestroyRef
  ) {}

  ngOnChanges(): void {
    this.viewContainer.clear();
    this.currentView = undefined;

    const context: LoadingContext<T> = { $implicit: null, loading: true, error: null };
    if (typeof (this.condition as Observable<T>).subscribe === 'function') {
      const source = this.condition as Observable<T>;
      const loadingView = this.loadingTemplate
        ? this.viewContainer.createEmbeddedView(this.loadingTemplate, context)
        : this.viewContainer.createEmbeddedView(this.template, context);
      this.currentView = loadingView;
      source.pipe(takeUntilDestroyed(this.destroyRef)).subscribe({
        next: value => this.showContent(value),
        error: err => this.showError(err)
      });
    } else {
      const loading = this.condition as boolean;
      if (loading) {
        const tpl = this.loadingTemplate ?? this.template;
        this.currentView = this.viewContainer.createEmbeddedView(tpl, context);
      } else {
        this.showContent(null);
      }
    }
  }

  private showContent(value: T | null): void {
    this.viewContainer.clear();
    this.currentView = this.viewContainer.createEmbeddedView(this.template, {
      $implicit: value,
      loading: false,
      error: null
    });
  }

  private showError(error: unknown): void {
    this.viewContainer.clear();
    if (this.loadingTemplate) {
      this.currentView = this.viewContainer.createEmbeddedView(this.loadingTemplate, {
        $implicit: null,
        loading: false,
        error
      });
    }
  }
}
```

## ベストプラクティス
- Fallbackテンプレートを`appLoadingIfElse`で受け取り柔軟に
- Observable対応で非同期読み込みを簡略化
- Contextにloading/errorを渡しテンプレートで条件分岐

## 注意点
- Observableが完了しない場合、ずっとローディング表示になるので注意
- booleanとObservable両対応にする際は型判定を明確に
- コンテンツが再生成されるため状態管理に注意

## 関連技術
- TemplateRef / ViewContainerRef
- takeUntilDestroyed
- Skeleton UI
