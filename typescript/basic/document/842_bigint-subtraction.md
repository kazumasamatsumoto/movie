# #842 「減算 - a - b」

四国めたん「bigintの減算も-演算子で簡単に行えます。」
ずんだもん「取引履歴の差分を計算するときに役立つね。」
四国めたん「符号付きで扱えるので残高との差分も安全です。」
ずんだもん「numberと混在しないように必ずbigint同士で差し引いてね。」
四国めたん「負の結果も問題なく保持できます。」
ずんだもん「減算で精度を犠牲にしないのが嬉しいよ。」
四国めたん「データ型の整合性を確保した上で差分処理に使いましょう。」
ずんだもん「bigintの減算をマスターしてね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 基本減算 */
const delta = 1000n - 750n;

/** Example 2: 残高更新 */
let balance: bigint = 5000n;
function withdraw(amount: bigint) {
  balance -= amount;
}

/** Example 3: pushする差分 */
const history: bigint[] = [];
history.push(2000n - 1999n);
```
