# #722 「日付範囲検証」

## 概要
日付範囲検証はFormGroupバリデーターでstartとendを比較し、終了日が開始日より前の場合にrangeエラーを返す。

## 学習目標
- 日付範囲バリデーションの実装手順を理解する
- 日付比較時の正規化方法を学ぶ
- エラー表示の設計を把握する

## 技術ポイント
- ISO文字列をDateに変換して比較
- エラーはrangeなどのキーで返す
- テンプレートでエラーをまとめて表示

## 📺 画面表示用コード（動画用）
```html
<div [formGroup]="dateRange">
  <input formControlName="start" type="date" />
  <input formControlName="end" type="date" />
  <span *ngIf="dateRange.errors?.range">終了日は開始日以降にしてください</span>
</div>
```

## 💻 詳細実装例（学習用）
```typescript
function dateRangeValidator(group: AbstractControl): ValidationErrors | null {
  const start = group.get('start')?.value as string | null;
  const end = group.get('end')?.value as string | null;
  if (!start || !end) {
    return null;
  }
  const startDate = new Date(start);
  const endDate = new Date(end);
  return startDate <= endDate ? null : { range: true };
}

protected dateRange = new FormGroup({
  start: new FormControl('', Validators.required),
  end: new FormControl('', Validators.required)
}, { validators: [dateRangeValidator] });
```

## ベストプラクティス
- 日付はUTCに正規化して比較する
- フォーム送信時に不正なフォーマットを再チェックする
- エラー詳細をUIで説明しユーザーの修正を助ける

## 注意点
- タイムゾーンの違いで計算結果が変わらないようにする
- 無効なDateオブジェクトを比較しない
- 開始・終了が同日許容かどうか要件で決める

## 関連技術
- FormGroup
- 日付比較
- Rangeバリデーション
