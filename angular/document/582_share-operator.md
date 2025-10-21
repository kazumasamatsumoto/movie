# #582 「share() オペレーターの併用」

## 概要
同じObservableを複数AsyncPipeで利用する場合、RxJSの`share()`や`shareReplay()`を使って購読を共有すれば、余分な購読が作成されず効率的に値を配信できる。

## 学習目標
- share/shareReplayで購読を共有する方法を理解する
- AsyncPipeとObservableの最適化を連携させる
- キャッシュや再利用の戦略を学ぶ

## 技術ポイント
- `source$.pipe(share())`でマルチキャスト
- `shareReplay(1)`で最新値をキャッシュ
- AsyncPipe側は従来通り`| async`を使用

## 📺 画面表示用コード（動画用）
```typescript
protected readonly stats$ = this.statsService.load().pipe(shareReplay(1));
```

```html
<p>{{ stats$ | async | json }}</p>
<p>{{ stats$ | async | titlecase }}</p>
```

## ベストプラクティス
- 複数AsyncPipeが必要な場合はObservable側で`shareReplay`して購読共有
- `shareReplay({ bufferSize: 1, refCount: true })`で必要な時のみ購読
- データが重い場合はキャッシュを適切に失効させる

## 注意点
- `shareReplay`はメモリを保持するため無制限に使用しない
- `share`のみでは購読解除後に再購読が遅れることがある
- エラーが発生した場合の再送ルールを設計

## 関連技術
- RxJS share/shareReplay
- AsyncPipe
- Hot/Cold Observable
