# #543 "Response Types"

Shikoku Metan: "Response unions need never to avoid missing states."
Zundamon: "ApiResponse<T> covered success/error/loading in handleResponse()."
Shikoku Metan: "PagedResponse<T> expressed data presence via hasData."
Zundamon: "reason was empty or error, with a final check: never = res;."
Shikoku Metan: "HttpResponse<T> split behavior by HTTP status."
Zundamon: "Codes >=400 threw errors, everything else returned data or null."
Shikoku Metan: "Strong response types keep clients safe."
Zundamon: "Never keeps watch over every branch."

---

## 📺 Code for Display

```typescript
/** Example 1: Standard response */
type ApiResponse<T> =
  | { status: "success"; data: T; timestamp: number }
  | { status: "error"; error: { code: string; message: string } }
  | { status: "loading" };

function handleResponse<T>(res: ApiResponse<T>): T | null {
  if (res.status === "success") return res.data;
  if (res.status === "error") {
    console.error(res.error);
    return null;
  }
  if (res.status === "loading") return null;
  const check: never = res;
  return null;
}
```

```typescript
/** Example 2: Pagination */
type PagedResponse<T> =
  | { hasData: true; items: T[]; total: number; page: number }
  | { hasData: false; reason: "empty" | "error" };

function processPage<T>(res: PagedResponse<T>): T[] {
  if (res.hasData) return res.items;
  if (!res.hasData && res.reason === "empty") return [];
  if (!res.hasData && res.reason === "error") throw new Error("Failed");
  const check: never = res;
  return [];
}
```

```typescript
/** Example 3: HTTP response */
type HttpResponse<T> =
  | { status: 200; data: T }
  | { status: 201; data: T; location: string }
  | { status: 204 }
  | { status: 400 | 404 | 500; error: string };

function handle<T>(res: HttpResponse<T>): T | null {
  if (res.status === 200) return res.data;
  if (res.status === 201) return res.data;
  if (res.status === 204) return null;
  if (res.status >= 400) throw new Error(res.error);
  const check: never = res;
  return null;
}
```
