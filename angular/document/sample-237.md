# #237 「動的フォーム生成」

## 概要
動的フォーム生成は、設定データやAPIレスポンスからフォームフィールドを動的に作成する技術です。Reactive Formsと動的コンポーネント生成を組み合わせることで、柔軟で再利用可能なフォームシステムを構築できます。

## 学習目標
- 動的フォームフィールド生成の実装方法を習得する
- Reactive Formsとの統合方法を理解する
- バリデーションを含む完全なフォームシステムを構築できる

## 技術ポイント
- **フィールド定義**: メタデータベースの設定
- **Reactive Forms**: FormGroupの動的生成
- **バリデーション**: 動的なバリデータ設定

## 📺 画面表示用コード

### 基本的なフィールド定義
```typescript
interface FieldConfig {
  type: 'text' | 'select' | 'checkbox';
  name: string;
  label: string;
  value?: any;
  options?: string[];
}

const config: FieldConfig = {
  type: 'text',
  name: 'email',
  label: 'メールアドレス'
};
```

### フィールドコンポーネント生成
```typescript
createField(config: FieldConfig) {
  const componentMap = new Map([
    ['text', TextInputComponent],
    ['select', SelectInputComponent],
    ['checkbox', CheckboxInputComponent]
  ]);

  const component = componentMap.get(config.type)!;
  const ref = this.container.createComponent(component);
  ref.setInput('config', config);
}
```

### FormGroup との統合
```typescript
buildForm(fields: FieldConfig[]) {
  const group: any = {};
  fields.forEach(field => {
    group[field.name] = new FormControl(field.value || '');
    this.createField(field);
  });
  this.form = new FormGroup(group);
}
```

## 実践的な活用例(continued)

### 完全な動的フォームシステム
```typescript
interface FieldConfig {
  type: 'text' | 'email' | 'number' | 'select' | 'checkbox' | 'date';
  name: string;
  label: string;
  value?: any;
  placeholder?: string;
  required?: boolean;
  validators?: ValidatorFn[];
  options?: Array<{ label: string; value: any }>;
}

@Component({
  selector: 'app-dynamic-form',
  template: `
    <form [formGroup]="form" (ngSubmit)="onSubmit()">
      <ng-container #fieldsContainer></ng-container>
      <button type="submit" [disabled]="!form.valid">送信</button>
    </form>
  `
})
export class DynamicFormComponent implements AfterViewInit {
  @ViewChild('fieldsContainer', { read: ViewContainerRef })
  container!: ViewContainerRef;

  @Input() config: FieldConfig[] = [];
  @Output() formSubmit = new EventEmitter<any>();

  form!: FormGroup;

  private componentMap = new Map<string, Type<any>>([
    ['text', TextFieldComponent],
    ['email', EmailFieldComponent],
    ['number', NumberFieldComponent],
    ['select', SelectFieldComponent],
    ['checkbox', CheckboxFieldComponent],
    ['date', DateFieldComponent]
  ]);

  ngAfterViewInit() {
    this.buildForm();
  }

  private buildForm() {
    const controls: any = {};

    this.config.forEach(fieldConfig => {
      // FormControl 作成
      const validators = this.getValidators(fieldConfig);
      controls[fieldConfig.name] = new FormControl(
        fieldConfig.value || '',
        validators
      );

      // フィールドコンポーネント生成
      this.createField(fieldConfig);
    });

    this.form = new FormGroup(controls);
  }

  private createField(config: FieldConfig) {
    const componentType = this.componentMap.get(config.type);
    if (!componentType) {
      console.error(`Unknown field type: ${config.type}`);
      return;
    }

    const ref = this.container.createComponent(componentType);
    ref.setInput('config', config);
    ref.setInput('control', this.form.get(config.name));
  }

  private getValidators(config: FieldConfig): ValidatorFn[] {
    const validators: ValidatorFn[] = [];

    if (config.required) {
      validators.push(Validators.required);
    }

    if (config.type === 'email') {
      validators.push(Validators.email);
    }

    if (config.validators) {
      validators.push(...config.validators);
    }

    return validators;
  }

  onSubmit() {
    if (this.form.valid) {
      this.formSubmit.emit(this.form.value);
    }
  }
}
```

### フィールドコンポーネントの実装例
```typescript
// テキストフィールド
@Component({
  selector: 'app-text-field',
  template: `
    <div class="field">
      <label>{{ config().label }}</label>
      <input
        type="text"
        [formControl]="control()"
        [placeholder]="config().placeholder || ''"
      >
      @if (control().invalid && control().touched) {
        <span class="error">{{ getErrorMessage() }}</span>
      }
    </div>
  `,
  standalone: true,
  imports: [ReactiveFormsModule]
})
export class TextFieldComponent {
  config = input.required<FieldConfig>();
  control = input.required<FormControl>();

  getErrorMessage(): string {
    const control = this.control();
    if (control.hasError('required')) {
      return `${this.config().label}は必須です`;
    }
    return '';
  }
}

// セレクトフィールド
@Component({
  selector: 'app-select-field',
  template: `
    <div class="field">
      <label>{{ config().label }}</label>
      <select [formControl]="control()">
        <option value="">選択してください</option>
        @for (option of config().options; track option.value) {
          <option [value]="option.value">{{ option.label }}</option>
        }
      </select>
    </div>
  `,
  standalone: true,
  imports: [ReactiveFormsModule]
})
export class SelectFieldComponent {
  config = input.required<FieldConfig>();
  control = input.required<FormControl>();
}
```

### APIからのフォーム生成
```typescript
@Injectable()
export class DynamicFormService {
  async getFormConfig(formId: string): Promise<FieldConfig[]> {
    const response = await fetch(`/api/forms/${formId}`);
    return response.json();
  }
}

@Component({
  selector: 'app-api-form',
  template: `
    @if (loading()) {
      <p>読み込み中...</p>
    } @else {
      <app-dynamic-form
        [config]="formConfig()"
        (formSubmit)="onSubmit($event)"
      />
    }
  `
})
export class ApiFormComponent implements OnInit {
  @Input() formId!: string;

  private formService = inject(DynamicFormService);

  loading = signal(true);
  formConfig = signal<FieldConfig[]>([]);

  async ngOnInit() {
    const config = await this.formService.getFormConfig(this.formId);
    this.formConfig.set(config);
    this.loading.set(false);
  }

  onSubmit(formValue: any) {
    console.log('Form submitted:', formValue);
  }
}
```

### 条件付きフィールド表示
```typescript
interface ConditionalFieldConfig extends FieldConfig {
  showIf?: {
    field: string;
    value: any;
  };
}

export class ConditionalFormComponent {
  private container = inject(ViewContainerRef);
  form!: FormGroup;
  private fieldRefs = new Map<string, ComponentRef<any>>();

  buildForm(config: ConditionalFieldConfig[]) {
    const controls: any = {};

    config.forEach(fieldConfig => {
      controls[fieldConfig.name] = new FormControl(fieldConfig.value || '');
    });

    this.form = new FormGroup(controls);

    // 条件付きフィールドの監視
    config.forEach(fieldConfig => {
      if (fieldConfig.showIf) {
        this.watchConditionalField(fieldConfig);
      } else {
        this.createField(fieldConfig);
      }
    });
  }

  private watchConditionalField(config: ConditionalFieldConfig) {
    const targetControl = this.form.get(config.showIf!.field);

    targetControl?.valueChanges.subscribe(value => {
      if (value === config.showIf!.value) {
        // 条件を満たす: フィールド表示
        if (!this.fieldRefs.has(config.name)) {
          this.createField(config);
        }
      } else {
        // 条件を満たさない: フィールド削除
        const ref = this.fieldRefs.get(config.name);
        if (ref) {
          ref.destroy();
          this.fieldRefs.delete(config.name);
        }
      }
    });
  }

  private createField(config: FieldConfig) {
    // フィールド生成ロジック
  }
}
```

### マルチステップフォーム
```typescript
interface FormStep {
  title: string;
  fields: FieldConfig[];
}

export class MultiStepFormComponent {
  private container = inject(ViewContainerRef);

  steps: FormStep[] = [];
  currentStep = signal(0);
  forms: FormGroup[] = [];

  loadSteps(steps: FormStep[]) {
    this.steps = steps;
    this.forms = steps.map(step => this.buildFormGroup(step.fields));
    this.showStep(0);
  }

  private buildFormGroup(fields: FieldConfig[]): FormGroup {
    const controls: any = {};
    fields.forEach(field => {
      controls[field.name] = new FormControl(field.value || '');
    });
    return new FormGroup(controls);
  }

  showStep(index: number) {
    this.container.clear();
    this.currentStep.set(index);

    const step = this.steps[index];
    step.fields.forEach(field => this.createField(field));
  }

  nextStep() {
    if (this.currentStep() < this.steps.length - 1) {
      this.showStep(this.currentStep() + 1);
    }
  }

  previousStep() {
    if (this.currentStep() > 0) {
      this.showStep(this.currentStep() - 1);
    }
  }

  submitAll() {
    const allValues = this.forms.map(form => form.value);
    console.log('All form data:', allValues);
  }

  private createField(config: FieldConfig) {
    // フィールド生成ロジック
  }
}
```

### カスタムバリデーション
```typescript
interface FieldConfigWithValidation extends FieldConfig {
  validations?: Array<{
    type: 'required' | 'email' | 'min' | 'max' | 'pattern' | 'custom';
    value?: any;
    message?: string;
  }>;
}

export class ValidatedFormBuilder {
  buildValidators(config: FieldConfigWithValidation): ValidatorFn[] {
    if (!config.validations) return [];

    return config.validations.map(validation => {
      switch (validation.type) {
        case 'required':
          return Validators.required;
        case 'email':
          return Validators.email;
        case 'min':
          return Validators.min(validation.value);
        case 'max':
          return Validators.max(validation.value);
        case 'pattern':
          return Validators.pattern(validation.value);
        case 'custom':
          return this.customValidator(validation.value);
        default:
          return Validators.nullValidator;
      }
    });
  }

  private customValidator(validatorFn: ValidatorFn): ValidatorFn {
    return (control: AbstractControl) => {
      return validatorFn(control);
    };
  }
}
```

## ベストプラクティス

### フィールド設定の型定義
```typescript
// ✅ 厳密な型定義
interface StrictFieldConfig {
  type: 'text' | 'email' | 'select';
  name: string;
  label: string;
}

// ❌ any型の使用
interface LooseFieldConfig {
  [key: string]: any;
}
```

### バリデーションの集約
```typescript
// ✅ バリデーションロジックを関数化
private getValidators(config: FieldConfig): ValidatorFn[] {
  return this.validatorBuilder.build(config);
}

// ✅ エラーメッセージの管理
private getErrorMessage(fieldName: string): string {
  return this.errorMessages.get(fieldName) || 'エラー';
}
```

### フォーム状態の管理
```typescript
// ✅ Signalでの状態管理
formValid = computed(() => this.form()?.valid ?? false);
formValue = computed(() => this.form()?.value);
```

## 注意点

### パフォーマンス
大量のフィールドを動的生成する場合、仮想スクロールの導入を検討してください。

### フォームのリセット
フォーム再生成時は、既存のフィールドを確実にクリアしてください。

### バリデーションタイミング
動的フィールドのバリデーションは、表示タイミングに注意が必要です。

### アクセシビリティ
動的生成フィールドにも適切なaria属性やラベルを設定してください。

## 関連技術
- **Reactive Forms**: Angular フォーム
- **FormGroup/FormControl**: フォーム管理
- **Validators**: バリデーション
- **Dynamic Components**: コンポーネント動的生成
- **JSON Schema**: フォーム定義標準
