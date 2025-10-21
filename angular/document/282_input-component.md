# #282 「Input Component - 入力フィールド」

## 概要
Input Componentはフォームで頻用されるテキスト入力を統一したスタイルとバリデーション表示で提供し、ControlValueAccessorを実装することでAngular Formsと連携する。

## 学習目標
- ControlValueAccessorを使った再利用可能な入力コンポーネントを作成する
- label・プレースホルダー・エラーメッセージのInput設計を学ぶ
- SignalとフォームAPIを同期させる

## 技術ポイント
- ControlValueAccessor
- バリデーション表示
- OnPush + signalによる状態同期

## 📺 画面表示用コード（動画用）
```typescript
@Component({ selector: 'app-input', standalone: true, template: `<label [for]="id">{{ label }}<input [id]="id" [value]="value" [attr.placeholder]="placeholder" (input)="update($any($event.target).value)" (blur)="onTouched()"></label>`, providers: [{ provide: NG_VALUE_ACCESSOR, useExisting: forwardRef(() => InputComponent), multi: true }], changeDetection: ChangeDetectionStrategy.OnPush })
export class InputComponent implements ControlValueAccessor {
  @Input() label = ''; @Input() placeholder = '';
  value = '';
  readonly id = crypto.randomUUID();
  private onChange = (v: string) => {}; private onTouched = () => {};
  update(next: string): void { this.value = next; this.onChange(next); }
  writeValue(value: string | null): void { this.value = value ?? ''; }
  registerOnChange(fn: (v: string) => void): void { this.onChange = fn; }
  registerOnTouched(fn: () => void): void { this.onTouched = fn; }
}
```

```html
<form [formGroup]="form"><app-input formControlName="name" label="お名前"></app-input></form>
```

```typescript
this.form = this.fb.group({ name: this.fb.control('') });
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-input-field',
  standalone: true,
  imports: [ReactiveFormsModule, InputComponent],
  template: `
    <app-input formControlName="email" label="メール" placeholder="example@domain.com"></app-input>
    <p *ngIf="form.controls.email.invalid && form.controls.email.touched" class="error">メール形式が正しくありません</p>
  `,
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class InputFieldComponent {
  readonly form = inject(NonNullableFormBuilder).group({ email: ['', [Validators.required, Validators.email]] });
}
```

## ベストプラクティス
- ControlValueAccessorを実装してTemplate-driven/Reactive両方に対応する
- エラー表示はコンポーネント外から差し込めるようSlotやInputを用意する
- labelとaria-describedbyを設定しアクセシビリティを確保する

## 注意点
- crypto.randomUUID()が使用できない環境ではユーティリティで代替する
- OnPush使用時はwriteValueで参照を更新する
- touched状態はregisterOnTouchedで反映させる

## 関連技術
- Reactive Forms
- ControlValueAccessor
- Accessibility
