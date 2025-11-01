# #645 「anyには何でも代入できる」

四国めたん「anyにはあらゆる値を代入できます」
ずんだもん「プリミティブもオブジェクトもPromiseも全部受け止めるんだよね」
四国めたん「はい。型制約が無いので自由に差し替えられます」
ずんだもん「でもそれだけ型情報が失われるってことだよ」
四国めたん「代入の自由はリスクでもあると理解しましょう」
ずんだもん「unknownなら安全性を保てるから置き換えを検討したいね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 様々な代入 */
let anything: any;
anything = 42;
anything = { ok: true };
anything = Promise.resolve("done");

/** Example 2: 型情報が消える */
const flag: boolean = anything;

/** Example 3: unknownなら安全 */
let safer: unknown = anything;
// safer.prop; // ❌ guardが必要
```
