# #665 「anyはIDEサポートを失わせる」

四国めたん「anyがあるとIDEの補完やリファクタリング支援が効かなくなります」
ずんだもん「型情報が無いからヒントも出ないし、誤字にも気づけないんだよね」
四国めたん「はい。開発体験が大きく低下してミスが増えます」
ずんだもん「unknownや具体的な型を付ければ強力な補完が戻ってくるよ」
四国めたん「IDEと協調するためにもanyを減らしましょう」
ずんだもん「快適な開発環境を維持したいね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: anyで補完無し */
const client: any = createClient();
client. // 補完が空

/** Example 2: 型あり補完 */
interface Client {
  connect(): Promise<void>;
  disconnect(): void;
}
const typedClient: Client = createClient();
typedClient.connect().then(() => typedClient.disconnect());

/** Example 3: unknownで段階的補完 */
const unknownClient: unknown = createClient();
if (typeof unknownClient === "object" && unknownClient !== null && "connect" in unknownClient) {
  console.log("has connect method");
}
```
