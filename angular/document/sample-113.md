# #113 「親子間通信のベストプラクティス」

## 概要
親子コンポーネント間の通信を設計する際のベストプラクティスを整理し、責務分離と可読性の高いAPI設計を目指します。

## 学習目標
- 親子コンポーネントの責務を明確に分ける
- Input/Outputの命名や型設計を統一する
- 状態の源泉を親に置き、子は表示と通知に集中させるパターンを理解する

## 技術ポイント
- **単方向データフロー**: 親が状態を持ち、子は表示＋イベント通知
- **契約の明確化**: 型注釈、必須Input、イベントデータのスキーマ
- **小さなAPI**: 最小限のInput/Outputでコンポーネント境界を保つ

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```typescript
@Input({ required: true }) item!: Item;
```

```typescript
@Output() update = new EventEmitter<Item>();
```

```html
<app-item-card
  [item]="item"
  (update)="handleUpdate($event)"
></app-item-card>
```

## 💻 詳細実装例（学習用）
```typescript
// item-card.component.ts
import { Component, EventEmitter, Input, Output } from '@angular/core';

type Item = { id: number; title: string; done: boolean };

@Component({
  selector: 'app-item-card',
  standalone: true,
  templateUrl: './item-card.component.html',
})
export class ItemCardComponent {
  @Input({ required: true }) item!: Item;
  @Output() update = new EventEmitter<Item>();

  toggleDone(): void {
    this.update.emit({ ...this.item, done: !this.item.done });
  }
}
```

```html
<!-- item-card.component.html -->
<article class="item-card">
  <h4>{{ item.title }}</h4>
  <p>状態: {{ item.done ? '完了' : '未完了' }}</p>
  <button type="button" (click)="toggleDone()">
    {{ item.done ? '未完に戻す' : '完了にする' }}
  </button>
</article>
```

```typescript
// parent.component.ts
import { Component, signal } from '@angular/core';
import { ItemCardComponent } from './item-card.component';

@Component({
  selector: 'app-task-board',
  standalone: true,
  imports: [ItemCardComponent],
  templateUrl: './task-board.component.html',
})
export class TaskBoardComponent {
  readonly item = signal<Item>({
    id: 1,
    title: 'Input/Outputベストプラクティス',
    done: false,
  });

  handleUpdate(next: Item): void {
    this.item.set(next);
  }
}
```

```html
<!-- task-board.component.html -->
<app-item-card
  [item]="item()"
  (update)="handleUpdate($event)"
></app-item-card>
```

## ベストプラクティス
- 親は状態を保持し、子はUI表示とイベント通知だけに絞る
- Input/Outputには明確な型を付け、契約としてドキュメント化する
- コンポーネント境界は単純に保ち、複雑化したら責務ごとに分割する

## 注意点
- 子が状態を持ちすぎると親との同期が難しくなるため注意する
- API変更時は破壊的変更にならないようエイリアスやバージョニングを活用する
- @Input()や@Output()が多くなったらサービスやSignalsへリファクタを検討する

## 関連技術
- Signalsによる状態管理
- Angular Style Guide（コンポーネントの責務）
- Smart/Dumbコンポーネントアーキテクチャ
