# #443 「Observableとvoid型」

四国めたん「RxJSでもObservable<void>が活躍します。」
ずんだもん「Subject<void>を作ってsaveComplete$を流していたね。」
四国めたん「subscribe側では値を使わず副作用だけを記述します。」
ずんだもん「tap(() => ...) でログを差し込むのも便利!」
四国めたん「pipeにvoidコールバックを挟めます。」
ずんだもん「Observable<void>ならイベントの完了通知にぴったりだね。」
四国めたん「値が不要なストリームは積極的にvoidにしましょう。」
ずんだもん「Observableの副作用ハンドラを整えるのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: Observable<void>の基本 */
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

/** Example 2: 購読 */
service.onSaveComplete().subscribe(() => {
  console.log('Save completed');
});

/** Example 3: tap()演算子 */
data$.pipe(
  tap((): void => {
    console.log('Data received');
  })
).subscribe();
```
