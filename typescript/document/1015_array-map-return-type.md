# #1015 「戻り値型 - 型変換」

四国めたん「mapの戻り値型はコールバックの戻り値型に依存します。」
ずんだもん「stringを返せばstring[]、オブジェクトならオブジェクト配列になるんだね。」
四国めたん「はい、型変換の自由度が高いメソッドです。」
ずんだんどん「誤った型を返すときは型注釈でエラーを拾えるよ。」
四国めたん「戻り値型を意識して変換ロジックを書きましょう。」
ずんだもん「型変換を楽しんでね！」

---

## 📺 画面表示用コード

```typescript
const values = [1, 2, 3];

/** Example 1: string[] */
const stringValues = values.map((value) => value.toString());

/** Example 2: オブジェクト配列 */
const wrapped = values.map((value) => ({ value, doubled: value * 2 }));

/** Example 3: 型注釈 */
const fixed = values.map<number>((value) => value * 1.5);
```
