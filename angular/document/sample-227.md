# #227 「動的 Component のイベント購読」

## 概要
動的に生成したコンポーネントからのイベントは、ComponentRefのinstanceプロパティを通じて@Output()イベントを購読することで受け取れます。適切な購読管理により、メモリリークを防ぎながら双方向のコミュニケーションを実現できます。

## 学習目標
- 動的コンポーネントのイベント購読方法を習得する
- 購読のライフサイクル管理を理解する
- Signal出力との連携方法を学ぶ

## 技術ポイント
- **instance経由のアクセス**: componentRef.instance.event
- **subscribe()での購読**: RxJSのObservableパターン
- **購読解除の重要性**: メモリリーク防止

## 📺 画面表示用コード

### 基本的なイベント購読
```typescript
const ref = this.container.createComponent(ModalComponent);
ref.instance.closeEvent.subscribe(() => {
  console.log('モーダルが閉じられました');
  ref.destroy();
});
```

### 複数イベントの購読
```typescript
const ref = this.container.createComponent(FormComponent);
ref.instance.submit.subscribe(data => console.log('送信:', data));
ref.instance.cancel.subscribe(() => console.log('キャンセル'));
```

### 購読管理（DestroyRef使用）
```typescript
const destroyRef = inject(DestroyRef);
const ref = this.container.createComponent(MyComponent);

ref.instance.dataChanged
  .pipe(takeUntilDestroyed(destroyRef))
  .subscribe(data => this.handleData(data));
```

## 実践的な活用例

### モーダルダイアログの実装
```typescript
// モーダルコンポーネント
@Component({
  selector: 'app-confirm-modal',
  template: `
    <div class="modal">
      <h2>{{ title() }}</h2>
      <p>{{ message() }}</p>
      <button (click)="onConfirm()">確認</button>
      <button (click)="onCancel()">キャンセル</button>
    </div>
  `
})
export class ConfirmModalComponent {
  title = input.required<string>();
  message = input.required<string>();

  confirmed = output<void>();
  cancelled = output<void>();

  onConfirm() {
    this.confirmed.emit();
  }

  onCancel() {
    this.cancelled.emit();
  }
}

// モーダルサービス
@Injectable()
export class ModalService {
  private container = inject(ViewContainerRef);
  private destroyRef = inject(DestroyRef);

  openConfirmModal(title: string, message: string): Promise<boolean> {
    return new Promise((resolve) => {
      const modalRef = this.container.createComponent(ConfirmModalComponent);

      modalRef.setInput('title', title);
      modalRef.setInput('message', message);

      // イベント購読
      modalRef.instance.confirmed
        .pipe(takeUntilDestroyed(this.destroyRef))
        .subscribe(() => {
          resolve(true);
          modalRef.destroy();
        });

      modalRef.instance.cancelled
        .pipe(takeUntilDestroyed(this.destroyRef))
        .subscribe(() => {
          resolve(false);
          modalRef.destroy();
        });
    });
  }
}

// 使用例
async deleteItem() {
  const confirmed = await this.modalService.openConfirmModal(
    '削除確認',
    '本当に削除しますか？'
  );

  if (confirmed) {
    // 削除処理
  }
}
```

### フォームコンポーネントとの連携
```typescript
@Component({
  selector: 'app-user-form',
  template: `
    <form (ngSubmit)="onSubmit()">
      <input [(ngModel)]="formData.name" name="name">
      <input [(ngModel)]="formData.email" name="email">
      <button type="submit">送信</button>
      <button type="button" (click)="onCancel()">キャンセル</button>
    </form>
  `
})
export class UserFormComponent {
  formData = { name: '', email: '' };

  submitted = output<{ name: string; email: string }>();
  cancelled = output<void>();

  onSubmit() {
    this.submitted.emit(this.formData);
  }

  onCancel() {
    this.cancelled.emit();
  }
}

// 動的フォーム表示
export class FormHostComponent {
  private container = inject(ViewContainerRef);
  private destroyRef = inject(DestroyRef);

  showForm() {
    const formRef = this.container.createComponent(UserFormComponent);

    formRef.instance.submitted
      .pipe(takeUntilDestroyed(this.destroyRef))
      .subscribe(data => {
        console.log('フォーム送信:', data);
        this.saveUser(data);
        formRef.destroy();
      });

    formRef.instance.cancelled
      .pipe(takeUntilDestroyed(this.destroyRef))
      .subscribe(() => {
        console.log('フォームキャンセル');
        formRef.destroy();
      });
  }

  saveUser(data: any) {
    // ユーザー保存処理
  }
}
```

### 通知コンポーネントの自動削除
```typescript
@Component({
  selector: 'app-toast',
  template: `
    <div class="toast" [@slideIn]>
      {{ message() }}
      <button (click)="close()">×</button>
    </div>
  `
})
export class ToastComponent {
  message = input.required<string>();
  duration = input(3000);

  closed = output<void>();

  ngOnInit() {
    // 指定時間後に自動クローズ
    setTimeout(() => this.close(), this.duration());
  }

  close() {
    this.closed.emit();
  }
}

@Injectable()
export class ToastService {
  private container = inject(ViewContainerRef);
  private toasts: ComponentRef<ToastComponent>[] = [];

  show(message: string, duration = 3000) {
    const toastRef = this.container.createComponent(ToastComponent);
    toastRef.setInput('message', message);
    toastRef.setInput('duration', duration);

    this.toasts.push(toastRef);

    // クローズイベントを購読
    toastRef.instance.closed.subscribe(() => {
      this.removeToast(toastRef);
    });
  }

  private removeToast(ref: ComponentRef<ToastComponent>) {
    const index = this.toasts.indexOf(ref);
    if (index !== -1) {
      this.toasts.splice(index, 1);
      ref.destroy();
    }
  }
}
```

### イベントチェーンの実装
```typescript
@Component({
  selector: 'app-wizard-step',
  template: `
    <div class="step">
      <h3>{{ title() }}</h3>
      <button (click)="next()">次へ</button>
      <button (click)="previous()">戻る</button>
    </div>
  `
})
export class WizardStepComponent {
  title = input.required<string>();
  stepData = input<any>();

  nextStep = output<any>();
  previousStep = output<void>();

  next() {
    this.nextStep.emit(this.stepData());
  }

  previous() {
    this.previousStep.emit();
  }
}

export class WizardComponent {
  private container = inject(ViewContainerRef);
  private currentStep = 0;
  private stepRefs: ComponentRef<WizardStepComponent>[] = [];

  private steps = [
    { title: 'ステップ1', data: {} },
    { title: 'ステップ2', data: {} },
    { title: 'ステップ3', data: {} }
  ];

  ngAfterViewInit() {
    this.showStep(0);
  }

  showStep(index: number) {
    this.container.clear();
    const step = this.steps[index];

    const stepRef = this.container.createComponent(WizardStepComponent);
    stepRef.setInput('title', step.title);
    stepRef.setInput('stepData', step.data);

    // 次へボタンのイベント
    stepRef.instance.nextStep.subscribe(data => {
      this.steps[index].data = data;
      if (index < this.steps.length - 1) {
        this.showStep(index + 1);
      } else {
        this.completeWizard();
      }
    });

    // 戻るボタンのイベント
    stepRef.instance.previousStep.subscribe(() => {
      if (index > 0) {
        this.showStep(index - 1);
      }
    });

    this.stepRefs[index] = stepRef;
  }

  completeWizard() {
    console.log('ウィザード完了:', this.steps);
  }
}
```

## ベストプラクティス

### 購読の自動管理
```typescript
// ✅ DestroyRef を使った自動購読解除
export class SafeComponent {
  private destroyRef = inject(DestroyRef);

  createWithEvent() {
    const ref = this.container.createComponent(MyComponent);
    ref.instance.myEvent
      .pipe(takeUntilDestroyed(this.destroyRef))
      .subscribe(data => this.handle(data));
  }
}

// ❌ 手動管理は漏れやすい
export class UnsafeComponent {
  private subscription?: Subscription;

  createWithEvent() {
    const ref = this.container.createComponent(MyComponent);
    this.subscription = ref.instance.myEvent.subscribe(data => {
      this.handle(data);
    });
  }
}
```

### 型安全なイベント処理
```typescript
// コンポーネント定義
export class DataComponent {
  dataChanged = output<{ id: number; value: string }>();
}

// イベント購読（型が保証される）
const ref = this.container.createComponent(DataComponent);
ref.instance.dataChanged.subscribe(data => {
  console.log(data.id);     // ✅ 型チェックが効く
  console.log(data.value);  // ✅ 型チェックが効く
});
```

### エラーハンドリング
```typescript
const ref = this.container.createComponent(ApiComponent);
ref.instance.error
  .pipe(
    takeUntilDestroyed(this.destroyRef),
    catchError(err => {
      console.error('コンポーネントエラー:', err);
      return EMPTY;
    })
  )
  .subscribe();
```

## 注意点

### 購読解除の重要性
イベントの購読は必ず解除してください。`takeUntilDestroyed()`などのオペレータを使うことで自動管理できます。

### コンポーネント破棄とイベント
コンポーネントを`destroy()`すると、そのイベント発行は停止します。購読側でエラーにならないよう適切に処理してください。

### 複数回の購読
同じイベントを複数回購読すると、イベントごとに全ての購読が実行されます。意図しない動作に注意してください。

### Signal出力との違い
`output()`（Signal出力）は従来の`@Output()`と同じように`.subscribe()`できますが、Signalベースのリアクティブな処理も可能です。

## 関連技術
- **@Output()**: イベント発行デコレータ
- **output()**: Signal出力（v17.3+）
- **EventEmitter**: イベント発行クラス
- **RxJS**: リアクティブプログラミング
- **takeUntilDestroyed()**: 自動購読解除
- **DestroyRef**: コンポーネント破棄の検知
