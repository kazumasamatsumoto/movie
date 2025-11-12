# #537 "Route Guards"

Shikoku Metan: "Never protects route guards from missing cases."
Zundamon: "canAccess() covered public, protected, and admin states."
Shikoku Metan: "Unknown states hit const check: never = state;."
Zundamon: "GuardCheck captured role vs permission checks as a union."
Shikoku Metan: "validateGuard() rejects anything outside those options."
Zundamon: "The functional authGuard handled none/user/admin."
Shikoku Metan: "A final check: never = requiredAuth; keeps it exhaustive."
Zundamon: "Even growing guard logic stays safe."

---

## 📺 Code for Display

```typescript
/** Example 1: Evaluating RouteState */
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
/** Example 2: GuardCheck exhaustiveness */
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
