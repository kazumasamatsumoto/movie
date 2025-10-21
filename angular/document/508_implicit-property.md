# #508 「$implicit プロパティ」

## 概要
`$implicit`プロパティはテンプレートで`let item`と書いたときに参照される暗黙の値で、構造ディレクティブがメインのデータを渡すのに使用される。

## 学習目標
- `$implicit`の役割と利用パターンを理解する
- `$implicit`と命名付きプロパティの使い分けを学ぶ
- Context更新によるテンプレート反映方法を把握する

## 技術ポイント
- Contextの`$implicit`キーに主データを入れる
- `let item`で受け取り、`let item2 = item`のような別名も設定可能
- $implicit以外にも`index`, `first`など任意のプロパティを追加

## 📺 画面表示用コード（動画用）
```typescript
this.viewContainer.createEmbeddedView(this.template, { $implicit: value });
```

## 💻 詳細実装例（学習用）
```typescript
interface AsyncContext<T> {
  $implicit: T | null;
  loading: boolean;
  error: unknown;
}

const context: AsyncContext<User> = { $implicit: null, loading: true, error: null };
this.viewContainer.createEmbeddedView(this.template, context);
```

## ベストプラクティス
- `$implicit`には最も使用頻度の高い値を割り当て、テンプレートを簡潔に
- 複数値が必要な場合は追加プロパティで提供し、命名も明確に
- Contextを更新する際は`viewRef.context.$implicit = newValue`のように更新

## 注意点
- `$implicit`は1つだけなので複数値を暗黙に扱うことは避ける
- Null許容かどうかを型で表現し、テンプレートで安全に参照
- OnPush環境では`markForCheck()`を呼ばないと変更が反映されない場合がある

## 関連技術
- Contextオブジェクト
- EmbeddedViewRef.context
- Structural Directiveテンプレート構文
