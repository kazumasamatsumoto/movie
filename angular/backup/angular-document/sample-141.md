# #141 「ViewChildren - 複数要素参照」

## 概要
`@ViewChildren`を用いて、テンプレート内の複数要素やコンポーネントをまとめて取得し操作する方法を学びます。

## 学習目標
- ViewChildrenの基本構文を理解する
- QueryListを利用した複数要素の処理方法を習得する
- `ngAfterViewInit`との連携で安全に参照を扱う

## 技術ポイント
- **宣言**: `@ViewChildren('item') items!: QueryList<ElementRef<HTMLLIElement>>;`
- **QueryList**: 取得結果には配列操作のためのメソッドが用意されている
- **changes**: 追加・削除をObservableで追跡可能

```html
<li #item *ngFor="let todo of todos">{{ todo }}</li>
```

```typescript
@ViewChildren('item')
items!: QueryList<ElementRef<HTMLLIElement>>;
```

```typescript
this.items.forEach((el) => el.nativeElement.classList.add('ready'));
```

## 💻 詳細実装例（学習用）
```typescript
// todo-list.component.ts
import { AfterViewInit, Component, ElementRef, QueryList, ViewChildren } from '@angular/core';

@Component({
  selector: 'app-todo-list',
  standalone: true,
  templateUrl: './todo-list.component.html',
})
export class TodoListComponent implements AfterViewInit {
  todos = ['仕様確認', '実装', 'レビュー'];

  @ViewChildren('todoItem')
  items!: QueryList<ElementRef<HTMLLIElement>>;

  ngAfterViewInit(): void {
    this.items.forEach((item, index) => {
      item.nativeElement.setAttribute('data-index', `${index + 1}`);
    });
  }
}
```

```html
<!-- todo-list.component.html -->
<ul>
  <li #todoItem *ngFor="let todo of todos">
    {{ todo }}
  </li>
</ul>
```

## ベストプラクティス
- QueryListは`ngAfterViewInit`で利用し、必要なら`changes`を購読して更新を追跡する
- DOM操作が必要な場合はRenderer2を活用して安全に処理する
- ViewChildrenを多用する場合はコンポーネント分割を検討し、責務を整理する

## 注意点
- `items`は遅延初期化されるので、`ngOnInit`ではundefinedのまま
- *ngIfによる表示切り替えでQueryListの内容が変わるため、nullチェックを行う
- 多数の要素を操作する場合はパフォーマンスに注意し、必要に応じて仮想スクロールを検討する

## 関連技術
- `@ViewChild`との違い（単一 vs 複数）
- `QueryList.changes` Observable
- `ContentChildren`による投影コンテンツ参照
