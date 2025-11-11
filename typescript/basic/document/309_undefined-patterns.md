# #309 「undefinedのパターン」

四国めたん「undefinedを使った実践的なパターンについて学びましょう!」
ずんだもん「Option型パターンで、値が存在しない可能性を型で表現できるんだね!」
四国めたん「はい。T | undefined というユニオン型で安全な値の扱いが可能です。」
ずんだもん「デフォルト値パターンは、Null合体演算子??で簡潔に書けるよね?」
四国めたん「その通りです。undefined時のフォールバック値を設定できます。」
ずんだもん「Partial型パターンで、全プロパティをオプショナルにできるのが便利だね!」
四国めたん「これらのパターンを使うと、エラーハンドリングが型安全になります。」
ずんだもん「Option型やPartial型で、undefinedを効果的に活用できるのだ!」

---


```typescript
/** Example 1: Option型パターン */
type Option<T> = T | undefined;
function divide(a: number, b: number): Option<number> {
  return b !== 0 ? a / b : undefined;
}

/** Example 2: デフォルト値パターン */
function greet(name?: string): void {
  const displayName = name ?? "Guest";
  console.log(`Hello, ${displayName}`);
}

/** Example 3: Partial型パターン */
interface User {
  name: string;
  age: number;
}
type PartialUser = Partial<User>;
// { name?: string; age?: number }
```
