# #544 "Practical Patterns"

Shikoku Metan: "Let's line up real-world patterns that lean on never."
Zundamon: "userReducer handled LOAD/UPDATE/DELETE actions."
Shikoku Metan: "Unknown action types hit const check: never = action."
Zundamon: "HTTP interceptors covered add-auth/retry/log scenarios."
Shikoku Metan: "Adding an InterceptorAction case forces a compile error."
Zundamon: "ServiceResult<T> flipped on a success flag."
Shikoku Metan: "executeService() returns data or throws, then reaches check: never."
Zundamon: "Bring never into production services."

---

## 📺 Code for Display

```typescript
/** Example 1: NgRx reducer */
type UserAction =
  | { type: "LOAD_USER"; id: string }
  | { type: "UPDATE_USER"; user: User }
  | { type: "DELETE_USER"; id: string };

function userReducer(state: UserState, action: UserAction): UserState {
  if (action.type === "LOAD_USER") return { ...state, loading: true };
  if (action.type === "UPDATE_USER") return { ...state, user: action.user };
  if (action.type === "DELETE_USER") return { ...state, user: null };
  const check: never = action;
  return state;
}
```

```typescript
/** Example 2: HTTP interceptor */
type InterceptorAction =
  | { type: "add-auth"; token: string }
  | { type: "retry"; maxRetries: number }
  | { type: "log" };

function intercept(req: HttpRequest<any>, next: HttpHandler, action: InterceptorAction) {
  if (action.type === "add-auth") {
    return next.handle(req.clone({ setHeaders: { Authorization: action.token } }));
  }
  if (action.type === "retry") {
    return next.handle(req).pipe(retry(action.maxRetries));
  }
  if (action.type === "log") {
    return next.handle(req).pipe(tap(res => console.log(res)));
  }
  const check: never = action;
}
```

```typescript
/** Example 3: Service layer */
type ServiceResult<T> =
  | { success: true; data: T }
  | { success: false; error: ServiceError };

async function executeService<T>(result: ServiceResult<T>): Promise<T> {
  if (result.success) return result.data;
  if (!result.success) throw new ServiceException(result.error);
  const check: never = result;
  return check;
}
```
