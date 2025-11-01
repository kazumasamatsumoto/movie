# #664 「anyはリファクタリングを難しくする」

四国めたん「anyがあるとリファクタリングの自動リネームが信用できなくなります」
ずんだもん「IDEが参照先を追跡できないから置換漏れが起きるんだよね」
四国めたん「はい。テストをしないと安心できず、コストが跳ね上がります」
ずんだもん「型を厳密にしておけば静的解析が修正をサポートしてくれるよ」
四国めたん「リファクタリング耐性を高めるためにもany排除が有効です」
ずんだもん「将来の開発速度を守るためにも型を大切にしよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: anyで追跡できない */
const service: any = legacyService();
service.executeTask();

/** Example 2: 型を付ければ追跡可能 */
interface Service {
  executeTask(): void;
}
const typed: Service = service;

/** Example 3: リファクタリングチェック */
function renameExample(service: Service) {
  service.executeTask();
}
```
