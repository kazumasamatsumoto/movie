# #457 "Testing void Functions"

Shikoku Metan: "Test void functions by inspecting side effects."
Zundamon: "We mocked logging and checked call counts."
Shikoku Metan: "Await Promise<void> before assertions."
Zundamon: "Use expect(() => fn()).toThrow for error cases?"
Shikoku Metan: "Exactly—assert side effects or exceptions instead of return values."

---

## 📺 Code for Display

```typescript
/** Example 1: Sync void test */
test('log called once', () => {
  const spy = vi.fn();
  logWith(spy);
  expect(spy).toHaveBeenCalledTimes(1);
});

/** Example 2: Async void test */
test('save resolves', async () => {
  await saveUser(user);
  expect(database.save).toHaveBeenCalled();
});

/** Example 3: Exception test */
test('validate throws', () => {
  expect(() => validate(invalidData)).toThrow('Invalid data');
});
```
