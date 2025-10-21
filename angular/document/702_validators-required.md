# #702 「Validators.required - 必須」

## 概要
Validators.requiredは必須入力を強制し、値がnull・undefined・空文字などの場合にrequiredエラーを返す。

## 学習目標
- requiredバリデーションの動作を理解する
- エラー表示の条件を把握する
- UIと組み合わせた必須表示を学ぶ

## 技術ポイント
- 空文字・null・undefinedはエラー
- 空白のみでもエラー扱い
- errors.requiredを使ってメッセージ表示

## 📺 画面表示用コード（動画用）
```html
<input [formControl]="nameCtrl" />
<span *ngIf="nameCtrl.errors?.required">必須です</span>
```

## 💻 詳細実装例（学習用）
```typescript
protected nameCtrl = new FormControl('', Validators.required);
```

## ベストプラクティス
- 必須項目には視覚的なマークと説明を付ける
- Submit時にmarkAllAsTouchedでエラー表示を確実に出す
- トリム処理が必要な場合はvalueChangesで整形する

## 注意点
- ユーザーが空白だけ入力した場合もエラーになることを明示する
- FormArrayの要素が空でもエラーにするならカスタム対応が必要
- 必須判定は国際化でテキスト入力の扱いが変わる可能性がある

## 関連技術
- Validators.required
- エラー表示
- フォームUX
