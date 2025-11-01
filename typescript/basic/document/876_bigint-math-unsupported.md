# #876 「Math関数は使えない」

四国めたん「bigint値にはMath.*関数が使えません。」
ずんだもん「Math.sqrt(4n)とか書くとTypeErrorになるんだね。」
四国めたん「Mathはnumber専用です。」
ずんだもん「必要なら独自実装やサードパーティライブラリを活用しよう。」
四国めたん「型レベルでもコンパイルエラーになるので早期に気づけます。」
ずんだもん「BigIntの制約を理解して別の手段を選ぼう！」
四国めたん「Math関数を使いたい場合はnumberへ変換するかアルゴリズムを工夫してください。」
ずんだもん「制約を押さえてBigIntを扱ってね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: コンパイルエラー */
// Math.sqrt(4n); // TS: Argument of type 'bigint' is not assignable to 'number'

/** Example 2: 変換して利用 */
const sqrt = Math.sqrt(Number(144n));

/** Example 3: ライブラリ使用例 */
import { sqrt as bigintSqrt } from "bigint-isqrt";
const result = bigintSqrt(144n);
```
