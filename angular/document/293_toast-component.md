# #293 「Toast Component - トースト通知」

## 概要
Toast Componentは短時間で消える通知を画面端に表示し、variant別のスタイルと自動消去を提供するUIコンポーネントである。

## 学習目標
- トーストのスタックと自動消去をSignalで管理する
- variantによるスタイル切り替えを実装する
- トーストサービスを用意してアプリ全体から表示する

## 技術ポイント
- Angular Signals
- setTimeoutによる自動破棄
- Overlay/Positioning

## 📺 画面表示用コード（動画用）
```typescript
@Component({ selector: 'app-toast', standalone: true, template: `<article class="toast" [class.toast--success]="variant==='success'" [class.toast--error]="variant==='error'"><p>{{ message }}</p><button type="button" (click)="dismiss.emit()">×</button></article>`, changeDetection: ChangeDetectionStrategy.OnPush })
export class ToastComponent {
  @Input({ required: true }) message!: string;
  @Input() variant: 'info' | 'success' | 'error' = 'info';
  @Output() dismiss = new EventEmitter<void>();
}
```

```typescript
@Injectable({ providedIn: 'root' })
export class ToastStore {
  private readonly toasts = signal<ReadonlyArray<{ id: string; message: string; variant: 'info' | 'success' | 'error' }>>([]);
  readonly list = this.toasts.asReadonly();
  show(message: string, variant: ToastComponent['variant'] = 'info'): void {
    const toast = { id: crypto.randomUUID(), message, variant };
    this.toasts.update(all => [...all, toast]);
    setTimeout(() => this.dismiss(toast.id), 4000);
  }
  dismiss(id: string): void { this.toasts.update(all => all.filter(item => item.id !== id)); }
}
```

```html
<div class="toast-stack">
  @for (toast of store.list(); track toast.id) {
    <app-toast [message]="toast.message" [variant]="toast.variant" (dismiss)="store.dismiss(toast.id)"></app-toast>
  }
</div>
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-toast-demo',
  standalone: true,
  imports: [AsyncPipe, ToastComponent],
  template: `
    <button type="button" (click)="notify('保存しました', 'success')">成功トースト</button>
    <button type="button" (click)="notify('エラーが発生しました', 'error')">エラートースト</button>
    <section class="toast-stack">
      @for (toast of store.list(); track toast.id) {
        <app-toast [message]="toast.message" [variant]="toast.variant" (dismiss)="store.dismiss(toast.id)"></app-toast>
      }
    </section>
  `,
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class ToastDemoComponent {
  constructor(public readonly store: ToastStore) {}
  notify(message: string, variant: ToastComponent['variant']): void {
    this.store.show(message, variant);
  }
}
```

## ベストプラクティス
- トーストの寿命と最大スタック数を設定して画面を圧迫しない
- variantごとにアイコンと色を統一し意味を伝える
- スクリーンリーダーにはaria-live="polite"で通知する

## 注意点
- 同時に多く表示するときはキュー投入の間隔を制御する
- 自動消去される前にユーザーが操作できるようCloseボタンを設置する
- モバイルでは位置とサイズを調整しタップミスを防ぐ

## 関連技術
- Angular Signals
- Overlay
- Accessibility
