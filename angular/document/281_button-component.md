# #281 「Button Component - ボタンの実装」

## 概要
Button Componentはアプリ全体で一貫したスタイルと振る舞いを提供し、variantやサイズを切り替えて多用途に活用できる基本UIパーツである。

## 学習目標
- 再利用可能なボタンのInput/Outputを設計する
- アクセシビリティを考慮した属性設定を行う
- Signalで状態を管理し動的な振る舞いを実装する

## 技術ポイント
- ChangeDetectionStrategy.OnPush
- variant/sizeによるスタイル切り替え
- disabled・loading制御

## 📺 画面表示用コード（動画用）
```typescript
@Component({ selector: 'app-button', standalone: true, template: `<button [ngClass]="['btn', variant, size]" [disabled]="disabled || loading" type="button" (click)="pressed.emit()">{{ label }}</button>`, changeDetection: ChangeDetectionStrategy.OnPush })
export class ButtonComponent {
  @Input({ required: true }) label = '';
  @Input() variant: 'primary' | 'secondary' = 'primary';
  @Input() size: 'sm' | 'md' | 'lg' = 'md';
  @Input() disabled = false;
  @Input() loading = false;
  @Output() pressed = new EventEmitter<void>();
}
```

```typescript
export type ButtonConfig = {
  readonly label: string;
  readonly variant?: 'primary' | 'secondary';
  readonly size?: 'sm' | 'md' | 'lg';
};
```

```html
<app-button [label]="'送信'" [variant]="'primary'" (pressed)="onSubmit()"></app-button>
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-button-container',
  standalone: true,
  imports: [ButtonComponent],
  template: `<app-button [label]="label" [variant]="variant" [loading]="isLoading()" (pressed)="handle()"></app-button>`
})
export class ButtonContainerComponent {
  readonly label = '保存';
  readonly variant: ButtonComponent['variant'] = 'primary';
  protected readonly isLoading = signal(false);

  handle(): void {
    this.isLoading.set(true);
    fakeSave().finally(() => this.isLoading.set(false));
  }
}
```

## ベストプラクティス
- type属性を指定しフォーム内での誤作動を防ぐ
- variantは限定的なUnion型で定義しデザインシステムと同期する
- disabled制御とローディング表示を組み合わせて二度押しを防止する

## 注意点
- Outputイベント名を動詞で揃え、クリック以外の意図を明確化する
- スタイル定義はShadow DOMではなくグローバル変数と連携させる
- スロットが必要になったらng-contentで拡張する

## 関連技術
- Standalone Component
- Angular Signals
- Design Token
