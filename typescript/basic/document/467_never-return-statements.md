# #467 「return文 - 到達しない」

四国めたん「never関数では到達可能なreturnを書いてはいけません。」
ずんだもん「failの後にreturn;って書いても意味がないんだね。」
四国めたん「invalid()ではifの後にreturn;が到達可能でエラーになります。」
ずんだもん「abortは最後にthrowすることで正しくneverになる!」
四国めたん「制御が戻る可能性が1%でもあるならneverは使えません。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 到達不可能なreturn */
function fail(message: string): never {
  throw new Error(message);
  // return;
}

/** Example 2: 到達可能でエラー */
function invalid(): never {
  if (Math.random() > 0.5) {
    throw new Error("Error");
  }
  // return;
}

/** Example 3: 正しい実装 */
function abort(message: string): never {
  console.error(message);
  throw new Error(message);
}
```
