# #676 「FormGroup.patchValue() - 部分更新」

## 概要
FormGroup.patchValueは指定したキーだけを更新し、存在しないキーは無視する。部分的なデータ更新やネストした構造の差分適用に使える。

## 学習目標
- patchValueのメリットを理解する
- ネスト構造の部分更新方法を学ぶ
- 通知制御オプションを把握する

## 技術ポイント
- 存在しないキーを渡しても例外にならない
- ネストしたオブジェクトをそのまま渡せる
- emitEvent/onlySelfオプションが利用可能

## 📺 画面表示用コード（動画用）
```typescript
this.profileGroup.patchValue({
  profile: {
    displayName: 'Alice'
  }
});
```

## 💻 詳細実装例（学習用）
```typescript
protected profileGroup = new FormGroup({
  credentials: new FormGroup({
    email: new FormControl(''),
    password: new FormControl('')
  }),
  profile: new FormGroup({
    displayName: new FormControl(''),
    bio: new FormControl('')
  })
});

protected updateDisplayName(name: string): void {
  this.profileGroup.patchValue({
    profile: { displayName: name }
  }, { emitEvent: false });
}
```

## ベストプラクティス
- 部分更新用のメソッドをサービスにまとめる
- ネスト構造の更新はオブジェクトリテラルで表現する
- emitEvent:falseを使うときは手動で必要な処理を呼ぶ

## 注意点
- 存在しないキーは静かに無視されるのでtypoに注意
- 入れ子の配列更新はFormArrayのメソッドを併用する
- 部分更新後にバリデーション状態が変わる可能性を考慮する

## 関連技術
- patchValue
- 差分更新
- ネスト構造
