# #492 「while(true)」

四国めたん「while(true)のような明示的ループもneverにつながります。」
ずんだもん「loop()はdoWork()を延々と実行してた!」
四国めたん「poll()ではキューをポーリングしていました。」
ずんだもん「monitor()みたいに待機しながら監視するパターンもあるんだね。」
四国めたん「ループ中にawaitやsleepを入れてCPUを解放する工夫も忘れずに。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 基本的なloop */
function loop(): never {
  while (true) {
    doWork();
  }
}

/** Example 2: ポーリング */
function poll(): never {
  while (true) {
    const data = fetchData();
    if (data) {
      process(data);
    }
    sleep(1000);
  }
}

/** Example 3: 監視ループ */
async function monitor(): never {
  while (true) {
    const status = checkStatus();
    if (status === "error") {
      handleError();
    }
    await delay(5000);
  }
}
```
