# #299 「Tab Component - タブシステム」

## 概要
Tab Componentは複数のコンテンツをタブ切り替えで表示するUIで、アクセシビリティ対応のロービングタブインデックスとARIA属性を備えたコンポーネントである。

## 学習目標
- タブリストとパネルのARIA属性を設定する
- キーボード操作を実装する
- Lazy loadやSignalで状態を管理する

## 技術ポイント
- roving tabindex
- aria-controls / aria-labelledby
- Signalsでアクティブタブ管理

## 📺 画面表示用コード（動画用）
```typescript
export interface TabItem {
  readonly id: string;
  readonly label: string;
  readonly content: string;
}
```

```typescript
@Component({ selector: 'app-tabs', standalone: true, template: `<div class="tabs" role="tablist" (keydown)="onKeydown($event)">@for (tab of tabs; let i = $index; track tab.id) {<button type="button" role="tab" [id]="tab.id" [attr.aria-selected]="activeIndex===i" [attr.aria-controls]="panelId(tab)" [tabIndex]="activeIndex===i ? 0 : -1" (click)="activate(i)">{{ tab.label }}</button>}</div><section class="tabs__panel" role="tabpanel" [id]="panelId(tabs[activeIndex])" [attr.aria-labelledby]="tabs[activeIndex]?.id">{{ tabs[activeIndex]?.content }}</section>`, changeDetection: ChangeDetectionStrategy.OnPush })
export class TabsComponent {
  @Input({ required: true }) tabs: ReadonlyArray<TabItem> = [];
  activeIndex = 0;
  activate(index: number): void { this.activeIndex = index; }
  panelId(tab: TabItem): string { return `${tab.id}-panel`; }
  onKeydown(event: KeyboardEvent): void {
    const last = this.tabs.length - 1;
    if (event.key === 'ArrowRight') this.activate((this.activeIndex + 1) % this.tabs.length);
    if (event.key === 'ArrowLeft') this.activate((this.activeIndex + last) % this.tabs.length);
    if (event.key === 'Home') this.activate(0);
    if (event.key === 'End') this.activate(last);
  }
}
```

```html
<app-tabs [tabs]="tabItems"></app-tabs>
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-tabs-demo',
  standalone: true,
  imports: [TabsComponent],
  template: `
    <app-tabs [tabs]="tabs"></app-tabs>
  `,
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class TabsDemoComponent {
  readonly tabs: ReadonlyArray<TabItem> = [
    { id: 'overview', label: '概要', content: 'プロジェクト概要を表示します。' },
    { id: 'metrics', label: 'メトリクス', content: '主要な指標を確認できます。' },
    { id: 'history', label: '履歴', content: '更新履歴を参照します。' }
  ];
}
```

## ベストプラクティス
- aria-selected/aria-controlsを設定し支援技術で文脈を伝える
- キーボード操作を仕様通りにサポートし操作感を統一する
- タブ配列はユニークなidを採番し衝突を避ける

## 注意点
- コンテンツが重い場合はLazy Loadしパフォーマンスを確保する
- overflow時は横スクロールや折返しを検討する
- 選択状態とフォーカススタイルを分けて表示する

## 関連技術
- Accessibility
- Keyboard Navigation
- Signals
