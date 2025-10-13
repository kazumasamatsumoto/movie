# #807 「実践例」

四国めたん「unique symbolを使ったサービスリゾルバの実例を見ましょう。」
ずんだもん「トークンと実装をMapで紐付けるやつだね。」
四国めたん「はい、トークンはconstアサーションでまとめます。」
ずんだもん「resolve関数でtypeof TOKENを受け取れば安全に取得できるよ。」
四国めたん「登録漏れを防ぐためにMapの型注釈もunique symbolベースにします。」
ずんだもん「実践例を参考に独自コンテナを作ってみよう！」
四国めたん「unique symbolが型安全なDIを支えてくれます。」
ずんだもん「コードで動きを確認してね！」

---

## 📺 画面表示用コード

```typescript
/** Token集 */
const TOKENS = {
  LOGGER: Symbol("LOGGER"),
  STORAGE: Symbol("STORAGE"),
} as const;

type Token = typeof TOKENS[keyof typeof TOKENS];

type Registry = {
  [TOKENS.LOGGER]: Console;
  [TOKENS.STORAGE]: { save: (data: unknown) => void };
};

const container = new Map<Token, Registry[keyof Registry]>([
  [TOKENS.LOGGER, console],
  [TOKENS.STORAGE, { save: (data) => console.log("save", data) }],
]);

function resolve<K extends keyof Registry>(token: K): Registry[K] {
  return container.get(TOKENS[token]) as Registry[K];
}
console.log(resolve("LOGGER").log("unique"));
```
