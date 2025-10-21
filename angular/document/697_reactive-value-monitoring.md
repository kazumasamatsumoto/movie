# #697 「値の変更監視」

## 概要
valueChangesを監視することでリアルタイムバリデーション、サジェスト、状態制御などを実装でき、RxJSオペレーターで制御すると使いやすくなる。

## 学習目標
- valueChangesの監視方法を理解する
- RxJSオペレーターとの組み合わせを学ぶ
- FormGroup/FormArrayでも使えることを把握する

## 技術ポイント
- 全てのフォーム要素でvalueChangesが利用可能
- debounceTime, distinctUntilChangedでノイズ抑制
- takeUntilDestroyedやAsyncPipeで購読解除する

## 📺 画面表示用コード（動画用）
```typescript
this.profileForm.valueChanges
  .pipe(debounceTime(300))
  .subscribe(value => this.preview = value);
```

## 💻 詳細実装例（学習用）
```typescript
protected profileForm = new FormGroup({
  name: new FormControl(''),
  bio: new FormControl('')
});

protected constructor() {
  this.profileForm.valueChanges
    .pipe(debounceTime(400), takeUntilDestroyed())
    .subscribe(value => this.autoSave(value));
}

private autoSave(value: unknown): void {
  console.log('autosave', value);
}
```

## ベストプラクティス
- 購読解除を組み込んでメモリリークを防ぐ
- 重い処理はdebounceTimeやswitchMapで制御する
- valueChanges内ではUI更新ロジックに徹する

## 注意点
- フォーム初期化時にも発火することを想定する
- switchMapを忘れると古いリクエストが残る
- setValueを呼ぶとループする可能性がある

## 関連技術
- valueChanges
- RxJSオペレーター
- 購読解除
