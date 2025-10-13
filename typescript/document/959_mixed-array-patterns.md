# #959 「パターン集」

四国めたん「混合型配列の代表的なパターンを整理しましょう。」
ずんだもん「ログストリーム、APIレスポンス、イベントキューなどがあったね。」
四国めたん「はい、型ガードとユーティリティを組み合わせると再利用性が高まります。」
ずんだもん「パターンを集めてテンプレート化しておこう。」
四国めたん「プロジェクトのドメインに合わせて必要なものを選んでください。」
ずんだもん「混合型配列パターンを引き出しに入れておこう！」

---

## 📺 画面表示用コード

```typescript
/** Pattern 1: ログ */
type LogToken = string | number;
const logTokens: LogToken[] = [];

/** Pattern 2: API結果 */
type ApiToken = { kind: "success"; data: string } | { kind: "error"; message: string };
const apiQueue: ApiToken[] = [];

/** Pattern 3: イベント */
interface MessageEvent { type: "message"; payload: string }
interface TimeoutEvent { type: "timeout"; timeout: number }
const events: (MessageEvent | TimeoutEvent)[] = [];
```
