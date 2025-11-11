# #288 「nullチェック」

四国めたん「今日はnullチェックの方法について学びましょう！」
ずんだもん「厳密等価演算子で安全にチェックできるんだね。」
四国めたん「型ガードを使えば、TypeScriptが型を絞り込んでくれます。」
ずんだもん「オプショナルチェーンで深いプロパティも安全にアクセスできるよ。」
四国めたん「Nullish Coalescing演算子でデフォルト値を設定できます。」
ずんだもん「これらを組み合わせて、堅牢なコードを書こう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 厳密等価演算子と型ガード */
if (user === null) {
  console.log("User is null");
}
function isNotNull<T>(value: T | null): value is T {
  return value !== null;
}
```

```typescript
/** Example 2: オプショナルチェーン */
const name = user?.name;
const zip = user?.address?.zipCode;
```

```typescript
/** Example 3: Nullish Coalescing */
const displayName = user ?? "Guest";
const port = config.port ?? 3000;
```
