# #228 「動的 Component の削除」

## 概要
動的に生成したコンポーネントを削除し、リソースを解放する方法を学びます。

## 学習目標
- ComponentRef.destroy()とViewContainerRef.clear()/remove()の使い方を理解する
- 削除時にライフサイクルがどう動くか把握する
- 複数コンポーネントを適切にクリーンアップする手順を習得する

## 技術ポイント
- **個別削除**: `componentRef.destroy()`でOnDestroyが呼ばれる
- **一括削除**: `viewContainerRef.clear()`ですべてのビューを破棄
- **部分削除**: `viewContainerRef.remove(index)`で特定のビューを削除

## 📺 画面表示用コード（動画用）

```typescript
const ref = this.host.createComponent(WidgetComponent);
ref.destroy();
```

```typescript
this.host.clear();
```

```typescript
this.host.remove(i);
```

## 💻 詳細実装例（学習用）
```typescript
// dynamic-delete.component.ts
import { Component, ComponentRef, ViewChild, ViewContainerRef } from '@angular/core';
import { WidgetComponent } from './widget.component';

@Component({
  selector: 'app-dynamic-delete',
  standalone: true,
  imports: [WidgetComponent],
  templateUrl: './dynamic-delete.component.html',
})
export class DynamicDeleteComponent {
  @ViewChild('host', { read: ViewContainerRef, static: true })
  host!: ViewContainerRef;

  refs: ComponentRef<WidgetComponent>[] = [];

  add(): void {
    const ref = this.host.createComponent(WidgetComponent);
    this.refs.push(ref);
  }

  removeLast(): void {
    const ref = this.refs.pop();
    ref?.destroy();
  }

  clearAll(): void {
    this.refs.forEach((ref) => ref.destroy());
    this.refs = [];
  }
}
```

## ベストプラクティス
- ComponentRefを必ず保持し、destroyし忘れない
- `clear()`を呼ぶ前に配列などの参照をクリアしてガーベジコレクションを促す
- OnDestroyに購読解除やタイマー停止処理を置き、クリーンアップを徹底する

## 注意点
- `clear()`はすべて破棄するため、状態を保存しておきたい場合はdestroy前に取得する
- DOMから除去された後も変数に参照が残るとメモリリークになる
- 破棄後のComponentRefやinstanceにアクセスしないようガードする

## 関連技術
- 動的コンポーネントの作成（#225）
- メモリ管理（#242）
- ComponentRef活用（#232）
