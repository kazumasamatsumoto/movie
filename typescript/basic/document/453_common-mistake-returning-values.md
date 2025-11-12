# #453 「間違い(3) - return値」

四国めたん「void関数で値をreturnするのはエラーになります。」
ずんだもん「processでfalseを返した例がまさにそれ!」
四国めたん「値を返したいなら戻り値型をbooleanなどに変えましょう。」
ずんだもん「voidのままにしたいときはreturn;だけ使えばいいんだね。」
四国めたん「副作用関数は早期リターンでも値を返さないこと。」
ずんだもん「returnスタイルを正しく選ぶのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 間違い: 値を返す */
function process(data: string): void {
  if (!data) {
    return false;
  }
  console.log(data);
}

/** Example 2: 戻り値型を変更 */
function process(data: string): boolean {
  if (!data) {
    return false;
  }
  console.log(data);
  return true;
}

/** Example 3: voidで早期リターン */
function process(data: string): void {
  if (!data) return;
  console.log(data);
}
```
