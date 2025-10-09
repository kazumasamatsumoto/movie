# #065 「ngOnInit のベストプラクティス」

## 概要
`ngOnInit`で初期化処理を書く際の設計指針を整理し、メンテナンス性とパフォーマンスを両立させるベストプラクティスを紹介します。

## 学習目標
- `ngOnInit`に置く処理の適切な範囲を理解する
- Signalやフォーム初期化を責務ごとに切り出す
- 非同期初期化のエラーハンドリングを設計する

## 技術ポイント
- **責務の明確化**: 初期状態の設定と初回データ取得に限定
- **メソッド分割**: `setupSignals()`, `fetchInitialData()`など小さな関数で構成
- **エラー対応**: try/catchや`catchError`で初期化失敗時のUIを定義

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```typescript
ngOnInit(): void {
  this.setupSignals();
  this.loadInitialData();
}
```

```typescript
private setupSignals() {
  this.state.set({ loading: true });
}
```

```typescript
private async loadInitialData() { /* ... */ }
```

## 💻 詳細実装例（学習用）
```typescript
import { Component, OnInit, signal } from '@angular/core';

type DashboardState = {
  loading: boolean;
  error: string | null;
  metrics: number[];
};

@Component({
  selector: 'app-dashboard',
  standalone: true,
  templateUrl: './dashboard.component.html',
})
export class DashboardComponent implements OnInit {
  readonly state = signal<DashboardState>({
    loading: true,
    error: null,
    metrics: [],
  });

  ngOnInit(): void {
    this.initializeState();
    void this.loadMetrics();
  }

  private initializeState(): void {
    this.state.set({ loading: true, error: null, metrics: [] });
  }

  private async loadMetrics(): Promise<void> {
    try {
      const metrics = await fetchMetrics();
      this.state.update((prev) => ({ ...prev, metrics }));
    } catch (error) {
      this.state.update((prev) => ({
        ...prev,
        error: '読み込みに失敗しました',
      }));
    } finally {
      this.state.update((prev) => ({ ...prev, loading: false }));
    }
  }
}

async function fetchMetrics(): Promise<number[]> {
  await new Promise((resolve) => setTimeout(resolve, 400));
  return [120, 250, 310];
}
```

```html
<section *ngIf="state().error as error">
  <p class="error">{{ error }}</p>
</section>

<section *ngIf="state().loading">読み込み中...</section>

<section *ngIf="!state().loading && !state().error">
  <h3>メトリクス</h3>
  <ul>
    <li @for (value of state().metrics; track value)>{{ value }}</li>
  </ul>
</section>
```

## ベストプラクティス
- `ngOnInit`内ではUI更新用の状態を一括で設定し、副作用は専用メソッドへ委譲する
- 非同期処理は`void`で呼び出し、戻り値を無視する意図を明示する（ESLint対策）
- 基盤ロジックはサービスへ切り出してテストや再利用を容易にする

## 注意点
- `ngOnInit`内で大量の同期処理を行うと初期描画がブロックされる
- スクロールやViewChildなどDOMが必要な処理は`ngAfterViewInit`に移す
- `async ngOnInit()`にする場合でもconstructorで状態を触らないこと

## 関連技術
- Signals / computedによる状態初期化
- RxJSを使った初期データ取得
- Angular ESLintでのLifecycleルール
