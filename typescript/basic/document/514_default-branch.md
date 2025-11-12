# #514 「default節」

四国めたん「default節は網羅性チェックの最後の砦だよ。」
ずんだもん「Directionのmove()はnorth/south/east/westをswitchで返してたね。」
四国めたん「defaultでconst check: never = dir; を投げれば未知の値を弾ける。」
ずんだもん「centerを追加した例ではdefaultに落ちて編集中に気付けたのだ。」
四国めたん「exhaustiveCheck()を作ってdefaultで呼ぶのも定番。」
ずんだもん「switchごとに同じ関数を使えば記述がそろって安心だね。」
四国めたん「defaultを捨てるより監視役として活用しよう。」
ずんだもん「neverのおかげで方向追加も怖くなくなるよ。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 4方向のmove */
type Direction = "north" | "south" | "east" | "west";

function move(dir: Direction): [number, number] {
  switch (dir) {
    case "north":
      return [0, 1];
    case "south":
      return [0, -1];
    case "east":
      return [1, 0];
    case "west":
      return [-1, 0];
    default:
      const check: never = dir;
      throw new Error(`未処理: ${check}`);
  }
}

/** Example 2: 新しい値で検出 */
type ExtendedDirection = Direction | "center";

function brokenMove(dir: ExtendedDirection) {
  switch (dir) {
    case "north":
      return [0, 1];
    case "south":
      return [0, -1];
    default:
      const check: never = dir; // centerがここに来て型エラー
      throw new Error();
  }
}

/** Example 3: exhaustiveCheckの利用 */
function exhaustiveCheck(value: never): never {
  throw new Error(`Unhandled: ${value}`);
}

function safeMove(dir: Direction) {
  switch (dir) {
    case "north":
      return [0, 1];
    case "south":
      return [0, -1];
    case "east":
      return [1, 0];
    case "west":
      return [-1, 0];
    default:
      return exhaustiveCheck(dir);
  }
}
```
