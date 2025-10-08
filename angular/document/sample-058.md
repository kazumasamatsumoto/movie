# #058 「バインディングのパフォーマンス考慮」

## 概要
バインディングが多いテンプレートでパフォーマンスを維持するためのポイントを整理し、Signalsや`@for`の`track`句など最新のAngular v20機能を活用する方法を学びます。

## 学習目標
- 変更検知がどのようにバインディングへ影響するか理解する
- `@for`の`track`句や`@defer`などパフォーマンス向上の仕組みを使用する
- 実測とモニタリングでボトルネックを把握する流れを学ぶ

## 技術ポイント
- **Signals**: プロパティの変更箇所を明確にし、不要な再計算を抑える
- **track句**: `@for (item of items(); track item.id)`で差分描画を最適化
- **@defer / @if**: 必要な要素のみ描画して初期レンダリングを軽くする

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```html
@for (item of items(); track item.id) {
  <app-card [data]="item"></app-card>
}
```

```html
<p>合計: {{ total() }} 円</p>
```

```html
@defer (when heavyReady()) {
  <heavy-panel />
}
```

## 💻 詳細実装例（学習用）
```typescript
import { Component, computed, effect, signal } from '@angular/core';
import { JsonPipe } from '@angular/common';

type Product = { id: number; name: string; price: number; favorite: boolean };

@Component({
  selector: 'app-binding-performance',
  standalone: true,
  imports: [JsonPipe],
  templateUrl: './binding-performance.component.html',
})
export class BindingPerformanceComponent {
  products = signal<Product[]>([
    { id: 1, name: 'Angular Signals入門', price: 4200, favorite: true },
    { id: 2, name: 'Control Flow完全ガイド', price: 3800, favorite: false },
    { id: 3, name: 'Standalone設計実践', price: 4500, favorite: true },
  ]);
  showFavorites = signal(false);
  heavyReady = signal(false);

  filtered = computed(() =>
    this.products().filter((item) =>
      this.showFavorites() ? item.favorite : true,
    ),
  );

  total = computed(() =>
    this.filtered().reduce((sum, item) => sum + item.price, 0),
  );

  constructor() {
    effect(() => {
      console.log('表示件数', this.filtered().length);
    });

    setTimeout(() => this.heavyReady.set(true), 1200);
  }

  toggleFavorites(): void {
    this.showFavorites.update((state) => !state);
  }
}
```

```html
<button type="button" (click)="toggleFavorites()">
  お気に入りのみ: {{ showFavorites() ? 'ON' : 'OFF' }}
</button>

<p>合計金額: {{ total() }} 円</p>

<ul>
  <li
    @for (product of filtered(); track product.id)
  >
    {{ product.name }} - {{ product.price }} 円
    <span *ngIf="product.favorite">★</span>
  </li>
</ul>

@defer (when heavyReady()) {
  <pre>{{ products() | json }}</pre>
}
```

## ベストプラクティス
- Signalやcomputedで参照の安定性を保ち、テンプレート式で新しいオブジェクトを生成しない
- `@for`では必ず`track`句を使い、リストの差分描画を最適化する
- 体感が重くなったらAngular DevToolsのProfilerで再描画回数を確認する

## 注意点
- 大量データの描画では仮想スクロールやページングを検討する
- 同期処理が重い場合はWeb Workerや遅延評価（@defer）で分割する
- デバッグ目的で`console.log`をテンプレート式に書くとパフォーマンスが大きく低下する

## 関連技術
- Angular DevTools Profiler
- CDK Virtual Scroll
- Signals + RxJSハイブリッド戦略
