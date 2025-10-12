# #564 「unknown基本パターン」

四国めたん「unknownを扱う基本パターンは三つに整理できます」
ずんだもん「受け取る、型ガードで絞る、結果を返すって流れだね」
四国めたん「その通りです。場合によってアサーションやデフォルト値も加えます」
ずんだもん「パターンをテンプレ化すると実装が早くなるよ」
四国めたん「まず入力境界でガードを書く習慣を付けましょう」
ずんだもん「安全なパイプラインが全体の保守性を上げるね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: ガードパターン */
function guard(value: unknown) {
  if (typeof value === "string") return value;
  throw new TypeError("expected string");
}

/** Example 2: フォールバックパターン */
function withDefault<T>(value: unknown, fallback: T): T {
  return (typeof value === typeof fallback ? (value as T) : fallback);
}

/** Example 3: セーフパイプライン */
function pipeline(value: unknown) {
  if (Array.isArray(value)) return value.map(String);
  return [];
}
```
