# #365 「代替手段」

四国めたん「!の代わりに安全な書き方を覚えましょう。」
ずんだもん「まずは古典的な型ガードだね?」
四国めたん「if (element !== null) で囲めば確実に存在チェックできます。」
ずんだもん「Optional Chainingならもっと簡潔に書ける?」
四国めたん「user?.name ?? "Unknown" のようにnullish時だけ補えます。」
ずんだもん「型ガード関数でfilterするテクもあるの?」
四国めたん「isNotNull を用意すると配列からnullを除去できます。」
ずんだもん「安全な代替手段で!への依存を減らすのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 型ガードでのチェック */
const element = document.getElementById("app");
if (element !== null) {
  element.innerHTML = "Hello";
}

/** Example 2: Optional Chaining */
const user = findUser(id);
const name = user?.name ?? "Unknown";
user?.greet();

/** Example 3: 型ガード関数 */
function isNotNull<T>(value: T | null): value is T {
  return value !== null;
}
const validUsers = users.filter(isNotNull);
```
