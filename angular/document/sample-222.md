# #222 「ViewContainerRef の基本」

## 概要
ViewContainerRefは、動的にビューやコンポーネントを挿入するためのコンテナを表すクラスです。テンプレート内の特定の位置に、プログラム的にコンポーネントを追加・削除する機能を提供します。

## 学習目標
- ViewContainerRefの役割を理解する
- ViewContainerRefの取得方法を習得する
- 基本的なメソッドの使い方を学ぶ

## 技術ポイント
- **挿入ポイントの管理**: ビューを挿入する場所を表現
- **@ViewChild での取得**: read オプションで ViewContainerRef を指定
- **主要メソッド**: createComponent(), clear(), insert(), remove()

## 📺 画面表示用コード

### ViewContainerRef の取得
```typescript
@Component({
  template: `<div #container></div>`
})
export class HostComponent {
  @ViewChild('container', { read: ViewContainerRef })
  container!: ViewContainerRef;
}
```

### コンポーネントの動的挿入
```typescript
ngAfterViewInit() {
  const componentRef = this.container.createComponent(AlertComponent);
}
```

### inject()での取得（v14+推奨）
```typescript
export class HostComponent {
  private container = viewChild('container', { read: ViewContainerRef });

  addComponent() {
    this.container()?.createComponent(AlertComponent);
  }
}
```

## 実践的な活用例

### 複数の挿入ポイント管理
```typescript
@Component({
  template: `
    <div class="header">
      <div #headerContainer></div>
    </div>
    <div class="main">
      <div #mainContainer></div>
    </div>
    <div class="footer">
      <div #footerContainer></div>
    </div>
  `
})
export class LayoutComponent {
  @ViewChild('headerContainer', { read: ViewContainerRef })
  headerContainer!: ViewContainerRef;

  @ViewChild('mainContainer', { read: ViewContainerRef })
  mainContainer!: ViewContainerRef;

  @ViewChild('footerContainer', { read: ViewContainerRef })
  footerContainer!: ViewContainerRef;

  loadHeader() {
    this.headerContainer.createComponent(HeaderWidgetComponent);
  }

  loadMain() {
    this.mainContainer.createComponent(DashboardComponent);
  }

  loadFooter() {
    this.footerContainer.createComponent(FooterComponent);
  }
}
```

### ディレクティブでの ViewContainerRef
```typescript
@Directive({
  selector: '[dynamicHost]',
  standalone: true
})
export class DynamicHostDirective {
  // ディレクティブ内で自動的に ViewContainerRef を取得
  viewContainer = inject(ViewContainerRef);

  loadComponent(component: Type<any>) {
    this.viewContainer.clear();
    return this.viewContainer.createComponent(component);
  }
}

// 使用例
@Component({
  template: `<ng-container dynamicHost></ng-container>`
})
export class AppComponent {
  @ViewChild(DynamicHostDirective)
  dynamicHost!: DynamicHostDirective;

  load() {
    this.dynamicHost.loadComponent(MyComponent);
  }
}
```

### インデックスを指定した挿入
```typescript
export class ContainerComponent {
  @ViewChild('container', { read: ViewContainerRef })
  container!: ViewContainerRef;

  // 先頭に挿入
  insertAtBeginning() {
    this.container.createComponent(Component1, { index: 0 });
  }

  // 2番目に挿入
  insertAtPosition() {
    this.container.createComponent(Component2, { index: 1 });
  }

  // 末尾に挿入（デフォルト）
  insertAtEnd() {
    this.container.createComponent(Component3);
  }
}
```

## ベストプラクティス

### ng-container を挿入先として使用
```typescript
// ✅ 推奨: ng-container はレンダリング後に残らない
@Component({
  template: `<ng-container #container></ng-container>`
})
export class HostComponent {
  @ViewChild('container', { read: ViewContainerRef })
  container!: ViewContainerRef;
}

// ❌ 非推奨: div は DOM に余分な要素として残る
@Component({
  template: `<div #container></div>`
})
export class HostComponent {}
```

### ViewContainerRef の存在確認
```typescript
export class SafeHostComponent {
  @ViewChild('container', { read: ViewContainerRef })
  container?: ViewContainerRef;

  addComponent() {
    if (this.container) {
      this.container.createComponent(MyComponent);
    } else {
      console.error('ViewContainerRef が取得できませんでした');
    }
  }
}
```

### ライフサイクルフックでの使用
```typescript
export class TimingComponent implements AfterViewInit {
  @ViewChild('container', { read: ViewContainerRef })
  container!: ViewContainerRef;

  ngAfterViewInit() {
    // ✅ AfterViewInit 以降で使用
    this.container.createComponent(MyComponent);
  }

  ngOnInit() {
    // ❌ OnInit では ViewContainerRef はまだ未定義
    // this.container.createComponent(MyComponent); // エラー!
  }
}
```

## 注意点

### ライフサイクルのタイミング
`@ViewChild`で取得したViewContainerRefは、`ngAfterViewInit()`以降でないと利用できません。`ngOnInit()`では未定義です。

### メモリ管理
ViewContainerRefに挿入したコンポーネントは、`clear()`や`remove()`で明示的に削除するか、親コンポーネントの破棄時に自動削除されます。

### 複数回の createComponent
同じViewContainerRefに対して複数回`createComponent()`を呼ぶと、コンポーネントが追加されていきます。置き換えたい場合は先に`clear()`を呼びます。

### インデックス範囲
`index`オプションに範囲外の値を指定するとエラーになります。現在のコンポーネント数（`container.length`）を超えない値を指定してください。

## 関連技術
- **ComponentRef**: 生成されたコンポーネントへの参照
- **TemplateRef**: テンプレートの参照（ng-template用）
- **ViewChild**: ビュー要素の取得
- **Directive**: カスタムディレクティブでのViewContainerRef活用
- **ElementRef**: DOM要素への直接アクセス
