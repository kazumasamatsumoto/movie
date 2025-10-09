# #057 「テンプレート式でのメソッド呼び出し注意点」

## 概要
テンプレート式からメソッドを呼ぶ際のパフォーマンス・副作用のリスクを理解し、安全で見通しの良い設計を行うための指針を示します。

## 学習目標
- 変更検知ごとにメソッドが呼ばれる仕組みを理解する
- 重い処理をメソッドにさせず、事前計算やキャッシュを活用する
- 副作用を伴うメソッドをテンプレートから排除する

## 技術ポイント
- **変更検知**: メソッドは検知サイクルごとに再評価されるため、コストが蓄積する
- **純粋性の確保**: テンプレートから呼ぶメソッドは副作用なし・短時間実行を徹底
- **Signals / computed**: 派生値はcomputedやgetterで準備してテンプレートでは呼び出すだけにする

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```html
<!-- ❌ {{ calculateTotal() }} -->
```

```html
<p>{{ totalWithTax() }} 円</p>
```

```html
<li @for (item of filteredItems(); track item.id)>{{ item.name }}</li>
```

## 💻 詳細実装例（学習用）
```typescript
import { Component, computed, signal } from '@angular/core';

@Component({
  selector: 'app-method-binding',
  standalone: true,
  templateUrl: './method-binding.component.html',
})
export class MethodBindingComponent {
  cart = signal([
    { id: 1, name: 'Angular本', price: 2500 },
    { id: 2, name: 'TypeScript本', price: 2800 },
  ]);
  keyword = signal('');
  taxRate = signal(0.1);

  filteredItems = computed(() =>
    this.cart().filter((item) =>
      item.name.toLowerCase().includes(this.keyword().toLowerCase()),
    ),
  );

  total = computed(() =>
    this.cart().reduce((sum, item) => sum + item.price, 0),
  );

  totalWithTax = computed(() =>
    Math.round(this.total() * (1 + this.taxRate())),
  );

  updateKeyword(event: Event): void {
    const input = event.target as HTMLInputElement;
    this.keyword.set(input.value);
  }
}
```

```html
<input
  placeholder="検索"
  (input)="updateKeyword($event)"
  [value]="keyword()"
/>

<ul>
  <li @for (item of filteredItems(); track item.id)">
    {{ item.name }} - {{ item.price }} 円
  </li>
</ul>

<p>小計: {{ total() }} 円</p>
<p>税込: {{ totalWithTax() }} 円</p>
```

## ベストプラクティス
- テンプレート式から呼ぶメソッドはSignalなどで事前計算しておき、getterやcomputedを返す
- フィルタリングやソートは@forの`track`句やcomputedを活用して最小限の再評価に抑える
- どうしてもメソッドを呼ぶ場合はメモ化やキャッシュを検討する

## 注意点
- 非同期処理やAPI呼び出しをテンプレート式から実行するとループ地獄になる
- 変更検知が頻繁に走るコンポーネントほどパフォーマンス影響が大きい
- Mutationを含むメソッドを呼ぶと予期しないExpressionChangedAfterItHasBeenCheckedが発生する

## 関連技術
- Angular Signals / computed
- OnPush戦略とChangeDetection
- Memoizationテクニック（RxJS shareReplayなど）
