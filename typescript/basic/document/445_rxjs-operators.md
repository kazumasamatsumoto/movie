# #445 「RxJSオペレータ」

四国めたん「tapやfinalizeなどのオペレータもvoid関数を受け取ります。」
ずんだもん「tap(() => ...) を重ねてログを出してたね。」
四国めたん「finalize(() => cleanup()) で後処理を定義できます。」
ずんだもん「Observable.forEachのコールバックもvoid扱い?」
四国めたん「はい。戻り値は無視されます。」
ずんだもん「voidコールバックを意識すると副作用の位置がはっきりするね。」
四国めたん「RxJSでもvoidの役割を明確にしましょう。」
ずんだもん「演算子ごとのvoidパターンを覚えるのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: tap()オペレータ */
data$.pipe(
  tap((data): void => {
    console.log('Data:', data);
  }),
  tap((): void => {
    console.log('Processing');
  })
).subscribe();

/** Example 2: finalize()オペレータ */
request$.pipe(
  finalize((): void => {
    console.log('Request complete');
    cleanup();
  })
).subscribe();

/** Example 3: forEach()メソッド */
users$.forEach((user): void => {
  console.log('User:', user.name);
});
```
