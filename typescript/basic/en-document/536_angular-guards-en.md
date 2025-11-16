# #536 "Angular Guards"

Shikoku Metan: "Never helps Angular guards stay exhaustive."
Zundamon: "GuardResult spelled out boolean | UrlTree | never."
Shikoku Metan: "Our canActivate() handled authenticated, guest, and expired states."
Zundamon: "A final const check: never = state; catches new states."
Shikoku Metan: "RedirectResult keeps allow/redirect data in a discriminated union."
Zundamon: "checkAccess() only allows admins, others get a redirect."
Shikoku Metan: "Never prevents routing branches from falling through."
Zundamon: "Let types shield complex guards."

---

## 📺 Code for Display

```typescript
/** Example 1: GuardResult type */
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
/** Example 2: State-driven guard */
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
/** Example 3: Redirect union */
type RedirectResult =
  | { allow: true }
  | { allow: false; redirect: string };

function checkAccess(role: string): RedirectResult {
  if (role === "admin") return { allow: true };
  return { allow: false, redirect: "/forbidden" };
}
```
