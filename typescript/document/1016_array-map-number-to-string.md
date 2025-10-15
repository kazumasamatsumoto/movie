# #1016 「number[]からstring[]」

四国めたん「mapを使えばnumber[]を簡単にstring[]へ変換できます。」
ずんだもん「toStringやテンプレートリテラルを使うだけでOKだね。」
四国めたん「はい、戻り値がstringなので結果の配列型もstring[]になります。」
ずんだもん「IDの文字列化や表示用データに便利だよ。」
四国めたん「具体例で操作感を確認しましょう。」
ずんだもん「型変換の基本テクだね！」

---

## 📺 画面表示用コード

```typescript
const numbers = [101, 202, 303];

/** Example 1: toString */
const asStrings = numbers.map((value) => value.toString());

/** Example 2: テンプレート */
const tagged = numbers.map((value) => `ID-${value}`);

/** Example 3: ロケールフォーマット */
const locale = numbers.map((value) => value.toLocaleString("ja-JP"));
```
