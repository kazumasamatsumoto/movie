# #419 「クラスベースGuard vs 関数型Guard あなたはどっち派？」

## 概要
クラスガードは再利用性とテスト容易性が高い。関数型はStandalone時代にマッチし、DIも自由。ルート特性に応じて選択する。

## 学習目標
- クラスベースの構成と得意なシナリオを整理する
- 関数型Guardの採用メリットを理解する
- プロジェクト条件に応じた使い分け基準を決める

## 技術ポイント
- クラスベースを成り立たせる主要API/構成要素
- 関数型Guardで押さえる設定やコード記述
- 両者を共存・移行させるためのブリッジ手法

## 📺 画面表示用コード（動画用）
**クラス派：`CanActivate`を実装**
```typescript
@Injectable({ providedIn: 'root' })
export class AuthGuard implements CanActivate {
  constructor(private readonly auth: AuthService, private readonly router: Router) {}
  canActivate(): boolean {
    return this.auth.isSignedIn() || this.router.createUrlTree(['/login']);
  }
}
```

**関数派：`CanActivateFn`で完結**
```typescript
export const authGuard: CanActivateFn = () => {
  const auth = inject(AuthService);
  const router = inject(Router);
  return auth.isSignedIn() || router.createUrlTree(['/login']);
};
```

## 💻 詳細実装例（学習用）
```typescript
export const routes: Routes = [
  {
    path: 'admin',
    loadComponent: () => import('./admin.component'),
    canActivate: [authGuard],
  },
];
```

## ベストプラクティス
- よく使うガードはクラスとして切り出し、局所的な条件は関数で`routes.ts`に書く
- `inject()`で取り出す依存はトップレベルに保持し、副作用を避ける
- ガードの戻り値に`UrlTree`を活用し、リダイレクト先を明示する

## 注意点
- 関数型ガードは`inject()`を同期的にしか呼べないので注意
- クラスガードと関数ガードが混在する場合、命名規約を決めて可読性を保つ
- ガードで重いAPI呼び出しをすると遷移体験が悪化するためResolverやPreloadingへ逃がす

## 関連技術
- CanActivate/CanMatch
- Functional Guards
- inject() API
