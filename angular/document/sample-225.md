# #225 「動的 Component の作成」

## 概要
動的コンポーネントの作成は、ViewContainerRefを取得し、createComponent()メソッドを呼び出すことで実現します。生成されたComponentRefを適切に管理することで、後から操作や削除が可能になります。

## 学習目標
- 動的コンポーネント作成の基本手順を習得する
- ComponentRefの管理方法を理解する
- 実践的な作成パターンを学ぶ

## 技術ポイント
- **ViewContainerRefの取得**: @ViewChildまたはinject()で取得
- **createComponent()の呼び出し**: コンポーネントタイプを指定
- **ComponentRefの保持**: 後続操作のために参照を保存

## 📺 画面表示用コード

### 基本的な作成手順
```typescript
@Component({
  template: `<ng-container #container></ng-container>`
})
export class HostComponent implements AfterViewInit {
  @ViewChild('container', { read: ViewContainerRef })
  container!: ViewContainerRef;

  ngAfterViewInit() {
    const componentRef = this.container.createComponent(AlertComponent);
  }
}
```

### ボタンクリックで作成
```typescript
@Component({
  template: `
    <button (click)="addAlert()">アラート追加</button>
    <ng-container #container></ng-container>
  `
})
export class DynamicHostComponent {
  @ViewChild('container', { read: ViewContainerRef })
  container!: ViewContainerRef;

  addAlert() {
    this.container.createComponent(AlertComponent);
  }
}
```

### ComponentRef の保持
```typescript
export class ManagedHostComponent {
  private container = inject(ViewContainerRef);
  private componentRef?: ComponentRef<AlertComponent>;

  create() {
    this.componentRef = this.container.createComponent(AlertComponent);
  }

  destroy() {
    this.componentRef?.destroy();
  }
}
```

## 実践的な活用例

### 完全な実装例
```typescript
@Component({
  selector: 'app-notification-container',
  template: `
    <div class="notification-area">
      <ng-container #notificationContainer></ng-container>
    </div>
  `,
  standalone: true
})
export class NotificationContainerComponent implements AfterViewInit, OnDestroy {
  @ViewChild('notificationContainer', { read: ViewContainerRef })
  container!: ViewContainerRef;

  private notifications: ComponentRef<NotificationComponent>[] = [];

  ngAfterViewInit() {
    // 初期通知を表示
    this.addNotification('アプリケーションを開始しました', 'success');
  }

  addNotification(message: string, type: 'success' | 'error' | 'info') {
    const componentRef = this.container.createComponent(NotificationComponent);
    componentRef.setInput('message', message);
    componentRef.setInput('type', type);

    this.notifications.push(componentRef);

    // 3秒後に自動削除
    setTimeout(() => {
      this.removeNotification(componentRef);
    }, 3000);
  }

  removeNotification(ref: ComponentRef<NotificationComponent>) {
    const index = this.notifications.indexOf(ref);
    if (index !== -1) {
      this.notifications.splice(index, 1);
      ref.destroy();
    }
  }

  ngOnDestroy() {
    // 全ての通知を削除
    this.notifications.forEach(ref => ref.destroy());
  }
}
```

### モーダルダイアログの作成
```typescript
@Injectable({ providedIn: 'root' })
export class ModalService {
  private appRef = inject(ApplicationRef);
  private injector = inject(Injector);
  private document = inject(DOCUMENT);

  open<T>(component: Type<T>, data?: any): ComponentRef<T> {
    // 1. コンポーネントを作成
    const componentRef = createComponent(component, {
      environmentInjector: this.appRef.injector,
      elementInjector: this.injector
    });

    // 2. DOMに追加
    this.appRef.attachView(componentRef.hostView);
    const domElem = (componentRef.hostView as EmbeddedViewRef<any>)
      .rootNodes[0] as HTMLElement;
    this.document.body.appendChild(domElem);

    // 3. データを設定
    if (data) {
      Object.assign(componentRef.instance, data);
    }

    return componentRef;
  }

  close(componentRef: ComponentRef<any>) {
    this.appRef.detachView(componentRef.hostView);
    componentRef.destroy();
  }
}

// 使用例
@Component({})
export class AppComponent {
  private modalService = inject(ModalService);

  openModal() {
    const modalRef = this.modalService.open(ConfirmModalComponent, {
      title: '確認',
      message: '本当に削除しますか？'
    });
  }
}
```

### タブシステムの実装
```typescript
@Component({
  selector: 'app-tab-container',
  template: `
    <div class="tab-buttons">
      @for (tab of tabs; track tab.id) {
        <button (click)="selectTab(tab)">{{ tab.title }}</button>
      }
      <button (click)="addTab()">+ タブ追加</button>
    </div>
    <div class="tab-content">
      <ng-container #tabContent></ng-container>
    </div>
  `
})
export class TabContainerComponent {
  @ViewChild('tabContent', { read: ViewContainerRef })
  contentContainer!: ViewContainerRef;

  tabs: Array<{ id: number; title: string; componentRef?: ComponentRef<any> }> = [];
  private tabCounter = 0;

  addTab() {
    const tabId = ++this.tabCounter;
    const tab = {
      id: tabId,
      title: `タブ ${tabId}`,
      componentRef: undefined
    };
    this.tabs.push(tab);
    this.selectTab(tab);
  }

  selectTab(tab: any) {
    // 既存のタブを非表示
    this.contentContainer.clear();

    // タブのコンポーネントを作成（初回のみ）
    if (!tab.componentRef) {
      tab.componentRef = this.contentContainer.createComponent(TabContentComponent);
      tab.componentRef.setInput('tabId', tab.id);
    } else {
      // 既存のコンポーネントを再挿入
      this.contentContainer.insert(tab.componentRef.hostView);
    }
  }

  removeTab(tab: any) {
    tab.componentRef?.destroy();
    const index = this.tabs.indexOf(tab);
    this.tabs.splice(index, 1);
  }
}
```

### ウィジェットダッシュボード
```typescript
export interface WidgetConfig {
  type: Type<any>;
  title: string;
  position: number;
}

@Component({
  selector: 'app-dashboard',
  template: `
    <div class="dashboard">
      @for (config of widgetConfigs; track config.title) {
        <div class="widget-wrapper">
          <h3>{{ config.title }}</h3>
          <ng-container #widgetContainer></ng-container>
        </div>
      }
    </div>
  `
})
export class DashboardComponent implements AfterViewInit {
  @ViewChildren('widgetContainer', { read: ViewContainerRef })
  containers!: QueryList<ViewContainerRef>;

  widgetConfigs: WidgetConfig[] = [
    { type: ChartWidgetComponent, title: 'グラフ', position: 0 },
    { type: StatsWidgetComponent, title: '統計', position: 1 },
    { type: ActivityWidgetComponent, title: 'アクティビティ', position: 2 }
  ];

  ngAfterViewInit() {
    this.containers.forEach((container, index) => {
      const config = this.widgetConfigs[index];
      container.createComponent(config.type);
    });
  }
}
```

## ベストプラクティス

### ライフサイクルの適切な使用
```typescript
// ✅ ngAfterViewInit で作成
ngAfterViewInit() {
  this.container.createComponent(MyComponent);
}

// ❌ ngOnInit では ViewChild が未定義
ngOnInit() {
  // this.container は undefined!
}
```

### ComponentRef の管理
```typescript
// ✅ 配列で複数管理
private refs: ComponentRef<any>[] = [];

addComponent() {
  const ref = this.container.createComponent(MyComponent);
  this.refs.push(ref);
}

ngOnDestroy() {
  this.refs.forEach(ref => ref.destroy());
}
```

### エラーハンドリング
```typescript
safeCreate() {
  if (!this.container) {
    console.error('ViewContainerRef が未定義です');
    return;
  }

  try {
    return this.container.createComponent(MyComponent);
  } catch (error) {
    console.error('コンポーネント生成エラー:', error);
    return null;
  }
}
```

## 注意点

### ViewChild の取得タイミング
`@ViewChild`で取得したViewContainerRefは、`ngAfterViewInit()`以降でないと使用できません。

### メモリリーク防止
生成したComponentRefは、不要になったら必ず`destroy()`を呼び出してメモリリークを防ぎます。

### Change Detection
動的に生成されたコンポーネントも通常の変更検知サイクルに含まれますが、手動で`detectChanges()`を呼ぶ必要がある場合もあります。

### 複数回の createComponent
同じViewContainerRefに対して複数回`createComponent()`を呼ぶと、コンポーネントが追加されます。置き換えたい場合は`clear()`を先に呼びます。

## 関連技術
- **ViewContainerRef**: コンテナの管理
- **ComponentRef**: コンポーネント参照
- **AfterViewInit**: ライフサイクルフック
- **QueryList**: 複数のViewChild管理
- **OnDestroy**: クリーンアップ処理
