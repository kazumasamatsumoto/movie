# #795 「継承」

四国めたん「symbolプロパティはプロトタイプ継承でも利用できます。」
ずんだもん「基底クラスに定義しておけば派生クラスから共有できるんだね。」
四国めたん「プロトタイプチェーンを通ってアクセスされます。」
ずんだもん「Object.getOwnPropertySymbolsは自分のプロパティだけ取るから注意だよ。」
四国めたん「Reflect.ownKeysとObject.getPrototypeOfを組み合わせて走査します。」
ずんだもん「継承構造を理解してメタデータを扱おう！」
四国めたん「シンボルを使ったAPIが上書きされにくいのも利点です。」
ずんだもん「設計で継承とシンボルを組み合わせてみよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 基底クラスで定義 */
const META = Symbol("meta");
class Base {
  protected [META] = { created: Date.now() };
  get meta() {
    return this[META];
  }
}

/** Example 2: 派生クラスから参照 */
class Service extends Base {
  print() {
    console.log(this.meta);
  }
}
new Service().print();

/** Example 3: プロトタイプを辿る */
function listAllSymbols(obj: object) {
  const symbols: symbol[] = [];
  let current: object | null = obj;
  while (current) {
    symbols.push(...Object.getOwnPropertySymbols(current));
    current = Object.getPrototypeOf(current);
  }
  return symbols;
}
console.log(listAllSymbols(Service.prototype));
```
