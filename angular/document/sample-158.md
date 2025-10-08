# #158 「QueryList のメソッド活用」

## 概要
`QueryList`が提供するメソッドを活用して、ViewChildren／ContentChildrenで取得した要素を柔軟に操作する方法を学びます。

## 学習目標
- QueryListの主要メソッド（`first`, `last`, `find`, `filter`, `map`, `toArray`）を理解する
- QueryListを配列に変換して高度な処理を行うテクニックを習得する
- QueryList操作の落とし穴を把握する

## 技術ポイント
- **first/last**: 先頭・末尾の要素に簡単アクセス
- **filter/map**: クエリ結果を配列的に加工
- **toArray**: スナップショットの配列を取得

## 📺 画面表示用コード（動画用）

```typescript
const active = this.tabs.find((tab) => tab.active);
```

```typescript
const labels = this.tabs.map((tab) => tab.title);
```

```typescript
const list = this.tabs.toArray();
```

## 💻 詳細実装例（学習用）
```typescript
// tag.directive.ts
import { Directive, Input } from '@angular/core';

@Directive({
  selector: '[appTag]',
  standalone: true,
})
export class TagDirective {
  @Input() appTag = '';
  active = false;
}
```

```typescript
// tag-list.component.ts
import { AfterViewInit, Component, QueryList, ViewChildren } from '@angular/core';
import { TagDirective } from './tag.directive';

@Component({
  selector: 'app-tag-list',
  standalone: true,
  imports: [TagDirective],
  templateUrl: './tag-list.component.html',
})
export class TagListComponent implements AfterViewInit {
  @ViewChildren(TagDirective)
  tags!: QueryList<TagDirective>;

  ngAfterViewInit(): void {
    const first = this.tags.first;
    if (first) {
      first.active = true;
    }
    const titles = this.tags.map((tag) => tag.appTag);
    console.log('タグ一覧', titles);
  }

  activate(label: string): void {
    this.tags.forEach((tag) => (tag.active = tag.appTag === label));
  }
}
```

```html
<!-- tag-list.component.html -->
<button
  type="button"
  @for (let tag of tags; track tag.appTag)
  (click)="activate(tag.appTag)"
  [class.active]="tag.active"
>
  {{ tag.appTag }}
</button>
<div appTag="Angular"></div>
<div appTag="Signals"></div>
<div appTag="ViewChild"></div>
```

## ベストプラクティス
- `toArray()`やスプレッド構文を使用する際は最新状態を取得するタイミングを意識する
- QueryListのメソッドはライブコレクションに対して動作するため、結果を変数に保存する場合はスナップショットであることを理解する
- 操作が複雑になる場合は、対象要素にディレクティブを付けて状態管理を任せる

## 注意点
- QueryListを配列に変換した後は、自動的に更新されないため、変化があれば再度変換する
- `find`や`filter`が返すのはディレクティブ/コンポーネントインスタンスであり、DOM操作する場合はElementRef経由が必要
- 大量要素で頻繁に操作するとパフォーマンスに影響するため、まとめて処理する

## 関連技術
- QueryListの`changes` Observable
- `@ViewChildren` と `@ContentChildren`
- RxJSでの配列処理と組み合わせたパイプライン
