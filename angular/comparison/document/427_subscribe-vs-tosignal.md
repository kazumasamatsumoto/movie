# #427 「RxJS subscribeでUI同期 vs toSignalブリッジ あなたはどっち派？」

## 概要
subscribe代入は柔軟だがリークリスクがある。toSignalはSignalグラフに統合でき、UI同期が簡潔になる。

## 学習目標
- subscribe派の構成と得意なシナリオを整理する
- toSignal派の採用メリットを理解する
- プロジェクト条件に応じた使い分け基準を決める

## 技術ポイント
- subscribe派を成り立たせる主要API/構成要素
- toSignal派で押さえる設定やコード記述
- 両者を共存・移行させるためのブリッジ手法

## 📺 画面表示用コード（動画用）
**subscribe派：手動で値を保持**
```typescript
private readonly destroyRef = inject(DestroyRef);

ngOnInit(): void {
  this.repo.list()
    .pipe(takeUntilDestroyed(this.destroyRef))
    .subscribe(items => (this.items = items));
}
```

**toSignal派：Signalへ変換**
```typescript
readonly items = toSignal(this.repo.list(), { initialValue: [] });

template: `<li @for (item of items())>{{ item.name }}</li>`
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-hero-feed',
  standalone: true,
  templateUrl: './hero-feed.component.html',
})
export class HeroFeedComponent {
  private readonly repo = inject(HeroRepository);
  readonly heroes = toSignal(this.repo.list(), { initialValue: [] });
}
```

## ベストプラクティス
- subscribe派でも`takeUntilDestroyed`や`AsyncPipe`で購読解除を自動化する
- `toSignal`を使う場合は`initialValue`を必ず渡し、テンプレート側でnullチェックを減らす
- Signalへの変換をサービス層で行い、コンポーネントはSignalのみ受け取る設計にすると移行が楽

## 注意点
- `toSignal`は`cold` Observableでも購読するので副作用の再実行に注意
- subscribeとtoSignalを同じObservableで併用すると重複購読になる
- Signalsへ変換しても重い処理は`computed`でキャッシュし直す必要がある

## 関連技術
- toSignal/toObservable
- AsyncPipe
- takeUntilDestroyed
