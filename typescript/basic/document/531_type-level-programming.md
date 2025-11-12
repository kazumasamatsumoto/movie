# #531 「型レベルプログラミング」

四国めたん「型レベルプログラミングはTypeScriptの真骨頂だよ。」
ずんだもん「If型は真偽値でTrue/Falseの型を切り替えてたね。」
四国めたん「Reverse<T>は配列を再帰展開して逆順を作ってた。」
ずんだもん「型レベル再帰で[1,2,3,4]が[4,3,2,1]になってたのだ。」
四国めたん「FilterNever<T>はnever要素だけを除去して配列をクリーンにする。」
ずんだもん「stringとnumberだけ残って読みやすい型になった。」
四国めたん「こういうパターンを組み合わせれば高度な型演算も怖くない。」
ずんだもん「ロジックを型に落とし込んでバグを未然に防ごう。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 型レベルif */
type If<Cond extends boolean, True, False> =
  Cond extends true ? True : False;

type A = If<true, string, number>;  // string
type B = If<false, string, number>; // number
```

```typescript
/** Example 2: 型レベル再帰でReverse */
type Reverse<T extends any[]> =
  T extends [infer First, ...infer Rest]
    ? [...Reverse<Rest>, First]
    : [];

type Result = Reverse<[1, 2, 3, 4]>; // [4, 3, 2, 1]
```

```typescript
/** Example 3: neverを除去 */
type FilterNever<T extends any[]> =
  T extends [infer First, ...infer Rest]
    ? First extends never
      ? FilterNever<Rest>
      : [First, ...FilterNever<Rest>]
    : [];

type Clean = FilterNever<[string, never, number, never]>; // [string, number]
```
