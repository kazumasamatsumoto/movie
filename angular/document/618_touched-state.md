# #618 「touched - タッチ済み状態」

## 概要
touchedフラグはユーザーがコントロールにフォーカスし離れたかどうかを示し、エラー表示のタイミング制御に利用される。

## 学習目標
- touchedフラグの変化条件を理解する
- エラーメッセージ表示のタイミングを調整する
- markAllAsTouchedの使いどころを学ぶ

## 技術ポイント
- フォーカス離脱でtouched=true、未フォーカスはuntouched
- FormGroup.markAllAsTouched()で一括変更
- テンプレート駆動でもngModel.touchedが取得可能

## 📺 画面表示用コード（動画用）
```html
<span *ngIf="control.invalid && control.touched">形式が不正です</span>
```

## 💻 詳細実装例（学習用）
```typescript
protected submit(): void {
  if (this.form.invalid) {
    this.form.markAllAsTouched();
    return;
  }
  // 送信処理
}

protected isTouched(controlName: string): boolean {
  return !!this.form.get(controlName)?.touched;
}
```

## ベストプラクティス
- touchedを使ってユーザー操作後にのみエラーを表示する
- markAllAsTouchedで送信前に一括チェック
- テンプレート駆動ではngModel.touchedを活用する

## 注意点
- プログラムでfocus()/blur()すると状態が変わることに注意
- モバイル端末ではタッチイベントとの挙動を確認する
- markAllAsTouchedの呼びすぎでパフォーマンス低下しないよう留意

## 関連技術
- untouched
- markAllAsTouched
- バリデーションUI
