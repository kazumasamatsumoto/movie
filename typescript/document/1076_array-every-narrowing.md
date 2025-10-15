# #1076 「型の絞り込み」

四国めたん「everyは型述語を使うと配列全体の要素型を絞り込めます。」
ずんだもん「values.every((value): value is string => ...) のように書くんだね。」
四国めたん「はい、trueになった場合、コンパイラは配列がstring[]だと判断します。」
ずんだもん「分岐後に追加の型チェックが不要になるよ。」
四国めたん「型の絞り込みを活用して安全な後続処理を書いてください。」
ずんだもん「全要素を確認したいときに便利だね！」

---

## 📺 画面表示用コード

```typescript
const values: (string | number)[] = ["ok", "ng"];

if (values.every((value): value is string => typeof value === "string")) {
  values.map((value) => value.toUpperCase());
}
```
