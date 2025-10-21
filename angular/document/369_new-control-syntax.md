# #369 「@if / @for / @switch 新構文」

## 概要
新しい`@if`/`@for`/`@switch`構文はTypeScriptライクなブロック記法で、テンプレートの読みやすさとコンパイル時最適化を両立する。

## 学習目標
- 各構文の基本記法と特徴を理解する
- `@for`のtrack句や`@switch`のケース指定を学ぶ
- 実際のテンプレートへの適用例を把握する

## 技術ポイント
- `@if`は`@else if`や`@else`をネスト可能
- `@for (item of items; track item.id; let i = $index)`のように追加情報を取得
- `@switch`は`@case`と`@default`で分岐

## 📺 画面表示用コード（動画用）
```html
@for (task of tasks; track task.id) {
  <li>{{ task.title }}</li>
}
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-new-syntax-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    @switch (status()) {
      @case ('loading') { <p>読み込み中...</p> }
      @case ('success') { <p>成功しました！</p> }
      @default { <p>状態不明</p> }
    }
  `
})
export class NewSyntaxDemoComponent {
  private readonly statusSignal = signal<'loading' | 'success' | 'unknown'>('loading');
  protected status = this.statusSignal.asReadonly();
}
```

## ベストプラクティス
- track句を適切に記述し、`@for`のパフォーマンスを最大化する
- ブロック内のHTMLはインデントを揃え可読性を高める
- チームで新構文利用ルールを共有し、一貫性あるテンプレートを書く

## 注意点
- 新構文導入後はテンプレートlintルールの更新が必要
- `@if`内でテンプレート参照を定義する場合のスコープに注意
- 旧構文との併用時はreviewで混乱がないか確認する

## 関連技術
- Angular v17 Template Syntax
- ESLint Template Plugins
- track句と$index等のメタ変数
