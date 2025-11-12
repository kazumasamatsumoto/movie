# #363 「!演算子の意味」

四国めたん「!演算子は型レベルでnullishを取り除く記号です。」
ずんだもん「value!: string のように型が変わるんだね?」
四国めたん「はい。TypeScript上でのみ効果があり、JavaScriptには残りません。」
ずんだもん「つまりトランスパイル後は普通のアクセスになるの?」
四国めたん「その通り。value!.length は value.length に変換されます。」
ずんだもん「number | null | undefined でも一気にnumberにできる?」
四国めたん「data! * 2 のように書けばnumberとして扱えます。」
ずんだもん「型変換だけが起きて実行時保護は無いことを理解するのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 型の変換 */
const value: string | null = getValue();
// value!: string (nullが除去される)
const upper = value!.toUpperCase();

/** Example 2: トランスパイル後のコード */
// TypeScript
const length = value!.length;
// JavaScript (トランスパイル後)
const length = value.length;

/** Example 3: 複数のnullish型から除去 */
const data: number | null | undefined = getData();
const doubled = data! * 2;  // number型として扱う
```
