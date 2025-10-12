# #702 「サードパーティでのany許容」

四国めたん「外部ライブラリがanyを返す場合、利用側で例外扱いすることがあります」
ずんだもん「型定義が無いときはラッパーを用意するまで暫定的にanyを許すんだね」
四国めたん「はい。ただし許容箇所を専用モジュールに閉じ込めましょう」
ずんだもん「eslint-disableに理由を添えて監査ログを残すと管理しやすいよ」
四国めたん「サードパーティのanyはガード下でのみ利用するルールを徹底します」
ずんだもん「安全な境界管理でリスクを抑えよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 専用モジュール */
// external/legacy-wrapper.ts
/* eslint-disable @typescript-eslint/no-explicit-any -- legacy SDK */
export const call = (method: string): any => legacySdk.invoke(method);

/** Example 2: 利用側でガード */
const payload = call("get");
if (typeof payload === "object" && payload !== null) {
  // 安全に扱う
}

/** Example 3: 監査ログ */
const audit = [{ module: "legacy-wrapper", reason: "vendor未対応", review: "quarterly" }];
```
