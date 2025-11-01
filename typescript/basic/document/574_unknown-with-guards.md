# #574 「型ガードでunknownを活用」

四国めたん「型ガードを使えばunknownを安全に扱えます」
ずんだもん「typeofやinstanceof、in演算子を組み合わせるんだよね」
四国めたん「はい。条件分岐の中では目的の型として操作できます」
ずんだもん「共通ガードをモジュール化すると使い回しが効くよ」
四国めたん「複数ガードを連携させれば複雑なデータも処理できます」
ずんだもん「ガード設計でunknownは最強の味方になるね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: typeofガード */
const payload: unknown = Math.random() > 0.5 ? "hi" : 123;
if (typeof payload === "string") {
  console.log(payload.toUpperCase());
}

/** Example 2: instanceofガード */
if (payload instanceof Date) {
  console.log(payload.getFullYear());
}

/** Example 3: in演算子ガード */
if (typeof payload === "object" && payload !== null && "id" in payload) {
  console.log((payload as { id: number }).id);
}
```
