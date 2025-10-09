# #102 「@Input() の変更検知」

## 概要
@Input()に渡された値が更新された際、Angularの変更検知がどのようにビューを再描画するかを理解し、参照型の注意点と最適化パターンを学びます。

## 学習目標
- 変更検知の基本フローを把握する
- 参照型を更新するときの注意点を理解する
- OnPush戦略やSignalsと合わせた最適化を考える

## 技術ポイント
- **プロパティバインディング再評価**: 親→子で直列に再評価される
- **参照型の落とし穴**: 同じ参照のままではOnPushで検知されない
- **最適化**: Immutable更新・Signalsで明示的に通知


```html
<app-status [state]="status"></app-status>
```

```typescript
@Input() state!: Status;
```

```typescript
this.status = { ...this.status, count: this.status.count + 1 };
```

## 💻 詳細実装例（学習用）
```typescript
type Status = { count: number; online: boolean };

import { ChangeDetectionStrategy, Component, Input } from '@angular/core';

@Component({
  selector: 'app-status',
  standalone: true,
  changeDetection: ChangeDetectionStrategy.OnPush,
  template: `
    <p>Count: {{ state.count }}</p>
    <p>Status: {{ state.online ? 'Online' : 'Offline' }}</p>
  `,
})
export class StatusComponent {
  @Input({ required: true }) state!: Status;
}
```

```typescript
// parent.component.ts
import { ChangeDetectionStrategy, Component, signal } from '@angular/core';
import { StatusComponent } from './status.component';

@Component({
  selector: 'app-status-board',
  standalone: true,
  changeDetection: ChangeDetectionStrategy.OnPush,
  imports: [StatusComponent],
  templateUrl: './status-board.component.html',
})
export class StatusBoardComponent {
  readonly state = signal<Status>({ count: 0, online: false });

  toggleOnline(): void {
    this.state.update((current) => ({ ...current, online: !current.online }));
  }

  increment(): void {
    this.state.update((current) => ({ ...current, count: current.count + 1 }));
  }
}
```

```html
<!-- status-board.component.html -->
<app-status [state]="state()"></app-status>
<button type="button" (click)="increment()">カウント</button>
<button type="button" (click)="toggleOnline()">オンライン切替</button>
```

## ベストプラクティス
- 参照型の変更は新しいオブジェクトを生成して渡し、OnPushでも検知できるようにする
- Signalsを使う場合は`state()`の戻り値を@Input()に渡し、Signalの更新で確実に再評価させる
- 変更検知の走りすぎを感じたらAngular DevToolsやProfilerで計測する

## 注意点
- 子で受け取った参照型を直接ミューテートすると、親が気付かず不整合が起きる
- 手動で`ChangeDetectorRef.markForCheck()`を呼ぶのは最後の手段にする
- OnPush戦略を導入すると@Input()の参照更新を忘れるケースが増えるため、開発ルールを定める

## 関連技術
- ChangeDetectionStrategy.OnPush
- Angular Signals
- Angular DevTools Profiler
