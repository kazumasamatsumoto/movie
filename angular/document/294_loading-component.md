# #294 「Loading Component - ローディング表示」

## 概要
Loading Componentは処理中の状態をユーザーに知らせるインジケーターで、インライン表示と全画面オーバーレイを統一したUIとして提供する。

## 学習目標
- ローディングインジケーターのデザインを統一する
- Signalでグローバルなロード状態を管理する
- アクセシビリティに配慮したテキストとARIA属性を設定する

## 技術ポイント
- role="status" / aria-live
- Angular Signals
- Overlayオプション

## 📺 画面表示用コード（動画用）
```typescript
@Component({ selector: 'app-loading', standalone: true, template: `<div class="loading" role="status" aria-live="polite"><span class="loading__spinner"></span><span class="loading__label">{{ label }}</span></div>`, changeDetection: ChangeDetectionStrategy.OnPush })
export class LoadingComponent {
  @Input() label = '読み込み中...';
}
```

```typescript
@Injectable({ providedIn: 'root' })
export class LoadingStore {
  private readonly state = signal(0);
  readonly isLoading = computed(() => this.state() > 0);
  start(): void { this.state.update(v => v + 1); }
  stop(): void { this.state.update(v => Math.max(0, v - 1)); }
}
```

```html
<ng-container *ngIf="loading.isLoading()"><app-loading label="データ取得中"></app-loading></ng-container>
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-loading-demo',
  standalone: true,
  imports: [CommonModule, LoadingComponent],
  template: `
    <button type="button" (click)="fetch()">データ取得</button>
    <section class="overlay" *ngIf="store.isLoading()">
      <app-loading label="保存しています"></app-loading>
    </section>
  `,
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class LoadingDemoComponent {
  constructor(public readonly store: LoadingStore) {}
  async fetch(): Promise<void> {
    this.store.start();
    await delay(1200);
    this.store.stop();
  }
}

async function delay(ms: number): Promise<void> {
  return new Promise(resolve => setTimeout(resolve, ms));
}
```

## ベストプラクティス
- カウンタ方式でネストした非同期処理でも正しく停止できるようにする
- テキストで何が行われているかを伝え、無限ループに見えないようにする
- 全画面オーバーレイでは背景を半透明にし操作できないことを明示する

## 注意点
- Loading表示が長い場合は進捗バーやキャンセル操作を検討する
- スピナーのアニメーションはprefers-reduced-motionを尊重する
- SSRでは初期状態をfalseにしブロッキングを避ける

## 関連技術
- Angular Signals
- Accessibility
- Change Detection
