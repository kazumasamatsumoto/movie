# #932 「アクセスの型」

四国めたん「配列インデックスアクセスの戻り値は要素型になります。」
ずんだもん「numbers[0]ならnumber型だね。」
四国めたん「はい、const宣言でリテラル型に絞られている場合はそのリテラル型が返ることもあります。」
ずんだもん「as constで固定した配列だとprop[0]が具体的な値になるよ。」
四国めたん「型推論を把握しておくと期待どおりの戻り値を扱えます。」
ずんだもん「アクセスの型を意識してね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 要素型 */
const ages: number[] = [18, 20];
const age = ages[0]; // number

/** Example 2: リテラル保持 */
const flags = ["ON", "OFF"] as const;
const firstFlag = flags[0]; // "ON"

/** Example 3: Union */
const mixed = ["start", 0];
const token = mixed[0]; // string | number
```
