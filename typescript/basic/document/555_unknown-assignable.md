# #555 「unknownは何でも代入可能」

四国めたん「unknownはトップ型なのでどんな値でも代入できます」
ずんだもん「stringでもnumberでもPromiseでも全部受け止めるんだよね」
四国めたん「はい。Unionにせずとも未知の値を扱えるのが強みです」
ずんだもん「ただし受け取った後の操作には注意が必要だよ」
四国めたん「代入の柔軟さと利用時の制約がセットだと覚えましょう」
ずんだもん「まず受け止めて、次に型ガードで絞り込む流れだね」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 多様な代入 */
let anything: unknown;
anything = 42;
anything = { ok: true };
anything = Promise.resolve("done");

/** Example 2: 関数戻り値としてunknown */
function resolve(value: unknown): unknown {
  return value;
}

/** Example 3: レコードに格納 */
const bucket: Record<string, unknown> = {};
bucket.payload = anything;
bucket.timestamp = Date.now();
```
