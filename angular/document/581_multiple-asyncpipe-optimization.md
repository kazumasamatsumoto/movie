# #581 「複数 AsyncPipe の最適化」

## 概要
同じObservableをテンプレート内で複数回`| async`するとその回数だけ購読が作成されるため、`as`構文で一度だけ購読し値を再利用することでパフォーマンスを最適化できる。

## 学習目標
- 複数AsyncPipeによる重複購読の問題点を理解する
- `*ngIf ... as`構文で値を使い回す方法を学ぶ
- Observable側で`share`/`shareReplay`を使う最適化手段を把握する

## 技術ポイント
- `*ngIf="obs$ | async as value"`で一度だけ購読
- `share()`でObservableをマルチキャスト化
- AsyncPipeを複数箇所に書くのは避ける

## 📺 画面表示用コード（動画用）
```html
<ng-container *ngIf="user$ | async as user">
  <h2>{{ user.name }}</h2>
  <p>{{ user.email }}</p>
</ng-container>
```

## 💻 詳細実装例（学習用）
```typescript
protected readonly user$ = this.userService.user$.pipe(shareReplay(1));
```

## ベストプラクティス
- `as`構文で値を再利用し、AsyncPipeの重複使用を避ける
- Observableを`shareReplay`でキャッシュし複数購読を防ぐ
- TemplateRefでWrappedコンポーネントがある場合でも同様に最適化

## 注意点
- shareReplayでキャッシュする場合はcompleteしないストリームのメモリ使用に注意
- `async as`の書き忘れで重複購読が再発することがある
- Observableを`share`しても初回購読は1つ目のAsyncPipe、追加のPipeが遅れる場合がある

## 関連技術
- share/shareReplay
- AsyncPipe
- Template変数
