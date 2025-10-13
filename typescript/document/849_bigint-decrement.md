# #849 「デクリメント」

四国めたん「bigintは--演算子でデクリメントできます。」
ずんだもん「インクリメントと同じく前置・後置が使えるんだね。」
四国めたん「はい、減算が多いカウンタや残タスク数の管理に便利です。」
ずんだもん「0nを下回っても精度を保てるのが強いよ。」
四国めたん「必要に応じて下限チェックを行いましょう。」
ずんだもん「--演算子でBigIntの減少を安全に扱ってね！」
四国めたん「numberとの混在は避けることを忘れずに。」
ずんだもん「デクリメントで精度を守ろう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 後置-- */
let value = 5n;
const prev = value--;

/** Example 2: 前置-- */
const now = --value;

/** Example 3: 下限チェック */
function decrementWithFloor(target: bigint, floor: bigint): bigint {
  return target > floor ? target - 1n : floor;
}
```
