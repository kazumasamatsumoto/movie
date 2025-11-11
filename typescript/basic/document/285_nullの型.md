# #285 「nullの型」

四国めたん「nullの型について詳しく学びましょう!」
ずんだもん「let value: null = null;で純粋なnull型を定義できるんだね!」
四国めたん「はい。type NullType = nullのように型エイリアスも作れます。」
ずんだもん「typeof nullは"object"になるのが面白いのだ!」
四国めたん「それはJavaScriptの古い仕様ですね。注意が必要です。」
ずんだもん「strictNullChecksをtrueにすると、型安全性が向上するんだね!」
四国めたん「はい。string型にnullを代入するとエラーになります。」
ずんだもん「NonNullable<T>でnullを除外できるのだ!」

---

## 📺 画面表示用コード

```typescript
// null型とtypeof
let value: null = null;
type NullType = null;
typeof null; // "object" (JavaScript仕様)
```

```typescript
// strictNullChecks: true
let str: string = null;  // エラー
let str: string | null = null;  // OK
```

```typescript
// NonNullable<T>で除外
type Result = string | number | null;
type NonNull = NonNullable<Result>;
// → string | number
```
