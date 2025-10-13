# #970 「どちらを使うべきか」

四国めたん「(string | number)[]とstring[] | number[]のどちらを使うかは要件次第です。」
ずんだもん「要素が混ざるなら前者、配列単位で切り替わるなら後者だね。」
四国めたん「はい、API仕様やデータ構造に合わせて選びましょう。」
ずんだもん「将来の拡張性や処理の簡潔さも考慮したいよ。」
四国めたん「決定事項はコメントや型エイリアスで残しておくと親切です。」
ずんだもん「意図を明確にして使い分けてね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 混在 */
type MixedTokens = (string | number)[];

/** Example 2: 排他的 */
type ExclusiveTokens = string[] | number[];

/** Example 3: コメント */
/**
 * MixedTokens: 日付ログなど異種混在を表現
 * ExclusiveTokens: API互換性のため配列単位で切り替え
 */
```
