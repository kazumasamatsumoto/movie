# #442 「(click)="onClick()"」

四国めたん「Angularの(click)バインディングでもvoidを使います。」
ずんだもん「handleClick(): void が基本の形だったね。」
四国めたん「$eventを受け取ればMouseEventを扱えます。」
ずんだもん「delete(user.id) のように引数を渡すこともある?」
四国めたん「はい。戻り値は使わないのでvoidで十分です。」
ずんだもん「テンプレート側での書き方も統一されて読みやすい!」
四国めたん「副作用ロジックだけをクラスに閉じ込めましょう。」
ずんだもん「(click)ハンドラはvoidで書くのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 基本的なクリックハンドラ */
@Component({
  selector: 'app-button',
  template: '<button (click)="handleClick()">Click</button>'
})
export class ButtonComponent {
  handleClick(): void {
    console.log('Clicked');
  }
}

/** Example 2: イベントオブジェクトを受け取る */
@Component({
  template: '<button (click)="onClick($event)">Click</button>'
})
export class Component {
  onClick(event: MouseEvent): void {
    console.log('Position:', event.clientX, event.clientY);
  }
}

/** Example 3: 引数を渡す */
@Component({
  template: '<button (click)="delete(user.id)">Delete</button>'
})
export class UserListComponent {
  delete(id: number): void {
    console.log('Deleting user:', id);
  }
}
```
