# #352 「nullish型の宣言」

四国めたん「nullish型の宣言パターンを押さえましょう!」
ずんだもん「stringやnumberに | null | undefined を付ければいいんだね?」
四国めたん「はい。nameやcountのような値に直接付けられます。」
ずんだもん「毎回書くのが大変なときはどうするの?」
四国めたん「type Nullish<T> を作って再利用すると楽です。」
ずんだもん「Nullish<number[]> みたいに配列にも使えるの?」
四国めたん「もちろん。APIレスポンスのdataやerrorにも指定できます。」
ずんだもん「nullish型を宣言して不確実な値を明示するのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 基本的な宣言 */
let name: string | null | undefined;
let count: number | null | undefined;
let flag: boolean | null | undefined;

/** Example 2: 型エイリアスの再利用 */
type Nullish<T> = T | null | undefined;
let value: Nullish<string>;
let data: Nullish<number[]>;

/** Example 3: APIレスポンスへの適用 */
interface ApiResponse {
  data: User | null | undefined;
  error: Error | null | undefined;
  timestamp: number;
}
```
