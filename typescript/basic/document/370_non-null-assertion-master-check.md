# #370 「マスターチェック」

四国めたん「Non-null Assertionの総仕上げテストです。」
ずんだもん「document.getElementById("app")! のような基本を確認するんだね?」
四国めたん「はい。HTMLElementとして扱える一方でnullなら危険です。」
ずんだもん「推奨される代替手段も覚えておく?」
四国めたん「element !== null や user?.name ?? "Unknown" を使って安全に書けます。」
ずんだもん「使うべきでないパターンも押さえるの?」
四国めたん「findUser(id)! のような楽観的な書き方は避けるのが鉄則です。」
ずんだもん「チェックリストで!の扱いをマスターするのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: Non-null Assertionの基本 */
const element = document.getElementById("app")!;
// HTMLElement型 (nullの可能性を無視)

/** Example 2: 推奨される代替手段 */
const element = document.getElementById("app");
if (element !== null) {
  element.innerHTML = "Hello";
}
const name = user?.name ?? "Unknown";

/** Example 3: 使用を避けるべき例 */
const user = findUser(id)!;  // 危険
const data = response.data!.items!;  // 乱用
```
