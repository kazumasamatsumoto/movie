# #689 「カスタム型定義を作る」

四国めたん「@typesが無い場合は自分たちで型定義を作りましょう」
ずんだもん「ambient d.tsを作成して最小限のシグネチャを記述するんだね」
四国めたん「はい。頻度の高いAPIから順番に型を整備します」
ずんだもん「テストで型定義の整合性もチェックしたいよ」
四国めたん「カスタム型定義はany排除のキーパーツになります」
ずんだもん「型整備を資産として育てよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: ambient d.ts */
// types/legacy-sdk.d.ts
declare module "legacy-sdk" {
  export function invoke(method: string): Promise<unknown>;
}

/** Example 2: 型テスト */
import { expectType } from "tsd";
import { invoke } from "legacy-sdk";
expectType<Promise<unknown>>(invoke("ping"));

/** Example 3: インデックス更新 */
// tsconfig.json
// "typeRoots": ["./types", "./node_modules/@types"]
```
