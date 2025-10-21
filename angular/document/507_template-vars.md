# #507 「テンプレート変数の渡し方」

## 概要
テンプレート変数は構造ディレクティブが提供するContextのプロパティを`let`構文で受け取り、テンプレート内で再利用する。キーと変数名を一致させて可読性を保つ。

## 学習目標
- Contextプロパティをテンプレート変数に渡す方法を理解する
- `$implicit`と命名付きプロパティの違いを学ぶ
- 複数値を受け取る場合の構文を把握する

## 技術ポイント
- `let item`は`$implicit`を参照
- `let i = index`は`context.index`
- `let loading = loading`など同名でも利用可能

## 📺 画面表示用コード（動画用）
```html
<ng-container *appRepeat="5; let i = index; let first = first">
  <p>{{ i }} {{ first }}</p>
</ng-container>
```

## 💻 詳細実装例（学習用）
```typescript
this.viewContainer.createEmbeddedView(this.template, {
  $implicit: item,
  index: i,
  first: i === 0,
  last: i === count - 1
});
```

## ベストプラクティス
- 明示的なキー名でコンテキストを提供し、テンプレート側で分かりやすい変数名に割り当て
- Contextオブジェクトは型定義し補完と型チェックを効かせる
- 変数を使用しない場合は命名省略で不要な警告を避ける

## 注意点
- `let`構文は1行に複数指定できるが読みやすさを意識
- `$implicit`を複数ディレクティブで利用すると衝突するため意図的に設計
- Context変更後は`viewRef.context`を更新することを忘れない

## 関連技術
- Contextオブジェクト
- EmbeddedViewRef
- Structural Directiveでのテンプレート構文
