# #560 「unknown型の特性」

四国めたん「unknownの特性は柔軟な代入と厳格な利用制限の両立です」
ずんだもん「トップ型だからキャッチオールになるけど操作制限が効いてるんだね」
四国めたん「はい。型推論にも関与して安全なUnion処理ができます」
ずんだもん「ジェネリック関数で扱うときもデフォルト型に使えるし便利だよ」
四国めたん「制限を超えるには型ガードかアサーションが必須です」
ずんだもん「特性を理解してチームの共通言語にしよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: デフォルト型として使用 */
function wrap<T = unknown>(value: T) {
  return { value };
}

/** Example 2: Unionとの相互作用 */
function merge(a: unknown, b: unknown) {
  if (typeof a === "string" && typeof b === "string") {
    return a + b;
  }
  return [a, b];
}

/** Example 3: 動的データのプロパティ検査 */
function inspect(value: unknown) {
  if (typeof value === "object" && value !== null && "id" in value) {
    console.log((value as { id: number }).id);
  }
}
```
