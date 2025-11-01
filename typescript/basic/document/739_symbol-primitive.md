# #739 「プリミティブ型」

四国めたん「Symbolは文字列や数値と同じプリミティブ型です。」
ずんだもん「typeofで"symbol"が返るのが証拠だよね。」
四国めたん「プリミティブなのでミュータブルな状態を持ちません。」
ずんだもん「Box化すればオブジェクトになりますが基本は値として扱うんだ。」
四国めたん「オブジェクトラッパーは滅多に使いません。」
ずんだもん「プリミティブなら比較やMapキーも軽量だね。」
四国めたん「TypeScriptの型体系でも基本型として扱われます。」
ずんだもん「プリミティブ特性を理解しておこう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: typeof は "symbol" */
const sid = Symbol("id");
console.log(typeof sid); // "symbol"

/** Example 2: Box化した場合 */
const boxed = Object(sid);
console.log(typeof boxed); // "object": ラッパーオブジェクト
console.log(boxed.valueOf() === sid); // true: 元のプリミティブを保持

/** Example 3: プリミティブとして扱う */
const registry = new Map<symbol, string>();
registry.set(sid, "resource");
console.log(registry.get(sid));
```
