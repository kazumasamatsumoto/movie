# #536 「Angularガード」

四国めたん「Angularのガードにもneverで網羅性を持ち込めるよ。」
ずんだもん「GuardResultはboolean | UrlTree | neverでリターン型を明示してたね。」
四国めたん「AuthStateを判定するcanActivate()では3状態を全部さばいてた。」
ずんだもん「最後にconst check: never = state; を置いて追加状態を検知するのだ。」
四国めたん「RedirectResultみたいなUnionでallow/redirectを管理すると型安全。」
ずんだもん「checkAccess()はadminだけallow: true、それ以外はリダイレクトを返してた。」
四国めたん「neverを使えばルーティングの分岐漏れを防げる。」
ずんだもん「複雑なガードこそ型で守ろう。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: GuardResultの型定義 */
type GuardResult = boolean | UrlTree | never;

@Injectable()
export class AuthGuard implements CanActivate {
  canActivate(route: ActivatedRouteSnapshot): Observable<GuardResult> {
    return this.authService.isAuthenticated$.pipe(
      map(isAuth => (isAuth ? true : this.router.parseUrl("/login")))
    );
  }
}
```

```typescript
/** Example 2: 状態ごとのガード */
type AuthState = "authenticated" | "guest" | "expired";

function canActivate(state: AuthState): boolean | UrlTree {
  if (state === "authenticated") return true;
  if (state === "guest") return this.router.parseUrl("/login");
  if (state === "expired") return this.router.parseUrl("/renew");
  const check: never = state;
  return this.router.parseUrl("/");
}
```

```typescript
/** Example 3: 型安全なリダイレクト */
type RedirectResult =
  | { allow: true }
  | { allow: false; redirect: string };

function checkAccess(role: string): RedirectResult {
  if (role === "admin") return { allow: true };
  return { allow: false, redirect: "/forbidden" };
}
```
