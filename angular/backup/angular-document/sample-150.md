# #150 「ContentChildren QueryList 活用」

## 概要
`@ContentChildren`で取得した`QueryList`を活用し、投影された複数コンテンツの状態管理や動的操作を行う方法を詳しく紹介します。

## 学習目標
- ContentChildrenの`QueryList`メソッドを把握する
- 投影要素の追加・削除を`changes`で監視するテクニックを習得する
- `QueryList`を配列に変換して再利用する処理を実装できるようにする

## 技術ポイント
- **反復**: `tabs.forEach((tab) => tab.activate())`
- **変換**: `[...tabs]`で配列に変換
- **changes監視**: `tabs.changes.subscribe(...)`で動的な更新に対応

```typescript
this.items.forEach((item) => item.updateState());
```

```typescript
const first = this.items.first;
```

```typescript
this.items.changes.subscribe(() => this.sync());
```

## 💻 詳細実装例（学習用）
```typescript
// step.directive.ts
import { Directive, Input } from '@angular/core';

@Directive({
  selector: '[appStep]',
  standalone: true,
})
export class StepDirective {
  @Input() label = '';
  active = false;

  activate(): void {
    this.active = true;
  }

  deactivate(): void {
    this.active = false;
  }
}
```

```typescript
// stepper.component.ts
import { AfterContentInit, Component, ContentChildren, QueryList } from '@angular/core';
import { StepDirective } from './step.directive';
import { takeUntilDestroyed } from '@angular/core/rxjs-interop';

@Component({
  selector: 'app-stepper',
  standalone: true,
  templateUrl: './stepper.component.html',
})
export class StepperComponent implements AfterContentInit {
  @ContentChildren(StepDirective)
  steps!: QueryList<StepDirective>;

  currentIndex = 0;

  ngAfterContentInit(): void {
    this.activate(0);
    this.steps.changes
      .pipe(takeUntilDestroyed())
      .subscribe(() => this.ensureActiveIndex());
  }

  next(): void {
    this.activate(Math.min(this.currentIndex + 1, this.steps.length - 1));
  }

  activate(index: number): void {
    this.currentIndex = index;
    this.steps.forEach((step, i) => step[i === index ? 'activate' : 'deactivate']());
  }

  private ensureActiveIndex(): void {
    if (this.currentIndex >= this.steps.length) {
      this.activate(Math.max(0, this.steps.length - 1));
    } else {
      this.activate(this.currentIndex);
    }
  }
}
```

```html
<!-- stepper.component.html -->
<nav class="stepper-header">
  <span
    @for (let step of steps; track step.label; let i = index)
    [class.active]="step.active"
  >
    {{ step.label }}
  </span>
</nav>
<section class="stepper-body">
  <ng-content></ng-content>
</section>
<button type="button" (click)="next()">次へ</button>
```

```html
<!-- parent.component.html -->
<app-stepper>
  <article appStep label="概要">概要内容</article>
  <article appStep label="詳細">詳細内容</article>
  <article appStep label="確認">確認内容</article>
</app-stepper>
```

## ベストプラクティス
- QueryListを操作するロジックは専用メソッドにまとめ、再利用しやすくする
- `changes`購読は`takeUntilDestroyed`などで管理し、リークを防ぐ
- 投影コンテンツにディレクティブを付与してAPIを統一すると、操作が簡潔になる

## 注意点
- QueryListの配列化はスナップショットであり、最新状態に合わせる場合は再取得が必要
- 投影コンテンツが非同期に追加される場合、初期化順序に気を付ける
- 複雑なロジックは状態管理サービスに抽出し、コンポーネントを薄くすることも検討する

## 関連技術
- `@ContentChild`で単一コンテンツを参照
- `Directive`で投影要素に機能を付与
- `takeUntilDestroyed`（Angular v16+）での購読解除
