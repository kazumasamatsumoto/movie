# #238 「動的タブシステム」

## 概要
動的タブシステムは、実行時にタブの追加・削除・切り替えが可能なUI機構です。動的コンポーネント生成とViewContainerRefの操作を組み合わせ、タブごとに異なるコンポーネントを表示し、状態を保持できます。

## 学習目標
- 動的タブの追加・削除機能を実装できる
- タブ状態の保持と復元方法を理解する
- パフォーマンスを考慮したタブ管理を学ぶ

## 技術ポイント
- **タブ管理**: 配列/Mapでの状態管理
- **コンテンツ切り替え**: detach/attachでの表示制御
- **状態保持**: コンポーネントの破棄せずに保存

## 📺 画面表示用コード

### 基本的なタブ構造
```typescript
interface Tab {
  id: string;
  title: string;
  component: Type<any>;
  data?: any;
}

tabs = signal<Tab[]>([]);
activeTabId = signal<string>('');
```

### タブ追加
```typescript
addTab(title: string, component: Type<any>) {
  const tab: Tab = {
    id: crypto.randomUUID(),
    title,
    component
  };
  this.tabs.update(tabs => [...tabs, tab]);
  this.activateTab(tab.id);
}
```

### タブ切り替え
```typescript
activateTab(tabId: string) {
  this.container.clear();
  const tab = this.tabs().find(t => t.id === tabId);
  if (tab) {
    this.container.createComponent(tab.component);
    this.activeTabId.set(tabId);
  }
}
```

## 実践的な活用例(continued)

### 完全なタブシステム実装
```typescript
interface TabConfig {
  id: string;
  title: string;
  component: Type<any>;
  data?: any;
  closable?: boolean;
}

interface TabState {
  ref?: ComponentRef<any>;
  config: TabConfig;
}

@Component({
  selector: 'app-dynamic-tabs',
  template: `
    <div class="tab-header">
      @for (tab of tabs(); track tab.id) {
        <div
          class="tab"
          [class.active]="activeTabId() === tab.id"
          (click)="activateTab(tab.id)">
          {{ tab.title }}
          @if (tab.closable) {
            <button (click)="closeTab(tab.id); $event.stopPropagation()">
              ×
            </button>
          }
        </div>
      }
      <button (click)="addNewTab()">+ タブ追加</button>
    </div>
    <div class="tab-content">
      <ng-container #tabContent></ng-container>
    </div>
  `
})
export class DynamicTabsComponent {
  @ViewChild('tabContent', { read: ViewContainerRef })
  container!: ViewContainerRef;

  tabs = signal<TabConfig[]>([]);
  activeTabId = signal<string>('');

  private tabStates = new Map<string, TabState>();
  private tabCounter = 0;

  addTab(config: TabConfig) {
    this.tabs.update(tabs => [...tabs, config]);
    this.tabStates.set(config.id, { config });
    this.activateTab(config.id);
  }

  addNewTab() {
    const id = `tab-${++this.tabCounter}`;
    this.addTab({
      id,
      title: `タブ ${this.tabCounter}`,
      component: DefaultTabContentComponent,
      closable: true
    });
  }

  activateTab(tabId: string) {
    // 現在のタブを非表示（破棄しない）
    const currentId = this.activeTabId();
    if (currentId) {
      this.detachTab(currentId);
    }

    // 新しいタブを表示
    this.attachTab(tabId);
    this.activeTabId.set(tabId);
  }

  closeTab(tabId: string) {
    const state = this.tabStates.get(tabId);
    if (state?.ref) {
      state.ref.destroy();
    }

    this.tabStates.delete(tabId);
    this.tabs.update(tabs => tabs.filter(t => t.id !== tabId));

    // アクティブタブが閉じられた場合
    if (this.activeTabId() === tabId) {
      const remainingTabs = this.tabs();
      if (remainingTabs.length > 0) {
        this.activateTab(remainingTabs[0].id);
      }
    }
  }

  private detachTab(tabId: string) {
    const state = this.tabStates.get(tabId);
    if (state?.ref) {
      const index = this.container.indexOf(state.ref.hostView);
      if (index !== -1) {
        this.container.detach(index);
      }
    }
  }

  private attachTab(tabId: string) {
    let state = this.tabStates.get(tabId);

    if (!state?.ref) {
      // 初回: コンポーネント生成
      const ref = this.container.createComponent(state!.config.component);
      if (state!.config.data) {
        ref.setInput('data', state!.config.data);
      }
      state!.ref = ref;
    } else {
      // 2回目以降: ビューを再アタッチ
      this.container.insert(state.ref.hostView);
    }
  }

  ngOnDestroy() {
    this.tabStates.forEach(state => state.ref?.destroy());
  }
}
```

### ルーティング連動タブ
```typescript
export class RoutedTabsComponent {
  private router = inject(Router);
  private route = inject(ActivatedRoute);

  tabs = signal<TabConfig[]>([
    { id: 'home', title: 'ホーム', component: HomeComponent },
    { id: 'settings', title: '設定', component: SettingsComponent }
  ]);

  ngOnInit() {
    // URLからアクティブタブを復元
    this.route.queryParams.subscribe(params => {
      const tabId = params['tab'];
      if (tabId) {
        this.activateTab(tabId);
      }
    });
  }

  activateTab(tabId: string) {
    // タブ切り替え処理
    this.activeTabId.set(tabId);

    // URLを更新
    this.router.navigate([], {
      queryParams: { tab: tabId },
      queryParamsHandling: 'merge'
    });
  }
}
```

### 遅延ロード対応タブ
```typescript
interface LazyTabConfig {
  id: string;
  title: string;
  loader: () => Promise<Type<any>>;
}

export class LazyTabsComponent {
  private container = inject(ViewContainerRef);
  private loadedComponents = new Map<string, Type<any>>();

  async activateTab(config: LazyTabConfig) {
    // キャッシュチェック
    let component = this.loadedComponents.get(config.id);

    if (!component) {
      // ローディング表示
      const loading = this.container.createComponent(LoadingComponent);

      // コンポーネント遅延ロード
      component = await config.loader();
      this.loadedComponents.set(config.id, component);

      loading.destroy();
    }

    // コンポーネント表示
    this.container.clear();
    this.container.createComponent(component);
  }
}
```

### ドラッグ&ドロップでの並び替え
```typescript
export class DraggableTabsComponent {
  tabs = signal<TabConfig[]>([]);

  onDragStart(event: DragEvent, index: number) {
    event.dataTransfer!.effectAllowed = 'move';
    event.dataTransfer!.setData('text/plain', index.toString());
  }

  onDrop(event: DragEvent, dropIndex: number) {
    event.preventDefault();
    const dragIndex = parseInt(event.dataTransfer!.getData('text/plain'));

    this.tabs.update(tabs => {
      const newTabs = [...tabs];
      const [removed] = newTabs.splice(dragIndex, 1);
      newTabs.splice(dropIndex, 0, removed);
      return newTabs;
    });
  }

  onDragOver(event: DragEvent) {
    event.preventDefault();
    event.dataTransfer!.dropEffect = 'move';
  }
}
```

### タブグループ管理
```typescript
interface TabGroup {
  id: string;
  name: string;
  tabs: TabConfig[];
}

export class TabGroupsComponent {
  groups = signal<TabGroup[]>([]);
  activeGroup = signal<string>('');

  addGroup(name: string) {
    const group: TabGroup = {
      id: crypto.randomUUID(),
      name,
      tabs: []
    };
    this.groups.update(groups => [...groups, group]);
  }

  addTabToGroup(groupId: string, tab: TabConfig) {
    this.groups.update(groups =>
      groups.map(g =>
        g.id === groupId
          ? { ...g, tabs: [...g.tabs, tab] }
          : g
      )
    );
  }

  switchGroup(groupId: string) {
    this.activeGroup.set(groupId);
    const group = this.groups().find(g => g.id === groupId);
    if (group && group.tabs.length > 0) {
      this.activateTab(group.tabs[0].id);
    }
  }

  private activateTab(tabId: string) {
    // タブアクティベーション処理
  }
}
```

### タブ履歴管理
```typescript
export class TabHistoryComponent {
  private history: string[] = [];
  private historyIndex = -1;

  activateTab(tabId: string) {
    // 履歴に追加
    this.history = this.history.slice(0, this.historyIndex + 1);
    this.history.push(tabId);
    this.historyIndex = this.history.length - 1;

    // タブ表示
    this.showTab(tabId);
  }

  goBack() {
    if (this.historyIndex > 0) {
      this.historyIndex--;
      this.showTab(this.history[this.historyIndex]);
    }
  }

  goForward() {
    if (this.historyIndex < this.history.length - 1) {
      this.historyIndex++;
      this.showTab(this.history[this.historyIndex]);
    }
  }

  canGoBack(): boolean {
    return this.historyIndex > 0;
  }

  canGoForward(): boolean {
    return this.historyIndex < this.history.length - 1;
  }

  private showTab(tabId: string) {
    // タブ表示処理
  }
}
```

## ベストプラクティス

### 状態保持の最適化
```typescript
// ✅ detach/attachで状態保持
private switchTab(fromId: string, toId: string) {
  this.detachTab(fromId);
  this.attachTab(toId);
}

// ❌ 毎回破棄・再生成（状態が失われる）
private switchTab(fromId: string, toId: string) {
  this.destroyTab(fromId);
  this.createTab(toId);
}
```

### メモリ管理
```typescript
// ✅ 最大タブ数の制限
private MAX_TABS = 10;

addTab(config: TabConfig) {
  if (this.tabs().length >= this.MAX_TABS) {
    this.closeOldestTab();
  }
  // タブ追加処理
}
```

### アクセシビリティ
```typescript
// ✅ ARIA属性の設定
<div
  role="tab"
  [attr.aria-selected]="tab.id === activeTabId()"
  [attr.aria-controls]="'panel-' + tab.id">
  {{ tab.title }}
</div>
```

## 注意点

### パフォーマンス
多数のタブを開くとメモリ使用量が増加します。非アクティブタブの破棄や仮想化を検討してください。

### 状態同期
タブ間でデータを共有する場合、Serviceやストア管理を使用してください。

### ルーティング
SPAでタブとルーティングを併用する場合、状態の同期に注意が必要です。

### メモリリーク
タブを閉じる際、イベントリスナーや購読を確実に解除してください。

## 関連技術
- **ViewContainerRef**: コンテナ管理
- **detach/attach**: ビュー制御
- **Router**: ルーティング連携
- **Drag and Drop API**: タブ並び替え
- **LocalStorage**: タブ状態の永続化
