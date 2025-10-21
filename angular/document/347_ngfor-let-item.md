# #347 「*ngFor=\"let item of items\"」

## 概要
`*ngFor="let item of items"`はコレクションから要素を順に取り出し、テンプレート変数`item`として利用する。

## 学習目標
- `let`キーワードの意味とスコープを理解する
- テンプレート変数の命名と使い方を学ぶ
- 実用的な表示例を作成する

## 技術ポイント
- `item`はループ毎に新しい参照が割り当てられる
- `let`で複数変数を宣言することも可能（`; let i = index`など）
- `as`構文とは異なり、`item`は常に存在する

## 📺 画面表示用コード（動画用）
```html
<li *ngFor="let product of products">
  {{ product.name }}
</li>
```

## 💻 詳細実装例（学習用）
```typescript
interface Product {
  id: number;
  name: string;
  price: number;
}

@Component({
  selector: 'app-ngfor-item-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <table>
      <tr *ngFor="let product of products">
        <td>{{ product.name }}</td>
        <td>{{ product.price | currency:'JPY' }}</td>
      </tr>
    </table>
  `
})
export class NgForItemDemoComponent {
  protected products: Product[] = [
    { id: 1, name: 'Angular Guide', price: 2800 },
    { id: 2, name: 'Directive Patterns', price: 3200 }
  ];
}
```

## ベストプラクティス
- 変数名は内容を示すようにし、`item`より具体的な名前を付ける
- 価格などのフォーマットはパイプを使ってテンプレート内で簡潔にする
- trackByでキーを返し再描画を抑える

## 注意点
- `item`に直接代入しても元のコレクションは書き換わらない（参照であるため）
- 可変データを扱う場合は`OnPush`と組み合わせて性能を最適化
- Observableを直接`items`に書くと未解決のままになるので`AsyncPipe`を使用する

## 関連技術
- CurrencyPipe
- trackBy
- ChangeDetectionStrategy.OnPush
