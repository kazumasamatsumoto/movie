# #458 "Documentation"

Shikoku Metan: "Document void functions to clarify intent."
Zundamon: "We included @returns void and side-effect descriptions."
Shikoku Metan: "Add @throws and @example to guide users."
Zundamon: "Since no value is returned, the comments explain the effects."

---

## 📺 Code for Display

```typescript
/** Example 1: Doc comment */
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

/** Example 2: Explain side effects */
/**
 * カウンターをインクリメントします
 * 副作用: グローバル変数 counter を +1 します
 */
function increment(): void {
  counter++;
}

/** Example 3: Example */
/**
 * イベントリスナーを登録します
 * @example addEventListener('click', () => console.log('Clicked'));
 */
function addEventListener(event: string, handler: () => void): void {
  listeners.push({ event, handler });
}
```
