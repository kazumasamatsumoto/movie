# #584 「typeof x === "boolean"」

四国めたん「typeof x === "boolean"でunknownを真偽値に絞りましょう」
ずんだもん「条件分岐やフラグ処理にすぐ使えるようになるね」
四国めたん「真偽値以外を弾くことで意図しないtruthy判定を避けられます」
ずんだもん「ユーティリティ関数にして再利用するのが便利だよ」
四国めたん「boolean専用の処理ブロックで副作用を管理しましょう」
ずんだもん「フラグ制御を型安全にできるのが嬉しいね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: booleanガード */
function toggle(value: unknown) {
  if (typeof value === "boolean") {
    return !value;
  }
  return value;
}

/** Example 2: 真偽値限定ヘルパー */
const isBoolean = (input: unknown): input is boolean =>
  typeof input === "boolean";

/** Example 3: 設定値の検証 */
function ensureFlag(value: unknown): boolean {
  if (!isBoolean(value)) return false;
  return value;
}
```
