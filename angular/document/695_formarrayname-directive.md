# #695 「formArrayName ディレクティブ」

## 概要
formArrayNameはテンプレートでFormArrayを扱うためのディレクティブで、*ngForと組み合わせて動的に要素をレンダリングする。

## 学習目標
- formArrayNameの使い方を理解する
- *ngForとの連携方法を学ぶ
- 要素追加・削除のテンプレート設計を把握する

## 技術ポイント
- formArrayNameディレクティブで子要素のコンテキストを切り替える
- *ngForでcontrolsをループしてformControlNameにindexを渡す
- 要素操作はボタンと配列メソッドを組み合わせる

## 📺 画面表示用コード（動画用）
```html
<div formArrayName="phones">
  <div *ngFor="let ctrl of phonesCtrl.controls; let i = index">
    <input [formControlName]="i" />
    <button type="button" (click)="removePhone(i)">削除</button>
  </div>
  <button type="button" (click)="addPhone()">追加</button>
</div>
```

## 💻 詳細実装例（学習用）
```typescript
protected profileForm = new FormGroup({
  phones: new FormArray<FormControl<string>>([
    new FormControl('')
  ])
});

protected get phonesCtrl() {
  return this.profileForm.get('phones') as FormArray<FormControl<string>>;
}

protected addPhone(): void {
  this.phonesCtrl.push(new FormControl(''));
}

protected removePhone(index: number): void {
  this.phonesCtrl.removeAt(index);
}
```

## ベストプラクティス
- テンプレート内でtrackByを指定して再描画コストを抑える
- 配列要素のフォームロジックはコンポーネントメソッドにまとめる
- 削除ボタンには確認ダイアログやundoを検討する

## 注意点
- インデックスを直接参照するため配列操作で順序が変わる点に注意
- FormArrayが空の場合の表示を考慮する
- フォームが大きい場合は子コンポーネント化してChangeDetectionを最適化する

## 関連技術
- formArrayName
- FormArray
- ngFor
