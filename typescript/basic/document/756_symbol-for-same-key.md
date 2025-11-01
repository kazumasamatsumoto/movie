# #756 「同じキーは同じ値」

四国めたん「Symbol.forは同じキーなら常に同じシンボル値を返します。」
ずんだもん「だからライブラリとアプリで同じ識別子を共有できるんだね。」
四国めたん「Mapのキーとして使っても参照が一致します。」
ずんだもん「複数のモジュールが同じキーを呼んでも問題ないよ。」
四国めたん「逆にキーが被ると意図せず共有されるので注意が必要です。」
ずんだもん「命名で名前空間を切るのがポイントだね。」
四国めたん「同じキーは同じ値という性質を活かしましょう。」
ずんだもん「Sharedキーの運用ルールを決めよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 一致の確認 */
const registryKey1 = Symbol.for("lib:service");
const registryKey2 = Symbol.for("lib:service");
console.log(registryKey1 === registryKey2); // true

/** Example 2: Mapへの登録 */
const store = new Map<symbol, number>();
store.set(Symbol.for("counter"), 1);
console.log(store.get(Symbol.for("counter"))); // 1

/** Example 3: 関数越しの共有 */
function useKey() {
  return Symbol.for("handler");
}
console.log(useKey() === useKey()); // true
```
