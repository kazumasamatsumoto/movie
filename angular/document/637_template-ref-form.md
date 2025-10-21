# #637 「テンプレート参照変数 #form」

## 概要
テンプレート参照変数を用いてNgFormを取得するとテンプレート上でフォーム状態や値にアクセスでき、送信処理や状態表示に活用できる。

## 学習目標
- #form="ngForm"の設定方法を理解する
- テンプレート内でNgFormプロパティを扱う
- イベント引数として活用する手順を学ぶ

## 技術ポイント
- <form #form="ngForm">でNgFormを参照
- #form.validや#form.submittedをテンプレートで利用
- (ngSubmit)="onSubmit(form)"でコンポーネントに渡す

## 📺 画面表示用コード（動画用）
```html
<form #form="ngForm" (ngSubmit)="onSubmit(form)">
  <input name="name" ngModel />
</form>
```

## 💻 詳細実装例（学習用）
```typescript
protected onSubmit(form: NgForm): void {
    console.log('valid:', form.valid, 'value:', form.value);
}
```

## ベストプラクティス
- テンプレート参照で未操作時の状態を表示する
- フォーム参照をイベントで渡してロジックを簡潔化する
- 複数フォームがある場合は意味のある変数名を付ける

## 注意点
- テンプレート参照変数を重複させない
- テンプレート内で複雑なロジックを書きすぎない
- フォーム参照を子コンポーネントへ直接渡すと密結合になりやすい

## 関連技術
- NgForm
- テンプレート参照変数
- ngSubmit
