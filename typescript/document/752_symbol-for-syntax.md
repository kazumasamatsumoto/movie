# #752 「構文」

四国めたん「Symbol.forの構文はシンプルで、文字列キーを渡すだけです。」
ずんだもん「Symbol.for("key")って書くだけで共有シンボルが手に入るんだね。」
四国めたん「第二引数などは存在せず、常に文字列一つです。」
ずんだもん「キーは大文字スネークケースなど規約を決めるとよさそうだよ。」
四国めたん「テンプレート文字列で名前空間を表現する手もあります。」
ずんだもん「構文を理解して読みやすいキーを定義しよう！」
四国めたん「簡潔なAPIだからこそ命名が重要です。」
ずんだもん「プロジェクト全体で統一しようね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 基本構文 */
const TOKEN = Symbol.for("APP_TOKEN");

/** Example 2: 名前空間付き */
const namespaced = Symbol.for(`app.module:${"UserService"}`);

/** Example 3: 補助関数 */
const createKey = (domain: string, name: string) => Symbol.for(`${domain}:${name}`);
const repositoryKey = createKey("repo", "User");
```
