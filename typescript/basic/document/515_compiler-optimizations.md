# #515 「コンパイラ最適化」

四国めたん「neverチェックは最適化のヒントにもなるよ。」
ずんだもん「DigitのisEven()は10個すべてをswitchでさばいてたね。」
四国めたん「defaultでconst check: never = n; と書けば到達不能を示せる。」
ずんだもん「Priorityをifで見るgetScore()でも同じくデッドコードが削除できるのだ。」
四国めたん「Boolのnot()はtrue/falseを返した後にthrowを置いてインライン化を促してた。」
ずんだもん「never扱いになるから余計なreturnを減らせるんだね。」
四国めたん「コンパイラに『ここには来ない』と伝えると性能も上がる。」
ずんだもん「型安全と最適化が両立するのは嬉しいポイントだよ。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: Digitの偶数判定 */
type Digit = 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9;

function isEven(n: Digit): boolean {
  switch (n) {
    case 0:
    case 2:
    case 4:
    case 6:
    case 8:
      return true;
    case 1:
    case 3:
    case 5:
    case 7:
    case 9:
      return false;
    default:
      const check: never = n;
      return false;
  }
}

/** Example 2: 優先度のスコア */
type Priority = "high" | "medium" | "low";

function getScore(p: Priority): number {
  if (p === "high") return 3;
  if (p === "medium") return 2;
  if (p === "low") return 1;
  const check: never = p;
  return 0;
}

/** Example 3: Boolの反転 */
type Bool = true | false;

function not(b: Bool): boolean {
  if (b === true) return false;
  if (b === false) return true;
  const check: never = b;
  throw new Error(`Invalid: ${check}`);
}
```
