# #404 「selector の命名規則」

## 概要
Directiveのselectorはプレフィックス＋役割名で命名し、他ライブラリとの衝突を避けつつ可読性を高める。

## 学習目標
- 属性ディレクティブのselector記法を理解する
- プレフィックスの重要性を説明できる
- プロジェクト内での命名規則策定方法を把握する

## 技術ポイント
- 属性ディレクティブ: `[appHighlight]`
- クラスディレクティブ: `.appDraggable`
- 要素ディレクティブ: `app-card`（基本はコンポーネント向け）

## 📺 画面表示用コード（動画用）
```typescript
@Directive({ selector: '[appHighlight]', standalone: true })
export class HighlightDirective {}
```

## 💻 詳細実装例（学習用）
```typescript
export const DIRECTIVE_PREFIX = 'app';

function selector(name: string): string {
  return `[${DIRECTIVE_PREFIX}${name[0].toUpperCase()}${name.slice(1)}]`;
}

@Directive({
  selector: selector('focusRing'),
  standalone: true
})
export class FocusRingDirective {}
```

## ベストプラクティス
- prefix + PascalCaseで役割が伝わるselectorを定義する
- カスタムライブラリでは`lib`, `acme`などブランドプレフィックスを採用
- 命名規則をREADMEやスタイルガイドに明記する

## 注意点
- プレフィックスなしで公開すると他ライブラリと衝突しやすい
- 文字列リテラル内でタイプミスしてもビルド時に検知されない
- クラスセレクタを使う場合はCSS命名との整合性を確保する

## 関連技術
- Angular Style Guide
- Schematics設定
- ESLintテンプレートルール
