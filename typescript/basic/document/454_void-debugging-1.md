# #454 「デバッグ(1)」

四国めたん「void関数でもデバッグログを丁寧に入れましょう。」
ずんだもん「processDataで引数や早期リターンをログしてたね。」
四国めたん「updateでは条件ごとに情報を出して流れを追っています。」
ずんだもん「ログを入れても戻り値を触らない点は変わらないんだ?」
四国めたん「はい。副作用の進行状況だけを可視化します。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: デバッグログの追加 */
function processData(data: Data): void {
  console.log('processData called with:', data);
  if (!data.isValid) {
    console.log('Invalid data, returning early');
    return;
  }
  console.log('Processing data...');
  doSomething(data);
  console.log('processData completed');
}

/** Example 2: 条件分岐のデバッグ */
function update(user: User): void {
  console.log('update start:', user.id);
  if (user.age < 18) {
    console.log('User is minor');
    return;
  }
  console.log('Updating user');
}

/** Example 3: 戻り値なしでトレース */
function process(): void {
  console.log('process start');
  step();
  console.log('process end');
}
```
