# #283 「Textarea Component - テキストエリア」

## 概要
Textarea Componentは複数行入力を扱い、自動リサイズや文字数カウントなどの振る舞いを統一したフォーム部品として提供する。

## 学習目標
- テキストエリアの高さ自動調整を実装する
- 文字数制限とカウンター表示を実装する
- ControlValueAccessorでフォームAPIと連携する

## 技術ポイント
- CDKTextareaAutosize
- maxlengthとカウンター表示
- ControlValueAccessor

## 📺 画面表示用コード（動画用）
```typescript
@Component({ selector: 'app-textarea', standalone: true, imports: [CdkTextareaAutosize], template: `<label [for]="id">{{ label }}<textarea cdkTextareaAutosize [cdkAutosizeMinRows]="minRows" [cdkAutosizeMaxRows]="maxRows" [id]="id" [value]="value" [attr.maxLength]="maxLength" (input)="onInput($any($event.target).value)"></textarea><small>{{ value.length }}/{{ maxLength }}</small></label>`, providers: [{ provide: NG_VALUE_ACCESSOR, useExisting: forwardRef(() => TextareaComponent), multi: true }], changeDetection: ChangeDetectionStrategy.OnPush })
export class TextareaComponent implements ControlValueAccessor {
  @Input() label = ''; @Input() minRows = 3; @Input() maxRows = 8; @Input() maxLength = 400;
  value = ''; readonly id = crypto.randomUUID();
  private onChange = (v: string) => {}; private onTouched = () => {};
  onInput(next: string): void { this.value = next; this.onChange(next); }
  writeValue(value: string | null): void { this.value = value ?? ''; }
  registerOnChange(fn: (v: string) => void): void { this.onChange = fn; }
  registerOnTouched(fn: () => void): void { this.onTouched = fn; }
}
```

```html
<app-textarea formControlName="bio" label="自己紹介" [maxLength]="200"></app-textarea>
```

```typescript
this.form = this.fb.group({ bio: this.fb.control('', [Validators.required, Validators.maxLength(200)]) });
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-textarea-demo',
  standalone: true,
  imports: [ReactiveFormsModule, TextareaComponent],
  template: `
    <form [formGroup]="form">
      <app-textarea formControlName="comment" label="コメント" [minRows]="2" [maxRows]="6"></app-textarea>
      <p *ngIf="form.controls.comment.invalid && form.controls.comment.touched" class="error">コメントは200文字以内で入力してください</p>
    </form>
  `,
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class TextareaDemoComponent {
  readonly form = inject(NonNullableFormBuilder).group({ comment: ['', [Validators.required, Validators.maxLength(200)]] });
}
```

## ベストプラクティス
- CDKTextareaAutosizeで高さを制御しユーザー体験を向上させる
- 文字数カウンターは最大値と同期させ、超過時は視覚的に警告する
- ControlValueAccessorでフォームライブラリ間の一貫性を確保する

## 注意点
- 自動リサイズはフォント変更時にも更新されるようChangeDetectorRefを使用する
- 大量テキストの場合はdebounceしてバリデーションを最適化する
- SSR環境ではcrypto.randomUUIDの代替を準備する

## 関連技術
- Angular CDK
- Reactive Forms
- ChangeDetectorRef
