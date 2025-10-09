# #099 「@Input() 配列の受け渡し」

## 概要
配列を@Input()で渡すときの再描画や副作用の扱い、Immutableな更新戦略について学びます。

## 学習目標
- 配列が参照渡しで共有される点を理解する
- 子コンポーネントでの安全な操作方法を身につける
- track句を使った差分描画の最適化を習得する

## 技術ポイント
- **不変更新**: `items = [...items, newItem];` などで新しい参照を作る
- **防御的コピー**: 子で`this.localItems = [...inputItems];`
- **track句**: `@for (item of items; track item.id)` で再描画を最小化


```typescript
@Input() items: ReadonlyArray<ListItem> = [];
```

```typescript
readonly localItems = computed(() => [...this.items]);
```

```html
<li @for (item of items; track item.id)>{{ item.label }}</li>
```

## 💻 詳細実装例（学習用）
```typescript
type ListItem = { id: number; label: string };

import { Component, Input, computed } from '@angular/core';

@Component({
  selector: 'app-item-list',
  standalone: true,
  templateUrl: './item-list.component.html',
})
export class ItemListComponent {
  @Input() items: ReadonlyArray<ListItem> = [];

  readonly displayItems = computed(() => this.items.slice());
}
```

```html
<!-- item-list.component.html -->
<ul class="item-list">
  <li
    @for (item of displayItems(); track item.id)
  >
    {{ item.label }}
  </li>
</ul>
```

```typescript
// parent.component.ts
import { Component, signal } from '@angular/core';
import { ItemListComponent } from './item-list.component';

@Component({
  selector: 'app-board',
  standalone: true,
  imports: [ItemListComponent],
  templateUrl: './board.component.html',
})
export class BoardComponent {
  readonly items = signal<ListItem[]>([
    { id: 1, label: '要件定義' },
    { id: 2, label: 'UI設計' },
  ]);

  addItem(): void {
    const nextId = Date.now();
    this.items.update((current) => [
      ...current,
      { id: nextId, label: `タスク${nextId}` },
    ]);
  }
}
```

```html
<!-- board.component.html -->
<button type="button" (click)="addItem()">タスク追加</button>
<app-item-list [items]="items()"></app-item-list>
```

## ベストプラクティス
- 配列はImmutableに扱い、pushやspliceではなく新しい配列を生成する
- 子コンポーネントでソートやフィルタを行う場合はコピーを作ってから操作する
- track句や`trackBy`関数を用いて再描画コストを削減する

## 注意点
- 参照が変わらないとOnPush戦略で検知されないため、更新時には新しい配列を作成する
- 大きい配列を毎回コピーするとパフォーマンスが落ちるので、必要な箇所だけ最適化する
- 可変操作を子が行うと親と状態が食い違うため、編集は親で行い子は表示に集中させる

## 関連技術
- Angular v17 control flow `@for`
- `trackBy`関数の実装
- RxJSやSignalsを使ったリスト管理
