# #230 「複数の動的 Component 管理」

## 概要
複数の動的コンポーネントを効率的に管理するには、適切なデータ構造（配列、Map、Set等）で参照を保持し、一括操作や個別操作を実装します。順序管理、ID管理、階層管理など、用途に応じた管理パターンを選択することで、複雑な動的UIも効率的に構築できます。

## 学習目標
- 複数コンポーネントの管理パターンを習得する
- データ構造の適切な選択方法を理解する
- 一括操作と個別操作の実装方法を学ぶ

## 技術ポイント
- **配列管理**: 順序を保持した管理
- **Map管理**: IDベースのアクセス
- **一括操作**: 全コンポーネントへの操作

## 📺 画面表示用コード

### 配列での管理
```typescript
private components: ComponentRef<any>[] = [];

add() {
  const ref = this.container.createComponent(MyComponent);
  this.components.push(ref);
}

removeAll() {
  this.components.forEach(c => c.destroy());
  this.components = [];
}
```

### Mapでの管理
```typescript
private components = new Map<string, ComponentRef<any>>();

add(id: string) {
  const ref = this.container.createComponent(MyComponent);
  this.components.set(id, ref);
}

remove(id: string) {
  this.components.get(id)?.destroy();
  this.components.delete(id);
}
```

### 一括更新
```typescript
updateAll(data: any) {
  this.components.forEach(ref => {
    ref.setInput('data', data);
  });
}
```

## 実践的な活用例

### 通知管理システム
```typescript
interface Notification {
  id: string;
  message: string;
  type: 'success' | 'error' | 'info';
  duration: number;
}

@Injectable({ providedIn: 'root' })
export class NotificationManager {
  private container = inject(ViewContainerRef);
  private notifications = new Map<string, {
    ref: ComponentRef<NotificationComponent>;
    timer: any;
  }>();

  show(notification: Notification) {
    // 既存の通知があれば削除
    this.remove(notification.id);

    // 新しい通知を作成
    const ref = this.container.createComponent(NotificationComponent);
    ref.setInput('message', notification.message);
    ref.setInput('type', notification.type);

    // 自動削除タイマーを設定
    const timer = setTimeout(() => {
      this.remove(notification.id);
    }, notification.duration);

    this.notifications.set(notification.id, { ref, timer });
  }

  remove(id: string) {
    const notification = this.notifications.get(id);
    if (notification) {
      clearTimeout(notification.timer);
      notification.ref.destroy();
      this.notifications.delete(id);
    }
  }

  removeAll() {
    this.notifications.forEach(({ ref, timer }) => {
      clearTimeout(timer);
      ref.destroy();
    });
    this.notifications.clear();
  }

  getCount(): number {
    return this.notifications.size;
  }
}
```

### ダッシュボードウィジェット管理
```typescript
interface Widget {
  id: string;
  type: Type<any>;
  position: { row: number; col: number };
  size: { width: number; height: number };
  data?: any;
}

export class DashboardComponent implements OnDestroy {
  private container = inject(ViewContainerRef);
  private widgets = new Map<string, ComponentRef<any>>();

  addWidget(widget: Widget) {
    if (this.widgets.has(widget.id)) {
      console.warn(`Widget ${widget.id} already exists`);
      return;
    }

    const ref = this.container.createComponent(widget.type, {
      index: this.calculateIndex(widget.position)
    });

    // ウィジェット共通の入力を設定
    ref.setInput('id', widget.id);
    ref.setInput('size', widget.size);
    ref.setInput('data', widget.data);

    this.widgets.set(widget.id, ref);
  }

  removeWidget(id: string) {
    const ref = this.widgets.get(id);
    if (ref) {
      ref.destroy();
      this.widgets.delete(id);
    }
  }

  updateWidget(id: string, data: any) {
    const ref = this.widgets.get(id);
    if (ref) {
      ref.setInput('data', data);
    }
  }

  moveWidget(id: string, newPosition: { row: number; col: number }) {
    const ref = this.widgets.get(id);
    if (ref) {
      // 位置を更新（実装は省略）
      ref.setInput('position', newPosition);
    }
  }

  getAllWidgets(): Widget[] {
    return Array.from(this.widgets.entries()).map(([id, ref]) => ({
      id,
      type: ref.componentType,
      position: ref.instance.position,
      size: ref.instance.size,
      data: ref.instance.data
    }));
  }

  ngOnDestroy() {
    this.widgets.forEach(ref => ref.destroy());
    this.widgets.clear();
  }

  private calculateIndex(position: { row: number; col: number }): number {
    return position.row * 12 + position.col;
  }
}
```

### タスク管理システム
```typescript
interface Task {
  id: string;
  title: string;
  status: 'pending' | 'in-progress' | 'completed';
  priority: number;
}

export class TaskListComponent implements OnDestroy {
  private container = inject(ViewContainerRef);
  private tasks = new Map<string, ComponentRef<TaskItemComponent>>();

  addTask(task: Task) {
    const ref = this.container.createComponent(TaskItemComponent);
    ref.setInput('task', task);

    // タスクイベントを購読
    ref.instance.statusChanged.subscribe((newStatus: string) => {
      this.onTaskStatusChanged(task.id, newStatus);
    });

    ref.instance.deleted.subscribe(() => {
      this.removeTask(task.id);
    });

    this.tasks.set(task.id, ref);
    this.sortTasks();
  }

  removeTask(id: string) {
    const ref = this.tasks.get(id);
    if (ref) {
      ref.destroy();
      this.tasks.delete(id);
    }
  }

  updateTask(id: string, updates: Partial<Task>) {
    const ref = this.tasks.get(id);
    if (ref) {
      const currentTask = ref.instance.task;
      ref.setInput('task', { ...currentTask, ...updates });
      this.sortTasks();
    }
  }

  filterByStatus(status: Task['status']) {
    this.tasks.forEach(ref => {
      const isVisible = ref.instance.task.status === status;
      ref.setInput('visible', isVisible);
    });
  }

  sortTasks() {
    const sorted = Array.from(this.tasks.entries())
      .sort((a, b) => {
        const priorityDiff = b[1].instance.task.priority - a[1].instance.task.priority;
        if (priorityDiff !== 0) return priorityDiff;
        return a[1].instance.task.title.localeCompare(b[1].instance.task.title);
      });

    this.container.clear();
    sorted.forEach(([id, ref]) => {
      this.container.insert(ref.hostView);
    });
  }

  private onTaskStatusChanged(taskId: string, newStatus: string) {
    this.updateTask(taskId, { status: newStatus as Task['status'] });
  }

  ngOnDestroy() {
    this.tasks.forEach(ref => ref.destroy());
    this.tasks.clear();
  }
}
```

### 階層型コンポーネント管理
```typescript
interface TreeNode {
  id: string;
  type: Type<any>;
  data?: any;
  children?: TreeNode[];
}

export class TreeComponent implements OnDestroy {
  private container = inject(ViewContainerRef);
  private nodes = new Map<string, {
    ref: ComponentRef<any>;
    children: string[];
    parent?: string;
  }>();

  buildTree(root: TreeNode) {
    this.clear();
    this.addNode(root);
  }

  private addNode(node: TreeNode, parentId?: string) {
    const ref = this.container.createComponent(node.type);
    ref.setInput('id', node.id);
    ref.setInput('data', node.data);

    const children: string[] = [];
    this.nodes.set(node.id, {
      ref,
      children,
      parent: parentId
    });

    // 子ノードを追加
    if (node.children) {
      node.children.forEach(child => {
        this.addNode(child, node.id);
        children.push(child.id);
      });
    }
  }

  removeNode(id: string, recursive = true) {
    const node = this.nodes.get(id);
    if (!node) return;

    // 再帰的に子ノードを削除
    if (recursive && node.children.length > 0) {
      node.children.forEach(childId => this.removeNode(childId, true));
    }

    // ノード自体を削除
    node.ref.destroy();
    this.nodes.delete(id);

    // 親から参照を削除
    if (node.parent) {
      const parent = this.nodes.get(node.parent);
      if (parent) {
        parent.children = parent.children.filter(c => c !== id);
      }
    }
  }

  updateNode(id: string, data: any) {
    const node = this.nodes.get(id);
    if (node) {
      node.ref.setInput('data', data);
    }
  }

  getNodesByLevel(level: number): string[] {
    // レベルごとのノードを取得（実装は省略）
    return [];
  }

  clear() {
    this.nodes.forEach(({ ref }) => ref.destroy());
    this.nodes.clear();
  }

  ngOnDestroy() {
    this.clear();
  }
}
```

### ページネーション対応リスト
```typescript
export class PaginatedListComponent {
  private container = inject(ViewContainerRef);
  private allItems: ComponentRef<any>[] = [];
  private visibleItems: ComponentRef<any>[] = [];

  currentPage = signal(1);
  pageSize = signal(10);
  totalPages = computed(() =>
    Math.ceil(this.allItems.length / this.pageSize())
  );

  loadItems(items: any[]) {
    // 既存アイテムをクリア
    this.clearVisible();

    // 全アイテムを作成（表示はしない）
    this.allItems = items.map(item => {
      const ref = this.container.createComponent(ListItemComponent, {
        index: -1  // 非表示
      });
      ref.setInput('data', item);
      return ref;
    });

    this.showPage(1);
  }

  showPage(page: number) {
    if (page < 1 || page > this.totalPages()) return;

    this.clearVisible();
    this.currentPage.set(page);

    const start = (page - 1) * this.pageSize();
    const end = start + this.pageSize();

    this.visibleItems = this.allItems.slice(start, end);
    this.visibleItems.forEach((ref, index) => {
      this.container.insert(ref.hostView, index);
    });
  }

  nextPage() {
    this.showPage(this.currentPage() + 1);
  }

  previousPage() {
    this.showPage(this.currentPage() - 1);
  }

  private clearVisible() {
    this.visibleItems.forEach(ref => {
      const index = this.container.indexOf(ref.hostView);
      if (index !== -1) {
        this.container.detach(index);
      }
    });
    this.visibleItems = [];
  }

  ngOnDestroy() {
    this.allItems.forEach(ref => ref.destroy());
    this.allItems = [];
  }
}
```

## ベストプラクティス

### 適切なデータ構造の選択
```typescript
// ✅ 順序が重要な場合は配列
private orderedComponents: ComponentRef<any>[] = [];

// ✅ IDベースのアクセスが多い場合はMap
private indexedComponents = new Map<string, ComponentRef<any>>();

// ✅ 重複チェックが必要な場合はSet
private uniqueComponents = new Set<ComponentRef<any>>();
```

### メモリ管理の徹底
```typescript
// ✅ ngOnDestroyで確実にクリーンアップ
ngOnDestroy() {
  this.components.forEach(ref => ref.destroy());
  this.components.clear();
}

// ✅ 削除時は参照も削除
remove(id: string) {
  const ref = this.map.get(id);
  if (ref) {
    ref.destroy();
    this.map.delete(id);  // 参照も削除
  }
}
```

### 型安全な実装
```typescript
class ComponentManager<T> {
  private components = new Map<string, ComponentRef<T>>();

  add(id: string, component: Type<T>): ComponentRef<T> {
    const ref = this.container.createComponent(component);
    this.components.set(id, ref);
    return ref;
  }

  get(id: string): ComponentRef<T> | undefined {
    return this.components.get(id);
  }
}
```

## 注意点

### パフォーマンスへの配慮
大量のコンポーネントを管理する場合、仮想スクロールやページネーションの導入を検討してください。

### イベント購読の管理
各コンポーネントのイベント購読も適切に管理し、メモリリークを防ぎましょう。

### 一括操作の効率化
多数のコンポーネントに対する一括更新は、変更検知のコストが高くなる可能性があります。必要に応じて`ChangeDetectorRef.detach()`を活用してください。

### インデックスの整合性
コンポーネントの追加・削除時、インデックスの整合性を保つよう注意してください。

## 関連技術
- **ComponentRef**: コンポーネント参照
- **ViewContainerRef**: コンテナ管理
- **Map/Set/Array**: データ構造
- **Signal**: 状態管理
- **仮想スクロール**: 大量データの効率的表示
