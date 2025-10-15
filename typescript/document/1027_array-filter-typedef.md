# #1027 「型定義」

四国めたん「filterの型定義もlib.d.tsで確認できます。」
ずんだもん「filter(callback: (value: T, index: number, array: T[]) => unknown, thisArg?: any): T[] ってなってるね。」
四国めたん「はい、戻り値の配列型は元の要素型Tがそのまま使われます。」
ずんだもん「型述語オーバーロードも用意されているよ。」
四国めたん「型定義を理解して挙動を把握しましょう。」
ずんだもん「libファイルは良い教科書だね！」

---

## 📺 画面表示用コード

```typescript
interface Array<T> {
  filter(predicate: (value: T, index: number, array: T[]) => unknown, thisArg?: any): T[];
  filter<S extends T>(predicate: (value: T, index: number, array: T[]) => value is S, thisArg?: any): S[];
}

const values = [1, 2, 3];
const even = values.filter((value) => value % 2 === 0);

type EvenType = typeof even; // number[]
```
