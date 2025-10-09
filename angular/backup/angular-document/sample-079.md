# #079 「Lifecycle でのタイマー処理」

## 概要
Lifecycle Hooksを用いて`setTimeout`や`setInterval`などのタイマーを開始・停止し、コンポーネントの寿命に合わせたタイマー管理を行う方法を学びます。

## 学習目標
- タイマーの開始タイミングを`ngOnInit`や`ngAfterViewInit`で制御する
- `ngOnDestroy`でタイマーを確実に解除する
- SignalsやRxJSのタイマーストリームを併用する

## 技術ポイント
- **開始**: `ngOnInit`で`setInterval`, `setTimeout`をセット
- **停止**: `ngOnDestroy`で`clearInterval`, `clearTimeout`
- **RxJS活用**: `timer`, `interval`を`takeUntil`で制御


```typescript
ngOnInit(): void {
  this.intervalId = window.setInterval(() => this.tick(), 1000);
}
```

```typescript
ngOnDestroy(): void {
  clearInterval(this.intervalId);
}
```

```typescript
timer(5000).pipe(takeUntilDestroyed(this.destroyRef));
```

## 💻 詳細実装例（学習用）
```typescript
import { Component, DestroyRef, OnDestroy, OnInit, inject, signal } from '@angular/core';
import { interval, takeUntilDestroyed } from '@angular/core/rxjs-interop';

@Component({
  selector: 'app-timer-manager',
  standalone: true,
  templateUrl: './timer-manager.component.html',
})
export class TimerManagerComponent implements OnInit, OnDestroy {
  private intervalId?: number;
  private readonly destroyRef = inject(DestroyRef);
  readonly seconds = signal(0);
  readonly fastTick = signal(0);

  ngOnInit(): void {
    this.intervalId = window.setInterval(() => {
      this.seconds.update((s) => s + 1);
    }, 1000);

    interval(500)
      .pipe(takeUntilDestroyed(this.destroyRef))
      .subscribe(() => this.fastTick.update((c) => c + 1));
  }

  ngOnDestroy(): void {
    if (this.intervalId) {
      clearInterval(this.intervalId);
    }
  }
}
```

```html
<p>1秒タイマー: {{ seconds() }}s</p>
<p>500msティック: {{ fastTick() }}</p>
```

## ベストプラクティス
- `setInterval`のIDはクラスプロパティで保持し、破棄時に確実に解除する
- RxJSの`interval`は`takeUntilDestroyed`でコンポーネント寿命に合わせて自動停止させる
- タイマー処理が重い場合はWeb Workerや`requestAnimationFrame`を検討する

## 注意点
- `setInterval`を多用するとブラウザのタスクが詰まりやすいので、必要最小限にする
- SSRでは`window`が存在しないため、タイマーを起動する前にプラットフォームを確認する
- タイマー内で直接DOM操作せず、Signalなど状態を介してUI更新する

## 関連技術
- RxJS `timer`, `interval`
- `DestroyRef`によるクリーンアップ
- Signalsの`effect`でタイマー状態を監視
