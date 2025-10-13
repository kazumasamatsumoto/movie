# #796 「プライベートプロパティ模倣」

四国めたん「symbolキーは疑似プライベートプロパティとして使われてきました。」
ずんだもん「外部から文字列でアクセスできないのがポイントだね。」
四国めたん「はい、TypeScriptのprivateフィールドが使えない環境で便利でした。」
ずんだもん「現在は#フィールドがあるけど、互換性を考えるとsymbolも選択肢だよ。」
四国めたん「閉包と組み合わせてさらに秘匿性を高めることもできます。」
ずんだもん「設計要件に合わせて使い分けてね。」
四国めたん「模倣とはいえ完全な秘匿ではない点に注意が必要です。」
ずんだもん「メタデータを安全に保持するテクとして覚えておこう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 疑似プライベート */
const SECRET = Symbol("secret");
class LegacyStore {
  [SECRET] = 0;
  increment() {
    this[SECRET] += 1;
  }
  get value() {
    return this[SECRET];
  }
}

/** Example 2: 閉包との併用 */
function createCounter() {
  const state = Symbol("state");
  return class {
    privateCounter = { [state]: 0 };
    inc() {
      this.privateCounter[state]++;
    }
    current() {
      return this.privateCounter[state];
    }
  };
}

/** Example 3: 直接アクセスの難しさ */
const store = new LegacyStore();
store.increment();
console.log(Object.keys(store)); // []
```
