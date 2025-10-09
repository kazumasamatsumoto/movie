# #075 「親子コンポーネントの Lifecycle 順序」

## 概要
親子コンポーネント間でLifecycle Hooksがどの順番で実行されるかを学び、データフローのタイミングを正しく設計します。

## 学習目標
- 親→子の初期化・破棄順序を理解する
- 子コンポーネントの参照を得るタイミングを把握する
- 親子間のフックを活用した同期処理パターンを学ぶ

## 技術ポイント
- **初期化**: 親`ngOnChanges`→親`ngOnInit`→親`ngAfterContentInit`→子`ngOnInit`→子`ngAfterViewInit`→親`ngAfterViewInit`
- **破棄**: 子の`ngOnDestroy`が先、次に親
- **データ同期**: 親から子への@Inputは親`ngOnChanges`より先に反映される


```typescript
@Component({ selector: 'app-parent', ... })
```

```typescript
@Component({ selector: 'app-child', ... })
```

```html
<app-child [value]="count"></app-child>
```

## 💻 詳細実装例（学習用）
```typescript
import { AfterViewInit, Component, Input, OnDestroy, OnInit } from '@angular/core';

@Component({
  selector: 'app-child',
  standalone: true,
  template: `<p>Child value: {{ value }}</p>`,
})
export class ChildComponent implements OnInit, AfterViewInit, OnDestroy {
  @Input() value = 0;

  ngOnInit(): void {
    console.log('Child OnInit');
  }
  ngAfterViewInit(): void {
    console.log('Child AfterViewInit');
  }
  ngOnDestroy(): void {
    console.log('Child OnDestroy');
  }
}

@Component({
  selector: 'app-parent',
  standalone: true,
  imports: [ChildComponent],
  templateUrl: './parent.component.html',
})
export class ParentComponent implements OnInit, AfterViewInit, OnDestroy {
  value = 1;

  ngOnInit(): void {
    console.log('Parent OnInit');
  }
  ngAfterViewInit(): void {
    console.log('Parent AfterViewInit');
  }
  ngOnDestroy(): void {
    console.log('Parent OnDestroy');
  }
}
```

```html
<app-child [value]="value"></app-child>
```

## ベストプラクティス
- 親から子への初期値依存ロジックは親`ngAfterViewInit`で子のViewChildを利用する
- 子から親へイベントを通知する場合は`@Output`でデータフローを制御する
- 破棄順序を意識して子コンポーネントが使っているリソースを先に解放する

## 注意点
- `ngOnChanges`の順序は親→子で入力が渡されるが、子の内容投影後に親の`ngAfterContentInit`が実行される点に注意
- `*ngIf`などで子コンポーネントを切り替えると、再作成時に再度フックが走る
- 親が`OnPush`で子がデフォルト戦略でも、順序は変わらない

## 関連技術
- `@ViewChild` / `@ContentChild` での子参照
- `@Output`とEventEmitter
- Angular DevToolsでのLifecycle可視化
