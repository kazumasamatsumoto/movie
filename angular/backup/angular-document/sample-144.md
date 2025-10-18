# #144 「ViewChildren 変更監視」

## 概要
`@ViewChildren`が返す`QueryList`の`changes` Observableを使い、ビュー内の要素追加・削除を監視してリアクティブに処理する方法を学びます。

## 学習目標
- QueryListの`changes` Observableの仕組みを理解する
- 監視を開始する適切なタイミングと購読解除の方法を習得する
- 変化に応じてUIや状態を更新する実装パターンを把握する

## 技術ポイント
- **changes**: `queryList.changes.subscribe(...)`
- **購読解除**: `takeUntilDestroyed`や`DestroyRef`を利用
- **再描画**: 変化に応じてメソッドを再実行する

```typescript
this.items.changes.subscribe(() => this.updateMarkers());
```

```typescript
import { takeUntilDestroyed } from '@angular/core/rxjs-interop';
```

```typescript
this.items.forEach((item) => item.nativeElement.classList.add('mounted'));
```

## 💻 詳細実装例（学習用）
```typescript
// dynamic-list.component.ts
import { AfterViewInit, Component, DestroyRef, ElementRef, QueryList, ViewChildren } from '@angular/core';
import { takeUntilDestroyed } from '@angular/core/rxjs-interop';

@Component({
  selector: 'app-dynamic-list',
  standalone: true,
  templateUrl: './dynamic-list.component.html',
})
export class DynamicListComponent implements AfterViewInit {
  items = ['A', 'B', 'C'];

  @ViewChildren('entry')
  entries!: QueryList<ElementRef<HTMLDivElement>>;

  constructor(private readonly destroyRef: DestroyRef) {}

  ngAfterViewInit(): void {
    this.applyMarkers();
    this.entries.changes
      .pipe(takeUntilDestroyed(this.destroyRef))
      .subscribe(() => this.applyMarkers());
  }

  add(): void {
    this.items = [...this.items, `Item ${Date.now()}`];
  }

  private applyMarkers(): void {
    this.entries.forEach((entry, index) => {
      entry.nativeElement.dataset.index = `${index}`;
    });
  }
}
```

```html
<!-- dynamic-list.component.html -->
<button type="button" (click)="add()">アイテム追加</button>
<div #entry *ngFor="let item of items">
  {{ item }}
</div>
```

## ベストプラクティス
- `changes`を購読する場合は必ず購読解除を行い、メモリリークを防ぐ
- 変化時に重い処理を避け、必要最小限の更新にとどめる
- QueryListの状態をログする際はデバッグ時のみにし、本番では削除する

## 注意点
- `changes`は初期状態では発火しないため、`ngAfterViewInit`で一度処理する必要がある
- *ngIfで要素が切り替わるたびに発火するので、連続更新時のパフォーマンスに注意
- `changes`はmicrotaskで通知されるため、同期処理の順序に気を付ける

## 関連技術
- RxJSオペレーター（`takeUntil`, `tap`など）
- `@ContentChildren`の`changes`
- Angular DevToolsでのビュー更新確認
