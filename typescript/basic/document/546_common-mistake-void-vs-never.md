# #546 「間違い(1) - void混同」

四国めたん「voidとneverを混同すると危険だよ。」
ずんだもん「logMessage()みたいなvoid関数は正常終了してundefinedを返すのだ。」
四国めたん「throwError()のように絶対戻らない処理はnever型にする必要がある。」
ずんだもん「process()をvoidで宣言して中でthrowすると設計の意図が伝わらないね。」
四国めたん「processCorrect()みたいにneverで宣言すればコンパイラも理解してくれる。」
ずんだもん「戻り値の代入ではvoidはundefined互換だけどneverは何とも互換じゃない。」
四国めたん「const d: never = undefined; はエラーになるから注意。」
ずんだもん「戻らない関数は必ずneverで書こう。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: voidとneverの違い */
function logMessage(msg: string): void {
  console.log(msg);
  // 通常終了
}

function throwError(msg: string): never {
  throw new Error(msg);
  // ここへは戻らない
}
```

```typescript
/** Example 2: 間違ったvoid */
function process(): void {
  throw new Error("Error"); // voidなのに戻らない
}

function processCorrect(): never {
  throw new Error("Error");
}
```

```typescript
/** Example 3: 代入の違い */
const a: void = logMessage("Hello"); // OK
const b: never = throwError("Error"); // 実行されない

const c: void = undefined; // OK
const d: never = undefined; // エラー
```
