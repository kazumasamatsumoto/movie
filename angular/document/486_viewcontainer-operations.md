# #486 「ビューコンテナの操作」

## 概要
ViewContainerRefを使うとEmbeddedViewの生成、挿入、削除、クリアなどの操作ができ、構造ディレクティブでテンプレートの表示を柔軟にコントロールできる。

## 学習目標
- ViewContainerRefの主要メソッドを理解する
- ビューの挿入位置や削除の手順を学ぶ
- EmbeddedViewRefを保持して再利用する方法を把握する

## 技術ポイント
- `createEmbeddedView(template, context?, index?)`
- `insert(viewRef, index)`/`move`/`remove(index)`
- `clear()`で全ビュー破棄

## 📺 画面表示用コード（動画用）
```typescript
const view = this.viewContainer.createEmbeddedView(this.template);
this.viewContainer.insert(view, 0);
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appViewOperations]',
  standalone: true
})
export class ViewOperationsDirective {
  private viewRefs: EmbeddedViewRef<unknown>[] = [];

  constructor(
    private readonly template: TemplateRef<unknown>,
    private readonly viewContainer: ViewContainerRef
  ) {}

  addView(): void {
    const viewRef = this.viewContainer.createEmbeddedView(this.template);
    this.viewRefs.push(viewRef);
  }

  removeLast(): void {
    if (this.viewRefs.length === 0) return;
    const viewRef = this.viewRefs.pop()!;
    const index = this.viewContainer.indexOf(viewRef);
    if (index !== -1) {
      this.viewContainer.remove(index);
    }
  }

  clearAll(): void {
    this.viewContainer.clear();
    this.viewRefs = [];
  }
}
```

## ベストプラクティス
- 生成したEmbeddedViewRefを配列で管理すると挿入/削除が容易
- 順序を維持したい場合は`insert`のindexや`move`を活用
- `clear()`でまとめて破棄できるため状態リセットに便利

## 注意点
- ViewRefを保持しない場合、remove時にindexを計算し直す必要がある
- 無闇にviewを生成するとパフォーマンスに影響するので必要な数だけ生成
- ビュー破棄後に参照を保持し続けるとメモリリークになる

## 関連技術
- EmbeddedViewRef
- TemplateRef
- Structural Directive制御
