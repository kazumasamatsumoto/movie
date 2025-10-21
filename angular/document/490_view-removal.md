# #490 「ビューの削除」

## 概要
`ViewContainerRef.remove`は指定インデックスのEmbeddedViewを削除し、複数ビューを管理する構造ディレクティブで部分的なビュー削除を可能にする。

## 学習目標
- removeメソッドの使用方法を理解する
- インデックス管理の重要性を把握する
- EmbeddedViewRefを保持して削除するフローを学ぶ

## 技術ポイント
- `viewContainer.remove(index)`でビュー削除
- `viewContainer.length`でビュー数を取得
- `indexOf(viewRef)`でインデックス取得

## 📺 画面表示用コード（動画用）
```typescript
const idx = this.viewContainer.indexOf(viewRef);
if (idx !== -1) this.viewContainer.remove(idx);
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appDynamicList]',
  standalone: true
})
export class DynamicListDirective {
  private viewRefs: EmbeddedViewRef<unknown>[] = [];

  constructor(
    private readonly template: TemplateRef<unknown>,
    private readonly viewContainer: ViewContainerRef
  ) {}

  add(): void {
    const view = this.viewContainer.createEmbeddedView(this.template);
    this.viewRefs.push(view);
  }

  remove(index: number): void {
    const view = this.viewRefs[index];
    if (!view) return;
    const containerIndex = this.viewContainer.indexOf(view);
    if (containerIndex !== -1) {
      this.viewContainer.remove(containerIndex);
    }
    this.viewRefs.splice(index, 1);
  }
}
```

## ベストプラクティス
- EmbeddedViewRefの配列を保持し、remove時のインデックス計算を簡略化
- ビューの状態（コンテキスト）が必要な場合はデータ構造に保存
- 削除後に残るビューのインデックスが変わることに注意

## 注意点
- remove後にViewRefを再利用できないため、必要なら再生成
- viewContainerが空の場合にremoveを呼ぶと例外になるので防御的に実装
- 複雑な操作では`detach`/`insert`を検討し負荷を抑える

## 関連技術
- ViewContainerRef.detach
- EmbeddedViewRef
- Structural Directive操作
