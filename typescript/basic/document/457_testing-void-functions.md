# #457 「テスト」

四国めたん「void関数のテストでは副作用を検証します。」
ずんだもん「ログ関数はモックを使って呼び出し回数を確認してたね。」
四国めたん「非同期Promise<void>はawaitしてから検証します。」
ずんだもん「例外を投げる関数もexpect(() => fn()).toThrowで確認するんだ?」
四国めたん「はい。戻り値が無い代わりに副作用や例外をアサートします。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 同期voidのテスト */
test('log called once', () => {
  const spy = vi.fn();
  logWith(spy);
  expect(spy).toHaveBeenCalledTimes(1);
});

/** Example 2: 非同期voidのテスト */
test('save resolves', async () => {
  await saveUser(user);
  expect(database.save).toHaveBeenCalled();
});

/** Example 3: 例外のテスト */
test('validate throws', () => {
  expect(() => validate(invalidData)).toThrow('Invalid data');
});
```
