# #361 「*ngSwitchCase - ケース分岐」

## 概要
`*ngSwitchCase`は`[ngSwitch]`で指定した値と一致する場合にテンプレートを表示する構造ディレクティブで、ケースごとのUIを整理できる。

## 学習目標
- `*ngSwitchCase`の働きと配置方法を理解する
- 共通テンプレートを複数ケースで共有する手法を学ぶ
- case値の型と比較ルールを把握する

## 技術ポイント
- `*ngSwitchCase`は厳密比較で一致判定
- 同じテンプレートを複数ケースで使う場合はテンプレート参照で共通化
- case順序は関係なく、一致した最初のケースが表示

## 📺 画面表示用コード（動画用）
```html
<p *ngSwitchCase="'success'">成功しました</p>
```

## 💻 詳細実装例（学習用）
```typescript
type PaymentStatus = 'pending' | 'succeeded' | 'failed';

@Component({
  selector: 'app-switchcase-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <section [ngSwitch]="status">
      <p *ngSwitchCase="'pending'">決済処理中です。</p>
      <p *ngSwitchCase="'succeeded'">決済が完了しました。</p>
      <p *ngSwitchCase="'failed'">決済に失敗しました。</p>
      <p *ngSwitchDefault>不明なステータスです。</p>
    </section>
  `
})
export class SwitchCaseDemoComponent {
  protected status: PaymentStatus = 'pending';
}
```

## ベストプラクティス
- case値は定数やenumで管理し、タイポを防ぐ
- 複数ケースで同じUIを表示したい場合は`ng-template`を使って共通化
- defaultケースで例外状態を検知し、ログ出力するなど品質を高める

## 注意点
- case値にオブジェクトや配列を渡すと毎回参照が変わるため一致しない
- 文字列比較では大文字小文字が区別されるため統一する
- SSRで状態が変わるとケースが一致せずdefaultが表示される可能性がある

## 関連技術
- Union Types
- Template Reference Variables
- SSR/Hydration
