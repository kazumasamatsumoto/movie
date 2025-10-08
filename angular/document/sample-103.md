# #103 「@Input() とngOnChanges の連携」

## 概要
@Input()プロパティの変化を`ngOnChanges`フックで検知し、差分に応じた処理を実行する方法を解説します。

## 学習目標
- `ngOnChanges(changes: SimpleChanges)` の使い方を理解する
- `previousValue` と `currentValue` の比較で差分を抽出する
- `isFirstChange()` を用いた初期化と更新の分岐を学ぶ

## 技術ポイント
- **SimpleChanges**: 変更のあったプロパティだけがキーに含まれる
- **初期化検知**: 初回呼び出し時は`isFirstChange()`がtrue
- **差分処理**: 前回値と現在値を比較して負荷の高い処理を最小化する

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```typescript
ngOnChanges(changes: SimpleChanges) {
  const status = changes['status'];
}
```

```typescript
if (status && !status.isFirstChange()) {
  this.loadDetails(status.currentValue);
}
```

```typescript
@Input() status!: string;
```

## 💻 詳細実装例（学習用）
```typescript
import { Component, Input, OnChanges, SimpleChanges } from '@angular/core';

type OrderSummary = { id: string; amount: number };

@Component({
  selector: 'app-order-status',
  standalone: true,
  templateUrl: './order-status.component.html',
})
export class OrderStatusComponent implements OnChanges {
  @Input({ required: true }) orderId!: string;
  @Input() status: 'pending' | 'confirmed' | 'shipped' = 'pending';
  @Input() summary?: OrderSummary;

  log: string[] = [];

  ngOnChanges(changes: SimpleChanges): void {
    const statusChange = changes['status'];
    if (statusChange) {
      const prev = statusChange.previousValue ?? '(初期値なし)';
      const current = statusChange.currentValue;
      this.log.push(`status: ${prev} → ${current}`);
    }

    if (changes['summary']?.isFirstChange()) {
      this.log.push('summaryが初期化されました');
    }
  }
}
```

```html
<!-- order-status.component.html -->
<section>
  <h4>注文 {{ orderId }}</h4>
  <p>状態: {{ status }}</p>
  <pre>{{ summary | json }}</pre>
  <ul>
    <li @for (item of log; track item)>{{ item }}</li>
  </ul>
</section>
```

```typescript
// parent.component.ts
import { Component, signal } from '@angular/core';
import { OrderStatusComponent } from './order-status.component';

@Component({
  selector: 'app-order-page',
  standalone: true,
  imports: [OrderStatusComponent],
  templateUrl: './order-page.component.html',
})
export class OrderPageComponent {
  readonly status = signal<'pending' | 'confirmed' | 'shipped'>('pending');
  readonly summary = signal({ id: 'A-100', amount: 12800 });

  confirm(): void {
    this.status.set('confirmed');
  }
}
```

```html
<!-- order-page.component.html -->
<app-order-status
  orderId="A-100"
  [status]="status()"
  [summary]="summary()"
></app-order-status>
<button type="button" (click)="confirm()">確定する</button>
```

## ベストプラクティス
- 差分比較は必要なプロパティに限定し、フック内で重い処理を行わない
- `isFirstChange()`を利用して初期ロード時のロジックを制御する
- 変更内容をログに残すとデバッグが容易になる

## 注意点
- `SimpleChanges`に含まれないプロパティは今回変更されていないので、アクセス時にundefinedチェックが必要
- 参照が変わらないと変更として検知されないため、Immutable更新を徹底する
- `ngOnChanges`は`@Input`を持たないコンポーネントでは呼び出されない

## 関連技術
- SimpleChange型のプロパティ (`previousValue`, `currentValue`)
- Angular Signalsと`input()`の組み合わせ
- RxJSでの変更検知（`distinctUntilChanged`）
