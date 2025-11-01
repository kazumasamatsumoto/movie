# #800 「シンボルとオブジェクトまとめ」

四国めたん「シンボルキーでオブジェクトを拡張するテクニックをまとめましょう。」
ずんだもん「プロパティ定義、列挙制御、コピー方法を押さえたね。」
四国めたん「Object.getOwnPropertySymbolsで状態を監査できることも覚えておきましょう。」
ずんだもん「JSON.stringifyには出さずに保持できるのも強みだったよ。」
四国めたん「DIレジストリやキャッシュなど実践パターンも確認しました。」
ずんだもん「symbolを使うと衝突しない拡張ポイントを作れるんだ。」
四国めたん「次章はunique symbolの詳細です。」
ずんだもん「ここまでのテクニックをベースに進もう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 定義 */
const KEY = Symbol("meta");
const obj = { [KEY]: { role: "system" } };

/** Example 2: 列挙 */
const symbols = Object.getOwnPropertySymbols(obj);

/** Example 3: コピー */
const copy = { ...obj };
console.log(copy[KEY]);
```
