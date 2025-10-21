# #284 「Select Component - セレクトボックス」

## 概要
Select Componentは選択肢の表示と値のバインディングを共通化し、オプション定義・バリデーション・アクセシビリティを統一したフォームコンポーネントである。

## 学習目標
- 型安全なオプションリストを定義する
- ControlValueAccessorでフォームとの連携を実装する
- 単一・複数選択に対応したUIを設計する

## 技術ポイント
- Optionモデル
- ControlValueAccessor
- trackBy/Signalsによるパフォーマンス向上

## 📺 画面表示用コード（動画用）
```typescript
export type SelectOption<T> = { readonly value: T; readonly label: string; };
```

```typescript
@Component({ selector: 'app-select', standalone: true, template: `<label [for]="id">{{ label }}<select [id]="id" [ngModel]="value" (ngModelChange)="change($event)"><option *ngFor="let option of options; trackBy: track" [ngValue]="option.value">{{ option.label }}</option></select></label>`, providers: [{ provide: NG_VALUE_ACCESSOR, useExisting: forwardRef(() => SelectComponent), multi: true }], changeDetection: ChangeDetectionStrategy.OnPush })
export class SelectComponent<T> implements ControlValueAccessor {
  @Input() label = ''; @Input() options: ReadonlyArray<SelectOption<T>> = [];
  value?: T; readonly id = crypto.randomUUID();
  private onChange = (v: T | undefined) => {}; private onTouched = () => {};
  change(next: T): void { this.value = next; this.onChange(next); this.onTouched(); }
  writeValue(value: T | undefined): void { this.value = value; }
  registerOnChange(fn: (v: T | undefined) => void): void { this.onChange = fn; }
  registerOnTouched(fn: () => void): void { this.onTouched = fn; }
  track = (_: number, item: SelectOption<T>) => item.value;
}
```

```html
<app-select formControlName="country" label="国" [options]="countries"></app-select>
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-select-demo',
  standalone: true,
  imports: [ReactiveFormsModule, SelectComponent],
  template: `
    <form [formGroup]="form">
      <app-select formControlName="country" label="国" [options]="countries"></app-select>
      <p *ngIf="form.controls.country.invalid && form.controls.country.touched" class="error">必須項目です</p>
    </form>
  `,
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class SelectDemoComponent {
  readonly countries: ReadonlyArray<SelectOption<string>> = [
    { value: 'jp', label: '日本' },
    { value: 'us', label: 'アメリカ' },
    { value: 'fr', label: 'フランス' }
  ];
  readonly form = inject(NonNullableFormBuilder).group({ country: ['', Validators.required] });
}
```

## ベストプラクティス
- Optionモデルを型定義し、value/labelの不整合を防ぐ
- trackByでオプション再描画を抑制する
- ラベルとエラーメッセージを外部から提供できるようにする

## 注意点
- 多言語対応時はlabelをi18nキーで扱う
- 複数選択を追加する場合は`multiple`属性と配列型FormControlを用意する
- ngModelを使用する場合はFormsModuleの単一責務を守る

## 関連技術
- Reactive Forms
- ControlValueAccessor
- i18n
