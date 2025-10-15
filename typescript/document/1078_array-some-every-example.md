# #1078 「実践例」

四国めたん「実践例として、フォーム入力のチェックにsome/everyを使ってみましょう。」
ずんだもん「必須項目が空ならsome、全項目が有効かどうかはeveryで確認できるね。」
四国めたん「はい、短絡評価を活かして効率的にチェックします。」
ずんだん「バリデーションコードが読みやすくなるよ。」
四国めたん「実例を参考にバリデーション処理を組み立ててください。」
ずんだん「ユーザー入力を安全に扱おう！」

---

## 📺 画面表示用コード

```typescript
interface Field {
  name: string;
  value: string;
  required: boolean;
}

const fields: Field[] = [
  { name: "email", value: "", required: true },
  { name: "name", value: "meta", required: true },
];

const hasEmptyRequired = fields.some((field) => field.required && field.value.trim() === "");

const allFilled = fields.every((field) => !field.required || field.value.trim() !== "");
```
