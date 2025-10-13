# #923 「初期化パターン」

四国めたん「配列はリテラル以外にもさまざまな初期化パターンがあります。」
ずんだもん「新しい配列を生成するときはArray.fromやfillも使えるね。」
四国めたん「はい、型注釈と合わせて初期値を明確にしましょう。」
ずんだもん「スプレッドでコピーする場合も元の配列と同じ型になるよ。」
四国めたん「初期化方法を理解して意図した型を維持してください。」
ずんだもん「パターンを覚えて効率よく配列を扱おう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: Array.from */
const doubled: number[] = Array.from({ length: 3 }, (_, i) => i * 2);

/** Example 2: fill */
const zeros: number[] = new Array<number>(5).fill(0);

/** Example 3: スプレッド */
const source = [1, 2, 3];
const copy: number[] = [...source];
```
