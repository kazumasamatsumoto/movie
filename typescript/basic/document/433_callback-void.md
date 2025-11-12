# #433 「Callback<void>」

四国めたん「Callback<void>は副作用だけのコールバック型です。」
ずんだもん「onCompleteの例では() => console.logだったね。」
四国めたん「はい。EventHandler<T = void> と組み合わせれば型安全になります。」
ずんだもん「非同期コールバックはPromise<void>を返すAsyncCallback<T>で表せる?」
四国めたん「その通り。saveCallbackが実例です。」
ずんだもん「用途に応じて同期void/非同期voidを使い分けられるんだね。」
四国めたん「シンプルな副作用APIを表現するのに最適です。」
ずんだもん「Callback<void>パターンを覚えるのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: Callback型の定義 */

type Callback<T> = (data: T) => void;
type VoidCallback = Callback<void>;
const onComplete: VoidCallback = () => {
  console.log("Complete");
};

/** Example 2: イベントハンドラ */

type EventHandler<T = void> = (event: T) => void;
const clickHandler: EventHandler<MouseEvent> = (e) => {
  console.log(e.clientX);
};

/** Example 3: 非同期コールバック */

type AsyncCallback<T> = (data: T) => Promise<void>;
const saveCallback: AsyncCallback<User> = async (user) => {
  await database.save(user);
};
```
