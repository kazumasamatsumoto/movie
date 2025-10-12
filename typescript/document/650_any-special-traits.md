# #650 「any型の特殊な性質」

四国めたん「anyは他の型にない特殊な性質を持っています」
ずんだもん「true | false | 0 みたいに広がるんじゃなくて、全てを吸収するんだよね」
四国めたん「はい。型演算でもanyが混ざると結果がanyになりやすいのも特徴です」
ずんだもん「条件付き型でもanyが現れると分配が止まるよ」
四国めたん「ジェネリクスの安全性を壊す性質だと認識しましょう」
ずんだもん「特殊な性質だからこそ取り扱い注意だね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: Unionとの合成 */
type Mixed = string | any; // any

/** Example 2: 条件付き型 */
type Condition<T> = T extends number ? "num" : "other";
type Result = Condition<any>; // any

/** Example 3: 配列操作 */
const list: any[] = [1, "two"];
const mapped = list.map((item) => item.trim?.()); // map結果もany
```
