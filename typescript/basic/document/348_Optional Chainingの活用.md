# #348 「Optional Chainingの活用」

四国めたん「Optional Chainingの活用方法を学びましょう!」
ずんだもん「?. でプロパティに安全にアクセスできるんだね!」
四国めたん「はい。user.name?.toUpperCase() のように、undefinedの場合も安全です。」
ずんだもん「メソッド呼び出しにも使えるの?」
四国めたん「その通りです。callback?.() で、関数がundefinedでも安全に呼べます。」
ずんだもん「ネストしたアクセスもできるの?」
四国めたん「はい。user?.address?.city のように、深い階層でも使えます。」
ずんだもん「Optional Chainingで簡潔なコードを書くのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: プロパティアクセス */
const user: { name?: string } = {};
const name = user.name?.toUpperCase();
const length = user.name?.length;

/** Example 2: メソッド呼び出し */
const callback: (() => void) | undefined = getCallback();
callback?.();

/** Example 3: ネストしたアクセスとデフォルト値 */
const city = user?.address?.city ?? "Unknown";
const phone = user?.contact?.phone?.trim();
```
