# #678 「FormArray - 動的配列」

## 概要
FormArrayはFormControlやFormGroupを配列として保持し、動的な要素追加・削除が必要なフォームに対応できる。

## 学習目標
- FormArrayの役割を理解する
- 動的フォームの管理ポイントを学ぶ
- 要素としてFormGroupを使うパターンを把握する

## 技術ポイント
- FormArrayはAbstractControlの配列
- lengthプロパティで要素数を確認
- valueは配列として取得できる

## 📺 画面表示用コード（動画用）
```html
<div formArrayName="tags">
  <input *ngFor="let ctrl of tagsCtrl.controls; let i = index"
         [formControlName]="i" />
</div>
```

## 💻 詳細実装例（学習用）
```typescript
protected tagsCtrl = new FormArray<FormControl<string>>([
  new FormControl('Angular'),
  new FormControl('RxJS')
]);

protected get tags(): string[] {
  return this.tagsCtrl.value as string[];
}
```

## ベストプラクティス
- 要素の型を明示して補完を効かせる
- 要素生成は専用ファクトリ関数に切り出す
- 配列の最大数や重複チェックなどUXを設計する

## 注意点
- controlsプロパティはMutableなので直接書き換えない
- valueはnullを含む可能性がある
- 大規模な配列はパフォーマンスに注意する

## 関連技術
- FormArray
- 動的フォーム
- 抽象コントロール
