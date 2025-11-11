# #331 「Optional Chaining - x?.property」

四国めたん「Optional Chainingについて学びましょう!」
ずんだもん「?. 演算子で安全にプロパティアクセスできるんだね!」
四国めたん「はい。user?.name で、userがnullやundefinedでもエラーにならず、undefinedを返します。」
ずんだもん「ネストしたプロパティにも使えるの?」
四国めたん「その通りです。user?.address?.city のように、深い階層でも安全にアクセスできます。」
ずんだもん「配列要素やメソッド呼び出しにも使えるんだね!」
四国めたん「はい。array?.[0] や obj?.method?.() のように、様々な場面で活用できます。」
ずんだもん「Optional Chainingで、より安全なコードを書くのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 基本的な使い方 */
const user: User | null = getUser();
const name = user?.name; // string | undefined
const email = user?.email;

/** Example 2: ネストしたプロパティ */
const city = user?.address?.city;
const zip = user?.address?.zipCode ?? "N/A";

/** Example 3: 配列とメソッド */
const firstItem = array?.[0];
const result = obj?.method?.();
```
