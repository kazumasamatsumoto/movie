# #540 "API Design"

Shikoku Metan: "Never guards API designs against missing branches."
Zundamon: "ApiResponse<T> covered success/error/loading in handleResponse()."
Shikoku Metan: "Adding a new status makes const check: never = res; complain."
Zundamon: "Endpoint unions captured GET/POST/DELETE specifics."
Shikoku Metan: "request() handles each method before hitting check: never = endpoint;."
Zundamon: "GqlOperation switched between query/mutation/subscription."
Shikoku Metan: "executeGql() ends with check: never = op; for safety."
Zundamon: "Locking down types keeps API layers resilient."

---

## 📺 Code for Display

```typescript
/** Example 1: API response */
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
/** Example 2: REST endpoints */
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
/** Example 3: GraphQL operations */
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
