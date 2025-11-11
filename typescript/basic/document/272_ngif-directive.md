# #272 「*ngIfディレクティブ」

四国めたん「*ngIfディレクティブについて学びましょう!」
ずんだもん「条件に応じて要素の表示・非表示を切り替えられるんだね!」
四国めたん「はい。booleanの値がtrueの時だけ要素が表示されます。」
ずんだもん「else節を使えば、条件が偽の時の表示も設定できるよね?」
四国めたん「その通りです。ng-templateと組み合わせることで柔軟な制御ができます。」
ずんだもん「DOM要素自体が追加・削除されるから、パフォーマンスにも良いね!」
四国めたん「CSSのdisplay:noneとは違い、完全に要素が削除される点が重要です。」
ずんだもん「ログイン状態によるUI切り替えなど、実用的な場面が多いのだ!」

---

## 📺 画面表示用コード

```typescript
// *ngIfディレクティブ

@Component({
  selector: 'app-example',
  template: `
    <div *ngIf="isVisible">表示されます</div>

    <div *ngIf="isLoggedIn; else loginTemplate">
      ログイン済み
    </div>
    <ng-template #loginTemplate>
      未ログイン
    </ng-template>
  `
})
export class ExampleComponent {
  isVisible: boolean = true;
  isLoggedIn: boolean = false;
}
```
