# #287 「Toggle Component - トグルスイッチ」

## 概要
Toggle Componentはオン/オフの状態を視覚的に切り替えるインタラクションを提供し、アクセシビリティ対応とアニメーションを統一したコンポーネントである。

## 学習目標
- トグルの状態管理と通知を実装する
- role="switch"とaria属性でアクセシビリティを確保する
- CSS変数でテーマに沿ったアニメーションを制御する

## 技術ポイント
- ControlValueAccessor
- CSS custom properties
- Keyboard accessibility

## 📺 画面表示用コード（動画用）
```typescript
@Component({ selector: 'app-toggle', standalone: true, template: `<button type="button" class="toggle" [class.on]="checked" [disabled]="disabled" role="switch" [attr.aria-checked]="checked" (click)="toggle()" (keyup.space)="toggle()" (keyup.enter)="toggle()"></button>`, providers: [{ provide: NG_VALUE_ACCESSOR, useExisting: forwardRef(() => ToggleComponent), multi: true }], changeDetection: ChangeDetectionStrategy.OnPush })
export class ToggleComponent implements ControlValueAccessor {
  @Input() disabled = false;
  checked = false;
  private onChange = (v: boolean) => {}; private onTouched = () => {};
  toggle(): void { if (this.disabled) return; this.checked = !this.checked; this.onChange(this.checked); this.onTouched(); }
  writeValue(value: boolean | null): void { this.checked = !!value; }
  registerOnChange(fn: (v: boolean) => void): void { this.onChange = fn; }
  registerOnTouched(fn: () => void): void { this.onTouched = fn; }
}
```

```css
.toggle { --track-color: #ccc; width: 48px; height: 24px; border-radius: 12px; background: var(--track-color); position: relative; transition: background .2s; }
.toggle::after { content: ''; position: absolute; width: 20px; height: 20px; border-radius: 50%; background: white; left: 2px; top: 2px; transition: transform .2s; }
.toggle.on { --track-color: #1877f2; }
.toggle.on::after { transform: translateX(24px); }
```

```html
<app-toggle formControlName="notifications"></app-toggle>
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-toggle-demo',
  standalone: true,
  imports: [ReactiveFormsModule, ToggleComponent],
  template: `
    <form [formGroup]="form">
      <label class="row">通知 <app-toggle formControlName="notifications"></app-toggle></label>
    </form>
    <p>現在: {{ form.value.notifications ? 'ON' : 'OFF' }}</p>
  `,
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class ToggleDemoComponent {
  readonly form = inject(NonNullableFormBuilder).group({ notifications: [true] });
}
```

## ベストプラクティス
- toggleはbutton要素で実装し、role="switch"とaria-checkedを同期させる
- キーボード操作はSpace/Enterで切り替えできるようにする
- CSS変数でテーマカラーを外部から変更可能にする

## 注意点
- disabled時はtoggle関数で状態更新を抑制する
- フォーカスリングを消さず、見た目に合わせカスタマイズする
- モバイルでのドラッグ操作は追加ジェスチャーを検討する

## 関連技術
- ControlValueAccessor
- Accessibility
- CSSアニメーション
