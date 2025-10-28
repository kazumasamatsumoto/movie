# #797 「メタデータ」

四国めたん「シンボルキーはメタデータ格納に最適です。」
ずんだもん「他のプロパティと衝突せずに追加できるのが強みだね。」
四国めたん「デコレータやDIコンテナで広く使われています。」
ずんだもん「Reflect.metadataがなくても自前で同じ仕組みを作れるよ。」
四国めたん「型定義でメタデータの内容を明示すると安心です。」
ずんだもん「メタデータ管理の基本として覚えておこう！」
四国めたん「運用ルールを決めて安全に活用してください。」
ずんだもん「拡張性の高いアーキテクチャに役立つよ！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: メタデータキー */
const META = Symbol("controller:meta");

type ControllerMeta = { path: string; guards: string[] };

/** Example 2: デコレータ風に付与 */
function setMeta(target: object, meta: ControllerMeta) {
  Object.defineProperty(target, META, { value: meta, enumerable: false });
}

class UserController {}
setMeta(UserController.prototype, { path: "/users", guards: ["AuthGuard"] });

/** Example 3: メタデータ取得 */
function getMeta(target: object): ControllerMeta | undefined {
  return (target as Record<symbol, ControllerMeta>)[META];
}
console.log(getMeta(UserController.prototype));
```
