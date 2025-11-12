# #478 "Error Type"

Shikoku Metan: "Understand never alongside the Error type."
Zundamon: "fail(message) always threw an Error."
Shikoku Metan: "Throw TypeError or RangeError to clarify the cause."
Zundamon: "validate() created an Error and logged its stack."
Shikoku Metan: "Choosing the right error type makes debugging easier."

---

## 📺 Code for Display

```typescript
/** Example 1: Basic Error */
function fail(message: string): never {
  throw new Error(message);
}

/** Example 2: Subclasses */
function invalidType(value: unknown): never {
  throw new TypeError(`Invalid type: ${typeof value}`);
}
function outOfRange(value: number): never {
  throw new RangeError(`Value ${value} is out of range`);
}

/** Example 3: Stack trace */
function validate(data: unknown): never {
  const error = new Error("Validation failed");
  console.error(error.stack);
  throw error;
}
```
