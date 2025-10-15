# #1086 「型の絞り込み制限」

四国めたん「includesは型の絞り込みには使えない点に注意しましょう。」
ずんだん「(string | number)[]に"value"が含まれていても要素型は変わらないんだね。」
四国めたん「はい、結果はbooleanであり、配列の型は変わりません。」
ずんだん「絞り込みたい場合はfilterや型ガードを使おう。」
四国めたん「型システムの挙動を理解して正しいメソッドを選択してください。」
ずんだん「booleanだけ得たいときに使おうね！」

---

## 📺 画面表示用コード

```typescript
const values: (string | number)[] = ["meta", 200];

const hasMeta = values.includes("meta"); // boolean

// valuesの型は依然として (string | number)[]
```
