# #554 「unknown型の宣言」

四国めたん「unknownは明示的に型注釈することで安全性が始まります」
ずんだもん「let value: unknownみたいに宣言するんだよね」
四国めたん「はい。関数の戻り値や引数にもunknownを使えます」
ずんだもん「ジェネリクスの型パラメータにも設定できて便利だよ」
四国めたん「宣言段階で未知性を表現するのが目的です」
ずんだもん「後で型ガードする前提がチームの約束になるね」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 変数宣言 */
let payload: unknown;
payload = localStorage.getItem("cache");
payload = JSON.parse("{}");

/** Example 2: 関数シグネチャ */
function parse(value: string): unknown {
  return JSON.parse(value);
}

/** Example 3: ジェネリクスでunknown */
function identity<T = unknown>(value: T): T {
  return value;
}
```
