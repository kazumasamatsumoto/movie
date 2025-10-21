# #389 「フォーム要素との連携」

## 概要
`ngModel`はinput、select、textareaなどのフォーム要素と連携し、ユーザー入力をコンポーネントと同期させる。各要素に応じたオプション設定も可能。

## 学習目標
- 各フォーム要素でngModelを使う際のポイントを理解する
- `ngModelOptions`でnameやupdateOnなどを設定する方法を学ぶ
- スタンドアロンフォームとテンプレート駆動フォームの使い分けを把握する

## 技術ポイント
- select要素では`[ngModel]`と`(ngModelChange)`で選択値を扱う
- `ngModelOptions`で`standalone`, `name`, `updateOn`を設定
- `[(ngModel)]`は`FormsModule`の`NgModel`ディレクティブに依存

## 📺 画面表示用コード（動画用）
```html
<select [(ngModel)]="selected" name="plan">
  <option value="basic">Basic</option>
  <option value="pro">Pro</option>
</select>
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-ngmodel-form-elements-demo',
  standalone: true,
  imports: [CommonModule, FormsModule],
  template: `
    <form>
      <label>
        プラン
        <select [(ngModel)]="plan" name="plan">
          <option value="basic">Basic</option>
          <option value="pro">Pro</option>
          <option value="enterprise">Enterprise</option>
        </select>
      </label>
      <label>
        メモ
        <textarea [(ngModel)]="memo" name="memo"></textarea>
      </label>
    </form>
    <pre>{{ { plan, memo } | json }}</pre>
  `
})
export class NgModelFormElementsDemoComponent {
  protected plan = 'basic';
  protected memo = '';
}
```

## ベストプラクティス
- select要素では型をUnionにして選択肢の制約を明確にする
- `updateOn: 'blur'`などで更新タイミングを変更し、入力中の変更を抑制する
- textareaでは`ngModelChange`と組み合わせて文字数カウントなどを実装

## 注意点
- radioボタンを束ねる際は`name`を揃える必要がある
- `standalone: true`を設定しないと親フォームの検証に影響を与えることがある
- `select`でオブジェクトを扱う場合は`[ngValue]`を使用する

## 関連技術
- ngModelOptions
- Template-driven Forms
- Reactive Forms
