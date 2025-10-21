# #718 「パラメータ付きバリデーター」

## 概要
パラメータ付きバリデーターは引数を受け取るファクトリ関数でValidatorFnを返し、利用時に柔軟に閾値や条件を設定できる。

## 学習目標
- パラメータ付きバリデーターのパターンを理解する
- ValidationErrorsに引数情報を含める方法を学ぶ
- テスト戦略を把握する

## 技術ポイント
- function factory(param) { return (control) => ValidationErrors | null } の形
- エラー情報にパラメータを含めてUIで利用する
- 複数のパラメータを受け取る場合はオブジェクト引数が便利

## 📺 画面表示用コード（動画用）
```typescript
function minNumber(count: number): ValidatorFn {
  return control => {
    const value = control.value as number | null;
    return value !== null && value >= count ? null : { minNumber: { min: count, actual: value } };
  };
}
```

## 💻 詳細実装例（学習用）
```typescript
protected quantityCtrl = new FormControl(0, [minNumber(5)]);
```

## ベストプラクティス
- 複数パラメータはオブジェクト引数にまとめて見通しを良くする
- バリデーターの説明と使用例をドキュメント化する
- デフォルト値が必要ならfactory内で設定する

## 注意点
- 制御文字や未入力の場合の扱いを明確にする
- パラメータ変更時の影響範囲を把握する
- テストで境界値と異常値を網羅する

## 関連技術
- ValidatorFn
- ValidationErrors
- ファクトリ関数
