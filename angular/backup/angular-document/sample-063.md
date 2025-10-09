# #063 「ngOnChanges - SimpleChanges の活用」

## 概要
`ngOnChanges`に渡される`SimpleChanges`から前回値・現在値・初回かどうかを読み取り、差分ベースで処理を行う方法を学びます。

## 学習目標
- `SimpleChanges`の構造を理解する
- `previousValue` / `currentValue` を比較して差分に応じた処理を実装する
- `isFirstChange()` を利用して初回だけのロジックを分岐させる

## 技術ポイント
- **SimpleChange**: `previousValue`, `currentValue`, `firstChange`を持つ
- **差分処理**: 値が変わったときだけAPIを再呼び出すなどの最適化が可能
- **初回判定**: `isFirstChange()`で初期化と以後の更新を分離

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```typescript
ngOnChanges(changes: SimpleChanges) {
  const item = changes['filter'];
}
```

```typescript
if (item && !item.isFirstChange()) {
  reload();
}
```

```typescript
console.log(item.previousValue, item.currentValue);
```

## 💻 詳細実装例（学習用）
```typescript
import { Component, Input, OnChanges, SimpleChanges, computed, signal } from '@angular/core';

@Component({
  selector: 'app-filter-panel',
  standalone: true,
  templateUrl: './filter-panel.component.html',
})
export class FilterPanelComponent implements OnChanges {
  @Input() category = 'all';
  @Input() sortOrder: 'asc' | 'desc' = 'asc';

  private readonly reloads = signal(0);
  readonly lastChange = signal<string | null>(null);
  readonly reloadCount = computed(() => this.reloads());

  ngOnChanges(changes: SimpleChanges): void {
    const categoryChange = changes['category'];
    const sortChange = changes['sortOrder'];

    if (categoryChange) {
      this.lastChange.set(
        `category: ${categoryChange.previousValue} → ${categoryChange.currentValue}`,
      );
    }

    if (sortChange && !sortChange.isFirstChange()) {
      this.reloads.update((count) => count + 1);
    }
  }
}
```

```html
<h4>Filter Panel</h4>
<p>カテゴリ: {{ category }}</p>
<p>ソート: {{ sortOrder }}</p>
<p>リロード回数: {{ reloadCount() }}</p>
<p *ngIf="lastChange()">最終更新: {{ lastChange() }}</p>
```

## ベストプラクティス
- `isFirstChange()`を活用して初期化と更新を分けると、無駄なAPI呼び出しを避けられる
- 差分が複数ある場合は`changes`オブジェクトから必要なキーのみを取り出し、キー存在をチェックしてから処理する
- 変更履歴をSignalやサービスに保存しておくとデバッグが容易になる

## 注意点
- 配列やオブジェクトは参照が変わらないと変更として認識されないため、immutable更新を心掛ける
- `SimpleChanges`に含まれるのは今回変更があったプロパティのみ
- `previousValue`は初回呼び出し時に`undefined`になるので必ずnullチェックする

## 関連技術
- Signalベースの`input()` APIによる自動同期
- RxJSの`distinctUntilChanged`との組み合わせ
- `OnPush`戦略での差分検知
