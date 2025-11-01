# #942 「分割代入の型推論」

四国めたん「分割代入でもTypeScriptは要素ごとの型を推論します。」
ずんだもん「const [id, name] = user; ならidとnameに適切な型が入るんだね。」
四国めたん「配列がタプルならリテラル型まで推論されます。」
ずんだもん「Union配列の場合は要素型がそのまま割り当てられるよ。」
四国めたん「推論を活かして型注釈を省略できる場面が多いです。」
ずんだもん「分割代入の推論を理解してね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: タプル */
const tuple = ["id", 42] as const;
const [key, value] = tuple; // key: "id", value: 42

/** Example 2: オブジェクト配列 */
const user: [string, number] = ["meta", 5];
const [name, level] = user; // name: string, level: number

/** Example 3: Union配列 */
const mixed: (string | number)[] = ["ok", 0];
const [firstMixed] = mixed; // string | number
```
