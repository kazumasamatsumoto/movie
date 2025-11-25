# #414 「NgRx Store vs Signals Store あなたはどっち派？」

## 概要
NgRx Storeは厳格なアーキテクチャで大規模向き。Signals Storeはボイラープレートを減らし、Signalと親和性の高い状態管理を提供する。

## 学習目標
- NgRx Storeの構成と得意なシナリオを整理する
- Signals Storeの採用メリットを理解する
- プロジェクト条件に応じた使い分け基準を決める

## 技術ポイント
- NgRx Storeを成り立たせる主要API/構成要素
- Signals Storeで押さえる設定やコード記述
- 両者を共存・移行させるためのブリッジ手法

## 📺 画面表示用コード（動画用）
**NgRx Store派：ReducerとActionで管理**
```typescript
export const heroReducer = createReducer(
  initialState,
  on(loadHeroesSuccess, (state, { heroes }) => ({ ...state, heroes }))
);
```

**Signals Store派：宣言的に状態定義**
```typescript
export const HeroesStore = signalStore(
  withState(initialState),
  withMethods((store, repo = inject(HeroRepository)) => ({
    load: () => repo.list().subscribe(heroes => store.patchState({ heroes })),
  })),
);
```

## 💻 詳細実装例（学習用）
```typescript
@Injectable({ providedIn: 'root' })
export class HeroesSignalsStore extends signalStore(
  withState({ heroes: [] as Hero[] }),
  withComputed(store => ({
    count: computed(() => store.heroes().length),
  })),
  withMethods((store, repo = inject(HeroRepository)) => ({
    load: () => repo.list().subscribe(heroes => store.patchState({ heroes })),
  })),
) {}
```

## ベストプラクティス
- NgRx StoreはAction命名やFeature構成をガイドライン化して統一する
- Signal Storeは`withHooks`で初期ロードなどを記述し、副作用を`effect`へ逃がす
- 両方を併用する場合はドメイン境界を決め、Signal StoreをFeature Storeのfacadeにする

## 注意点
- Signal StoreはNgRx v16+が必要で、DevToolsとの統合が限定的
- NgRx StoreのActionを乱立させると可読性が落ちるので命名規約を徹底する
- Signals StoreでObservableを直接購読する際はメモリリーク対策を忘れない

## 関連技術
- @ngrx/store
- @ngrx/signals
- signalStore API
