# #483 「TemplateRef の注入」

## 概要
TemplateRefはディレクティブが適用されたテンプレート自体を表す参照で、構造ディレクティブでビューを生成する際のテンプレート元になる。

## 学習目標
- TemplateRefが提供する機能を理解する
- コンストラクタでの注入方法を学ぶ
- コンテキストを持つビュー生成との関係を把握する

## 技術ポイント
- `constructor(private template: TemplateRef<unknown>)`
- `template.createEmbeddedView`ではなく`ViewContainerRef`から`createEmbeddedView`を呼ぶ
- ジェネリクスでコンテキスト型を明示できる

## 📺 画面表示用コード（動画用）
```typescript
constructor(private template: TemplateRef<unknown>) {}
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appTemplateRefSample]',
  standalone: true
})
export class TemplateRefSampleDirective {
  constructor(private readonly template: TemplateRef<{ $implicit: number }>) {}

  createView(viewContainer: ViewContainerRef, index: number): void {
    viewContainer.createEmbeddedView(this.template, { $implicit: index });
  }
}
```

## ベストプラクティス
- コンテキストを利用する場合はジェネリクスで型を定義し、テンプレート側の補完を有効化
- TemplateRefはビュー生成時に何度でも再利用可能
- 処理を共通化するためラッパーサービスでTemplateRefを受け取ることも検討

## 注意点
- TemplateRefは構造ディレクティブ内でのみ注入できる
- コンポーネントテンプレートで直接createEmbeddedViewを呼ぶのは推奨されない
- コンテキストのKeysはテンプレートの`let`宣言と一致させる

## 関連技術
- ViewContainerRef
- Contextオブジェクト
- Structural Directive基礎
