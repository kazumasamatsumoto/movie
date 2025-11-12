# #540 「API設計」

四国めたん「API設計でもneverでレスポンス漏れを防げるよ。」
ずんだもん「ApiResponse<T>はsuccess/error/loadingの3種類をhandleResponse()で網羅してた。」
四国めたん「statusを追加するとconst check: never = res; が怒ってくれる。」
ずんだもん「Endpoint型もmethodごとに必要なフィールドを持ってたね。」
四国めたん「request()でGET/POST/DELETEを全部処理してからcheck: never = endpoint; を置いてた。」
ずんだもん「GraphQLのGqlOperationもquery/mutation/subscriptionを切り替えてた。」
四国めたん「executeGql()の最後にもcheck: never = op; を仕込んでいる。」
ずんだもん「API層こそ型を固めると変更に強くなるのだ。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: APIレスポンス */
type ApiResponse<T> =
  | { status: "success"; data: T }
  | { status: "error"; error: { code: string; message: string } }
  | { status: "loading" };

function handleResponse<T>(res: ApiResponse<T>): T | null {
  if (res.status === "success") return res.data;
  if (res.status === "error") throw new Error(res.error.message);
  if (res.status === "loading") return null;
  const check: never = res;
  return null;
}
```

```typescript
/** Example 2: RESTエンドポイント */
type Endpoint =
  | { method: "GET"; path: string }
  | { method: "POST"; path: string; body: unknown }
  | { method: "DELETE"; path: string };

async function request(endpoint: Endpoint): Promise<Response> {
  if (endpoint.method === "GET") return fetch(endpoint.path);
  if (endpoint.method === "POST") {
    return fetch(endpoint.path, { method: "POST", body: JSON.stringify(endpoint.body) });
  }
  if (endpoint.method === "DELETE") {
    return fetch(endpoint.path, { method: "DELETE" });
  }
  const check: never = endpoint;
  throw new Error("Invalid endpoint");
}
```

```typescript
/** Example 3: GraphQL操作 */
type GqlOperation =
  | { type: "query"; query: string }
  | { type: "mutation"; mutation: string }
  | { type: "subscription"; subscription: string };

function executeGql(op: GqlOperation): Promise<any> {
  if (op.type === "query") return client.query({ query: op.query });
  if (op.type === "mutation") return client.mutate({ mutation: op.mutation });
  if (op.type === "subscription") return client.subscribe({ query: op.subscription });
  const check: never = op;
  return Promise.reject(new Error("Unknown operation"));
}
```
