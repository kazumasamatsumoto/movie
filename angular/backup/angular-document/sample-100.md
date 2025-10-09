# #100 「@Input() 関数の受け渡し」

## 概要
親コンポーネントから子へコールバック関数を渡し、子が特定のタイミングで親のロジックを呼び出す方法を学びます。

## 学習目標
- 関数型の@Input()宣言方法を理解する
- コールバック呼び出し時のthis束縛に注意する
- 関数を渡す場合と@Output()で通知する場合の使い分けを把握する

## 技術ポイント
- **型注釈**: `@Input() onSelect: (id: number) => void = () => {};`
- **バインド**: 親で`(id) => this.handleSelect(id)`のように渡す
- **use-case**: UIレンダリング以外の戦略ロジックを親に委譲できる


```typescript
@Input() onAction: () => void = () => {};
```

```html
<button type="button" (click)="onAction()">実行</button>
```

```html
<app-toolbar [onAction]="handleAction"></app-toolbar>
```

## 💻 詳細実装例（学習用）
```typescript
// toolbar.component.ts
import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-toolbar',
  standalone: true,
  templateUrl: './toolbar.component.html',
})
export class ToolbarComponent {
  @Input() onRefresh: () => void = () => {};
  @Input() onExport: () => void = () => {};
}
```

```html
<!-- toolbar.component.html -->
<div class="toolbar">
  <button type="button" (click)="onRefresh()">更新</button>
  <button type="button" (click)="onExport()">エクスポート</button>
</div>
```

```typescript
// parent.component.ts
import { Component } from '@angular/core';
import { ToolbarComponent } from './toolbar.component';

@Component({
  selector: 'app-report-page',
  standalone: true,
  imports: [ToolbarComponent],
  template: `
    <app-toolbar
      [onRefresh]="handleRefresh"
      [onExport]="handleExport"
    ></app-toolbar>
  `,
})
export class ReportPageComponent {
  handleRefresh = () => {
    console.log('レポートを更新');
  };

  handleExport = () => {
    console.log('CSVを書き出し');
  };
}
```

## ベストプラクティス
- 初期値として空関数を用意し、親が渡さなくても実行時エラーにならないようにする
- 親から渡す関数はアロー関数で定義し、this文脈の問題を避ける
- 関数が複雑になってきたら@Output()によるイベント通知へ切り替えを検討する

## 注意点
- 関数を何度も新しい参照で渡すとChangeDetectionで毎回差分と見なされるため、`handleClick = this.handleClick.bind(this)`などで安定させる
- 子で関数を遅延実行したい場合はエラーが起きないようにtry/catchを入れる
- 関数と@Output()を併用すると混乱を招くため、チーム内でルールを決める

## 関連技術
- RxJS Subjectsでの通知
- Signalsによる状態管理と関数渡しの違い
- Angularスタイルガイド（Input/Outputの使い分け）
