# #086 「Lifecycle のパフォーマンス影響」

## 概要
Lifecycle Hooksがパフォーマンスに与える影響を理解し、不要な処理や再計算を抑えた設計にする方法を学びます。

## 学習目標
- フック呼び出し頻度が高い箇所を把握する
- 重い処理がパフォーマンスに与える影響を測定する
- SignalsやOnPush戦略で再レンダリングを最適化する

## 技術ポイント
- **高頻度フック**: `ngDoCheck`, `ngAfterViewChecked`, `ngAfterContentChecked`
- **測定**: Angular DevTools Profiler、`performance.now()`で計測
- **最適化**: Signalsのcomputed、`@for`の`track`句、`takeUntilDestroyed`

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```typescript
const start = performance.now();
```

```typescript
ngAfterViewChecked() {
  if (performance.now() - start > 5) { console.warn('重い処理'); }
}
```

```typescript
@for (item of items(); track item.id) { ... }
```

## 💻 詳細実装例（学習用）
```typescript
import { AfterViewChecked, ChangeDetectionStrategy, Component, computed, signal } from '@angular/core';

type Product = { id: number; name: string; price: number };

@Component({
  selector: 'app-performance-monitor',
  standalone: true,
  templateUrl: './performance-monitor.component.html',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class PerformanceMonitorComponent implements AfterViewChecked {
  private readonly start = performance.now();
  readonly items = signal<Product[]>([]);
  readonly expensiveComputed = computed(() =>
    this.items().map((item) => ({ ...item, gross: item.price * 1.1 })),
  );
  checkCount = 0;

  constructor() {
    this.items.set(
      Array.from({ length: 1000 }, (_, i) => ({
        id: i,
        name: `Item ${i}`,
        price: 100 + i,
      })),
    );
  }

  ngAfterViewChecked(): void {
    this.checkCount++;
    const elapsed = performance.now() - this.start;
    if (elapsed > 5 && this.checkCount % 50 === 0) {
      console.warn('描画処理に時間がかかっています', elapsed);
    }
  }
}
```

```html
<p>チェック回数: {{ checkCount }}</p>
<ul>
  <li @for (item of expensiveComputed(); track item.id)">
    {{ item.name }} - {{ item.gross | number: '1.0-0' }} 円
  </li>
</ul>
```

## ベストプラクティス
- ループレンダリングでは`@for`の`track`句を必ず指定し、差分描画を有効にする
- Heavyな計算は`computed`でメモ化し、テンプレート式で繰り返し実行しない
- Angular DevToolsのProfilerでフックの呼び出し回数を確認し、無駄な検知を減らす

## 注意点
- `console.warn`などもコストがかかるため、条件を絞って出力する
- OnPush戦略でもSignalの更新があれば再描画される。不要なSignal更新を避ける
- `ChangeDetectorRef.detectChanges()`を乱用すると逆に性能が悪化する

## 関連技術
- ChangeDetectionStrategy.OnPush
- Signalsと`computed` / `effect`
- Angular DevTools Profiler
