# #494 「Repeat Directive - 繰り返し」

## 概要
Repeatディレクティブは指定回数だけテンプレートを生成し、シンプルなループを提供する。`*appRepeat="5; let i = index"`のように使用できる。

## 学習目標
- 指定回数でテンプレートを繰り返す構造を理解する
- コンテキストでインデックスなどを提供する方法を学ぶ
- ViewContainerRefを活用したビュー生成パターンを把握する

## 技術ポイント
- Inputで回数を受け取り`for`ループでcreateEmbeddedView
- Contextに`$implicit`や`index`を設定
- 生成前に`clear()`でクリーンな状態に

## 📺 画面表示用コード（動画用）
```html
<li *appRepeat="5; let i = index">Item {{ i }}</li>
```

## 💻 詳細実装例（学習用）
```typescript
interface RepeatContext {
  $implicit: number;
  index: number;
}

@Directive({
  selector: '[appRepeat]',
  standalone: true
})
export class RepeatDirective implements OnChanges {
  @Input('appRepeat') count = 0;

  constructor(
    private readonly template: TemplateRef<RepeatContext>,
    private readonly viewContainer: ViewContainerRef
  ) {}

  ngOnChanges(): void {
    this.viewContainer.clear();
    for (let i = 0; i < this.count; i++) {
      this.viewContainer.createEmbeddedView(this.template, {
        $implicit: i,
        index: i
      });
    }
  }
}
```

## ベストプラクティス
- countが負数のときは0扱いなど防御的に整える
- Contextに必要な情報（index, first, lastなど）を追加し使い勝手を向上
- データ配列ではなく数値の繰り返しにフォーカスし役割を明確に

## 注意点
- 大きな数値での繰り返しはパフォーマンスに注意
- `count`変更時に再レンダリングするためdiffが大きくならないよう設計
- クライアントだけでなくSSRでも動作するよう初期値設定

## 関連技術
- TemplateRef
- ViewContainerRef
- Contextオブジェクト
