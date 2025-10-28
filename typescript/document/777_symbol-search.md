# #777 「Symbol.search」

四国めたん「Symbol.searchはString.prototype.searchを置き換えるフックです。」
ずんだもん「独自の検索アルゴリズムを注入できるんだね。」
四国めたん「(text) => numberの関数を実装します。」
ずんだもん「見つからなければ-1を返すのが契約だよ。」
四国めたん「複雑なパターンマッチや全角半角対応に活用できます。」
ずんだもん「検索条件をTypeScriptで型安全に表現しよう！」
四国めたん「Symbol.searchを使えば柔軟な探索ロジックが書けます。」
ずんだもん「文字列処理の拡張ポイントとして覚えておこう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: カスタムsearch */
const kanaSearch = {
  keyword: "ﾀｲﾌﾟ",
  [Symbol.search](text: string): number {
    const normalized = text.normalize("NFKC");
    return normalized.indexOf(this.keyword.normalize("NFKC"));
  },
};

/** Example 2: 使用例 */
console.log("TypeScript".search(kanaSearch)); // 0
console.log("Java".search(kanaSearch)); // -1

/** Example 3: ラッパー関数 */
function includesKeyword(text: string) {
  return text.search(kanaSearch) !== -1;
}
console.log(includesKeyword("タイプガード"));
```
