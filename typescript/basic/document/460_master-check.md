# #460 「マスターチェック」

四国めたん「void型の総仕上げとしてマスターチェックをしましょう。」
ずんだもん「logやsaveのような基礎を押さえる!」
四国めたん「ジェネリクスCallback<T>やAngular/Nestの実例も思い出してください。」
ずんだもん「voidパターンを全部網羅できたか振り返るんだね。」
四国めたん「副作用・ジェネリクス・フレームワーク活用を総チェックです。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 基本的な使い方 */
function log(msg: string): void {
  console.log(msg);
}
async function save(data: Data): Promise<void> {
  await database.save(data);
}

/** Example 2: ジェネリクスとの組み合わせ */
type Callback<T> = (data: T) => void;
const handler: Callback<User> = (user) => {
  console.log(user.name);
};

/** Example 3: Angular/Nest.jsでの使用 */
@Component({...})
class UserComponent {
  onClick(): void {
    this.service.save(this.user);
  }
}
```
