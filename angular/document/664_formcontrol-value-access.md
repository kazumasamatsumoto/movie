# #664 「FormControl の値取得」

## 概要
FormControlの現在値はvalueプロパティで取得でき、valueChangesを購読するとリアルタイムに変化を追跡できる。購読解除が重要。

## 学習目標
- valueプロパティの使い方を理解する
- valueChangesでの購読手順を学ぶ
- 購読解除のベストプラクティスを押さえる

## 技術ポイント
- valueは最新値を返すgetter
- valueChangesはObservableで変化を通知
- AsyncPipeならテンプレートで購読/解除が自動

## 📺 画面表示用コード（動画用）
```html
<input [formControl]="searchCtrl" placeholder="検索語" />
```

## 💻 詳細実装例（学習用）
```typescript
protected searchCtrl = new FormControl('');

protected constructor() {
  this.searchCtrl.valueChanges
    .pipe(takeUntilDestroyed())
    .subscribe(term => this.fetchSuggestion(term ?? ''));
}

private fetchSuggestion(term: string): void {
  console.log('suggest', term);
}
```

## ベストプラクティス
- valueChangesはtakeUntilDestroyedやAsyncPipeで購読解除する
- nullを許容する場合は空文字へ変換する
- 高頻度のリクエストはdebounceTimeを併用する

## 注意点
- valueChangesは初期値でも発火する点に注意
- subscribe内でsetValueするとループが発生する場合がある
- Observableの購読解除を怠るとメモリリークになる

## 関連技術
- valueChanges
- 購読解除
- RxJS
