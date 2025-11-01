# #1082 「型定義」

四国めたん「includesの型定義もlib.d.tsで確認できます。」
ずんだん「includes(searchElement: T, fromIndex?: number): boolean ってなってるね。」
四国めたん「戻り値は常にbooleanです。」
ずんだん「第二引数で検索開始位置を指定できることも覚えておこう。」
四国めたん「型定義を理解して挙動を把握しましょう。」
ずんだん「細かな仕様も押さえてね！」

---

## 📺 画面表示用コード

```typescript
interface Array<T> {
  includes(searchElement: T, fromIndex?: number): boolean;
}

const values = [1, 2, 3];

const hasTwo = values.includes(2);
const hasTwoFromIndex = values.includes(2, 2);
```
