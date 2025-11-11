# #259 「instanceof型ガード」

四国めたん「instanceof型ガードについて学びましょう!」
ずんだもん「instanceofはクラスのインスタンスを判定するんだよね!」
四国めたん「はい。DateやErrorなどの組み込みクラスやカスタムクラスに使えます。」
ずんだもん「value instanceof Dateでチェックできるの?」
四国めたん「その通りです。型が絞り込まれて、Date専用メソッドが使えます。」
ずんだもん「複数のクラスを判定することもできる?」
四国めたん「はい。UserとAdminクラスを区別するような使い方が一般的です。」
ずんだもん「クラスベースの型チェックで、より柔軟なコードが書けるのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 基本的な使用例 */
function processValue(value: Date | string) {
  if (value instanceof Date) {
    console.log(value.getFullYear());
  } else {
    console.log(value.toUpperCase());
  }
}

/** Example 2: 複数のクラス */
class User { name: string = ''; }
class Admin { role: string = ''; }

function processEntity(entity: User | Admin) {
  if (entity instanceof Admin) {
    console.log(entity.role);
  } else {
    console.log(entity.name);
  }
}
```
