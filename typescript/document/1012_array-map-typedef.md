# #1012 「型定義」

四国めたん「TypeScriptのlib.d.tsではmapの型がきちんと定義されています。」
ずんだもん「配列ジェネリクスでmap<U>(callback: ...) => U[]ってなってるやつだね。」
四国めたん「はい、コールバックの戻り値型に応じて新しい配列型が決まります。」
ずんだもん「型定義を理解すると候補や補完の理由が分かるよ。」
四国めたん「libファイルを覗いて挙動を確認してみましょう。」
ずんだもん「型定義を味方にしてね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 型定義の抜粋 */
interface Array<T> {
  map<U>(callbackfn: (value: T, index: number, array: T[]) => U, thisArg?: any): U[];
}

/** Example 2: 型推論 */
const values = [1, 2, 3];
const result = values.map((value) => value.toString()); // 推論: string[]

type ResultType = typeof result; // string[]

/** Example 3: 明示的ジェネリック */
const explicit = values.map<string>((value) => value.toFixed(2));
```
