# #445 "RxJS Operators"

Shikoku Metan: "RxJS operators like tap/finalize accept void callbacks."
Zundamon: "We stacked tap(() => ...) for logging."
Shikoku Metan: "finalize(() => cleanup()) defines teardown logic."
Zundamon: "Observable.forEach callbacks are void as well?"
Shikoku Metan: "Yes, their return values are ignored."
Zundamon: "Void callbacks highlight where side effects occur."
Shikoku Metan: "Keep void semantics clear even in RxJS."
Zundamon: "I'll memorize these operator patterns!"

---

## 📺 Code for Display

```typescript
/** Example 1: tap() operator */
data$.pipe(
  tap((data): void => {
    console.log('Data:', data);
  }),
  tap((): void => {
    console.log('Processing');
  })
).subscribe();

/** Example 2: finalize() operator */
request$.pipe(
  finalize((): void => {
    console.log('Request complete');
    cleanup();
  })
).subscribe();

/** Example 3: forEach() method */
users$.forEach((user): void => {
  console.log('User:', user.name);
});
```
