# #544 「実践パターン」

四国めたん「neverを活かす実践パターンを並べてみよう。」
ずんだもん「NgRxのuserReducerはLOAD/UPDATE/DELETEを全部ifで処理してたね。」
四国めたん「未知のaction.typeはconst check: never = action; で検知。」
ずんだもん「HTTP Interceptorでもadd-auth/retry/logの3種類を網羅してたのだ。」
四国めたん「InterceptorActionが増えたらcompileが止めてくれる。」
ずんだもん「ServiceResult<T>もsuccessフラグで戻り値を分けてた。」
四国めたん「executeService()はsuccessならdata、失敗なら例外を投げ、最後はcheck: never。」
ずんだもん「実サービスでもneverを使いこなそう。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: NgRx Reducer */
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
/** Example 2: HTTP Interceptor */
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
/** Example 3: サービスレイヤー */
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
