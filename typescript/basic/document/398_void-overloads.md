# #398 「オーバーロード」

四国めたん「オーバーロードではシグネチャごとに戻り値を分けられます。」
ずんだもん「processはstringならstring、numberならvoidなんだね。」
四国めたん「はい。実装ではstring | voidを返しています。」
ずんだもん「logのように引数パターンが増えても全部voidで揃えられる?」
四国めたん「はい。メッセージの出し分けだけならvoidで十分です。」
ずんだもん「forEachのオーバーロード例もstart引数の有無だけが違うんだね。」
四国めたん「どちらもvoidなので返り値の扱いが簡単です。」
ずんだもん「シグネチャ設計でvoidをうまく使うのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: オーバーロードでvoid */
function process(data: string): string;
function process(data: number): void;
function process(data: string | number): string | void {
  if (typeof data === "string") return data.toUpperCase();
  console.log(data);
}

/** Example 2: 実用例 */
function log(message: string): void;
function log(level: string, message: string): void;
function log(levelOrMsg: string, message?: string): void {
  if (message) {
    console.log(`[${levelOrMsg}] ${message}`);
  } else {
    console.log(levelOrMsg);
  }
}

/** Example 3: コールバックのオーバーロード */
function forEach(callback: (item: number) => void): void;
function forEach(start: number, callback: (item: number) => void): void;
function forEach(startOrCb: any, callback?: any): void {
  // 実装
}
```
