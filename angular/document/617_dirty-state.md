# #617 「dirty - 変更済み状態」

## 概要
dirtyフラグはユーザーが値を変更したことを示し、保存ロジックやナビゲーションガードで変更検知に利用される。

## 学習目標
- dirtyフラグが変化するタイミングを理解する
- 保存処理の最適化に活かす方法を学ぶ
- 離脱警告などUX改善に活用する

## 技術ポイント
- ユーザー変更またはプログラムによるsetValueでdirty=true
- FormGroup全体のdirtyでフォーム単位の変更を把握
- dirtyとpristineは互いに反転する関係

## 📺 画面表示用コード（動画用）
```typescript
if (this.form.dirty) {
  this.promptUnsavedChanges();
}
```

## 💻 詳細実装例（学習用）
```typescript
protected canDeactivate(): boolean {
  return !this.form.dirty || confirm('変更を破棄しますか？');
}

protected save(): void {
  if (!this.form.dirty) {
    return;
  }
  // 保存処理
  this.form.markAsPristine();
}
```

## ベストプラクティス
- dirtyを利用して無駄なAPIコールを避ける
- 保存後はmarkAsPristineで状態をリセットする
- 離脱ガードでdirty状態をチェックする

## 注意点
- プログラムで値を更新するとdirtyが意図せずtrueになる
- 配列コントロールでは個別のdirtyも確認する
- markAsPristineを忘れると再保存の判定がズレる

## 関連技術
- pristine
- CanDeactivateガード
- FormArray
