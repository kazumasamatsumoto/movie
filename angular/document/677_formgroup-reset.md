# #677 「FormGroup.reset() - リセット」

## 概要
FormGroup.resetは値と状態を初期化し、引数に初期値オブジェクトを渡すとその値でフォーム全体を再初期化できる。

## 学習目標
- FormGroup.resetの挙動を理解する
- 初期値オブジェクトを渡す方法を学ぶ
- リセット後の状態変化を把握する

## 技術ポイント
- reset()で値と状態を初期化
- reset(initialValue)で指定値に戻せる
- disabled状態は維持されるため必要ならenableする

## 📺 画面表示用コード（動画用）
```typescript
this.profileGroup.reset({
  name: '',
  email: '',
  id: 'readonly-id'
});
```

## 💻 詳細実装例（学習用）
```typescript
protected readonly initialProfile = {
  name: '',
  email: '',
  id: 'readonly-id'
} as const;

protected profileGroup = new FormGroup({
  name: new FormControl(this.initialProfile.name, { nonNullable: true }),
  email: new FormControl(this.initialProfile.email, { nonNullable: true }),
  id: new FormControl(this.initialProfile.id, { nonNullable: true })
});

protected clear(): void {
  this.profileGroup.reset(this.initialProfile);
}
```

## ベストプラクティス
- 初期値オブジェクトを定数化してresetで再利用する
- リセット後のフォーカスやメッセージ表示をUXとして検討する
- 非同期で初期値を取得する場合は値取得後にresetする

## 注意点
- resetでエラー状態も消えるためユーザーへの案内を工夫する
- disabledは維持されるので必要に応じてenable/disableする
- FormArrayを含む場合は要素数も戻ることを想定する

## 関連技術
- reset
- 初期化
- UX配慮
