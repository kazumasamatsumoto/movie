# #301 「Directive とは？DOM拡張の仕組み」

## 概要
DirectiveはAngularがDOMを再利用可能に拡張するための仕組みで、テンプレートを書き換えずに振る舞いや表示ロジックを差し込める。

## 学習目標
- Directiveの基本的な役割と種類を把握する
- コンポーネントとの違いを理解する
- DOM拡張を行う際の安全なアプローチを学ぶ

## 技術ポイント
- `@Directive`デコレータによる定義
- ElementRef/Renderer2を使ったDOM操作
- Attribute/Structural/Component Directiveの分類

## Overview
Directives are Angular's mechanism for extending the DOM in a reusable way, allowing you to inject behavior and display logic without rewriting templates.

## Learning Objectives
* Understand the basic role and types of Directives
* Understand the differences from Components
* Learn safe approaches when extending the DOM

## Technical Points
* Definition using the `@Directive` decorator
* DOM manipulation using ElementRef/Renderer2
* Classification into Attribute/Structural/Component Directives

```typescript
@Directive({ selector: '[appAccent]' })
export class AccentDirective implements OnInit {
  constructor(private readonly el: ElementRef, private readonly renderer: Renderer2) {}
  ngOnInit(): void {
    this.renderer.setStyle(this.el.nativeElement, 'outline', '2px solid #3b82f6');
  }
}
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-directive-sample',
  standalone: true,
  imports: [CommonModule, AccentDirective],
  template: `
    <p appAccent>DirectiveでDOMにアウトラインを付与します。</p>
    <button appAccent type="button">対象ボタン</button>
  `
})
export class DirectiveSampleComponent {}
```

## ベストプラクティス
- テンプレート自体を持たない薄いロジックをDirectiveに集約する
- DOM操作はRenderer2を使いプラットフォーム非依存に保つ
- 命名は`app`などプレフィックスを付け衝突を避ける

## 注意点
- 直接`nativeElement`を触るとSSRやWeb Workerで失敗する
- コンポーネントへ切り出した方が明確な場合は無理にDirectiveにしない
- 複雑な状態管理はサービスと連携させ責務を分散する

## 関連技術
- Angularコンポーネント
- Renderer2
- Dependency Injection
