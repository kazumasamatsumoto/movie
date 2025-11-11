# #271 「Angularテンプレートでのboolean」

四国めたん「Angularテンプレートでbooleanを使ってみましょう!」
ずんだもん「コンポーネントのプロパティをテンプレートで活用できるんだね!」
四国めたん「はい。*ngIfディレクティブで条件付き表示ができます。」
ずんだもん「[disabled]属性でボタンの無効化もできるよね?」
四国めたん「その通りです。booleanの状態によってUIの制御が可能です。」
ずんだもん「プロパティバインディングで動的な制御ができるから便利だね!」
四国めたん「TypeScriptの型定義とAngularのテンプレートが連携しているのがポイントです。」
ずんだもん「リアクティブなUIを作るのに必須の機能なのだ!」

---

## 📺 画面表示用コード

```typescript
// Angularテンプレートでのboolean

// コンポーネント
@Component({
  selector: 'app-user',
  template: `
    <div *ngIf="isLoggedIn">ログイン済み</div>
    <button [disabled]="!isValid">送信</button>
  `
})
export class UserComponent {
  isLoggedIn: boolean = true;
  isValid: boolean = false;

  checkStatus(): void {
    if (this.isLoggedIn && this.isValid) {
      console.log('OK');
    }
  }
}
```
