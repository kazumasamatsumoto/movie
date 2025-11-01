# #1058 「型述語」

四国めたん「findにも型述語シグネチャがあります。」
ずんだもん「(value: T) => value is U を返すと戻り値がU | undefinedになるんだね。」
四国めたん「Unionから特定の型を探したいときに有効です。」
ずんだもん「filterと同様に型述語を覚えておこう。」
四国めたん「型述語を使ってfindの戻り値型をコントロールしてください。」
ずんだもん「絞り込みがより安全になるよ！」

---

## 📺 画面表示用コード

```typescript
const tokens: (string | number)[] = ["ok", 200];

const isString = (value: string | number): value is string => typeof value === "string";

const maybeString = tokens.find(isString);

if (maybeString !== undefined) {
  console.log(maybeString.toUpperCase());
}
```
