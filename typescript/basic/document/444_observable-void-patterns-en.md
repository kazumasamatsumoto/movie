# #444 "Observable<void> Patterns"

Shikoku Metan: "Subject<void> or fromEvent can emit void signals."
Zundamon: "We triggered click$.next() to fire the event."
Shikoku Metan: "fromEvent mapped to undefined creates an Observable<void>."
Zundamon: "finalize(() => ...) handled cleanup too."
Shikoku Metan: "Observable<void> excels at signaling side effects only."
Zundamon: "No payload keeps the types simple."
Shikoku Metan: "Use it for completion or loading indicators."
Zundamon: "I'll represent signals with void streams!"

---

## 📺 Code for Display

```typescript
/** Example 1: Subject<void> */
const click$ = new Subject<void>();
click$.subscribe(() => {
  console.log('Clicked');
});
click$.next();

/** Example 2: fromEvent usage */
const clicks$: Observable<void> = fromEvent(button!, 'click')
  .pipe(map(() => undefined));

/** Example 3: Using finalize() */
operation$.pipe(
  finalize((): void => {
    console.log('Cleanup');
  })
).subscribe();
```
