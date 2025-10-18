# #116 「兄弟 Component 間の通信」

## 概要
同じ親にぶら下がる兄弟コンポーネント間で状態やイベントを共有する際の基本戦略を解説します。

## 学習目標
- 親を中継する方法と共有サービスを使う方法を理解する
- 兄弟間で状態を同期させる実装例を習得する
- 双方向更新を防ぎつつ整合性を保つ設計パターンを学ぶ

## 技術ポイント
- **親中継**: 兄弟間の通信は親を経由する（Input/Output）
- **共有サービス**: `providedIn: 'root'`や親の`providers`で状態共有
- **Signals**: 共有サービスでSignalを持つと反応的な同期が容易

```html
<app-filter-panel (filterChange)="onFilterChange($event)"></app-filter-panel>
<app-list [filter]="filter"></app-list>
```

```typescript
filter = signal('all');
```

```typescript
onFilterChange(value: string) { this.filter.set(value); }
```

## 💻 詳細実装例（学習用）
```typescript
// filter-panel.component.ts
import { Component, EventEmitter, Output } from '@angular/core';

@Component({
  selector: 'app-filter-panel',
  standalone: true,
  template: `
    <button type="button" (click)="change('all')">すべて</button>
    <button type="button" (click)="change('active')">進行中</button>
    <button type="button" (click)="change('done')">完了</button>
  `,
})
export class FilterPanelComponent {
  @Output() filterChange = new EventEmitter<string>();

  change(value: string): void {
    this.filterChange.emit(value);
  }
}
```

```typescript
// task-list.component.ts
import { Component, Input, computed, signal } from '@angular/core';

type Task = { id: number; title: string; done: boolean };

@Component({
  selector: 'app-task-list',
  standalone: true,
  templateUrl: './task-list.component.html',
})
export class TaskListComponent {
  @Input() filter: 'all' | 'active' | 'done' = 'all';

  readonly tasks = signal<Task[]>([
    { id: 1, title: '仕様確認', done: false },
    { id: 2, title: '実装', done: true },
  ]);

  readonly filtered = computed(() => {
    switch (this.filter) {
      case 'active':
        return this.tasks().filter((task) => !task.done);
      case 'done':
        return this.tasks().filter((task) => task.done);
      default:
        return this.tasks();
    }
  });
}
```

```html
<!-- task-list.component.html -->
<ul>
  <li @for (task of filtered(); track task.id)">
    {{ task.title }} - {{ task.done ? '完了' : '進行中' }}
  </li>
</ul>
```

```typescript
// parent.component.ts
import { Component, signal } from '@angular/core';
import { FilterPanelComponent } from './filter-panel.component';
import { TaskListComponent } from './task-list.component';

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [FilterPanelComponent, TaskListComponent],
  templateUrl: './dashboard.component.html',
})
export class DashboardComponent {
  readonly filter = signal<'all' | 'active' | 'done'>('all');

  onFilterChange(next: string): void {
    this.filter.set(next as 'all' | 'active' | 'done');
  }
}
```

```html
<!-- dashboard.component.html -->
<app-filter-panel (filterChange)="onFilterChange($event)"></app-filter-panel>
<app-task-list [filter]="filter()"></app-task-list>
```

## ベストプラクティス
- 兄弟間通信は親を経由する単方向データフローが基本
- 状態が複数兄弟間で共有されるならサービスで集約し、コンポーネントを薄く保つ
- Signalsを共有サービスに持たせると再描画が自動で同期される

## 注意点
- 兄弟間で直接参照を渡すと依存が循環しやすくなるので避ける
- 大量の兄弟コンポーネントが同時に状態更新するときはパフォーマンスを測定する
- フィルタリングなどの重い処理はcomputedやmemoizationで最適化する

## 関連技術
- Shared Service + Signals
- NgRxやNgXsなどの状態管理ライブラリ
- Router Outletを利用した兄弟コンポーネント切り替え
