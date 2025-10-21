# #346 「*ngFor の基本構文」

## 概要
`*ngFor`の基本構文は`*ngFor="let item of items"`で、テンプレート内にコレクション要素を展開する。

## 学習目標
- `let`宣言と`of`キーワードの意味を理解する
- インラインで追加変数を宣言する構文を把握する
- 配列以外のIterableを扱うパターンを学ぶ

## 技術ポイント
- `let item of items; let i = index`など構文糖衣を提供
- `items`は配列、`ReadonlyArray`, `Iterable`, `Signal`結果などが利用可能
- `; trackBy: fn`で識別子を設定し再利用を促進

## 📺 画面表示用コード（動画用）
```html
<div *ngFor="let user of users; let i = index">
  {{ i + 1 }}. {{ user }}
</div>
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-ngfor-syntax-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <ul>
      <li *ngFor="let user of users; let i = index">
        {{ i + 1 }}: {{ user }}
      </li>
    </ul>
  `
})
export class NgForSyntaxDemoComponent {
  protected users = ['Alice', 'Bob', 'Carol'];
}
```

## ベストプラクティス
- コレクションはReadonlyに保ち、副作用を避ける
- コンテキスト変数を使ってテンプレートロジックを簡潔にする
- trackByを併用してDOM再生成を抑える

## 注意点
- `;`以降の構文は順序に依存するため、可読性に配慮して並べる
- メソッド呼び出しを`items`に書くと毎回評価されるため避ける
- Signalを直接`items`に渡す場合は`items()`と呼び出す必要がある

## 関連技術
- Angular Signals
- trackBy
- Structural Directive構文糖衣
