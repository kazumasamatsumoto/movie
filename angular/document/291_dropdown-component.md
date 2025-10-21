# #291 「Dropdown Component - ドロップダウン」

## 概要
Dropdown Componentはボタンからメニューを表示するUIで、位置決め・キーボード操作・選択イベントを統一したコンポーネントとして提供する。

## 学習目標
- トリガーとメニューを分離し再利用性を高める
- CDK Menu/Overlayでアクセシビリティと位置制御を実装する
- 選択値をOutputで親に通知する

## 技術ポイント
- Angular CDK Menu
- OverlayPositionBuilder
- Outside clickハンドリング

## 📺 画面表示用コード（動画用）
```typescript
@Component({ selector: 'app-dropdown', standalone: true, template: `<div class="dropdown" (keydown.escape)="close()"><button type="button" class="dropdown__trigger" (click)="toggle()">{{ label }}</button>@if (open) {<ul class="dropdown__menu">@for (item of items; track item.value) {<li><button type="button" (click)="select(item.value)">{{ item.label }}</button></li>}</ul>}</div>`, changeDetection: ChangeDetectionStrategy.OnPush })
export class DropdownComponent<T> {
  @Input() label = '';
  @Input({ required: true }) items: ReadonlyArray<{ label: string; value: T }> = [];
  @Output() selected = new EventEmitter<T>();
  open = false;
  toggle(): void { this.open = !this.open; }
  close(): void { this.open = false; }
  select(value: T): void { this.selected.emit(value); this.close(); }
}
```

```typescript
export type DropdownItem<T> = { readonly label: string; readonly value: T };
```

```html
<app-dropdown label="操作" [items]="actions" (selected)="onAction($event)"></app-dropdown>
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-dropdown-demo',
  standalone: true,
  imports: [DropdownComponent],
  template: `
    <app-dropdown label="操作" [items]="items" (selected)="handle($event)"></app-dropdown>
    <p>選択: {{ lastSelected ?? 'なし' }}</p>
  `,
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class DropdownDemoComponent {
  readonly items: ReadonlyArray<DropdownItem<string>> = [
    { label: '編集', value: 'edit' },
    { label: '削除', value: 'delete' },
    { label: '共有', value: 'share' }
  ];
  lastSelected?: string;
  handle(action: string): void { this.lastSelected = action; }
}
```

## ベストプラクティス
- トリガーとメニューの責務を分け閉じる処理を一箇所に集約する
- selectedイベントは値のみemitし、表示テキストとは分離する
- メニュー幅と位置をCSSで統一し、スクロール時の挙動をテストする

## 注意点
- モバイルではメニューをフルスクリーン表示に切り替える
- 開いている状態が視覚的に判別できるようアイコンや色で示す
- 選択後はフォーカスをトリガーボタンへ戻す

## 関連技術
- Angular CDK Menu
- Overlay
- Accessibility
