# #329 「Directive の命名規則」

## 概要
統一された命名規則はディレクティブの発見性と保守性を高め、プレフィックスやサフィックスを揃えることで衝突を防ぐ。

## 学習目標
- クラス名・ファイル名・セレクタ名の命名ルールを理解する
- プレフィックスを活用した衝突回避を学ぶ
- テストファイルやディレクトリ構造の揃え方を把握する

## 技術ポイント
- クラス名は`PascalCase`＋`Directive`
- ファイル名は`kebab-case.directive.ts`
- セレクタはプロジェクトプレフィックス＋用途名

## 📺 画面表示用コード（動画用）
```typescript
@Directive({ selector: '[appHighlight]', standalone: true })
export class HighlightDirective {}
```

## 💻 詳細実装例（学習用）
```typescript
// src/app/directives/highlight/highlight.directive.ts
@Directive({
  selector: '[appHighlight]',
  standalone: true
})
export class HighlightDirective {
  @Input({ alias: 'appHighlight' }) color = '#fde047';
}

// src/app/directives/highlight/highlight.directive.spec.ts
describe('HighlightDirective', () => {
  // 命名規則に沿ったテストファイル
});
```

## ベストプラクティス
- プレフィックス（例: `app`, `lib`）をセレクタ先頭に付与し外部ライブラリと区別する
- ディレクトリ名とファイル名を揃え、`highlight.directive.ts`と`highlight.directive.spec.ts`を並べる
- エクスポート名や`exportAs`も命名規約を統一し、ドキュメントに記載する

## 注意点
- ネームスペースが衝突するとDIトークンも混乱するため、プロジェクトごとにプレフィックスを定義する
- 大文字小文字を混在させるとコンポーネントテンプレートで認識されないことがある
- セレクタの意味が曖昧だと利用者が誤解するため、動詞や形容詞を使い目的を明確にする

## 関連技術
- Angular Style Guide
- Schematics
- Storybookドキュメント
