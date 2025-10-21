# #601 「Angular Forms とは？2つのアプローチ」

## 概要
Angularのフォーム機能はテンプレート駆動フォームとリアクティブフォームの2系統を提供し、入力とバリデーションを柔軟に実装できる。

## 学習目標
- フォームAPIが提供する2つのアプローチを把握する
- それぞれの特徴と得意領域を理解する
- プロジェクトに合わせて選択する視点を身につける

## 技術ポイント
- テンプレート駆動はテンプレート中心、リアクティブはTypeScript中心
- どちらもフォーム状態やバリデーションの追跡が可能
- 対応モジュールのインポートが必須（FormsModule / ReactiveFormsModule）

## 📺 画面表示用コード（動画用）
```html
<form #profileForm="ngForm">
  <input name="name" ngModel required />
</form>
```

```html
<form [formGroup]="profileForm">
  <input formControlName="name" required />
</form>
```

## 💻 詳細実装例（学習用）
```typescript
protected profileForm = new FormGroup({
  name: new FormControl('', { nonNullable: true })
});

protected onSubmit(): void {
  console.log(this.profileForm.value);
}
```

## ベストプラクティス
- 要件と規模に応じてテンプレート駆動とリアクティブを選択する
- フォーム状態を可視化して検証エラーを早期に検出する
- テスト戦略を事前に決めてフォームロジックを検証する

## 注意点
- モジュールをインポートし忘れるとディレクティブが機能しない
- 混在させると保守が難しくなるためアプローチを明確にする
- 初期値や型定義を曖昧にするとバグにつながる

## 関連技術
- FormsModule
- ReactiveFormsModule
- FormControl / FormGroup
