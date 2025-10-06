# #239 「動的ウィジェットシステム」

## 概要
動的ウィジェットシステムは、実行時にウィジェットを追加・配置・リサイズできるカスタマイズ可能なダッシュボードです。グリッドレイアウトと動的コンポーネント生成を組み合わせ、ユーザーごとに最適化されたUIを提供できます。

## 学習目標
- ウィジェットベースのダッシュボード設計を理解する
- グリッドレイアウトとの統合方法を習得する
- ウィジェット設定の永続化を実装できる

## 技術ポイント
- **ウィジェット定義**: メタデータベースの管理
- **グリッドシステム**: CSS GridまたはFlexboxレイアウト
- **設定永続化**: LocalStorageやAPI連携

## 📺 画面表示用コード

### ウィジェット定義
```typescript
interface WidgetConfig {
  id: string;
  type: string;
  position: { x: number; y: number };
  size: { width: number; height: number };
  data?: any;
}

const widget: WidgetConfig = {
  id: 'chart-1',
  type: 'chart',
  position: { x: 0, y: 0 },
  size: { width: 2, height: 2 }
};
```

### ウィジェット生成
```typescript
createWidget(config: WidgetConfig) {
  const component = this.widgetTypes.get(config.type)!;
  const ref = this.container.createComponent(component);
  ref.setInput('config', config);
  return ref;
}
```

### レイアウト管理
```typescript
widgets = signal<WidgetConfig[]>([]);

updateLayout(id: string, position: Position) {
  this.widgets.update(widgets =>
    widgets.map(w =>
      w.id === id ? { ...w, position } : w
    )
  );
}
```

## 実践的な活用例(continued)

### 完全なウィジェットダッシュボード
```typescript
interface WidgetDefinition {
  id: string;
  type: string;
  title: string;
  component: Type<any>;
  defaultSize: { width: number; height: number };
  minSize?: { width: number; height: number };
  maxSize?: { width: number; height: number };
}

@Injectable()
export class WidgetRegistry {
  private widgets = new Map<string, WidgetDefinition>([
    ['chart', {
      id: 'chart',
      type: 'chart',
      title: 'チャート',
      component: ChartWidgetComponent,
      defaultSize: { width: 4, height: 3 },
      minSize: { width: 2, height: 2 }
    }],
    ['stats', {
      id: 'stats',
      type: 'stats',
      title: '統計',
      component: StatsWidgetComponent,
      defaultSize: { width: 2, height: 2 }
    }],
    ['calendar', {
      id: 'calendar',
      type: 'calendar',
      title: 'カレンダー',
      component: CalendarWidgetComponent,
      defaultSize: { width: 3, height: 4 }
    }]
  ]);

  get(type: string): WidgetDefinition | undefined {
    return this.widgets.get(type);
  }

  getAll(): WidgetDefinition[] {
    return Array.from(this.widgets.values());
  }
}

@Component({
  selector: 'app-dashboard',
  template: `
    <div class="dashboard-header">
      <button (click)="showWidgetPicker()">+ ウィジェット追加</button>
      <button (click)="saveLayout()">レイアウト保存</button>
    </div>

    <div
      class="dashboard-grid"
      [style.grid-template-columns]="gridColumns()">
      @for (widget of widgets(); track widget.id) {
        <div
          class="widget-container"
          [style.grid-column]="getGridColumn(widget)"
          [style.grid-row]="getGridRow(widget)">
          <div class="widget-header">
            <h3>{{ widget.title }}</h3>
            <button (click)="removeWidget(widget.id)">×</button>
          </div>
          <ng-container #widgetContent></ng-container>
        </div>
      }
    </div>
  `,
  styles: [`
    .dashboard-grid {
      display: grid;
      gap: 16px;
      padding: 16px;
    }

    .widget-container {
      background: white;
      border-radius: 8px;
      box-shadow: 0 2px 4px rgba(0,0,0,0.1);
      padding: 16px;
    }
  `]
})
export class DashboardComponent implements AfterViewInit {
  @ViewChildren('widgetContent', { read: ViewContainerRef })
  widgetContainers!: QueryList<ViewContainerRef>;

  private registry = inject(WidgetRegistry);

  widgets = signal<WidgetConfig[]>([]);
  gridColumns = signal('repeat(12, 1fr)');

  ngAfterViewInit() {
    this.loadLayout();
  }

  addWidget(type: string) {
    const definition = this.registry.get(type);
    if (!definition) return;

    const widget: WidgetConfig = {
      id: crypto.randomUUID(),
      type,
      title: definition.title,
      position: this.findAvailablePosition(definition.defaultSize),
      size: definition.defaultSize
    };

    this.widgets.update(widgets => [...widgets, widget]);

    // コンポーネント生成
    setTimeout(() => {
      const index = this.widgets().length - 1;
      const container = this.widgetContainers.get(index);
      if (container) {
        const ref = container.createComponent(definition.component);
        ref.setInput('config', widget);
      }
    });
  }

  removeWidget(id: string) {
    this.widgets.update(widgets => widgets.filter(w => w.id !== id));
  }

  private findAvailablePosition(size: Size): Position {
    // 空いている位置を探すロジック
    return { x: 0, y: 0 };
  }

  saveLayout() {
    const layout = this.widgets().map(w => ({
      id: w.id,
      type: w.type,
      position: w.position,
      size: w.size
    }));
    localStorage.setItem('dashboard-layout', JSON.stringify(layout));
  }

  loadLayout() {
    const saved = localStorage.getItem('dashboard-layout');
    if (saved) {
      const layout = JSON.parse(saved);
      layout.forEach((config: any) => this.addWidget(config.type));
    }
  }

  getGridColumn(widget: WidgetConfig): string {
    return `${widget.position.x + 1} / span ${widget.size.width}`;
  }

  getGridRow(widget: WidgetConfig): string {
    return `${widget.position.y + 1} / span ${widget.size.height}`;
  }

  showWidgetPicker() {
    // ウィジェット選択モーダル表示
  }
}
```

### ドラッグ&ドロップ対応
```typescript
export class DraggableWidgetComponent {
  private draggedWidget: WidgetConfig | null = null;

  onDragStart(event: DragEvent, widget: WidgetConfig) {
    this.draggedWidget = widget;
    event.dataTransfer!.effectAllowed = 'move';
  }

  onDragOver(event: DragEvent, targetWidget: WidgetConfig) {
    event.preventDefault();
    event.dataTransfer!.dropEffect = 'move';
  }

  onDrop(event: DragEvent, targetWidget: WidgetConfig) {
    event.preventDefault();

    if (this.draggedWidget && this.draggedWidget.id !== targetWidget.id) {
      // 位置を入れ替え
      this.widgets.update(widgets => {
        const newWidgets = [...widgets];
        const draggedIndex = newWidgets.findIndex(w => w.id === this.draggedWidget!.id);
        const targetIndex = newWidgets.findIndex(w => w.id === targetWidget.id);

        const draggedPos = newWidgets[draggedIndex].position;
        newWidgets[draggedIndex].position = newWidgets[targetIndex].position;
        newWidgets[targetIndex].position = draggedPos;

        return newWidgets;
      });
    }

    this.draggedWidget = null;
  }
}
```

### リサイズ機能
```typescript
export class ResizableWidgetComponent {
  private resizing = false;
  private startX = 0;
  private startY = 0;
  private startWidth = 0;
  private startHeight = 0;

  onResizeStart(event: MouseEvent, widget: WidgetConfig) {
    this.resizing = true;
    this.startX = event.clientX;
    this.startY = event.clientY;
    this.startWidth = widget.size.width;
    this.startHeight = widget.size.height;

    document.addEventListener('mousemove', this.onResizeMove);
    document.addEventListener('mouseup', this.onResizeEnd);
  }

  private onResizeMove = (event: MouseEvent) => {
    if (!this.resizing) return;

    const deltaX = event.clientX - this.startX;
    const deltaY = event.clientY - this.startY;

    // グリッド単位に変換
    const gridSize = 100; // px
    const widthDelta = Math.round(deltaX / gridSize);
    const heightDelta = Math.round(deltaY / gridSize);

    this.updateWidgetSize(
      this.startWidth + widthDelta,
      this.startHeight + heightDelta
    );
  };

  private onResizeEnd = () => {
    this.resizing = false;
    document.removeEventListener('mousemove', this.onResizeMove);
    document.removeEventListener('mouseup', this.onResizeEnd);
  };

  private updateWidgetSize(width: number, height: number) {
    // サイズ制限チェック
    const minWidth = 1;
    const maxWidth = 12;
    const clampedWidth = Math.max(minWidth, Math.min(maxWidth, width));
    const clampedHeight = Math.max(1, height);

    // ウィジェット更新
    this.widgets.update(widgets =>
      widgets.map(w =>
        w.id === this.currentWidgetId
          ? { ...w, size: { width: clampedWidth, height: clampedHeight } }
          : w
      )
    );
  }
}
```

### ウィジェット設定
```typescript
interface WidgetSettings {
  refreshInterval?: number;
  dataSource?: string;
  theme?: 'light' | 'dark';
  customOptions?: Record<string, any>;
}

export class ConfigurableWidgetComponent {
  openSettings(widget: WidgetConfig) {
    const dialogRef = this.dialog.open(WidgetSettingsDialog, {
      data: widget.settings || {}
    });

    dialogRef.afterClosed().subscribe(settings => {
      if (settings) {
        this.updateWidgetSettings(widget.id, settings);
      }
    });
  }

  updateWidgetSettings(id: string, settings: WidgetSettings) {
    this.widgets.update(widgets =>
      widgets.map(w =>
        w.id === id ? { ...w, settings } : w
      )
    );

    // ウィジェットに設定を通知
    const ref = this.widgetRefs.get(id);
    if (ref) {
      ref.setInput('settings', settings);
    }
  }
}
```

### レイアウトプリセット
```typescript
interface LayoutPreset {
  name: string;
  widgets: WidgetConfig[];
}

export class LayoutPresetsService {
  presets: LayoutPreset[] = [
    {
      name: 'デフォルト',
      widgets: [
        { id: '1', type: 'chart', position: { x: 0, y: 0 }, size: { width: 6, height: 4 } },
        { id: '2', type: 'stats', position: { x: 6, y: 0 }, size: { width: 6, height: 4 } }
      ]
    },
    {
      name: 'アナリティクス',
      widgets: [
        { id: '1', type: 'chart', position: { x: 0, y: 0 }, size: { width: 8, height: 6 } },
        { id: '2', type: 'stats', position: { x: 8, y: 0 }, size: { width: 4, height: 3 } },
        { id: '3', type: 'calendar', position: { x: 8, y: 3 }, size: { width: 4, height: 3 } }
      ]
    }
  ];

  applyPreset(presetName: string) {
    const preset = this.presets.find(p => p.name === presetName);
    if (preset) {
      this.widgets.set(preset.widgets);
    }
  }

  saveAsPreset(name: string, widgets: WidgetConfig[]) {
    this.presets.push({ name, widgets: [...widgets] });
  }
}
```

## ベストプラクティス

### ウィジェット登録の管理
```typescript
// ✅ レジストリパターンで管理
@Injectable()
export class WidgetRegistry {
  private widgets = new Map<string, WidgetDefinition>();

  register(definition: WidgetDefinition) {
    this.widgets.set(definition.type, definition);
  }
}

// ✅ 型安全なウィジェット定義
interface TypedWidgetConfig<T = any> {
  type: string;
  data: T;
}
```

### パフォーマンス最適化
```typescript
// ✅ 仮想スクロールの使用
@Component({
  template: `
    <cdk-virtual-scroll-viewport itemSize="200">
      @for (widget of widgets(); track widget.id) {
        <!-- ウィジェット -->
      }
    </cdk-virtual-scroll-viewport>
  `
})

// ✅ 遅延ロード
async loadWidget(type: string) {
  const { component } = await import(`./widgets/${type}.component`);
  return component;
}
```

### 状態管理
```typescript
// ✅ Signal での一元管理
class DashboardStore {
  private state = signal({
    widgets: [] as WidgetConfig[],
    layout: 'grid' as 'grid' | 'flex',
    theme: 'light' as 'light' | 'dark'
  });

  widgets = computed(() => this.state().widgets);
  layout = computed(() => this.state().layout);
}
```

## 注意点

### グリッド計算
位置とサイズの計算は、グリッドシステムの仕様に合わせて調整が必要です。

### メモリ管理
多数のウィジェットを配置すると、メモリ使用量が増加します。適切な制限を設けてください。

### レスポンシブ対応
画面サイズに応じてグリッド列数を調整する必要があります。

### データ更新
ウィジェットのデータ更新は、パフォーマンスへの影響を考慮して実装してください。

## 関連技術
- **CSS Grid**: レイアウトシステム
- **Drag and Drop API**: ドラッグ操作
- **ResizeObserver**: リサイズ検知
- **LocalStorage**: 設定永続化
- **CDK**: Angular Material CDK
