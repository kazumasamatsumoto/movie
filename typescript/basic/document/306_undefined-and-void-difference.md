# #306 「undefinedとvoidの違い」

四国めたん「undefinedとvoidの違いについて学びましょう!」
ずんだもん「void型は戻り値を使わないことを示す型なんだね!」
四国めたん「はい。undefined型は明示的にundefinedを返す場合に使います。」
ずんだもん「voidを返す関数でも、実際にはundefinedが返されるんだよね?」
四国めたん「その通りです。voidは型レベルで戻り値を使わないという意図を示します。」
ずんだもん「undefined型はユニオン型で使って、値が存在しないケースを表現できるね!」
四国めたん「関数の戻り値で区別することで、コードの意図が明確になります。」
ずんだもん「voidは副作用のための関数、undefined型は値を返す可能性がある関数なのだ!」

---


```typescript
/** Example 1: void型 - 戻り値を使わない */
function log(msg: string): void {
  console.log(msg);
}
log("Hello"); // 戻り値は使えない

/** Example 2: undefined型 - 明示的にundefined */
function find(): User | undefined {
  return undefined;
}
const user = find(); // undefined

/** Example 3: voidはundefinedを返す */
function noReturn(): void { }
const result = noReturn(); // undefined (型はvoid)
```
