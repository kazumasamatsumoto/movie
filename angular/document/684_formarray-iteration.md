# #684 「FormArray の反復処理」

## 概要
FormArrayの反復処理はテンプレートで*ngForを使い、コードではcontrolsやvalueをmap/forEachする。ジェネリクス指定で型安全に扱える。

## 学習目標
- テンプレートでの反復方法を理解する
- コード側での配列操作を学ぶ
- 型安全な反復処理のポイントを把握する

## 技術ポイント
- controls配列を*ngForで描画
- value.mapでDTOを作成できます
- FormArray.controlsはAbstractControl[]なので型注釈が重要

## 📺 画面表示用コード（動画用）
```html
<div formArrayName="tags">
  <label *ngFor="let ctrl of tagsCtrl.controls; index as i">
    <input [formControlName]="i" />
  </label>
</div>
```

## 💻 詳細実装例（学習用）
```typescript
protected get tagValues(): string[] {
  return this.tagsCtrl.controls.map(control => control.value ?? '');
}

protected removeEmptyTags(): void {
  for (let i = this.tagsCtrl.length - 1; i >= 0; i--) {
    if (!this.tagsCtrl.at(i)?.value) {
      this.tagsCtrl.removeAt(i);
    }
  }
}
```

## ベストプラクティス
- テンプレートではtrackByでパフォーマンスを改善する
- DTO生成はmapなどの配列関数で実装する
- 削除処理は逆順ループでインデックスずれを防ぐ

## 注意点
- controls配列を直接変更するとAngularの検知と合わなくなる
- valueがnull許容の場合は変換時にフォールバックを用意する
- 大量要素は仮想スクロールなどの検討が必要

## 関連技術
- FormArray
- ngFor
- 型安全な反復
