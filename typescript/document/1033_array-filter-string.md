# #1033 「(string | number)[]からstring[]」

四国めたん「(string | number)[]からstring[]に絞り込む例を見ましょう。」
ずんだもん「型述語filterで文字列だけ取り出すんだね。」
四国めたん「はい、typeof value === "string" を述語にすればstring[]に変わります。」
ずんだもん「その後はstring専用の処理を安心して書けるよ。」
四国めたん「パターンを覚えて色んなUnion配列に応用してください。」
ずんだもん「型安全に文字列だけ抽出しよう！」

---

## 📺 画面表示用コード

```typescript
const tokens: (string | number)[] = ["start", 200, "end"];

/** Example 1: filterで抽出 */ 
const strings = tokens.filter((token): token is string => typeof token === "string");

/** Example 2: mapチェーン */
const upper = strings.map((token) => token.toUpperCase());

/** Example 3: join */
const joined = strings.join(",");
```
