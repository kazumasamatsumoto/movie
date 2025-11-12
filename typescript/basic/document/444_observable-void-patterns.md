# #444 「Observable<void>」

四国めたん「Subject<void>やfromEventでイベントをvoid化できます。」
ずんだもん「click$.next() でイベントを発火させていたね。」
四国めたん「fromEventでもmap(() => undefined)とすればvoidストリームになります。」
ずんだもん「finalize(() => ...) でクリーンアップを書く例もあった!」
四国めたん「Observable<void>は副作用の発火だけを伝える用途に最適です。」
ずんだもん「値を持たせないことで型がすっきりするんだね。」
四国めたん「イベント完了通知やローディング制御に活用しましょう。」
ずんだもん「voidストリームでシグナルを表現するのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: Subject<void> */
const click$ = new Subject<void>();
click$.subscribe(() => {
  console.log('Clicked');
});
click$.next();

/** Example 2: fromEventでの使用 */
const clicks$: Observable<void> = fromEvent(button!, 'click')
  .pipe(map(() => undefined));

/** Example 3: finalize()との組み合わせ */
operation$.pipe(
  finalize((): void => {
    console.log('Cleanup');
  })
).subscribe();
```
