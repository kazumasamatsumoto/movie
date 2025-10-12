# #624 「io-tsで型とランタイム検証」

四国めたん「io-tsもunknownの検証に使える関数型スタイルのライブラリです」
ずんだもん「codecを定義してdecodeするやつだね」
四国めたん「はい。fp-tsと組み合わせるとエラー処理も型安全になります」
ずんだもん「anyからの移行で段階的に導入するのに向いてるよ」
四国めたん「型定義とランタイムチェックを同じ記述で管理できます」
ずんだもん「関数型が好きなチームにぴったりだね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: codec定義 */
import * as t from "io-ts";
const UserCodec = t.type({ id: t.number, name: t.string });

/** Example 2: decode */
const payload: unknown = JSON.parse('{ "id": 1, "name": "Mame" }');
const decoded = UserCodec.decode(payload);

/** Example 3: foldで処理 */
import { fold } from "fp-ts/Either";
fold(
  (errors) => console.error(errors),
  (user: t.TypeOf<typeof UserCodec>) => console.log(user.name)
)(decoded);
```
