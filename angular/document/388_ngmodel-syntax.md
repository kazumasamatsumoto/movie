# #388 「[(ngModel)] の使用」

## 概要
`[(ngModel)]`シンタックスはプロパティバインディングとイベントバインディングを組み合わせた糖衣構文で、テンプレートとコンポーネントの値を同期する。

## 学習目標
- `[(ngModel)]`の構造と実際に行われている処理を理解する
- スタンドアロンコンポーネントでの使い方を把握する
- フォームコントロールとの連携を学ぶ

## 技術ポイント
- `[(ngModel)]="value"`は`[ngModel]="value"`＋`(ngModelChange)="value = $event"`の糖衣
- `name`属性がないとテンプレート駆動フォームで自動登録されない
- `ngModelOptions`で`standalone: true`を設定すると所属フォーム外で利用可能

## 📺 画面表示用コード（動画用）
```html
<input [(ngModel)]="email" name="email" />
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-ngmodel-syntax-demo',
  standalone: true,
  imports: [CommonModule, FormsModule],
  template: `
    <form>
      <label>
        メール
        <input [(ngModel)]="email" name="email" />
      </label>
      <label>
        ニックネーム
        <input [(ngModel)]="nickname" name="nickname" />
      </label>
    </form>
    <pre>{{ { email, nickname } | json }}</pre>
  `
})
export class NgModelSyntaxDemoComponent {
  protected email = '';
  protected nickname = '';
}
```

## ベストプラクティス
- name属性を付けてフォームコントロールが正しく管理されるようにする
- 双方向バインディングを乱用せず、片方向で十分な場合は`[value]`＋`(input)`を検討
- 変更監視が必要なときは`ngModelChange`でハンドリングする

## 注意点
- コンポーネント外から直接`value`を変更したい場合は`@ViewChild(NgModel)`で参照
- `standalone: true`の設定を忘れると親フォームに意図せず登録される
- 双方向バインディングはテストが複雑になる場合があるため、必要性を見極める

## 関連技術
- ngModelChange
- Template-driven Forms
- Reactive Formsへの移行
