# #229 「動的 Component の置き換え」

## 概要
既に表示されている動的コンポーネントを別のコンポーネントへ置き換える方法を学び、ビューを切り替える際の注意点を整理します。

## 学習目標
- ViewContainerRefを使って既存コンポーネントを削除し、新しいコンポーネントを生成する手順を理解する
- 置き換え時に状態を保存・引き継ぐ方法を把握する
- 複数コンポーネントを順次切り替える実装パターンを習得する

## 技術ポイント
- **置き換え**: `viewContainerRef.clear()` → `createComponent(newComponent)`
- **状態引き継ぎ**: 旧コンポーネントから必要なデータを取得し、新コンポーネントのInputへ設定
- **アニメーション**: 置き換え前後でフェードなどのトランジションを追加するとUX向上

## 📺 画面表示用コード（動画用）

```typescript
this.host.clear();
this.activeRef = this.host.createComponent(componentMap[type]);
```

```typescript
this.activeRef.instance.config = config;
```

```typescript
oldRef.destroy();
```

## 💻 詳細実装例（学習用）
```typescript
// component-switcher.component.ts
import { Component, ComponentRef, ViewChild, ViewContainerRef } from '@angular/core';
import { ChartWidgetComponent } from './chart-widget.component';
import { TableWidgetComponent } from './table-widget.component';

const COMPONENTS = {
  chart: ChartWidgetComponent,
  table: TableWidgetComponent,
} as const;

@Component({
  selector: 'app-component-switcher',
  standalone: true,
  imports: [ChartWidgetComponent, TableWidgetComponent],
  templateUrl: './component-switcher.component.html',
})
export class ComponentSwitcherComponent {
  @ViewChild('host', { read: ViewContainerRef, static: true })
  host!: ViewContainerRef;

  activeRef?: ComponentRef<any>;

  switch(type: keyof typeof COMPONENTS) {
    const prevState = this.activeRef?.instance?.state ?? null;
    this.activeRef?.destroy();
    const ref = this.host.createComponent(COMPONENTS[type]);
    if (prevState) {
      ref.instance.state = prevState;
    }
    this.activeRef = ref;
  }
}
```

## ベストプラクティス
- 置き換え前に旧コンポーネントの状態を保存し、必要なら新コンポーネントへ反映する
- 複数タイプのコンポーネントをマップにまとめ、識別子で切り替える
- 破棄と生成のタイミングで一瞬のちらつきが出る場合はプレースホルダ表示を挟む

## 注意点
- 旧コンポーネントのdestroyを忘れるとビューが残り、メモリリークの原因になる
- Inputの型が異なる場合は共通インターフェースを定義するか、型ガードを挟む
- 非同期処理中に置き換える場合、Promiseやサブスクを適切にキャンセルする

## 関連技術
- 動的コンポーネントの生成（#225）
- メモリ管理と破棄（#228、#242）
- ポータル/ダイナミックウィジェット設計（#239、#246）
