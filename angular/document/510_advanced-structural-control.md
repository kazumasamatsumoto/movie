# #510 「高度な構造制御の実装」

## 概要
高度な構造制御では複数のテンプレート切り替えやコンテキストの豊富な提供、非同期状態管理などを組み合わせ、複雑な表示ロジックを持つ構造ディレクティブを実現する。

## 学習目標
- 複数テンプレートを切り替える設計を理解する
- コンテキストに関数やObservableを渡す応用を学ぶ
- 高度な制御でパフォーマンスと可読性を両立させる方法を把握する

## 技術ポイント
- Inputでメイン/else/placeholderテンプレートを受け取る
- ContextにCallableを渡してテンプレートから動的に実行
- ObservableやSignalsと連携して再描画を制御

## 📺 画面表示用コード（動画用）
```html
<section *appSwitch="state; case 'loading': loadingTpl; case 'error': errorTpl">{{ data }}</section>
```

## 💻 詳細実装例（学習用）
```typescript
interface SwitchCase<T> {
  match: (value: T) => boolean;
  template: TemplateRef<unknown>;
}

@Directive({
  selector: '[appSwitch]',
  standalone: true
})
export class SwitchDirective<T> implements OnChanges {
  @Input('appSwitch') value!: T;
  @Input('appSwitchDefault') defaultTemplate?: TemplateRef<unknown>;
  private cases: SwitchCase<T>[] = [];

  constructor(private readonly viewContainer: ViewContainerRef) {}

  registerCase(match: (value: T) => boolean, template: TemplateRef<unknown>): void {
    this.cases.push({ match, template });
  }

  ngOnChanges(): void {
    this.viewContainer.clear();
    const found = this.cases.find(c => c.match(this.value));
    const tpl = found?.template ?? this.defaultTemplate;
    if (tpl) {
      this.viewContainer.createEmbeddedView(tpl);
    }
  }
}
```

## ベストプラクティス
- 構造ディレクティブを小さな責務に分割し、複数のテンプレートを登録・切り替え
- コンテキストで関数やObservableを渡しテンプレート内で動的ロジックを実行
- パフォーマンスを考慮し不要なビュー再生成を避ける仕組みを設計

## 注意点
- 複雑になりすぎるとテンプレートの可読性が落ちるためドキュメントや例を用意
- 多数のテンプレート切り替えではインデックスやキー管理を行う
- 非同期処理でレースコンディションが発生しないようステート管理を慎重に

## 関連技術
- Structural Directiveコンビネーション
- Signals/Observable連携
- テンプレート駆動の状態管理パターン
