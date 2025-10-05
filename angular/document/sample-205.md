# #205 「ngTemplateOutlet の活用」

## 概要
Angular v20のngTemplateOutletを使用して動的なテンプレート投影を制御する方法を学習します。

## 学習目標
- ngTemplateOutletでの動的テンプレート投影方法を理解する
- 実行時のテンプレート切り替えを習得する
- 動的なテンプレート投影制御を実現できるようになる

## 技術ポイント
- ngTemplateOutlet
- 動的テンプレート投影
- 実行時切り替え

## 📺 画面表示用コード

```html
<!-- 親コンポーネント -->
<app-dynamic-template [templateType]="currentTemplate">
  <ng-template #headerTemplate>
    <h1>ヘッダーテンプレート</h1>
  </ng-template>
  <ng-template #contentTemplate>
    <p>コンテンツテンプレート</p>
  </ng-template>
  <ng-template #footerTemplate>
    <footer>フッターテンプレート</footer>
  </ng-template>
</app-dynamic-template>
```

```html
<!-- 子コンポーネント（app-dynamic-template） -->
<div class="dynamic-container">
  <ng-container [ngTemplateOutlet]="getTemplate()"></ng-container>
</div>
```

```typescript
// コンポーネントクラス
@ContentChild('headerTemplate') headerTemplate!: TemplateRef<any>;
@ContentChild('contentTemplate') contentTemplate!: TemplateRef<any>;
@ContentChild('footerTemplate') footerTemplate!: TemplateRef<any>;

getTemplate(): TemplateRef<any> {
  switch (this.templateType) {
    case 'header': return this.headerTemplate;
    case 'content': return this.contentTemplate;
    case 'footer': return this.footerTemplate;
    default: return this.contentTemplate;
  }
}
```

## 実践的な活用例

```html
<!-- 動的レイアウト -->
<app-layout-switcher [layoutType]="selectedLayout">
  <ng-template #gridLayout>
    <div class="grid">グリッドレイアウト</div>
  </ng-template>
  <ng-template #listLayout>
    <div class="list">リストレイアウト</div>
  </ng-template>
  <ng-template #cardLayout>
    <div class="cards">カードレイアウト</div>
  </ng-template>
</app-layout-switcher>
```

## ベストプラクティス
- テンプレートの切り替えロジックを明確にする
- デフォルトのテンプレートを用意する
- テンプレートの依存関係を最小限にする

## 注意点
- テンプレート参照の存在チェック
- 動的切り替えのパフォーマンス
- メモリリークの防止

## 関連技術
- Template References
- Dynamic Components
- Template Outlets
