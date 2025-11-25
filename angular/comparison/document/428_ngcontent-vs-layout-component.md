# #428 「ng-contentレイアウト vs Standalone Layoutコンポーネント あなたはどっち派？」

## 概要
ng-contentはシンプルで柔軟だが構造が暗黙的。LayoutコンポーネントはInputs/TemplateRefで受け取り、構造を明文化できる。

## 学習目標
- ng-contentの構成と得意なシナリオを整理する
- Layoutコンポーネントの採用メリットを理解する
- プロジェクト条件に応じた使い分け基準を決める

## 技術ポイント
- ng-contentを成り立たせる主要API/構成要素
- Layoutコンポーネントで押さえる設定やコード記述
- 両者を共存・移行させるためのブリッジ手法

## 📺 画面表示用コード（動画用）
**ng-content派：Slotで構成**
```typescript
<section class="shell">
  <header><ng-content select="[header]"></ng-content></header>
  <main><ng-content></ng-content></main>
</section>
```

**Layoutコンポーネント派：Inputsで渡す**
```typescript
@Component({
  selector: 'app-dashboard-layout',
  standalone: true,
  template: `
    <header><ng-container *ngTemplateOutlet="header"></ng-container></header>
    <main><ng-content></ng-content></main>
  `,
})
export class DashboardLayoutComponent {
  @Input({ required: true }) header!: TemplateRef<unknown>;
}
```

## 💻 詳細実装例（学習用）
```typescript
<app-dashboard-layout [header]="headerTpl">
  <p>content</p>
</app-dashboard-layout>

<ng-template #headerTpl>
  <h1>Title</h1>
</ng-template>
```

## ベストプラクティス
- ng-contentを使う場合は`select`でスロットを明示し、使い方をドキュメント化する
- Layoutコンポーネントは`TemplateRef`や`Portal`をInputにし、可読性と型安全性を両立させる
- Slot構造の共通スタイルをglobalで管理しつつ、挿入する内容はcomponent styleで調整する

## 注意点
- ng-contentは子要素のChangeDetection戦略に影響されるため、投影元と整合を取る
- Layoutコンポーネントを増やしすぎるとネストが深くなるので粒度を決める
- TemplateRefをInputにする場合はnullチェックを徹底する

## 関連技術
- Content Projection
- TemplateRef
- Standalone Layout
