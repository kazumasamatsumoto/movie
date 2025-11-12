# #397 「インターフェースのメソッド」

四国めたん「インターフェースでもvoidメソッドを定義します。」
ずんだもん「Lifecycle.init/destroyは典型だね。」
四国めたん「実装クラスComponentがそれを満たしています。」
ずんだもん「イベント系のインターフェースでもvoidばかり?」
四国めたん「handleClickやhandleKeyPressなど、戻り値を使いません。」
ずんだもん「契約として副作用のみを許可しているんだ。」
四国めたん「その通り。インターフェースで明示すると安心です。」
ずんだもん「voidメソッドで契約内容をはっきりさせるのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: インターフェース */
interface Lifecycle {
  init(): void;
  destroy(): void;
}

/** Example 2: 実装クラス */
class Component implements Lifecycle {
  init(): void {
    console.log("Initialized");
  }

  destroy(): void {
    console.log("Destroyed");
  }
}

/** Example 3: イベントリスナーのインターフェース */
interface EventListener {
  handleClick(event: MouseEvent): void;
  handleKeyPress(event: KeyboardEvent): void;
}
```
