# #736 「シンボルの一意性」

四国めたん「Symbolは同じ変数に再代入しない限り、一意性が保たれます。」
ずんだもん「Setに入れても重複して扱われないのが便利だね。」
四国めたん「Object.isでも===でも比較結果は同じで、生成順を問わず一致しません。」
ずんだもん「イベント名やメタデータを安全に識別できるよ。」
四国めたん「外部から説明文字列が被っても一意性は壊れません。」
ずんだもん「協調開発での衝突事故を未然に防げるんだね。」
四国めたん「unique symbol型と組み合わせれば静的保証も強化できます。」
ずんだもん「実装と型の両面で一意性を守っていこう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: Setでの一意性 */
const s1 = Symbol("event");
const s2 = Symbol("event");
const set = new Set([s1, s2]);
console.log(set.size); // 2

/** Example 2: === と Object.is */
console.log(Object.is(s1, s2)); // false
console.log(s1 === s2); // false

/** Example 3: 安全なイベントキー */
const createEvent = (name: string) => Symbol(name);
const onLoad = createEvent("load");
const onDispose = createEvent("load");
console.log(onLoad === onDispose); // false
```
