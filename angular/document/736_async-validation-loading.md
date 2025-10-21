# #736 「非同期検証のローディング表示」

## 概要
非同期バリデーション中はPENDING状態を利用してローディング表示を出し、ユーザーに待機を伝える。

## 学習目標
- フォームコントロールのPENDING状態を検知する方法を理解する
- statusChangesからローディング表示を制御する
- 非同期検証のUXを改善するUIパターンを学ぶ

## 技術ポイント
- FormControl.pendingまたはstatusChangesで状態を監視する
- AsyncPipeと@ifでローディング表示を簡潔に配置する
- バリデーション結果とローディング表示を統一したViewModelにまとめる

## 📺 画面表示用コード（動画用）
```html
@if (usernameCtrl.pending) {
  <span class="hint">確認中です...</span>
} @else if (usernameCtrl.hasError('usernameTaken')) {
  <span class="error">このユーザー名は使用されています</span>
}
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-username-field',
  template: `
    <input [formControl]="usernameCtrl" placeholder="ユーザー名" />
    @if (isPending()) {
      <app-inline-spinner />
    } @else if (usernameCtrl.hasError('usernameTaken')) {
      <span class="error">使用済みです</span>
    }
  `,
  standalone: true,
  imports: [ReactiveFormsModule, InlineSpinnerComponent]
})
export class UsernameFieldComponent {
  private readonly validator = inject(UsernameValidatorService);
  protected readonly usernameCtrl = new FormControl('', {
    validators: [Validators.required],
    asyncValidators: [this.validator.unique()],
    updateOn: 'blur'
  });
  protected readonly isPending = toSignal(
    this.usernameCtrl.statusChanges.pipe(map(status => status === 'PENDING')),
    { initialValue: false }
  );
}
```

## ベストプラクティス
- PENDING状態を信号化して複数のUI要素で共有する
- ローディング表示はインラインで見せて入力エリアの近くに配置する
- リクエスト失敗時はローディング表示を即座に解除しエラーメッセージを出す

## 注意点
- setErrorsを手動で呼び出すとPENDINGが解除されないケースに注意する
- エラーメッセージとローディング表示が重ならないように条件を整理する
- 多数のフィールドを同時に監視する場合はChangeDetection負荷を考慮する

## 関連技術
- FormControl.pending
- statusChanges
- toSignal
