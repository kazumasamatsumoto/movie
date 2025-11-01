# #762 「注意点」

四国めたん「Symbol.forで生成した値はレジストリから解放できません。」
ずんだもん「だからユーザー入力をそのままキーにしない方がいいんだね。」
四国めたん「命名衝突も注意点です。第三者とキーが被ると意図せず共有されます。」
ずんだもん「名前空間とドキュメント化で防ぎたいところだよ。」
四国めたん「また、テストでレジストリ状態が共有される点にも気をつけてください。」
ずんだもん「テスト前後でSymbol.keyForを使って検証すると安心だね。」
四国めたん「注意点を押さえて安全に活用しましょう。」
ずんだもん「シンボルのライフサイクル管理を忘れずに！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: ユーザー入力をフィルタ */
function createPublicKey(raw: string) {
  if (!/^[\w:-]+$/.test(raw)) {
    throw new Error("invalid key");
  }
  return Symbol.for(`app:${raw}`);
}

/** Example 2: テスト時のクリーンアップ確認 */
const before = Symbol.keyFor(Symbol.for("test:key"));
// ...テスト...
const after = Symbol.keyFor(Symbol.for("test:key"));
console.log(before === after); // true (レジストリは持続)

/** Example 3: 衝突チェック */
function assertUnique(key: string) {
  if (Symbol.keyFor(Symbol.for(key))) {
    console.warn(`key '${key}' is already used`);
  }
}
assertUnique("shared:name");
```
