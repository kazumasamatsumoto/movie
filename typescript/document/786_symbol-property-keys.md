# #786 「シンボルをプロパティキーに」

四国めたん「symbolはオブジェクトのプロパティキーとして利用できます。」
ずんだもん「[]で括って定義するんだよね。」
四国めたん「はい、列挙されにくい隠しプロパティを追加する用途に向いています。」
ずんだもん「メタデータや内部状態を安全に保持できるよ。」
四国めたん「TypeScriptでもComputed Property Nameで型付けできます。」
ずんだもん「シンボルキーで拡張ポイントを作ると衝突しないね。」
四国めたん「基本的な使い方を確認しましょう。」
ずんだもん「シンボルキーはオブジェクト操作の武器だよ！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: シンボルプロパティ定義 */
const KEY = Symbol("meta");
const entity = {
  id: 1,
  [KEY]: { owner: "system" },
};

/** Example 2: 参照 */
console.log(entity[KEY]);

/** Example 3: 型注釈 */
interface WithMeta {
  [KEY]: { owner: string };
}
const typed: WithMeta = { [KEY]: { owner: "core" } };
```
