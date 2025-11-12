# #360 「nullish型まとめ」

四国めたん「nullish型のまとめをしましょう!」
ずんだもん「type Nullish<T> = T | null | undefined で定義できるんだよね?」
四国めたん「はい。getValue() の結果のような不確実な値を表します。」
ずんだもん「操作するときは user?.name ?? 'Guest' を使えばいい?」
四国めたん「ええ。?? と ?. と != null の組み合わせで安全に扱えます。」
ずんだもん「設定オブジェクトでも env?.HOST ?? 'localhost' みたいに?」
四国めたん「その通り。response?.data ?? [] で欠損時の配列も補えます。」
ずんだもん「nullish型を理解して信頼できるコードを書くのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: nullish型の定義 */
type Nullish<T> = T | null | undefined;
const value: string | null | undefined = getValue();

/** Example 2: 安全な操作 */
const displayName = user?.name ?? "Guest";
const age = user?.age ?? 0;
if (value != null) {
  console.log(value);
}

/** Example 3: 実践パターン */
const config = {
  host: env?.HOST ?? "localhost",
  port: env?.PORT ?? 8080,
  data: response?.data ?? [],
};
```
