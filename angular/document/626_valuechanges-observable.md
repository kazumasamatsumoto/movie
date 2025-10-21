# #626 「valueChanges Observable」

## 概要
valueChanges Observableはフォームやコントロールの値変化を通知し、リアルタイム検証や補助機能のトリガーとして活用できる。

## 学習目標
- valueChangesが通知するタイミングを理解する
- RxJSオペレーターとの組み合わせ方を学ぶ
- 購読解除パターンを把握する

## 技術ポイント
- valueChangesはFormGroup/FormControl双方で利用可能
- debounceTimeやdistinctUntilChangedでノイズを低減
- フォーム初期化時にも初期値が通知される

## 📺 画面表示用コード（動画用）
```typescript
this.form.get('keyword')?.valueChanges
  .pipe(debounceTime(300))
  .subscribe(term => this.search(term));
```

## 💻 詳細実装例（学習用）
```typescript
protected ngOnInit(): void {
  this.form.valueChanges
    .pipe(takeUntil(this.destroy$))
    .subscribe(value => this.logger.debug('form changed', value));
}

protected setupKeywordWatcher(): void {
  this.form.get('keyword')?.valueChanges
    .pipe(debounceTime(300), distinctUntilChanged(), takeUntil(this.destroy$))
    .subscribe(term => this.suggest(term));
}
```

## ベストプラクティス
- RxJSオペレーターでイベント回数を調整する
- ログ出力やサジェストなど副作用をサービスに委譲する
- 購読解除を徹底してメモリリークを防ぐ

## 注意点
- valueChangesは初期値でも発火するので初回イベントを意識
- 重い処理を直接書かずswitchMapなどで非同期化する
- ネストしたFormGroupではvalue構造を把握する

## 関連技術
- statusChanges
- RxJS operators
- オートコンプリート
