# #603 「Reactive Forms - リアクティブフォーム」

## 概要
リアクティブフォームはFormGroupやFormControlをTypeScriptで構築し、テンプレートと同期させることで強力な状態管理とテスト性を提供する。

## 学習目標
- FormGroupとFormControlの役割を理解する
- リアクティブフォームのテンプレート記法を学ぶ
- サービスと連携したフォームロジックの構成を想像する

## 技術ポイント
- ReactiveFormsModuleをインポートしてディレクティブを有効化
- FormBuilderで宣言的にコントロールを作成可能
- valueChangesやstatusChangesで状態監視ができる

## 📺 画面表示用コード（動画用）
```html
<form [formGroup]="userForm" (ngSubmit)="save()">
  <input formControlName="email" />
  <button type="submit">保存</button>
</form>
```

## 💻 詳細実装例（学習用）
```typescript
protected userForm = new FormGroup({
  email: new FormControl('', { nonNullable: true, validators: [Validators.email] })
});

protected save(): void {
  if (this.userForm.valid) {
    console.log('save', this.userForm.value);
  }
}
```

## ベストプラクティス
- FormBuilderを活用してネスト構造を見通し良く書く
- バリデーションや変換ロジックはサービスに切り出す
- ユニットテストでフォームの状態遷移を確認する

## 注意点
- テンプレートにformControlNameを設定し忘れると同期しない
- 同期処理で副作用を起こす場合はdebounceなどを併用
- 巨大なFormGroupは機能別に分割して保守性を保つ

## 関連技術
- ReactiveFormsModule
- FormGroup
- FormBuilder
