# #240 「プラグインアーキテクチャ」

## 概要
プラグインアーキテクチャは、アプリケーションに動的に機能を追加できる拡張可能な設計パターンです。インターフェース定義、レジストリ管理、動的ロードを組み合わせることで、コアシステムを変更せずに新機能を追加できます。

## 学習目標
- プラグインシステムの設計原則を理解する
- プラグインの登録・管理・実行方法を習得する
- 拡張可能なアーキテクチャの構築方法を学ぶ

## 技術ポイント
- **プラグインインターフェース**: 統一された契約
- **レジストリパターン**: プラグイン管理
- **動的ロード**: 遅延読み込み対応

## 📺 画面表示用コード

### プラグインインターフェース
```typescript
interface Plugin {
  id: string;
  name: string;
  version: string;
  initialize(): void;
  execute(context: any): void;
  destroy?(): void;
}
```

### プラグイン登録
```typescript
@Injectable()
export class PluginRegistry {
  private plugins = new Map<string, Plugin>();

  register(plugin: Plugin) {
    this.plugins.set(plugin.id, plugin);
    plugin.initialize();
  }

  get(id: string): Plugin | undefined {
    return this.plugins.get(id);
  }
}
```

### プラグイン実行
```typescript
executePlugin(id: string, context: any) {
  const plugin = this.registry.get(id);
  if (plugin) {
    plugin.execute(context);
  }
}
```

## 実践的な活用例

### 完全なプラグインシステム
```typescript
// プラグインベースインターフェース
interface PluginBase {
  readonly id: string;
  readonly name: string;
  readonly version: string;
  readonly description?: string;
  readonly author?: string;
  readonly dependencies?: string[];
}

// UIプラグイン
interface UIPlugin extends PluginBase {
  component: Type<any>;
  renderPosition: 'header' | 'sidebar' | 'main' | 'footer';
  initialize(context: PluginContext): void;
  destroy?(): void;
}

// アクションプラグイン
interface ActionPlugin extends PluginBase {
  execute(context: PluginContext): Promise<void>;
  canExecute?(context: PluginContext): boolean;
}

// プラグインコンテキスト
interface PluginContext {
  container: ViewContainerRef;
  data?: any;
  api: PluginAPI;
}

interface PluginAPI {
  showNotification(message: string): void;
  getData(key: string): any;
  setData(key: string, value: any): void;
}

// プラグインマネージャー
@Injectable({ providedIn: 'root' })
export class PluginManager {
  private uiPlugins = new Map<string, UIPlugin>();
  private actionPlugins = new Map<string, ActionPlugin>();
  private pluginRefs = new Map<string, ComponentRef<any>>();

  registerUIPlugin(plugin: UIPlugin) {
    // 依存関係チェック
    if (plugin.dependencies) {
      const missing = plugin.dependencies.filter(
        dep => !this.hasPlugin(dep)
      );
      if (missing.length > 0) {
        throw new Error(`Missing dependencies: ${missing.join(', ')}`);
      }
    }

    this.uiPlugins.set(plugin.id, plugin);
    console.log(`UI Plugin registered: ${plugin.name} v${plugin.version}`);
  }

  registerActionPlugin(plugin: ActionPlugin) {
    this.actionPlugins.set(plugin.id, plugin);
    console.log(`Action Plugin registered: ${plugin.name} v${plugin.version}`);
  }

  loadUIPlugin(
    pluginId: string,
    container: ViewContainerRef,
    context: PluginContext
  ): ComponentRef<any> | null {
    const plugin = this.uiPlugins.get(pluginId);
    if (!plugin) {
      console.error(`Plugin not found: ${pluginId}`);
      return null;
    }

    plugin.initialize(context);

    const ref = container.createComponent(plugin.component);
    this.pluginRefs.set(pluginId, ref);

    return ref;
  }

  async executeAction(pluginId: string, context: PluginContext): Promise<void> {
    const plugin = this.actionPlugins.get(pluginId);
    if (!plugin) {
      throw new Error(`Action plugin not found: ${pluginId}`);
    }

    if (plugin.canExecute && !plugin.canExecute(context)) {
      console.warn(`Plugin ${pluginId} cannot execute in current context`);
      return;
    }

    await plugin.execute(context);
  }

  unloadPlugin(pluginId: string) {
    const ref = this.pluginRefs.get(pluginId);
    if (ref) {
      ref.destroy();
      this.pluginRefs.delete(pluginId);
    }

    const uiPlugin = this.uiPlugins.get(pluginId);
    if (uiPlugin?.destroy) {
      uiPlugin.destroy();
    }

    this.uiPlugins.delete(pluginId);
    this.actionPlugins.delete(pluginId);
  }

  private hasPlugin(id: string): boolean {
    return this.uiPlugins.has(id) || this.actionPlugins.has(id);
  }

  getPlugins(type: 'ui' | 'action' = 'ui'): PluginBase[] {
    const map = type === 'ui' ? this.uiPlugins : this.actionPlugins;
    return Array.from(map.values());
  }
}
```

### プラグインの実装例
```typescript
// UIプラグインの実装
@Component({
  selector: 'app-weather-widget',
  template: `
    <div class="weather-widget">
      <h3>天気ウィジェット</h3>
      <p>{{ weather() }}</p>
    </div>
  `,
  standalone: true
})
export class WeatherWidgetComponent {
  weather = signal('晴れ');
}

export const WeatherPlugin: UIPlugin = {
  id: 'weather-widget',
  name: '天気ウィジェット',
  version: '1.0.0',
  description: '現在の天気を表示します',
  component: WeatherWidgetComponent,
  renderPosition: 'sidebar',

  initialize(context: PluginContext) {
    console.log('Weather plugin initialized');
    // 初期化処理
  },

  destroy() {
    console.log('Weather plugin destroyed');
    // クリーンアップ処理
  }
};

// アクションプラグインの実装
export const ExportPlugin: ActionPlugin = {
  id: 'export-data',
  name: 'データエクスポート',
  version: '1.0.0',
  description: 'データをCSV形式でエクスポート',

  async execute(context: PluginContext) {
    const data = context.data;
    const csv = this.convertToCSV(data);
    this.downloadCSV(csv, 'export.csv');
  },

  canExecute(context: PluginContext): boolean {
    return !!context.data && Array.isArray(context.data);
  },

  convertToCSV(data: any[]): string {
    // CSV変換ロジック
    return data.map(row => Object.values(row).join(',')).join('\n');
  },

  downloadCSV(csv: string, filename: string) {
    const blob = new Blob([csv], { type: 'text/csv' });
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = filename;
    a.click();
    window.URL.revokeObjectURL(url);
  }
};
```

### 動的プラグインロード
```typescript
interface PluginManifest {
  id: string;
  name: string;
  version: string;
  path: string;
  type: 'ui' | 'action';
}

@Injectable()
export class DynamicPluginLoader {
  private manager = inject(PluginManager);

  async loadPlugin(manifest: PluginManifest): Promise<void> {
    try {
      // 動的インポート
      const module = await import(/* @vite-ignore */ manifest.path);
      const plugin = module.default || module[manifest.id];

      if (!plugin) {
        throw new Error(`Plugin not found in module: ${manifest.path}`);
      }

      // プラグイン登録
      if (manifest.type === 'ui') {
        this.manager.registerUIPlugin(plugin);
      } else {
        this.manager.registerActionPlugin(plugin);
      }

      console.log(`Plugin loaded: ${manifest.name} v${manifest.version}`);
    } catch (error) {
      console.error(`Failed to load plugin ${manifest.id}:`, error);
      throw error;
    }
  }

  async loadPluginFromURL(url: string): Promise<void> {
    // リモートからプラグインを取得
    const response = await fetch(url);
    const code = await response.text();

    // 動的に評価（セキュリティに注意）
    const module = new Function('exports', code);
    const exports: any = {};
    module(exports);

    this.manager.registerUIPlugin(exports.default);
  }
}
```

### プラグイン設定管理
```typescript
interface PluginConfig {
  pluginId: string;
  enabled: boolean;
  settings: Record<string, any>;
}

@Injectable()
export class PluginConfigService {
  private configs = new Map<string, PluginConfig>();

  saveConfig(config: PluginConfig) {
    this.configs.set(config.pluginId, config);
    localStorage.setItem(
      `plugin-config-${config.pluginId}`,
      JSON.stringify(config)
    );
  }

  loadConfig(pluginId: string): PluginConfig | null {
    const cached = this.configs.get(pluginId);
    if (cached) return cached;

    const stored = localStorage.getItem(`plugin-config-${pluginId}`);
    if (stored) {
      const config = JSON.parse(stored);
      this.configs.set(pluginId, config);
      return config;
    }

    return null;
  }

  isEnabled(pluginId: string): boolean {
    const config = this.loadConfig(pluginId);
    return config?.enabled ?? true;
  }

  getSettings(pluginId: string): Record<string, any> {
    const config = this.loadConfig(pluginId);
    return config?.settings ?? {};
  }
}
```

### プラグインマーケットプレイス
```typescript
interface PluginListing {
  id: string;
  name: string;
  description: string;
  version: string;
  author: string;
  downloadUrl: string;
  rating: number;
  downloads: number;
}

@Injectable()
export class PluginMarketplace {
  private http = inject(HttpClient);
  private loader = inject(DynamicPluginLoader);

  async searchPlugins(query: string): Promise<PluginListing[]> {
    return firstValueFrom(
      this.http.get<PluginListing[]>(`/api/plugins/search?q=${query}`)
    );
  }

  async installPlugin(listing: PluginListing): Promise<void> {
    // プラグインをダウンロード
    const manifest: PluginManifest = {
      id: listing.id,
      name: listing.name,
      version: listing.version,
      path: listing.downloadUrl,
      type: 'ui' // またはAPIから取得
    };

    // ロードして登録
    await this.loader.loadPlugin(manifest);

    // インストール記録
    this.recordInstallation(listing.id);
  }

  async uninstallPlugin(pluginId: string): Promise<void> {
    const manager = inject(PluginManager);
    manager.unloadPlugin(pluginId);

    // インストール記録を削除
    localStorage.removeItem(`plugin-installed-${pluginId}`);
  }

  private recordInstallation(pluginId: string) {
    localStorage.setItem(
      `plugin-installed-${pluginId}`,
      new Date().toISOString()
    );
  }
}
```

### イベントシステム統合
```typescript
interface PluginEvent {
  type: string;
  source: string;
  data: any;
}

@Injectable()
export class PluginEventBus {
  private events$ = new Subject<PluginEvent>();

  emit(event: PluginEvent) {
    this.events$.next(event);
  }

  on(eventType: string): Observable<PluginEvent> {
    return this.events$.pipe(
      filter(event => event.type === eventType)
    );
  }

  subscribe(pluginId: string, eventType: string, handler: (event: PluginEvent) => void) {
    return this.on(eventType).subscribe(event => {
      if (event.source !== pluginId) {
        handler(event);
      }
    });
  }
}

// プラグインでのイベント使用例
export class EventAwarePlugin implements UIPlugin {
  // ... プラグイン定義

  initialize(context: PluginContext) {
    const eventBus = context.api.getEventBus();

    // イベント購読
    eventBus.subscribe(this.id, 'data-updated', (event) => {
      console.log('Data updated:', event.data);
    });

    // イベント発行
    eventBus.emit({
      type: 'plugin-loaded',
      source: this.id,
      data: { version: this.version }
    });
  }
}
```

## ベストプラクティス

### セキュリティ考慮
```typescript
// ✅ プラグイン検証
private validatePlugin(plugin: Plugin): boolean {
  return (
    typeof plugin.id === 'string' &&
    typeof plugin.name === 'string' &&
    typeof plugin.execute === 'function'
  );
}

// ✅ サンドボックス化
private executeSafely(plugin: Plugin, context: any) {
  try {
    plugin.execute(context);
  } catch (error) {
    console.error(`Plugin ${plugin.id} error:`, error);
  }
}
```

### バージョン管理
```typescript
// ✅ セマンティックバージョニング
private isCompatible(required: string, actual: string): boolean {
  const [reqMajor] = required.split('.');
  const [actMajor] = actual.split('.');
  return reqMajor === actMajor;
}
```

### パフォーマンス
```typescript
// ✅ 遅延ロード
async loadPluginOnDemand(id: string) {
  if (!this.loadedPlugins.has(id)) {
    await this.loader.loadPlugin(id);
  }
  return this.getPlugin(id);
}
```

## 注意点

### セキュリティ
サードパーティプラグインの実行は、セキュリティリスクを伴います。適切な検証とサンドボックス化が必要です。

### 依存関係管理
プラグイン間の依存関係を適切に管理しないと、ロード順序の問題が発生します。

### API互換性
コアAPIの変更は、既存プラグインを破壊する可能性があります。バージョニング戦略が重要です。

### パフォーマンス
多数のプラグインをロードすると、起動時間とメモリ使用量が増加します。

## 関連技術
- **動的インポート**: ES Modules
- **依存性注入**: Angular DI
- **イベント駆動**: Pub/Subパターン
- **レジストリパターン**: デザインパターン
- **マイクロフロントエンド**: アーキテクチャパターン
