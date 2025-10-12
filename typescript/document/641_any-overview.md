# #641 「any型とは？」

四国めたん「any型はTypeScriptで最も自由度が高いトップレベル型です」
ずんだもん「型チェックを完全に無効化して、JavaScriptの動きそのままだね」
四国めたん「はい。代入も利用も制約が無い代わりに安全性が失われます」
ずんだもん「プロトタイプ段階では便利だけど乱用は禁物だよ」
四国めたん「anyの性質を理解して適切に扱いましょう」
ずんだもん「次のステップでリスクも見ていこう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: any宣言 */
let value: any = "text";
value = 123;
value(); // runtimeまで検査されない

/** Example 2: 関数のany */
function passThrough(input: any) {
  return input;
}

/** Example 3: 代入先も自由 */
const num: number = value;
```
