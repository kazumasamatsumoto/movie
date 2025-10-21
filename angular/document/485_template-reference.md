# #485 「テンプレートの参照」

## 概要
構造ディレクティブはTemplateRefを通じてテンプレートの参照を取得し、必要なタイミングで`createEmbeddedView`を呼び出してビューを生成する。

## 学習目標
- TemplateRefとng-templateの関係を理解する
- テンプレート参照を活用したビュー生成の手順を学ぶ
- 複数テンプレートを扱う場合の構造を把握する

## 技術ポイント
- TemplateRefは暗黙にng-templateへ変換されたテンプレートを表す
- `templateRef.elementRef`でDOM要素へアクセス可能
- `ViewContainerRef.createEmbeddedView(template, context)`でビュー生成

## 📺 画面表示用コード（動画用）
```typescript
this.viewContainer.createEmbeddedView(this.template, context);
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appTemplateReference]',
  standalone: true
})
export class TemplateReferenceDirective {
  constructor(
    private readonly template: TemplateRef<{ $implicit: number }>,
    private readonly viewContainer: ViewContainerRef
  ) {}

  renderTimes(times: number): void {
    this.viewContainer.clear();
    for (let i = 0; i < times; i++) {
      this.viewContainer.createEmbeddedView(this.template, { $implicit: i });
    }
  }
}
```

## ベストプラクティス
- テンプレートに渡すデータはContextオブジェクトで一括管理
- ViewContainerRefをクリアしてから再生成するとビューの重複を防げる
- TemplateRefはキャッシュして再利用できるため余分なDOM生成を抑える

## 注意点
- TemplateRefを直接操作してDOMを変更するのは避け、ViewContainerRef経由で管理
- 多数のビューを生成する場合はパフォーマンスへの影響を考慮
- Structural Directiveは複数同時に適用できないため設計時に注意

## 関連技術
- TemplateRef
- ViewContainerRef
- Contextオブジェクト
