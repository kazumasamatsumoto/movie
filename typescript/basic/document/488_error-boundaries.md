# #488 「エラーバウンダリ」

四国めたん「never関数を呼ぶ処理の外側ではバウンダリも用意しましょう。」
ずんだもん「safeExecuteがthrowをcatchしてfallbackを返してたね。」
四国めたん「非同期版のsafeAsyncも紹介しました。」
ずんだもん「ReactのErrorBoundaryもcomponentDidCatchでログを出すんだ!」
四国めたん「バウンダリで例外を閉じ込めればアプリ全体が落ちにくくなります。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 同期バウンダリ */
function safeExecute<T>(fn: () => T, fallback: T): T {
  try {
    return fn();
  } catch (error) {
    console.error("Error caught:", error);
    return fallback;
  }
}

/** Example 2: 非同期バウンダリ */
async function safeAsync<T>(fn: () => Promise<T>, fallback: T): Promise<T> {
  try {
    return await fn();
  } catch (error) {
    console.error("Async error:", error);
    return fallback;
  }
}

/** Example 3: Reactエラーバウンダリ */
class ErrorBoundary extends React.Component {
  componentDidCatch(error: Error): void {
    console.error("Component error:", error);
  }
  render() {
    return this.props.children;
  }
}
```
