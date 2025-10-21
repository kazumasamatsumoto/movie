# #633 「name 属性の必須性」

## 概要
テンプレート駆動フォームではngModelをフォームに登録する際にname属性が必須となり、nameが無ければNgFormがコントロールを管理できない。

## 学習目標
- ngModelとname属性の関係を理解する
- name不足による不具合を把握する
- 命名ルールの重要性を認識する

## 技術ポイント
- name属性はフォーム内で一意にする
- nameが無いとform.valueに含まれない
- テンプレート参照変数やaria属性と合わせて管理

## 📺 画面表示用コード（動画用）
```html
<input name="email" [(ngModel)]="form.email" required />
```

## 💻 詳細実装例（学習用）
```typescript
protected form = { email: '' };

protected onSubmit(form: NgForm): void {
    console.log(form.value);
}
```

## ベストプラクティス
- name値は意味が分かるように命名する
- 共有コンポーネントではnameを入力として受け取る
- テストでnameが設定されているか確認する

## 注意点
- name重複でフォーム値が上書きされる
- nameの付け忘れでバリデーションが効かない
- i18n対応時のname変更を慎重に行う

## 関連技術
- NgForm
- テンプレート駆動フォーム
- フォーム設計
