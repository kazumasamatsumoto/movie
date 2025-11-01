# #741 「unique symbolとは」

四国めたん「unique symbolは特定のシンボル値だけを表すリテラル型です。」
ずんだもん「constでSymbol()を作ると型推論でunique symbolになるんだよね。」
四国めたん「その値をtypeofで参照すればプロパティキー型に流用できます。」
ずんだもん「判別プロパティとしても活躍するよ。」
四国めたん「unique symbolは再代入不可な識別子に最適です。」
ずんだもん「トークンを型安全に共有できるのが嬉しいね。」
四国めたん「宣言にはconstまたはreadonly staticが必要です。」
ずんだもん「使いどころを押さえてunique symbolに慣れよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: constで生成 */
const INJECT_TOKEN = Symbol("INJECT_TOKEN");
// 型: typeof INJECT_TOKEN (unique symbol)

/** Example 2: typeofでプロパティキーに利用 */
const KEY = Symbol("KEY");
type Registry = { [typeof KEY]: string };
const registry: Registry = { [KEY]: "value" };

/** Example 3: 判別プロパティ */
const KIND_A = Symbol("A");
const KIND_B = Symbol("B");
type Node =
  | { kind: typeof KIND_A; value: number }
  | { kind: typeof KIND_B; label: string };
```
