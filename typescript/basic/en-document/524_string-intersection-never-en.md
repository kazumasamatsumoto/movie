# #524 "string & never = never"

Shikoku Metan: "Never's behavior shows up in intersections too."
Zundamon: "string & never always reduces to never."
Shikoku Metan: "The same holds for number, boolean, or even unknown."
Zundamon: "Contradiction types like { type: 'A' } & { type: 'B' } collapse to never."
Shikoku Metan: "Compatible combos such as { type: 'A' } & { value: number } stay intact."
Zundamon: "Extract keeps only matching members, so the rest become never."
Shikoku Metan: "Pulling just number from a union leaves plain number."
Zundamon: "Think of never as a certificate proving a contradiction."

---

## 📺 Code for Display

```typescript
/** Example 1: string & never identity */
type Test1 = string & never;   // never
type Test2 = number & never;   // never
type Test3 = boolean & never;  // never
type Test4 = unknown & never;  // never
type Test5 = any & never;      // never
```

```typescript
/** Example 2: Contradicting intersections */
type Contradiction = { type: "A" } & { type: "B" }; // never
type Valid = { type: "A" } & { value: number }; // { type: "A"; value: number }
```

```typescript
/** Example 3: Extract mechanics */
type Extract<T, U> = T extends U ? T : never;

type OnlyNumber = Extract<string | number, number>; // number
type Keys = Extract<"a" | "b" | "c", "a" | "b">; // "a" | "b"
```
