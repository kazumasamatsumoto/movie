# #072 「ngOnDestroy - クリーンアップ処理」

## 概要
コンポーネント破棄時に呼び出される`ngOnDestroy`を使って、購読解除やイベントリスナーの片付けを行う方法を学びます。

## 学習目標
- `ngOnDestroy`が呼ばれるタイミングを理解する
- Observable購読・タイマー・外部リソースを適切に解放する
- クリーンアップ処理をサービスやユーティリティ関数に切り出すパターンを習得する

## 技術ポイント
- **OnDestroyインターフェース**: `ngOnDestroy(): void` を実装
- **購読解除**: `Subscription.unsubscribe()` や `Subject` を用いた解放
- **リソース解放**: `removeEventListener`, `clearInterval`, WebSocket close などをまとめて処理

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```typescript
private readonly destroy$ = new Subject<void>();
```

```typescript
ngOnDestroy(): void {
  this.destroy$.next();
  this.destroy$.complete();
}
```

```typescript
interval(1000).pipe(takeUntil(this.destroy$)).subscribe();
```

## 💻 詳細実装例（学習用）
```typescript
import { Component, OnDestroy, signal } from '@angular/core';
import { Subject, interval, takeUntil } from 'rxjs';

@Component({
  selector: 'app-timer-panel',
  standalone: true,
  templateUrl: './timer-panel.component.html',
})
export class TimerPanelComponent implements OnDestroy {
  readonly count = signal(0);
  private readonly destroy$ = new Subject<void>();
  private readonly timer$ = interval(1000).pipe(takeUntil(this.destroy$));

  constructor() {
    this.timer$.subscribe((value) => this.count.set(value));
    window.addEventListener('resize', this.onResize);
  }

  ngOnDestroy(): void {
    this.destroy$.next();
    this.destroy$.complete();
    window.removeEventListener('resize', this.onResize);
  }

  private onResize = () => console.log('resize');
}
```

```html
<p>経過秒: {{ count() }}</p>
```

## ベストプラクティス
- `Subject`+`takeUntil`や`DestroyRef.onDestroy`で解放ロジックを統一する
- イベントリスナーのコールバックはクラスプロパティで参照を保持し、解除時に同じ関数を渡す
- 破棄時に必要なサービスの後処理はメソッド化し、`ngOnDestroy`で呼び出す

## 注意点
- `ngOnDestroy`はガード等でコンポーネントが再利用される場合でも必ず呼ばれるとは限らない（Angularが破棄するタイミングを理解する）
- `Subscription`を配列で管理する場合、`unsubscribe()`の呼び出し漏れがないようまとめて処理する
- SSRでは`window`が存在しないため、イベントリスナー登録時にプラットフォームチェックが必要

## 関連技術
- `DestroyRef` (Angular v16+) によるクリーンアップ
- RxJS `takeUntil`, `takeWhile`
- Angular CDK `takeUntilDestroyed`
