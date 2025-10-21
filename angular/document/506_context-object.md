# #506 「Context オブジェクトの提供」

## 概要
Contextオブジェクトは構造ディレクティブがテンプレートへ渡すデータをまとめたもので、`createEmbeddedView`の第二引数に渡すことでテンプレート内の`let`構文から参照できる。

## 学習目標
- Contextオブジェクトの役割を理解する
- `$implicit`やカスタムプロパティを設定する方法を学ぶ
- テンプレート側でContext値を扱う構文を把握する

## 技術ポイント
- `{ $implicit: value, index: i, loading: state }`
- `let item`は`$implicit`を参照、`let i = index`は`context.index`
- Context型を定義し型安全を向上

## 📺 画面表示用コード（動画用）
```typescript
const context = { $implicit: value, index: i };
this.viewContainer.createEmbeddedView(this.template, context);
```

## 💻 詳細実装例（学習用）
```typescript
interface LoadingContext<T> {
  $implicit: T | null;
  loading: boolean;
  error: unknown;
}

this.viewContainer.createEmbeddedView(this.template, {
  $implicit: data,
  loading: true,
  error: null
} satisfies LoadingContext<T>);
```

## ベストプラクティス
- Context型をエクスポートしテンプレート補完を有効化
- `$implicit`には主要な値を渡し、その他メタ情報は別プロパティに
- Contextを更新する際は`viewRef.context`を操作し`markForCheck`で反映

## 注意点
- Contextプロパティ名はテンプレートの`let`と一致させる必要がある
- `$implicit`を使わない場合でも明示的なキーで提供できるが可読性に注意
- OnPushコンポーネント内では`markForCheck()`を呼ぶ必要があるケースがある

## 関連技術
- EmbeddedViewRef.context
- TemplateRef
- Structural Directiveコンテキスト
