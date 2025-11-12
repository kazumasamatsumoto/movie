# #355 「Nullish Coalescing - ??」

四国めたん「Nullish Coalescing演算子 ?? を押さえましょう!」
ずんだもん「nullやundefinedだけをデフォルト値に置き換えてくれるんだね?」
四国めたん「はい。null ?? 'default' や undefined ?? 'default' が代表例です。」
ずんだもん「関数の引数でGuestにフォールバックできる?」
四国めたん「そうです。name ?? 'Guest' のように書けます。」
ずんだもん「設定値でもport ?? 8080みたいに使えるの?」
四国めたん「ええ。options?.timeout ?? 3000 のようにネストした値にも効きます。」
ずんだもん「?? でnullishなときだけ安全に補完するのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: Nullish Coalescingの基本 */
const value1 = null ?? "default";      // "default"
const value2 = undefined ?? "default"; // "default"
const value3 = "hello" ?? "default";   // "hello"

/** Example 2: 関数引数での利用 */
function greet(name: string | null | undefined) {
  const displayName = name ?? "Guest";
  console.log(`Hello, ${displayName}`);
}

/** Example 3: 設定値のデフォルト */
const config = {
  port: options?.port ?? 8080,
  timeout: options?.timeout ?? 3000,
  retries: options?.retries ?? 3,
};
```
