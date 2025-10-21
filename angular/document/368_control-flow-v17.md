# #368 「Control Flow構文（v17+）」

## 概要
Angular v17以降で導入されたControl Flow構文は、`@if`/`@for`/`@switch`といった新しいテンプレート記法で、より直感的かつ最適化されたレンダリングを提供する。

## 学習目標
- Control Flow構文の概要とメリットを理解する
- 従来の`*`構文との違いを把握する
- 移行時の考慮点を学ぶ

## 技術ポイント
- `@if (condition) { ... } @else { ... }`形式で記述
- `@for (item of items; track item.id)`でtrack句が標準化
- `@switch`はTypeScriptのswitch文に近いシンタックス

## 📺 画面表示用コード（動画用）
```html
@if (user()) {
  <p>{{ user()!.name }}</p>
} @else {
  <p>未ログイン</p>
}
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-control-flow-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    @if (items().length === 0) {
      <p>アイテムがありません。</p>
    } @else {
      @for (item of items(); track item.id) {
        <p>{{ item.label }}</p>
      }
    }
  `
})
export class ControlFlowDemoComponent {
  private readonly itemsSignal = signal([{ id: 1, label: '新構文' }]);
  protected items = this.itemsSignal.asReadonly();
}
```

## ベストプラクティス
- 新構文はOpt-inなので、プロジェクト単位で導入計画を立てる
- track句を必ず指定し、最適化の恩恵を受ける
- リファクタ時はテストで挙動を確認しながら段階的に置き換える

## 注意点
- v17以降でのみ利用可能、旧バージョンではビルドできない
- ESLintやテンプレート解析ツールの対応状況を確認する
- 新構文と従来構文が混在すると可読性が落ちるためルールを設ける

## 関連技術
- Angular v17+
- Template Control Flow
- track句 (`track item.id`)
