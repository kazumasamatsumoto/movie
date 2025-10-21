# #359 「*ngSwitch の基本構文」

## 概要
`*ngSwitch`の基本構文はラッパー要素に`[ngSwitch]`を設定し、内部で`*ngSwitchCase`と`*ngSwitchDefault`を組み合わせて分岐を記述する。

## 学習目標
- 基本構文とディレクティブの配置を理解する
- 値の比較方法とケースの書き方を学ぶ
- ケースごとのテンプレート管理を身につける

## 技術ポイント
- `ngSwitch`はディレクティブではなくプロパティバインディング、ケースは構造ディレクティブ扱い
- caseの値は定数・式どちらも可だが型を揃える
- 同じ値のケースは1つだけ有効

## 📺 画面表示用コード（動画用）
```html
<div [ngSwitch]="mode">
  <p *ngSwitchCase="'preview'">プレビュー</p>
  <p *ngSwitchCase="'edit'">編集モード</p>
  <p *ngSwitchDefault>未選択</p>
</div>
```

## 💻 詳細実装例（学習用）
```typescript
type Mode = 'preview' | 'edit' | 'readonly';

@Component({
  selector: 'app-switch-syntax-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <div [ngSwitch]="mode">
      <p *ngSwitchCase="'preview'">プレビュー表示です。</p>
      <p *ngSwitchCase="'edit'">編集可能なフォームを表示します。</p>
      <p *ngSwitchCase="'readonly'">閲覧のみです。</p>
      <p *ngSwitchDefault>モードを選択してください。</p>
    </div>
  `
})
export class SwitchSyntaxDemoComponent {
  protected mode: Mode = 'preview';
}
```

## ベストプラクティス
- モード値は型で制約し、予期しない値を防ぐ
- ケースが増えたらテンプレートを別ファイルまたはコンポーネントへ分割
- defaultケースにガイドメッセージを表示してUXを高める

## 注意点
- `*ngSwitchCase`で使う値はプリミティブ比較なのでオブジェクトは不適
- ラッパー要素が必要なため、DOM構造が増える場合は`ng-container`を活用
- 新構文`@switch`を併用する際は互換性を確認する

## 関連技術
- Union Types
- Template Composition
- @switch構文
