# #428 「Directive の再利用性」

## 概要
再利用性の高いディレクティブは特定シナリオに依存せず、設定可能なAPIと最小限の副作用で設計されており、多数のコンポーネントで活用できる。

## 学習目標
- 再利用性を高める設計指針を理解する
- Input/Outputで柔軟性を確保する方法を学ぶ
- 依存の少ないアーキテクチャを構築する

## 技術ポイント
- 設定値はInputで受け取りデフォルトを用意
- イベントはOutputで通知し外部制御を可能に
- DOM操作はRenderer2/HostBindingで抽象化

## 📺 画面表示用コード（動画用）
```typescript
@Input() appToggleClass = 'is-active';
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appToggleClass]',
  standalone: true
})
export class ToggleClassDirective {
  @Input() appToggleClass = 'is-active';
  @HostBinding('class') hostClass = '';

  @HostListener('click')
  onClick(): void {
    this.hostClass = this.hostClass === this.appToggleClass ? '' : this.appToggleClass;
  }
}
```

## ベストプラクティス
- 共通ユーティリティとして`shared/directives`等に配置
- テストとドキュメントを整備し利用方法を明確にする
- 依存サービスは抽象化し、注入で差し替え可能にする

## 注意点
- ドメイン固有の文言やAPI依存を含めない
- 過度に汎用にしようとすると複雑化するため適切なスコープを見極める
- バージョンアップでBreaking Changeが発生しないよう慎重に変更

## 関連技術
- Dependency Injection
- Storybook
- Shared Module/Standalone組織
