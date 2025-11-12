# #353 "Nullish Type Use Cases"

Shikoku Metan: "Let's review practical uses of nullish types."
Zundamon: "API responses often return data or null/undefined, right?"
Shikoku Metan: "Yes, modeling them as T | null | undefined forces callers to check safely."
Zundamon: "Database calls can return undefined from a catch block?"
Shikoku Metan: "Exactly. Returning undefined on errors lets callers tell failures apart."
Zundamon: "Form inputs like email or phone can also be nullish when blank?"
Shikoku Metan: "Right, string | null | undefined accurately reflects optional entries."
Zundamon: "I'll align my types with real-world data states!"

---

## 📺 Code for Display

```typescript
/** Example 1: Typing an API response */
interface ApiResponse<T> {
  data: T | null | undefined;
  error: string | null | undefined;
  status: number;
}

/** Example 2: Database query */
async function getUser(id: number): Promise<User | null | undefined> {
  try {
    return await db.users.findById(id);
  } catch {
    return undefined;
  }
}

/** Example 3: Typing form input */
interface FormData {
  name: string;
  email: string | null | undefined;
  phone: string | null | undefined;
}
```
