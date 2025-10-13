# #995 「ループまとめ」

四国めたん「配列ループの要点をまとめましょう。」
ずんだもん「for、for...of、forEach、map/filter/reduce、それぞれの型挙動を学んだね。」
四国めたん「はい、型ガードやNullish Coalescingで安全性も確保できました。」
ずんだもん「状況に応じて最適なループを選ぶことが大事だよ。」
四国めたん「次のチャプターでも型推論を意識しながら進みましょう。」
ずんだもん「これで配列ループはばっちりだね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: for...of */
for (const item of items) {
  console.log(item);
}

/** Example 2: map */
const transformed = items.map((item) => transform(item));

/** Example 3: reduce */
const aggregated = items.reduce((acc, item) => merge(acc, item), initialValue);
```
