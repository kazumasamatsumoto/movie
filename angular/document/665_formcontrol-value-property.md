# #665 「FormControl.value プロパティ」

## 概要
FormControl.valueは現在値を返す読み取り専用プロパティで、nonNullable設定でnull禁止にできる。値の更新はsetValue系メソッドを使う。

## 学習目標
- valueプロパティの型決定ロジックを理解する
- nonNullable設定の利点を把握する
- 値更新はメソッド経由で行う意識を持つ

## 技術ポイント
- FormControl.nonNullableでnull非許容インスタンスを生成
- valueはgetterであり直接代入できない
- strictTemplates下で型エラーを防げる

## 📺 画面表示用コード（動画用）
```html
<span>現在地: {{ cityCtrl.value }}</span>
```

## 💻 詳細実装例（学習用）
```typescript
protected cityCtrl = new FormControl('Tokyo', { nonNullable: true });

protected updateCity(city: string): void {
  this.cityCtrl.setValue(city);
}
```

## ベストプラクティス
- nonNullableオプションでnullチェックを減らす
- getter経由で値を参照しテンプレートに渡す
- 値変更はsetValue/patchValueを通す

## 注意点
- nonNullable設定でも空文字は許容される点に注意
- valueを直接代入してもビューは更新されない
- null許容が必要な場合は型にnullを含める

## 関連技術
- nonNullable
- 型安全性
- FormControl
