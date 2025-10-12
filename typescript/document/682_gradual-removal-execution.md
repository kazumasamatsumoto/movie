# #682 「段階的排除② 実行」

四国めたん「実行フェーズでは優先順位順にanyを置き換えていきます」
ずんだもん「ガードやDTOを追加しながらコンパイルエラーを解消するんだね」
四国めたん「はい。影響が大きいファイルから着手し、PRを小さく分割します」
ずんだもん「自動テストを随時回してリグレッションを防ごう」
四国めたん「レビューではガード漏れがないかチェックリストを使いましょう」
ずんだもん「段階実行でチームの負荷を抑えよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 置き換えテンプレート */
function replaceAny(payload: any) {
  const safe: unknown = payload;
  if (typeof safe === "object" && safe !== null) {
    return safe;
  }
  throw new TypeError("invalid payload");
}

/** Example 2: 小さなPR例 */
const changes = ["controller.ts", "dto.ts", "test/controller.spec.ts"] as const;

/** Example 3: 自動テスト */
// npx vitest run
```
