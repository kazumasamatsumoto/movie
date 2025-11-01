# #754 「グローバルシンボルの一意性」

四国めたん「Symbol.forの値はキーごとに一意ですが、同一キーなら共有されます。」
ずんだもん「つまりグローバルレジストリで重複しないよう管理されてるんだね。」
四国めたん「同じ文字列キーが2度登録されることはありません。」
ずんだもん「モジュールを跨いでも同じシンボルが取れるから安心だよ。」
四国めたん「キーを変えれば別のシンボルとして共存できます。」
ずんだもん「命名規約で衝突を防げば一意性が担保されるね。」
四国めたん「グローバルシンボルは共有の仕組みを理解して使いましょう。」
ずんだもん「チーム全体でルールを決めて運用しよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 同じキーは共有 */
const first = Symbol.for("feature");
const second = Symbol.for("feature");
console.log(first === second); // true

/** Example 2: 別キーは独立 */
const other = Symbol.for("feature:v2");
console.log(first === other); // false

/** Example 3: グローバルオブジェクトを介した共有 */
const KEY = Symbol.for("app:config");
(globalThis as any)[KEY] = { locale: "ja-JP" };
console.log((globalThis as any)[KEY]);
```
