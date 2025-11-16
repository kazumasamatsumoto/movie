# #257 "Typeof Type Guard"

Shikoku Metan: "Let's learn about typeof type guards!"
Zundamon: "We can check primitive types with typeof!"
Shikoku Metan: "Yes. It's used for type checking string, number, boolean, etc."
Zundamon: "When we narrow the type with an if statement, can we safely use methods inside?"
Shikoku Metan: "Exactly. Type-specific methods become available."
Zundamon: "Narrowing from unknown to number for calculations is safe too!"
Shikoku Metan: "Returning undefined when types don't match is also commonly used."
Zundamon: "Type-safe processing prevents bugs!"

---

## 📺 Code for Display

```typescript
/** Example 1: Processing multiple types */
function processValue(value: string | number | boolean) {
  if (typeof value === 'string') {
    console.log(value.toUpperCase());
  } else if (typeof value === 'number') {
    console.log(value.toFixed(2));
  } else {
    console.log(!value);
  }
}

/** Example 2: Type-safe processing */
function double(value: unknown): number | undefined {
  if (typeof value === 'number') {
    return value * 2;
  }
  return undefined;
}
```
