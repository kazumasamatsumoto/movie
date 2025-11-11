# #332 「Nullish Coalescing - x ?? default」

四国めたん「Nullish Coalescing演算子について学びましょう!」
ずんだもん「?? 演算子でデフォルト値を設定できるんだね!」
四国めたん「はい。userName ?? "Guest" で、userNameがnullやundefinedの時だけデフォルト値を使います。」
ずんだもん「|| 演算子とは違うの?」
四国めたん「その通りです。|| は0や空文字もfalsyとして扱いますが、?? はnullとundefinedのみを対象とします。」
ずんだもん「Optional Chainingと組み合わせられるんだね!」
四国めたん「はい。user?.age ?? 18 のように、安全なアクセスとデフォルト値を両立できます。」
ずんだもん「Nullish Coalescingで、より柔軟なコードを書くのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 基本的な使い方 */
const name = userName ?? "Guest";
const port = config.port ?? 3000;

/** Example 2: || との違い */
const count1 = 0 || 10;  // 10 (0はfalsy)
const count2 = 0 ?? 10;  // 0  (0は有効値)

/** Example 3: Optional Chainingと組み合わせ */
const city = user?.address?.city ?? "Unknown";
const age = user?.age ?? 18;
```
