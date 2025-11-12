# #537 「ルートガード」

四国めたん「ルートガードでもneverが漏れを防いでくれるよ。」
ずんだもん「RouteStateを分岐するcanAccess()はpublic/protected/adminを全部チェックしてた。」
四国めたん「未知の状態はconst check: never = state; で検出する仕組みだね。」
ずんだもん「GuardCheckではroleとpermissionの2種類をUnionで表現してた。」
四国めたん「validateGuard()はどちらの条件も満たさないとneverに落ちる。」
ずんだもん「CanActivateFn版authGuardでもrequiredAuthを網羅してたよ。」
四国めたん「none/user/adminを処理したあとにcheck: never = requiredAuth; を置いてる。」
ずんだもん「ガードロジックが増えてもneverが見張ってくれるのだ。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: RouteStateの判定 */
type RouteState =
  | { type: "public" }
  | { type: "protected"; requiredRole: string }
  | { type: "admin" };

function canAccess(state: RouteState, userRole: string): boolean {
  if (state.type === "public") return true;
  if (state.type === "protected") return userRole === state.requiredRole;
  if (state.type === "admin") return userRole === "admin";
  const check: never = state;
  return false;
}
```

```typescript
/** Example 2: GuardCheckの網羅性 */
type Permission = "read" | "write" | "delete";
type GuardCheck =
  | { check: "role"; role: string }
  | { check: "permission"; permission: Permission };

function validateGuard(check: GuardCheck, user: User): boolean {
  if (check.check === "role") return user.role === check.role;
  if (check.check === "permission") return user.permissions.includes(check.permission);
  const exhaustive: never = check;
  return false;
}
```

```typescript
/** Example 3: CanActivateFn */
export const authGuard: CanActivateFn = (route, state) => {
  const requiredAuth = route.data["auth"] as AuthType;

  if (requiredAuth === "none") return true;
  if (requiredAuth === "user") return checkUser();
  if (requiredAuth === "admin") return checkAdmin();
  const check: never = requiredAuth;
  return false;
};
```
