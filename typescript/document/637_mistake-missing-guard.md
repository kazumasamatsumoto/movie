# #637 「間違い② 型ガード不足」

四国めたん「次の間違いは型ガードを途中で省略してしまうことです」
ずんだもん「一部だけチェックして、ネストしたプロパティをそのまま触っちゃうんだよね」
四国めたん「はい。ネストが深い場合でも段階的に型を保証する必要があります」
ずんだもん「ガード関数を分割すれば読みやすくなるよ」
四国めたん「中途半端なガードは静的保証を失わせます」
ずんだもん「丁寧に絞り込んでunknownを安全に扱おう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 不十分なガード */
function hasProfile(value: unknown) {
  return typeof value === "object";
}
// hasProfile(payload) && payload.profile.name; // ❌

/** Example 2: 段階的ガード */
function isProfile(value: unknown): value is { profile: { name: string } } {
  if (typeof value !== "object" || value === null) return false;
  const record = value as Record<string, unknown>;
  const profile = record.profile;
  return typeof profile === "object"
    && profile !== null
    && typeof (profile as Record<string, unknown>).name === "string";
}

/** Example 3: 安全アクセス */
if (isProfile(payload)) console.log(payload.profile.name);
```
