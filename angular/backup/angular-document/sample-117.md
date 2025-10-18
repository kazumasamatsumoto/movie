# #117 「Service を使った Component 間通信」

## 概要
共有サービスを使って複数コンポーネント間で状態とイベントをやり取りするパターンを紹介します。SignalやSubjectを活用したリアクティブな同期方法を学びます。

## 学習目標
- サービスに状態を集約し、コンポーネントから利用する流れを理解する
- SignalまたはSubjectを用いて状態を更新・購読する方法を習得する
- プロバイダのスコープを管理し、必要な範囲で状態を共有する

## 技術ポイント
- **サービスの状態**: `signal`または`BehaviorSubject`で状態を保持
- **更新メソッド**: サービスに`set`, `update`などのメソッドを用意
- **スコープ**: `providedIn: 'root'`でアプリ全体、コンポーネント`providers`で限定共有

```typescript
@Injectable({ providedIn: 'root' })
export class CounterStore {
  readonly count = signal(0);
  increment() { this.count.update((c) => c + 1); }
}
```

```typescript
constructor(readonly counter: CounterStore) {}
```

```html
<p>{{ counter.count() }}</p>
```

## 💻 詳細実装例（学習用）
```typescript
// counter-store.service.ts
import { Injectable, signal } from '@angular/core';

@Injectable({ providedIn: 'root' })
export class CounterStore {
  readonly count = signal(0);

  increment(): void {
    this.count.update((value) => value + 1);
  }

  reset(): void {
    this.count.set(0);
  }
}
```

```typescript
// counter-button.component.ts
import { Component } from '@angular/core';
import { CounterStore } from './counter-store.service';

@Component({
  selector: 'app-counter-button',
  standalone: true,
  template: `
    <button type="button" (click)="counter.increment()">+1</button>
    <button type="button" (click)="counter.reset()">リセット</button>
  `,
})
export class CounterButtonComponent {
  constructor(public readonly counter: CounterStore) {}
}
```

```typescript
// counter-display.component.ts
import { Component } from '@angular/core';
import { CounterStore } from './counter-store.service';

@Component({
  selector: 'app-counter-display',
  standalone: true,
  template: `<p>現在のカウント: {{ counter.count() }}</p>`,
})
export class CounterDisplayComponent {
  constructor(public readonly counter: CounterStore) {}
}
```

```typescript
// dashboard.component.ts
import { Component } from '@angular/core';
import { CounterButtonComponent } from './counter-button.component';
import { CounterDisplayComponent } from './counter-display.component';

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [CounterButtonComponent, CounterDisplayComponent],
  template: `
    <app-counter-display></app-counter-display>
    <app-counter-button></app-counter-button>
  `,
})
export class DashboardComponent {}
```

## ベストプラクティス
- サービスは状態と更新メソッドを提供し、コンポーネントはUI表示とユーザー操作に専念する
- 状態が複数のコンポーネントで共有される場合はSignalやObservableでリアクティブに更新する
- クリーンアップが必要な場合は`DestroyRef`や`takeUntilDestroyed`を利用し、購読解除を忘れない

## 注意点
- `providedIn: 'root'`のサービスはアプリ全体で一意になるため、テスト時にはリセット処理を行う
- 大規模な状態管理が必要な場合はNgRxなど専用ライブラリを検討する
- 共有サービスを乱用すると依存が複雑になるため、コンポーネントの責務とサービスの責務を明確にする

## 関連技術
- Angular Signals Storeパターン
- RxJS Subject/BehaviorSubject
- NgRx, NgXs, Akitaなどの状態管理ライブラリ
