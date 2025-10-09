# #073 「ngOnDestroy でのメモリリーク対策」

## 概要
`ngOnDestroy`でクリーンアップ処理を徹底し、Angularアプリで発生しがちなメモリリークを防ぐテクニックを学びます。

## 学習目標
- メモリリークの典型例（購読、タイマー、DOMリスナー）を把握する
- `ngOnDestroy`での解放パターンを実装する
- `DestroyRef`やAngular CDKヘルパーを活用する

## 技術ポイント
- **購読解除**: RxJS `takeUntil`, `takeUntilDestroyed`で自動解放
- **タイマー停止**: `clearInterval`, `clearTimeout` を忘れずに実行
- **effect cleanup**: Signalsの`effect`戻り値で破棄処理を行う

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```typescript
const destroyRef = inject(DestroyRef);
```

```typescript
effect(() => { /* ... */ return () => cleanup(); }, { scope: destroyRef });
```

```typescript
takeUntilDestroyed(destroyRef)
```

## 💻 詳細実装例（学習用）
```typescript
import { Component, DestroyRef, OnDestroy, effect, inject, signal } from '@angular/core';
import { interval } from 'rxjs';
import { takeUntilDestroyed } from '@angular/core/rxjs-interop';

@Component({
  selector: 'app-leak-safe',
  standalone: true,
  templateUrl: './leak-safe.component.html',
})
export class LeakSafeComponent implements OnDestroy {
  private readonly destroyRef = inject(DestroyRef);
  readonly tick = signal(0);
  readonly title = signal('Lifecycle Demo');
  private intervalId!: number;

  constructor() {
    interval(1000)
      .pipe(takeUntilDestroyed(this.destroyRef))
      .subscribe((value) => this.tick.set(value));

    this.intervalId = window.setInterval(() => console.log('alive'), 5000);

    effect(
      () => {
        document.title = this.title();
        return () => {
          document.title = 'Angular App';
        };
      },
      { scope: this.destroyRef },
    );
  }

  ngOnDestroy(): void {
    clearInterval(this.intervalId);
  }
}
```

```html
<p>Tick: {{ tick() }}</p>
```

## ベストプラクティス
- `DestroyRef`を使うと`ngOnDestroy`を書かずにクリーンアップ処理を登録できる
- DOMリスナーは`Renderer2.listen`を使用すると解除関数が返り、自動的に`ngOnDestroy`で呼べる
- `signal.effect`の戻り値や`takeUntilDestroyed`で解放を自動化する

## 注意点
- グローバル状態（localStorageなど）は破棄タイミングが異なるため、必要に応じてサービス側で管理する
- `takeUntilDestroyed`はAngular v16以降で利用可能、バージョンに注意
- エラーハンドリングで`destroyRef.onDestroy`内から再度状態更新すると無限ループになる可能性がある

## 関連技術
- Angular CDKの`coerceBooleanProperty`などユーティリティ
- Web APIの`AbortController`でfetchを中断
- Signals `effect` とLifecycleの統合
