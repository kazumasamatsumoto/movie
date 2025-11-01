# #605 「any型が許される場面」

四国めたん「anyが許容されるのはごく限定的なケースです」
ずんだもん「プロトタイピングや型定義がまだない外部SDKとかだね」
四国めたん「はい。短期間で仮実装するときや、型安全性より速度が最優先な場面です」
ずんだもん「でも後で必ずunknownや正確な型に置き換えるべきだよ」
四国めたん「eslint-disableなどは期限を決めて管理しましょう」
ずんだもん「例外扱いで、常用しないってルールが大事だね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: プロトタイプ */
let temp: any; // TODO: 後で型定義を作成
temp = fetchExperimental();

/** Example 2: 限定的なdisable */
// eslint-disable-next-line @typescript-eslint/no-explicit-any
function passthrough(value: any) {
  return value;
}

/** Example 3: 外部SDKの暫定対応 */
declare const thirdParty: any;
const raw = thirdParty.invoke();
```
