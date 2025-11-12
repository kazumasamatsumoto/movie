# #441 「Angularイベントハンドラ」

四国めたん「Angularのイベントハンドラでもvoidが活躍します。」
ずんだもん「onClick(): void でボタン処理を書いていたね。」
四国めたん「フォーム送信や入力イベントもvoidで副作用のみを表現します。」
ずんだもん「テンプレートの(click)とメソッドを結びつけるのが基本?」
四国めたん「はい。戻り値を使わないのでvoidが最適です。」
ずんだもん「ロジックはコンポーネントクラスに閉じ込められるんだね。」
四国めたん「副作用の結果はUIだけに反映されます。」
ずんだもん「Angularでもvoidハンドラで処理を整理するのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: Angularコンポーネント */
@Component({
  selector: 'app-user',
  template: '<button (click)="onClick()">Click</button>'
})
export class UserComponent {
  onClick(): void {
    console.log('Button clicked');
  }
}

/** Example 2: フォーム送信 */
@Component({
  selector: 'app-form',
  template: '<form (submit)="onSubmit()">...</form>'
})
export class FormComponent {
  onSubmit(): void {
    console.log('Form submitted');
  }
}

/** Example 3: 入力イベント */
onInput(event: Event): void {
  const value = (event.target as HTMLInputElement).value;
  console.log('Input:', value);
}
```
