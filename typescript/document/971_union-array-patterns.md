# #971 「パターン」

四国めたん「配列とUnion型の組み合わせでよく使うパターンを整理します。」
ずんだもん「混在配列、排他的配列、配列と単体値のUnionなどがあったね。」
四国めたん「はい、それぞれに対応する型ガードやユーティリティを用意すると便利です。」
ずんだもん「パターン化しておけば新しいケースでも素早く対応できるよ。」
四国めたん「ドメインに合わせて必要なものをテンプレート化しましょう。」
ずんだもん「Union配列のパターンを蓄積してね！」

---

## 📺 画面表示用コード

```typescript
/** Pattern 1: 混在配列 */
type Mixed = (string | number)[];

/** Pattern 2: 排他的配列 */
type Exclusive = string[] | number[];

/** Pattern 3: 単体 or 配列 */
type SingleOrMany<T> = T | T[];
function ensureArray<T>(value: SingleOrMany<T>): T[] {
  return Array.isArray(value) ? value : [value];
}
```
