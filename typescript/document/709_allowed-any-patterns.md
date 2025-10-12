# #709 「any許容パターン集」

四国めたん「許容してよいanyのパターンをカタログ化しましょう」
ずんだもん「サードパーティ境界、プロト、緊急対応などパターン別に定義するんだね」
四国めたん「はい。それぞれコメントルールや期限、責任者を紐付けます」
ずんだもん「パターン外のanyは自動的に検知して議論できる状態にしたいよ」
四国めたん「共通辞書があれば判断のブレを抑えられます」
ずんだもん「パターン集を定期的にアップデートしよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: パターン定義 */
type AllowedPattern = {
  id: string;
  description: string;
  expiry: string;
  owner: string;
};
const patterns: AllowedPattern[] = [];

/** Example 2: メタデータコメント */
// ANY-PATTERN: third-party-boundary (owner:backend, expires:2024-07-01)

/** Example 3: チェックツール */
const validatePattern = (comment: string): boolean => comment.includes("ANY-PATTERN");
```
