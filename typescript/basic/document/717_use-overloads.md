# #717 「オーバーロードの活用」

四国めたん「関数の振る舞いが入力によって変わるならオーバーロードでanyを避けましょう」
ずんだもん「シグネチャを複数書いて呼び出し側に型を提示できるんだよね」
四国めたん「はい。実装は1つで、オーバーロード定義は型の契約として機能します」
ずんだもん「複雑な条件をUnionで書きづらいときに便利だよ」
四国めたん「オーバーロードで意図を明確にすればany不要になります」
ずんだもん「使い分けを丁寧に表現しよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: オーバーロード定義 */
function format(value: string): string;
function format(value: number): string;
function format(value: Date): string;

/** Example 2: 実装 */
function format(value: string | number | Date): string {
  if (value instanceof Date) return value.toISOString();
  return value.toString();
}

/** Example 3: 利用 */
format("hello");
format(123);
format(new Date());
```
