# #379 「条件付きクラス適用」

## 概要
条件付きクラスは`ngClass`を用いて状態に応じたクラスを付与し、視覚的フィードバックやアクセシビリティ向上を実現する。

## 学習目標
- 条件付きクラスを設計する際の考慮事項を理解する
- コンポーネント側で状態管理しテンプレートを簡潔にする方法を学ぶ
- フォームやリストなど多様なシナリオで応用できるようになる

## 技術ポイント
- 状態とクラスをマッピングするテーブルを用意
- computedやgetterでクラス集合を返すとテストしやすい
- アクセシビリティ属性（`aria-*`）と併せて使う

## 📺 画面表示用コード（動画用）
```html
<input [ngClass]="{ 'is-invalid': control.invalid && control.touched }" />
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-conditional-class-demo',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule],
  template: `
    <form [formGroup]="form">
      <label>
        メール
        <input formControlName="email" [ngClass]="classMap('email')" />
      </label>
      <p *ngIf="form.controls.email.invalid && form.controls.email.touched" class="error">
        正しいメールアドレスを入力してください
      </p>
    </form>
  `,
  styles: [`
    input { border: 1px solid #94a3b8; border-radius: 0.5rem; padding: 0.5rem; width: 100%; }
    .is-invalid { border-color: #f97316; background: #fff7ed; }
    .error { color: #f97316; font-size: 0.875rem; }
  `]
})
export class ConditionalClassDemoComponent {
  protected form = new FormGroup({
    email: new FormControl('', { nonNullable: true, validators: [Validators.email, Validators.required] })
  });

  protected classMap(controlName: string): Record<string, boolean> {
    const control = this.form.controls[controlName];
    return { 'is-invalid': control.invalid && control.touched };
  }
}
```

## ベストプラクティス
- フォームの状態やAPIレスポンスに応じてクラスを切り替え、ユーザーへ明確なフィードバックを与える
- クラス付与と同時に`aria-invalid`などアクセシビリティ属性も設定する
- 複数条件が衝突しないよう優先順位を整理し、ドキュメント化する

## 注意点
- コントロールが存在しない状態でクラスを参照するとエラーになるのでnullガードを入れる
- クラスで表示切り替えする場合も、必要なら`role`や`aria-live`を設定
- 条件が複雑化したらコンポーネントメソッドやサービスにロジックを移す

## 関連技術
- Reactive Forms
- Accessibility属性
- Angular Signals
