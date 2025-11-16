# #443 "Observable<void>"

Shikoku Metan: "Observable<void> is common in RxJS."
Zundamon: "We built saveComplete$ using Subject<void>."
Shikoku Metan: "Subscribers perform side effects only."
Zundamon: "tap(() => ...) inserts logging nicely."
Shikoku Metan: "Pipe void callbacks wherever you need hooks."
Zundamon: "Observable<void> works great for completion events."
Shikoku Metan: "Use void whenever payloads aren't needed."
Zundamon: "I'll tidy my RxJS side effects with Observable<void>!"

---

## 📺 Code for Display

```typescript
/** Example 1: Subject<void> */
class Service {
  private saveComplete$ = new Subject<void>();

  save(data: Data): void {
    database.save(data);
    this.saveComplete$.next();
  }

  onSaveComplete(): Observable<void> {
    return this.saveComplete$.asObservable();
  }
}

/** Example 2: Subscription */
service.onSaveComplete().subscribe(() => {
  console.log('Save completed');
});

/** Example 3: tap() operator */
data$.pipe(
  tap((): void => {
    console.log('Data received');
  })
).subscribe();
```
