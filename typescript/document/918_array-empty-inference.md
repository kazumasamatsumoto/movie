# #918 「空配列の型推論」

四国めたん「空配列リテラルだけを書くと型はnever[]に推論されます。」
ずんだもん「const arr = [];ってするとpushできなくなるやつだね。」
四国めたん「要素がないので最も狭い型never[]になります。」
ずんだもん「as constを付けると読み取り専用のnever[]になるよ。」
四国めたん「要素を追加するつもりなら型注釈を忘れないようにしましょう。」
ずんだもん「空配列推論の仕組みを理解してね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 推論結果 */
const empty = [];
// empty.push("x"); // エラー: never[]

/** Example 2: 型注釈で解決 */
const mutable: string[] = [];
mutable.push("ok");

/** Example 3: as const */
const readonlyEmpty = [] as const; // 型: readonly []
```
