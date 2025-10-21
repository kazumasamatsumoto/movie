# #685 「FormBuilder - フォーム構築」

## 概要
FormBuilderはFormControlやFormGroupを簡潔に生成するユーティリティで、配列記法で初期値とバリデーションをまとめられる。

## 学習目標
- FormBuilderの役割と利点を理解する
- 配列記法による省略表現を学ぶ
- 依存注入での取得方法を把握する

## 技術ポイント
- fb.control / fb.group / fb.arrayで生成できる
- 配列記法 [value, validators, asyncValidators] をサポート
- inject(FormBuilder)またはコンストラクタDIで取得

## 📺 画面表示用コード（動画用）
```typescript
protected form = this.fb.group({
  name: ['', Validators.required],
  email: ['', [Validators.email]]
});
```

## 💻 詳細実装例（学習用）
```typescript
protected readonly fb = inject(FormBuilder);

protected form = this.fb.group({
  name: this.fb.control('', { nonNullable: true }),
  email: ['', [Validators.required, Validators.email]]
});
```

## ベストプラクティス
- フォーム生成はFormBuilder専用メソッドに切り出す
- 配列記法とcontrolメソッドを状況に応じて使い分ける
- FormBuilderインスタンスはreadonlyで保持する

## 注意点
- 配列記法は読みづらくなる場合があるためコメントを添える
- 非同期バリデーションを忘れると配列の第三要素が未使用になる
- フォーム構造が大きい場合はFactory関数で分割する

## 関連技術
- FormBuilder
- 依存注入
- 配列記法
