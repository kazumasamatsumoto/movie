# #101 「@Input() での不変性の考慮」

## 概要
@Input()で受け取ったデータを不変に扱うことで、状態の予測可能性と変更検知の安定性を高めるテクニックを学びます。

## 学習目標
- @Input()における不変データの利点を理解する
- 子コンポーネントでのcopy-on-write戦略を習得する
- TypeScriptのReadonly型やユーティリティの活用を学ぶ

## 技術ポイント
- **Readonly型**: `@Input() item!: Readonly<Item>;`
- **copy-on-write**: 必要なときだけ新しいオブジェクトを生成
- **変更検知最適化**: 不変性でOnPushと組み合わせやすくする


```typescript
@Input() item!: Readonly<Card>;
```

```typescript
get displayItem(): Card {
  return { ...this.item };
}
```

```html
<p>{{ item.title }}</p>
```

## 💻 詳細実装例（学習用）
```typescript
type Card = {
  title: string;
  description: string;
  tags: readonly string[];
};

import { ChangeDetectionStrategy, Component, Input } from '@angular/core';

@Component({
  selector: 'app-card-view',
  standalone: true,
  changeDetection: ChangeDetectionStrategy.OnPush,
  templateUrl: './card-view.component.html',
})
export class CardViewComponent {
  @Input({ required: true }) item!: Readonly<Card>;

  get tags(): string[] {
    return [...this.item.tags];
  }
}
```

```html
<!-- card-view.component.html -->
<article class="card">
  <h3>{{ item.title }}</h3>
  <p>{{ item.description }}</p>
  <ul>
    <li @for (tag of tags; track tag)>{{ tag }}</li>
  </ul>
</article>
```

```typescript
// parent.component.ts
import { Component, signal } from '@angular/core';
import { CardViewComponent } from './card-view.component';

@Component({
  selector: 'app-card-page',
  standalone: true,
  imports: [CardViewComponent],
  template: `
    <app-card-view [item]="card()"></app-card-view>
  `,
})
export class CardPageComponent {
  readonly card = signal<Card>({
    title: 'Angular Immutability',
    description: '不変データで安全なコンポーネント通信を行う',
    tags: ['Angular', 'Immutability'] as const,
  });
}
```

## ベストプラクティス
- 受け取ったデータを直接変更せず、必要に応じてコピーしてから加工する
- TypeScriptのreadonly修飾子やas constで意図を明確化する
- OnPush戦略と組み合わせるとパフォーマンスと安全性が両立する

## 注意点
- 深いネスト構造の不変化には`structuredClone`やImmutableライブラリを検討する
- コピー処理が重くなる場合はSignalsやMemoizationで負荷を分散する
- 参照が変わらないと変化を検知できないため、親側で新しい参照を生成する

## 関連技術
- ChangeDetectionStrategy.OnPush
- Angular Signalsによるstate管理
- ImmerやImmutable.jsなどのライブラリ
