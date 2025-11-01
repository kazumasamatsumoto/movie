# #827 「bigint型の宣言」

四国めたん「bigint型は型注釈で明示できます。」
ずんだもん「let amount: bigint = 0n; みたいに書けばいいんだね。」
四国めたん「constでもletでも型注釈が可能です。」
ずんだもん「オプショナルなプロパティにもbigintを指定できるよ。」
四国めたん「TypeScriptはbigintリテラルの型を自動推論しますが、共有する変数には注釈すると安心です。」
ずんだもん「宣言スタイルを押さえてbigintを使いこなそう！」
四国めたん「型宣言でエコシステムとの連携がスムーズになります。」
ずんだもん「型付きbigintで安全性アップだね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: let宣言 */
let amount: bigint = 0n;
amount += 500n;

/** Example 2: プロパティ宣言 */
interface LedgerEntry {
  id: bigint;
  payload?: string;
}

/** Example 3: クラスフィールド */
class Counter {
  value: bigint = 0n;
}
```
