# #118 「Input/Output のパフォーマンス考慮」

## 概要
@Input()と@Output()を多用するコンポーネントで発生しやすいパフォーマンス課題を理解し、変更検知や描画の最適化方法を学びます。

## 学習目標
- Immutableデータと参照更新の重要性を理解する
- @Output()イベントの呼び出し回数を制御する方法を把握する
- Angular DevToolsでの計測と最適化手順を習得する

## 技術ポイント
- **Immutable更新**: 参照を更新しOnPushでも検知できるようにする
- **track句**: リスト表示で`@for (item of items; track item.id)`
- **イベント頻度制御**: `throttleTime`, `auditTime`, `requestAnimationFrame`

```typescript
@Component({ changeDetection: ChangeDetectionStrategy.OnPush })
```

```typescript
@for (item of items(); track item.id) { ... }
```

```typescript
saveEvents.pipe(throttleTime(500))
  .subscribe(handle);
```

## 💻 詳細実装例（学習用）
```typescript
// performance.component.ts
import { ChangeDetectionStrategy, Component, EventEmitter, Input, Output, computed, signal } from '@angular/core';
import { auditTime } from 'rxjs/operators';
import { fromEventPattern } from 'rxjs';

type RecordItem = { id: number; value: number };

@Component({
  selector: 'app-performance-panel',
  standalone: true,
  changeDetection: ChangeDetectionStrategy.OnPush,
  templateUrl: './performance-panel.component.html',
})
export class PerformancePanelComponent {
  @Input() items: ReadonlyArray<RecordItem> = [];
  @Output() valueChange = new EventEmitter<RecordItem>();

  readonly topItems = computed(() =>
    this.items.slice().sort((a, b) => b.value - a.value).slice(0, 5),
  );

  onClick(item: RecordItem): void {
    this.valueChange.emit(item);
  }
}
```

```html
<!-- performance-panel.component.html -->
<ul>
  <li
    @for (item of topItems(); track item.id)
    (click)="onClick(item)"
  >
    {{ item.id }} : {{ item.value }}
  </li>
</ul>
```

```typescript
// parent.component.ts
import { Component, ChangeDetectionStrategy, signal } from '@angular/core';
import { PerformancePanelComponent } from './performance-panel.component';
import { throttleTime } from 'rxjs/operators';

@Component({
  selector: 'app-dashboard',
  standalone: true,
  changeDetection: ChangeDetectionStrategy.OnPush,
  imports: [PerformancePanelComponent],
  templateUrl: './dashboard.component.html',
})
export class DashboardComponent {
  readonly items = signal<RecordItem[]>(Array.from({ length: 1000 }, (_, i) => ({ id: i, value: Math.random() * 100 })));

  handleValueChange(item: RecordItem): void {
    console.log('Clicked item', item);
  }
}
```

```html
<!-- dashboard.component.html -->
<app-performance-panel
  [items]="items()"
  (valueChange)="handleValueChange($event)"
></app-performance-panel>
```

## ベストプラクティス
- ChangeDetectionStrategy.OnPushを活用し、Immutableな更新で無駄な再描画を防ぐ
- 大量データでは仮想スクロールや`@defer`を活用し、初期描画コストを抑える
- イベント連打が予想されるUIではRxJSオペレーターで頻度を調整する

## 注意点
- OnPush戦略でも参照が変わらないと更新されないため、更新時は必ず新しいオブジェクトを生成する
- イベントのthrottleやdebounceをかけすぎるとリアクションが遅くなるのでバランスを取る
- Performance最適化はDevToolsで測定してから着手する

## 関連技術
- Angular DevTools Profiler
- CDK Virtual Scroll
- Signals + computed/effect の最適化
