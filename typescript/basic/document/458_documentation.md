# #458 「ドキュメント」

四国めたん「void関数もドキュメントコメントで意図を明示しましょう。」
ずんだもん「@returns void や副作用の説明が入っていた!」
四国めたん「throws、exampleなどを活用すると読み手が安心します。」
ずんだもん「void関数だからこそコメントで副作用や例外を説明するんだね。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: ドキュメントコメント */
/**
 * ユーザーをデータベースに保存します
 * @param user 保存するユーザー
 * @returns void
 * @throws {ValidationError}
 */
function saveUser(user: User): void {
  validateUser(user);
  database.save(user);
}

/** Example 2: 副作用の説明 */
/**
 * カウンターをインクリメントします
 * 副作用: グローバル変数 counter を +1 します
 */
function increment(): void {
  counter++;
}

/** Example 3: 例と注釈 */
/**
 * イベントリスナーを登録します
 * @example addEventListener('click', () => console.log('Clicked'));
 */
function addEventListener(event: string, handler: () => void): void {
  listeners.push({ event, handler });
}
```
