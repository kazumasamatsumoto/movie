# #411 「constructor注入 vs inject()関数 あなたはどっち派？」

## 概要
constructor注入は明示的で既存コードとの互換が高い。inject()はStandalone APIと相性がよく、関数領域でもDIが使える。

## 学習目標
- constructor注入の構成と得意なシナリオを整理する
- inject()関数の採用メリットを理解する
- プロジェクト条件に応じた使い分け基準を決める

## 技術ポイント
- constructor注入を成り立たせる主要API/構成要素
- inject()関数で押さえる設定やコード記述
- 両者を共存・移行させるためのブリッジ手法

## 📺 画面表示用コード（動画用）
**constructor派：依存を引数で宣言**
```typescript
constructor(private readonly router: Router) {}

goDetail(id: string) {
  this.router.navigate(['/heroes', id]);
}
```

**inject派：フィールドで完結**
```typescript
private readonly router = inject(Router);

goDetail(id: string) {
  this.router.navigate(['/heroes', id]);
}
```

## 💻 詳細実装例（学習用）
```typescript
export const heroResolver: ResolveFn<Hero> = () => {
  const repo = inject(HeroRepository);
  const route = inject(ActivatedRouteSnapshot);
  return repo.find(route.params['id']);
};
```

## ベストプラクティス
- クラスの依存はconstructorで宣言し、内部ユーティリティやSignals初期化は`inject()`を併用する
- `inject()`呼び出しはトップレベルで行い、メソッド内で毎回呼ばない
- DIを単体テストする際はTestBedの`overrideProvider`で共通化する

## 注意点
- `inject()`は同期的に呼ぶ必要があり、非同期関数内では使えない
- constructor注入でも`public`で露出させると意図せずAPIになるため`private`/`protected`を付ける
- 同じ依存をconstructorとinject両方で取得しない

## 関連技術
- Angular Dependency Injection
- inject() API
- Standalone関数
