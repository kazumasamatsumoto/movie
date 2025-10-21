# #286 「Radio Component - ラジオボタン」

## 概要
Radio Componentは単一選択を行うフォーム入力で、グループ管理・アクセシビリティ・スタイルを統一した実装を提供する。

## 学習目標
- ラジオグループをControlValueAccessorで実装する
- オプションリストとlabel紐付けを設計する
- アクセシビリティ属性とフォーカス制御を整える

## 技術ポイント
- name属性の共有
- ControlValueAccessor
- aria-describedby

## 📺 画面表示用コード（動画用）
```typescript
export type RadioOption<T> = { readonly value: T; readonly label: string; };
```

```typescript
@Component({ selector: 'app-radio-group', standalone: true, template: `<fieldset [attr.aria-describedby]="hintId"><legend>{{ label }}</legend><label *ngFor="let option of options; trackBy: track"><input type="radio" [name]="name" [value]="option.value" [checked]="option.value === value" (change)="select(option.value)">{{ option.label }}</label></fieldset>`, providers: [{ provide: NG_VALUE_ACCESSOR, useExisting: forwardRef(() => RadioGroupComponent), multi: true }], changeDetection: ChangeDetectionStrategy.OnPush })
export class RadioGroupComponent<T> implements ControlValueAccessor {
  @Input() label = ''; @Input() options: ReadonlyArray<RadioOption<T>> = []; @Input() hintId?: string;
  value?: T; readonly name = crypto.randomUUID();
  private onChange = (v: T | undefined) => {}; private onTouched = () => {};
  select(next: T): void { this.value = next; this.onChange(next); this.onTouched(); }
  writeValue(value: T | undefined): void { this.value = value; }
  registerOnChange(fn: (v: T | undefined) => void): void { this.onChange = fn; }
  registerOnTouched(fn: () => void): void { this.onTouched = fn; }
  track = (_: number, item: RadioOption<T>) => item.value;
}
```

```html
<app-radio-group formControlName="payment" label="支払い方法" [options]="payments"></app-radio-group>
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-radio-demo',
  standalone: true,
  imports: [ReactiveFormsModule, RadioGroupComponent],
  template: `
    <form [formGroup]="form">
      <app-radio-group formControlName="payment" label="支払い方法" [options]="payments" [hintId]="hintId"></app-radio-group>
      <p [id]="hintId">クレジットカードまたは銀行振込を選択してください</p>
    </form>
  `,
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class RadioDemoComponent {
  readonly hintId = 'payment-hint';
  readonly payments: ReadonlyArray<RadioOption<string>> = [
    { value: 'card', label: 'クレジットカード' },
    { value: 'bank', label: '銀行振込' },
    { value: 'cash', label: '代引き' }
  ];
  readonly form = inject(NonNullableFormBuilder).group({ payment: ['card', Validators.required] });
}
```

## ベストプラクティス
- name属性はグループ内で共有し、複数設置時に衝突しないようユニークに生成する
- fieldset/legendを使いグループラベルを明示する
- hintやエラーのaria-describedbyを設定して支援技術に情報を提供する

## 注意点
- オプションリストが動的に変化する場合は選択値の整合性を確認する
- キーボード操作で選択が巡回することをテストする
- formControlName使用時に値の型を厳密に一致させる

## 関連技術
- Reactive Forms
- Accessibility
- Design Tokens
