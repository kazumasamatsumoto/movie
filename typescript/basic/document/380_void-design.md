# #380 「設計思想」

四国めたん「voidを使うと関数の役割を設計レベルで分けられます。」
ずんだもん「addみたいに値を返す純粋関数と対比できるんだね。」
四国めたん「はい。純粋関数はnumberを返し、副作用関数はvoidで宣言します。」
ずんだもん「logResultは結果を受け取って表示するだけだからvoidが最適?」
四国めたん「その通り。戻り値がないことで『表示だけ』と伝えられます。」
ずんだもん「DataServiceのインターフェースでもgetDataは値、saveDataはvoidで区別してる!」
四国めたん「責務を明確にするため、取得系は値、更新系はvoidにする設計が有効です。」
ずんだもん「voidを設計言語として活用するのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 純粋関数 */
function add(a: number, b: number): number {
  return a + b;
}

/** Example 2: 副作用関数 */
function logResult(result: number): void {
  console.log(`Result: ${result}`);
}

/** Example 3: 設計の明確化 */
interface DataService {
  getData(): Data;        // 値を取得
  saveData(data: Data): void;  // 副作用のみ
  deleteData(id: number): void;  // 副作用のみ
}
```
