# #230 「複数の動的 Component 管理」

## 概要
複数の動的コンポーネントを同一ViewContainerRefに追加・削除し、順序や配列で管理する手法を整理します。

## 学習目標
- ComponentRefを複数保持するデータ構造を理解する
- `ViewContainerRef.insert/remove`を使った部分削除を習得する
- 再描画や順序変更の注意点を把握する

## 技術ポイント
- **配列管理**: `ComponentRef[]`または`Map<string, ComponentRef>`で追跡
- **部分削除**: `viewContainerRef.remove(index)`で特定コンポーネントを破棄
- **再並び替え**: `insert(ref.hostView, newIndex)`で順序を入れ替え可能

## 📺 画面表示用コード（動画用）

```typescript
const ref = this.host.createComponent(WidgetComponent);
this.refs.splice(index, 0, ref);
```

```typescript
this.host.remove(index);
```

```typescript
this.host.insert(ref.hostView, target);
```

## 💻 詳細実装例（学習用）
```typescript
// widgets-manager.component.ts
import { Component, ComponentRef, ViewChild, ViewContainerRef } from '@angular/core';
import { WidgetAComponent } from './widget-a.component';
import { WidgetBComponent } from './widget-b.component';

const WIDGETS = [WidgetAComponent, WidgetBComponent];

@Component({
  selector: 'app-widgets-manager',
  standalone: true,
  imports: [WidgetAComponent, WidgetBComponent],
  templateUrl: './widgets-manager.component.html',
})
export class WidgetsManagerComponent {
  @ViewChild('host', { read: ViewContainerRef, static: true })
  host!: ViewContainerRef;

  refs: ComponentRef<any>[] = [];

  add(type: number) {
    const ref = this.host.createComponent(WIDGETS[type]);
    this.refs.push(ref);
  }

  remove(index: number) {
    this.host.remove(index);
    this.refs.splice(index, 1);
  }
}
```

## ベストプラクティス
- ComponentRefを集合で管理し、destroy忘れを防ぐ
- ビューの順序を操作する場合は`insert`と配列のインデックスを同期する
- 生成/削除イベントをログに残し、デバッグしやすい設計にする

## 注意点
- `remove`は自動でdestroyを呼ぶが、配列からの削除を忘れると参照が残る
- 過剰な再生成を避けるため、必要ならコンポーネントプールを検討する
- 大量のコンポーネントを同一ViewContainerRefに追加すると描画負荷が高まる

## 関連技術
- ComponentRef活用（#232）
- メモリ管理（#242）
- 動的ウィジェット/タブシステム（#238, #239）
