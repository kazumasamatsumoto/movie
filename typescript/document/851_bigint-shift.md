# #851 「シフト演算」

四国めたん「bigintは<< や >> などのシフト演算にも対応しています。」
ずんだもん「ビットを左にずらしてIDを構築する時に便利だよね。」
四国めたん「はい、符号付き右シフト>>はbigintでも利用できますが>>>は使えません。」
ずんだもん「非符号右シフトはnumber専用だから注意しよう。」
四国めたん「巨大なシフト値でも正確に処理できるのがBigIntの強みです。」
ずんだもん「シフト演算を活用してビット配置をコントロールしよう！」
四国めたん「桁数が増えるほどコストも上がるので適切に使いましょう。」
ずんだもん「BigIntで柔軟なビット操作を実現してね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 左シフト */
const shifted = 1n << 40n;

/** Example 2: 右シフト */
const restored = shifted >> 40n;

/** Example 3: ID構築 */
const nodeId = 0xFFn;
const sequence = 0x1n;
const composed = (nodeId << 12n) | sequence;
```
