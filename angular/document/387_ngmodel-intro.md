# #387 「ngModel - 双方向バインディング」

## 概要
`ngModel`はテンプレート駆動フォームで値の双方向バインディングを提供し、フォーム要素とコンポーネントプロパティを同期させるディレクティブである。

## 学習目標
- ngModelの役割とフォームにおける位置づけを理解する
- 双方向バインディングの仕組みを把握する
- Reactive Formsとの違いと使い分けを説明できる

## 技術ポイント
- `[(ngModel)]`シンタックスで双方向同期
- `FormsModule`をインポートして使用
- `ngModelOptions`でバリューアクセスを細かく制御

## 📺 画面表示用コード（動画用）
```html
<input [(ngModel)]="username" placeholder="ユーザー名" />
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-ngmodel-demo',
  standalone: true,
  imports: [CommonModule, FormsModule],
  template: `
    <label>
      ユーザー名
      <input [(ngModel)]="username" />
    </label>
    <p>入力値: {{ username }}</p>
  `
})
export class NgModelDemoComponent {
  protected username = '';
}
```

## ベストプラクティス
- 小規模・単純なフォームでngModelを使い、複雑なケースではReactive Formsを検討
- 双方向バインディングの副作用を最小化するため、`ngModelChange`で必要な処理だけ追加
- 共有フォームロジックはコンポーネントやサービスに切り出す

## 注意点
- Standaloneコンポーネントで使用する際は`FormsModule`を忘れずにインポート
- `ngModel`とReactive Formsの`formControlName`を同じ要素で併用しない
- 変更検知が走るたびに同期が行われるため、重い処理は`ngModelChange`でdebounceする

## 関連技術
- FormsModule
- Reactive Forms
- ngModelChange
