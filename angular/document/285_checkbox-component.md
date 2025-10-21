# #285 「Checkbox Component - チェックボックス」

## 概要
Checkbox Componentはオン/オフおよび三状態の入力を統一されたUIと型安全なAPIで提供し、フォーム連携とアクセシビリティを確保するコンポーネントである。

## 学習目標
- checked/indeterminate状態を管理する
- ControlValueAccessorを用いたフォーム連携を行う
- 複数選択リストへの展開方法を理解する

## 技術ポイント
- indeterminate属性
- ChangeDetectionStrategy.OnPush
- ControlValueAccessor

## 📺 画面表示用コード（動画用）
```typescript
@Component({ selector: 'app-checkbox', standalone: true, template: `<label class="checkbox" [class.left]="labelPosition==='left'"><span *ngIf="labelPosition==='left'">{{ label }}</span><input type="checkbox" [checked]="checked" [indeterminate]="indeterminate" (change)="onToggle($any($event.target).checked)"><span *ngIf="labelPosition==='right'">{{ label }}</span></label>`, providers: [{ provide: NG_VALUE_ACCESSOR, useExisting: forwardRef(() => CheckboxComponent), multi: true }], changeDetection: ChangeDetectionStrategy.OnPush })
export class CheckboxComponent implements ControlValueAccessor {
  @Input() label = ''; @Input() labelPosition: 'left' | 'right' = 'right';
  checked = false; indeterminate = false;
  private onChange = (v: boolean) => {}; private onTouched = () => {};
  onToggle(next: boolean): void { this.indeterminate = false; this.checked = next; this.onChange(next); this.onTouched(); }
  writeValue(value: boolean | null): void { this.checked = !!value; }
  registerOnChange(fn: (v: boolean) => void): void { this.onChange = fn; }
  registerOnTouched(fn: () => void): void { this.onTouched = fn; }
}
```

```html
<app-checkbox formControlName="terms" label="利用規約に同意する"></app-checkbox>
```

```typescript
this.form = this.fb.group({ terms: this.fb.control(false, Validators.requiredTrue) });
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-checkbox-group',
  standalone: true,
  imports: [ReactiveFormsModule, CheckboxComponent],
  template: `
    <form [formGroup]="form">
      <div formArrayName="subscriptions">
        <app-checkbox *ngFor="let option of options; let i = index; trackBy: track" [label]="option.label" labelPosition="left" [formControlName]="i"></app-checkbox>
      </div>
    </form>
  `,
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class CheckboxGroupComponent {
  readonly options = [
    { label: 'ニュース', value: 'news' },
    { label: 'イベント', value: 'event' },
    { label: 'お知らせ', value: 'notice' }
  ];
  private readonly fb = inject(NonNullableFormBuilder);
  readonly form = this.fb.group({ subscriptions: this.fb.array(this.options.map(() => this.fb.control(false))) });
  track = (_: number, item: { value: string }) => item.value;
}
```

## ベストプラクティス
- indeterminateは描画時にのみ設定されるため状態変更後は解除する
- label位置の切り替えをInputで提供しアクセシビリティ属性を調整する
- 複数選択は配列FormControlとtrackByで性能を確保する

## 注意点
- 複合コンポーネントでngModelを使用する場合はControlValueAccessor実装を検討する
- display:blockラベルでクリック領域を拡大し操作ミスを防ぐ
- キーボード操作でフォーカスリングを意図的に保持する

## 関連技術
- Reactive Forms
- ControlValueAccessor
- Accessibility
