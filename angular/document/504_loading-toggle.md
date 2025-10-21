# #504 「読み込み中の表示切り替え」

## 概要
読み込み中の表示切り替えではローディング状態がtrueならスケルトンテンプレートを、falseなら本来のテンプレートを描画し、状態変化に応じてViewContainerを切り替える。

## 学習目標
- ローディング状態に応じたテンプレート切り替えロジックを理解する
- `appLoadingIfElse`のようなelseテンプレートの設計を学ぶ
- 状態変化時のビュー管理を把握する

## 技術ポイント
- ViewContainerを`clear`してから適切なテンプレートで`createEmbeddedView`
- Contextでloading状態をテンプレートへ渡す
- Observable対応時はloadingテンプレート→コンテンツテンプレートへ切り替え

## 📺 画面表示用コード（動画用）
```typescript
this.viewContainer.clear();
const tpl = loading ? this.loadingTemplate ?? this.template : this.template;
this.viewContainer.createEmbeddedView(tpl, context);
```

## 💻 詳細実装例（学習用）
```typescript
private renderLoading(context: LoadingContext<T>): void {
  this.viewContainer.clear();
  const tpl = this.loadingTemplate ?? this.template;
  context.loading = true;
  context.error = null;
  this.currentView = this.viewContainer.createEmbeddedView(tpl, context);
}

private renderContent(value: T | null): void {
  this.viewContainer.clear();
  this.currentView = this.viewContainer.createEmbeddedView(this.template, {
    $implicit: value,
    loading: false,
    error: null
  });
}
```

## ベストプラクティス
- loading→content→errorなど状態遷移を明確にしコードを分割
- elseテンプレートをoptionalにし、未指定時はデフォルト表示
- Contextへloading/errorを渡しテンプレートで柔軟に表示

## 注意点
- ビュー切り替えでアニメーションを行う場合はCSSやAnimation APIを活用
- Observableが多重に発火する場合に備え、古い購読は解除
- SSRではloadingテンプレートのみ描画されないよう初期状態を配慮

## 関連技術
- LoadingIf Directive
- Skeleton UI
- Observable購読管理
