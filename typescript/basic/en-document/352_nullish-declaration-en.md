# #352 "Declaring Nullish Types"

Shikoku Metan: "Let's cover the declaration patterns for nullish types!"
Zundamon: "I just add | null | undefined to string or number, right?"
Shikoku Metan: "Yes, you can attach it directly to fields like name or count."
Zundamon: "What if writing it every time feels verbose?"
Shikoku Metan: "Define a reusable type Nullish<T> so you don't repeat yourself."
Zundamon: "Can I use Nullish<number[]> for arrays as well?"
Shikoku Metan: "Of course, and it's perfect for API responses like data or error fields."
Zundamon: "I'll declare nullish shapes whenever a value isn't guaranteed!"

---

## 📺 Code for Display

```typescript
/** Example 1: Basic declarations */
let name: string | null | undefined;
let count: number | null | undefined;
let flag: boolean | null | undefined;

/** Example 2: Reusing a type alias */
type Nullish<T> = T | null | undefined;
let value: Nullish<string>;
let data: Nullish<number[]>;

/** Example 3: Applying it to an API response */
interface ApiResponse {
  data: User | null | undefined;
  error: Error | null | undefined;
  timestamp: number;
}
```
