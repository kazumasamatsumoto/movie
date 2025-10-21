# #669 「FormGroup - コントロールのグループ」

## 概要
FormGroupは複数のFormControlや他のFormGroup/FormArrayをまとめて管理し、値をオブジェクトとして扱えるコンテナーで複合バリデーションにも対応する。

## 学習目標
- FormGroupの役割と構造を理解する
- 値がオブジェクトになる仕組みを把握する
- グループ単位のバリデーションを意識する

## 技術ポイント
- FormGroupはコントロール辞書を受け取る
- valueは同じ形のオブジェクトを返す
- setErrorsでグループ全体のエラーを表現できる

## 📺 画面表示用コード（動画用）
```html
<form [formGroup]="profileGroup">
  <input formControlName="name" />
  <input formControlName="email" type="email" />
</form>
```

## 💻 詳細実装例（学習用）
```typescript
protected profileGroup = new FormGroup({
  name: new FormControl('', { nonNullable: true }),
  email: new FormControl('', { validators: [Validators.email] })
});

protected submit(): void {
  console.log(this.profileGroup.value);
}
```

## ベストプラクティス
- コントロール構造はインターフェースで型定義する
- 再利用可能なグループは専用ファクトリ関数を用意する
- グループレベルのバリデーションを見越して設計する

## 注意点
- FormGroup内のキー名とテンプレートのformControlNameは一致させる
- valueは部分的にnullが含まれる可能性がある
- ネストが深いと可読性が下がるため構造を整理する

## 関連技術
- FormGroup
- 複合バリデーション
- Reactive Forms
