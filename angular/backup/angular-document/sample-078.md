# #078 「ngOnDestroy での購読解除」

## 概要
Observableの購読を`ngOnDestroy`で確実に解除し、不要なデータストリームやイベントが残らないようにする方法を学びます。

## 学習目標
- Subscription解除パターン（配列管理、`takeUntil`、`DestroyRef`）を理解する
- `ngOnDestroy`で購読解除を統一する
- Signals化やAsyncPipeなど解除が不要な手段も検討する

## 技術ポイント
- **Subscription管理**: `private subscription?: Subscription`
- **takeUntil**: `Subject`や`takeUntilDestroyed`で自動解除
- **AsyncPipe**: テンプレート側で購読しAngularに解除を任せる


```typescript
private readonly destroy$ = new Subject<void>();
```

```typescript
stream$.pipe(takeUntil(this.destroy$)).subscribe();
```

```typescript
ngOnDestroy() {
  this.destroy$.next();
  this.destroy$.complete();
}
```

## 💻 詳細実装例（学習用）
```typescript
import { Component, DestroyRef, OnDestroy, inject } from '@angular/core';
import { Subject, interval, takeUntil } from 'rxjs';

@Component({
  selector: 'app-subscription-cleaner',
  standalone: true,
  templateUrl: './subscription-cleaner.component.html',
})
export class SubscriptionCleanerComponent implements OnDestroy {
  private readonly destroy$ = new Subject<void>();
  private readonly destroyRef = inject(DestroyRef);

  constructor() {
    interval(1000)
      .pipe(takeUntil(this.destroy$))
      .subscribe((value) => console.log('tick', value));

    interval(500)
      .pipe(takeUntilDestroyed(this.destroyRef))
      .subscribe();
  }

  ngOnDestroy(): void {
    this.destroy$.next();
    this.destroy$.complete();
  }
}
```

```html
<p>購読解除のデモ。コンポーネント破棄時にログが止まります。</p>
```

## ベストプラクティス
- 複数購読を管理する場合は`Subscription`を配列に溜めて`forEach(unsubscribe)`するか、`add`メソッドでまとめる
- Angular v16以降は`DestroyRef`を利用すると`takeUntilDestroyed`で簡潔に書ける
- AsyncPipeを利用できる場面ではテンプレートに任せ、購読解除コードを減らす

## 注意点
- `Subject`を使う場合は`complete()`も呼び、メモリ解放を確実にする
- `takeUntil`に使うSubjectが外部から`next()`されないようカプセル化する
- `interval`などストリームが永続的に動くものは特に解除を忘れない

## 関連技術
- `AsyncPipe`でのテンプレート購読
- Angular CDK `takeUntilDestroyed`
- SignalsでのObservableブリッジ (`toSignal`)
