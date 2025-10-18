# #134 「ViewChild 子コンポーネント参照」

## 概要
親コンポーネントから子コンポーネントのインスタンスを参照して、公開メソッドやプロパティを利用する方法を学びます。

## 学習目標
- 子コンポーネントを型指定で取得する`@ViewChild`の構文を理解する
- 子から公開されたメソッドを親が呼び出す手順を習得する
- 密結合を避けるためのガイドラインを把握する

## 技術ポイント
- **型指定**: `@ViewChild(ChildComponent) child?: ChildComponent;`
- **インスタンスアクセス**: `child?.refresh()`のようにメソッドを呼び出す
- **公開API設計**: 親が利用するメソッドはpublicとして明示的に公開する

```typescript
@ViewChild(ChildWidget)
widget?: ChildWidget;
```

```typescript
this.widget?.refresh();
```

```html
<app-child-widget></app-child-widget>
```

## 💻 詳細実装例（学習用）
```typescript
// child-widget.component.ts
import { Component } from '@angular/core';

@Component({
  selector: 'app-child-widget',
  standalone: true,
  template: `<p>子コンポーネント</p>`,
})
export class ChildWidgetComponent {
  refresh(): void {
    console.log('ChildWidget refreshed');
  }
}
```

```typescript
// parent.component.ts
import { AfterViewInit, Component, ViewChild } from '@angular/core';
import { ChildWidgetComponent } from './child-widget.component';

@Component({
  selector: 'app-parent',
  standalone: true,
  imports: [ChildWidgetComponent],
  templateUrl: './parent.component.html',
})
export class ParentComponent implements AfterViewInit {
  @ViewChild(ChildWidgetComponent)
  child?: ChildWidgetComponent;

  ngAfterViewInit(): void {
    this.child?.refresh();
  }

  handleClick(): void {
    this.child?.refresh();
  }
}
```

```html
<!-- parent.component.html -->
<app-child-widget></app-child-widget>
<button type="button" (click)="handleClick()">子を更新</button>
```

## ベストプラクティス
- 親が呼び出すメソッドはコンポーネントのpublic APIとしてドキュメント化する
- 双方向依存を避け、可能なら@Outputイベントで通知する設計を優先する
- @ViewChildで取得した参照は存在確認を行い、テスト環境でも安全に扱う

## 注意点
- 子コンポーネントのライフサイクルが完了する前に呼び出すとエラーになる
- *ngIfで子を切り替える場合は参照がnullになるため、変更検知の度にチェックが必要
- 過度にメソッド呼び出しに依存すると親子の結合度が高まりテストが難しくなる

## 関連技術
- `@ViewChildren`で複数子コンポーネントを参照する
- `@Output()`によるイベント通知
- AngularのDIで親から子へ依存を渡すパターン
