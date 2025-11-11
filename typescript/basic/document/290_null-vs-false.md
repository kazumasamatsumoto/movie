# #290 「nullとfalseの違い」

四国めたん「今日はnullとfalseの違いについて学びましょう！」
ずんだもん「nullはnull型、falseはboolean型で、完全に別の型なんだね。」
四国めたん「厳密等価演算子で比較すると、常にfalseになります。」
ずんだもん「Nullish Coalescingでの扱いも異なるよ。」
四国めたん「nullは空値を表し、falseは論理値の偽を表します。」
ずんだもん「型システムを理解して、正しく使い分けよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 型の違い */
let a: null = null;     // null型
let b: boolean = false; // boolean型
null === false;  // false
```

```typescript
/** Example 2: Nullish Coalescingの動作 */
const v1 = null ?? "default";  // "default"
const v2 = false ?? "default"; // false
```

```typescript
/** Example 3: 型安全性 */
let flag: boolean = null;  // エラー
let flag: boolean | null = null;  // OK
```
