# #580 「unknown制限まとめ」

四国めたん「unknownの制限を最後に整理しましょう」
ずんだもん「プロパティ、メソッド、演算、呼び出しが全部禁止だね」
四国めたん「はい。型ガードかアサーションで安全性を証明してから使います」
ずんだもん「制限があるおかげでランタイムエラーが減るんだよ」
四国めたん「制限と向き合えば安心してトップ型を採用できます」
ずんだもん「まとめを意識しながら実践していこう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 禁止操作一覧 */
const value: unknown = { ok: true };
// value.ok;
// value();
// value + 1;

/** Example 2: ガードで許可 */
if (typeof value === "object" && value !== null) {
  console.log(value);
}

/** Example 3: アサーションとセット */
const result = value as { ok: boolean };
console.log(result.ok);
```
