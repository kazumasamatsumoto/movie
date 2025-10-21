# #484 「ViewContainerRef の注入」

## 概要
ViewContainerRefはテンプレートから生成したビューを挿入・削除するコンテナで、Structural DirectiveがDOM構造を制御する中核となる。

## 学習目標
- ViewContainerRefの役割を理解する
- createEmbeddedView/clear/insert/removeなどの操作を学ぶ
- Structural Directiveのライフサイクルでどう利用するか把握する

## 技術ポイント
- `constructor(private vc: ViewContainerRef)`
- `vc.createEmbeddedView(template, context?)`
- `vc.clear()`でビューを破棄

## 📺 画面表示用コード（動画用）
```typescript
constructor(private viewContainer: ViewContainerRef) {}
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appViewContainerSample]',
  standalone: true
})
export class ViewContainerSampleDirective {
  constructor(
    private readonly template: TemplateRef<{ $implicit: string }>,
    private readonly viewContainer: ViewContainerRef
  ) {}

  render(message: string): void {
    this.viewContainer.clear();
    this.viewContainer.createEmbeddedView(this.template, { $implicit: message });
  }
}
```

## ベストプラクティス
- ビューの生成・破棄はViewContainerRefに委ね、状態をフラグで管理
- 複数ビューを扱う場合は`insert`, `remove`でインデックス管理
- 生成した`EmbeddedViewRef`を保持して再利用することも可能

## 注意点
- clearを忘れるとビューが残りメモリリークに繋がる
- ViewContainerRefの操作は同期的に行われるため非同期処理のタイミングに注意
- Structural Directive以外で多用するとテンプレートの可読性が下がる

## 関連技術
- TemplateRef
- EmbeddedViewRef
- Structural Directiveライフサイクル
