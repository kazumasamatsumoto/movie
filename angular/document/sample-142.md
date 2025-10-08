# #142 「ViewChildren QueryList の活用」

## 概要
`@ViewChildren`が返す`QueryList`の操作方法を掘り下げ、複数要素を効率的に扱うテクニックを学びます。

## 学習目標
- QueryListの主要メソッド（`forEach`, `map`, `filter`, `toArray`）を理解する
- `changes` Observableで更新を監視する方法を習得する
- QueryListから配列へ変換してロジックを実装するフローを把握する

## 技術ポイント
- **反復処理**: `queryList.forEach((item) => ...)`
- **配列変換**: `[...queryList]`または`queryList.toArray()`
- **更新監視**: `queryList.changes.subscribe(...)`

## 📺 画面表示用コード（動画用）

```typescript
this.tabs.forEach((tab) => tab.deactivate());
```

```typescript
const actives = this.tabs.filter((tab) => tab.active);
```

```typescript
this.tabs.changes.subscribe(() => console.log('updated'));
```

## 💻 詳細実装例（学習用）
```typescript
// tabs.component.ts
import { AfterViewInit, Component, QueryList, ViewChildren } from '@angular/core';
import { TabComponent } from './tab.component';

@Component({
  selector: 'app-tabs',
  standalone: true,
  imports: [TabComponent],
  templateUrl: './tabs.component.html',
})
export class TabsComponent implements AfterViewInit {
  @ViewChildren(TabComponent)
  tabs!: QueryList<TabComponent>;

  ngAfterViewInit(): void {
    this.activateFirst();
    this.tabs.changes.subscribe(() => this.activateFirst());
  }

  activate(tab: TabComponent): void {
    this.tabs.forEach((item) => item.deactivate());
    tab.activate();
  }

  private activateFirst(): void {
    const first = this.tabs.first;
    if (first) {
      this.activate(first);
    }
  }
}
```

```html
<!-- tabs.component.html -->
<div class="tab-list">
  <button
    type="button"
    @for (let tab of tabs; track tab.id)
    (click)="activate(tab)"
  >
    {{ tab.title }}
  </button>
</div>
<ng-content></ng-content>
```

```typescript
// tab.component.ts
import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-tab',
  standalone: true,
  template: `
    <section *ngIf="active">
      <ng-content></ng-content>
    </section>
  `,
})
export class TabComponent {
  @Input() title = '';
  active = false;

  activate(): void {
    this.active = true;
  }

  deactivate(): void {
    this.active = false;
  }
}
```

## ベストプラクティス
- QueryListを利用するときは配列化するか、そのままメソッドを使うか統一する
- `changes`購読は`takeUntilDestroyed`や`DestroyRef`で解除し、メモリリークを防ぐ
- QueryListに対する処理は描画サイクルに影響しないよう軽量に保つ

## 注意点
- QueryListは遅延評価されるため、`ngAfterViewInit`より前にアクセスしない
- 配列化した結果は静的スナップショットなので、最新状態が必要な場合は再度QueryListから取得する
- ループの中でDOMを頻繁に操作するとパフォーマンスが低下するため、まとめて処理する

## 関連技術
- `QueryList.first` / `last` / `length`
- `@ContentChildren`でのQueryList操作
- RxJS `takeUntilDestroyed`での購読解除
