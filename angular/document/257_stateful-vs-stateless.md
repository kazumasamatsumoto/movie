# #257 「Stateful vs Stateless Component」

## 概要
Stateful Componentは内部状態や副作用を持ち、Stateless Componentは外部から受け取った情報を表示するだけの純粋なコンポーネントである。

## 学習目標
- StatefulとStatelessの役割差を理解する
- 状態の配置によるテスト容易性の違いを把握する
- Signalsを用いたリファクタリング方法を学ぶ

## 技術ポイント
- Signalによる状態保有
- OnPushレンダリングでStateless化
- ViewModelの型定義

## 📺 画面表示用コード（動画用）
```typescript
@Component({
  selector: 'app-counter-stateful',
  standalone: true,
  template: `<button (click)="increment()">Count: {{ count() }}</button>`
})
export class CounterStatefulComponent {
  protected readonly count = signal(0);
  increment(): void { this.count.update(v => v + 1); }
}
```

```typescript
@Component({
  selector: 'app-counter-stateless',
  standalone: true,
  template: `<button (click)="increment.emit()">Count: {{ value }}</button>`,
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class CounterStatelessComponent {
  @Input({ required: true }) value = 0;
  @Output() increment = new EventEmitter<void>();
}
```

```typescript
export type CounterVm = {
  readonly value: number;
};
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-counter-container',
  standalone: true,
  imports: [CounterStatelessComponent],
  template: `<app-counter-stateless [value]="vm()" (increment)="increment()" />`
})
export class CounterContainerComponent {
  private readonly state = signal(0);
  readonly vm = computed(() => this.state());

  increment(): void {
    this.state.update(v => v + 1);
  }
}
```

## ベストプラクティス
- 状態が必要なコンポーネントだけStatefulにし、表示専用はStatelessへ分離する
- リファクタリング時はSignal Storeやサービスへの移動を検討する
- Stateless ComponentにはOnPush戦略とイミュータブルな入力を組み合わせる

## 注意点
- Stateful Componentが副作用を増やし過ぎるとテストが難しくなる
- Stateless Componentにも過剰なInputを渡さない
- 共有StateはサービスやStoreへ出して複数コンポーネントから使い回す

## 関連技術
- Angular Signals
- Smart/Dumbパターン
- Change Detection戦略
