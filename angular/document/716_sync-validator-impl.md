# #716 「同期バリデーター実装」

## 概要
同期バリデーターはValidatorFnを純粋関数として実装し、必要であればファクトリ関数で引数を受け取る形にする。

## 学習目標
- 同期バリデーターの実装パターンを理解する
- 引数付きバリデーターの作り方を学ぶ
- テスト戦略を把握する

## 技術ポイント
- ValidatorFnを返すファクトリで柔軟性を確保
- ValidationErrors | nullの戻り値を守る
- 副作用を避けてテストしやすくする

## 📺 画面表示用コード（動画用）
```typescript
function minWords(count: number): ValidatorFn {
  return control => {
    const value = control.value as string | null;
    const words = value?.trim().split(/\s+/).filter(Boolean) ?? [];
    return words.length >= count ? null : { minWords: { required: count, actual: words.length } };
  };
}
```

## 💻 詳細実装例（学習用）
```typescript
protected descriptionCtrl = new FormControl('', [minWords(3)]);
```

## ベストプラクティス
- バリデーターはユーティリティファイルにまとめる
- 戻り値の型をtype aliasで表現する
- 境界値と異常系をテストする

## 注意点
- 制御文字や多言語入力に注意する
- 長文処理はパフォーマンスに配慮する
- control.parentを参照する場合はnullチェックが必要

## 関連技術
- ValidatorFn
- 同期バリデーション
- テスト
