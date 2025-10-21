# #602 「Template-driven Forms - テンプレート駆動」

## 概要
テンプレート駆動フォームはテンプレート側のディレクティブ記述でフォーム定義を行い、Angularが内部でFormControlを生成して扱いやすくする。

## 学習目標
- ngModelによる双方向バインディングを理解する
- テンプレートでのバリデーション宣言方法を学ぶ
- テンプレート駆動が向くユースケースを把握する

## 技術ポイント
- FormsModuleをインポートするとngModelやngFormが使える
- #loginForm="ngForm"でTemplateReferenceを取得
- requiredなどのHTML属性とバリデーションを連携できる

## 📺 画面表示用コード（動画用）
```html
<form #loginForm="ngForm" (ngSubmit)="onSubmit(loginForm.value)">
  <input name="email" ngModel required />
  <button type="submit">送信</button>
</form>
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-template-login',
  templateUrl: './template-login.component.html',
  standalone: true,
  imports: [FormsModule]
})
export class TemplateLoginComponent {
  protected onSubmit(value: Record<string, unknown>): void {
    console.log('login', value);
  }
}
```

## ベストプラクティス
- 入力項目が少ない画面に適用しテンプレートの見通しを保つ
- テンプレート参照変数でフォーム状態をUIに反映する
- 共通バリデーションはディレクティブ化して再利用する

## 注意点
- テンプレートコードが肥大化すると読みにくくなる
- 型安全性が低いのでTypeScriptでの補完が弱い
- 大規模フォームでは検証ロジックの分離が難しい

## 関連技術
- FormsModule
- ngModel
- Template Reference Variables
