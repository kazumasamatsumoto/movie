# #349 「index - インデックス取得」

## 概要
`*ngFor`では`let i = index`で0始まりのインデックスが取得でき、番号表示や条件によるスタイル分岐に利用できる。

## 学習目標
- `index`変数の使い方とスコープを理解する
- 表示番号やスタイルの制御に活用する
- `count`と組み合わせた高度な利用例を学ぶ

## 技術ポイント
- `index`は0から始まり、各反復で更新
- `count`で総数を取得し、逆順インデックスを計算できる
- `*ngFor="let item of items; let i = index; let count = count"`で複数変数を取得

## 📺 画面表示用コード（動画用）
```html
<li *ngFor="let city of cities; let i = index">
  {{ i + 1 }}. {{ city }}
</li>
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-ngfor-index-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <ol>
      <li *ngFor="let city of cities; let i = index; let count = count">
        {{ i + 1 }} / {{ count }}: {{ city }}
      </li>
    </ol>
  `
})
export class NgForIndexDemoComponent {
  protected cities = ['Sapporo', 'Sendai', 'Tokyo', 'Fukuoka'];
}
```

## ベストプラクティス
- 表示用の番号は`i + 1`のようにテンプレートで補正する
- 条件スタイルには`[class.is-odd]="i % 2 === 1"`といった式を利用
- 逆順表示など複雑なロジックはコンポーネントで計算しておく

## 注意点
- `index`をtrackByの戻り値に使うと並び替えでDOMが再生成される
- ネストした*ngForで同じ変数名を使うと混乱するので名前を変える
- `index`は読み取り専用で再代入できない

## 関連技術
- trackBy
- CSSクラスバインディング
- Computed Signals
