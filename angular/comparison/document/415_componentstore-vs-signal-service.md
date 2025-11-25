# #415 「NgRx ComponentStore vs Signalサービス あなたはどっち派？」

## 概要
ComponentStoreはRxJSベースで複雑なEffectに強い。Signalサービスは軽量で読みやすい。Feature規模とメンバーの習熟で選ぶ。

## 学習目標
- ComponentStoreの構成と得意なシナリオを整理する
- Signalサービスの採用メリットを理解する
- プロジェクト条件に応じた使い分け基準を決める

## 技術ポイント
- ComponentStoreを成り立たせる主要API/構成要素
- Signalサービスで押さえる設定やコード記述
- 両者を共存・移行させるためのブリッジ手法

## 📺 画面表示用コード（動画用）
**ComponentStore派：updater/effectで制御**
```typescript
export class FiltersStore extends ComponentStore<FiltersState> {
  readonly updateStatus = this.updater((state, status: string) => ({
    ...state,
    status,
  }));
}
```

**Signalサービス派：signal()で保持**
```typescript
@Injectable({ providedIn: 'root' })
export class FiltersService {
  readonly status = signal<'all' | 'done'>('all');
  readonly computedLabel = computed(() => `status: ${this.status()}`);
}
```

## 💻 詳細実装例（学習用）
```typescript
export class TodosStore extends ComponentStore<TodosState> {
  readonly load = this.effect((trigger$) =>
    trigger$.pipe(
      switchMap(() => this.repo.list()),
      tapResponse(
        (todos) => this.patchState({ todos }),
        (error) => this.patchState({ error }),
      ),
    ),
  );
}
```

## ベストプラクティス
- ComponentStoreはFeature単位に閉じ込め、責務を増やしすぎない
- Signalサービスは`computed`で派生値を公開し、直接状態を書き換えられないよう`update`メソッドを設ける
- 両方式の共通インターフェースを定義し、テストダブルを入れ替えられるようにする

## 注意点
- ComponentStoreのEffectは購読解除が必要なので`takeUntilDestroyed`を使う
- SignalサービスでもMutableオブジェクトをそのまま更新すると検知されないので不変更新する
- どちらもUIから直接RxJS/Signal APIを触らせずFacadeを通す

## 関連技術
- @ngrx/component-store
- Angular Signals
- Facadeパターン
