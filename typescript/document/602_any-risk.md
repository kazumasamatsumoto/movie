# #602 「any型の危険性」

四国めたん「any型を多用すると静的保証が崩壊します」
ずんだもん「実行時にしかエラーがわからなくなるんだよね」
四国めたん「はい。IDEの補完も効かなくなり、タイプミスに気づけません」
ずんだもん「レビューでも意図しないバグを見逃しやすいよ」
四国めたん「安全性を重視する開発では最小限に抑えるべき型です」
ずんだもん「危険性を理解してunknownや具体的な型に切り替えよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 実行時エラー */
const user: any = {};
user.profile.name.toUpperCase(); // runtimeで落ちる

/** Example 2: 補完喪失 */
function greet(value: any) {
  value.toFix(); // typoでも通る
}

/** Example 3: 伝播リスク */
const payload: any = JSON.parse("null");
const dto: { id: number } = payload; // 型破壊
```
