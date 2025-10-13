# #916 「配列型の宣言」

四国めたん「配列型は変数宣言時に型注釈で指定できます。」
ずんだもん「const users: string[] = [] みたいに書くんだね。」
四国めたん「はい、letでもconstでも同じです。」
ずんだもん「オブジェクトのプロパティにも配列型を付けられるよ。」
四国めたん「インターフェースやタイプエイリアスで再利用しやすくなります。」
ずんだもん「配列宣言をしっかり押さえて型安全を高めよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 変数宣言 */
const users: string[] = ["meta", "zunda"];

/** Example 2: プロパティ */
interface Team {
  members: Array<string>;
}

/** Example 3: タイプエイリアス */
type Scores = number[];
const math: Scores = [90, 85, 100];
```
