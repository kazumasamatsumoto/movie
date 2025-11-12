# #358 「Optional Chaining - ?.」

四国めたん「Optional Chaining ?. を復習しましょう!」
ずんだもん「user?.name ならuserがnullでも落ちないんだね?」
四国めたん「はい。プロパティアクセスが安全になります。」
ずんだもん「メソッド呼び出しにも使えるの?」
四国めたん「obj?.method?.() のように存在するときだけ実行されます。」
ずんだもん「配列アクセスやネストにも使える?」
四国めたん「array?.[0] や user?.contacts?.[0]?.phone で深い階層もOKです。」
ずんだもん「?. を使ってundefinedチェックの嵐から解放されるのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: プロパティアクセス */
const user: User | null | undefined = getUser();
const name = user?.name;
const email = user?.email;

/** Example 2: メソッド呼び出し */
const result = obj?.method?.();
const length = str?.toUpperCase()?.length;

/** Example 3: 配列アクセスとネスト */
const firstItem = array?.[0];
const city = user?.address?.city;
const phone = user?.contacts?.[0]?.phone;
```
