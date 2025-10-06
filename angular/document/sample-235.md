# #235 「遅延ロード Component」

## 概要
遅延ロードコンポーネントは、Dynamic Import（import()）を使用して実行時に必要なコンポーネントだけをロードする技術です。初期バンドルサイズを削減し、アプリケーションの起動時間を短縮できます。

## 学習目標
- Dynamic Importの使い方を習得する
- 遅延ロードコンポーネントの実装方法を理解する
- パフォーマンス最適化の手法を学ぶ

## 技術ポイント
- **Dynamic Import**: import()による非同期モジュールロード
- **コード分割**: バンドルサイズの最適化
- **lazy()関数**: Angular 19+の新しい遅延ロードAPI

## 📺 画面表示用コード

### Dynamic Import の基本
```typescript
async loadLazyComponent() {
  const { LazyComponent } = await import('./lazy.component');
  const ref = this.container.createComponent(LazyComponent);
}
```

### Standalone Component の遅延ロード
```typescript
export class LazyHost {
  private container = inject(ViewContainerRef);

  async load() {
    const module = await import('./features/dashboard.component');
    const ref = this.container.createComponent(
      module.DashboardComponent
    );
  }
}
```

### エラーハンドリング付き
```typescript
async loadSafe() {
  try {
    const { MyComponent } = await import('./my.component');
    this.container.createComponent(MyComponent);
  } catch (error) {
    console.error('ロード失敗:', error);
    this.container.createComponent(ErrorComponent);
  }
}
```

## 実践的な活用例

### 完全な遅延ロードシステム
```typescript
@Injectable()
export class LazyComponentLoader {
  private container = inject(ViewContainerRef);
  private cache = new Map<string, Type<any>>();

  async load(
    path: string,
    componentName: string
  ): Promise<ComponentRef<any>> {
    // キャッシュチェック
    if (this.cache.has(path)) {
      return this.container.createComponent(this.cache.get(path)!);
    }

    // ローディング表示
    const loading = this.container.createComponent(LoadingComponent);

    try {
      // 動的インポート
      const module = await import(/* @vite-ignore */ path);
      const componentType = module[componentName];

      if (!componentType) {
        throw new Error(`Component ${componentName} not found in ${path}`);
      }

      // キャッシュに保存
      this.cache.set(path, componentType);

      // ローディング削除、コンポーネント表示
      loading.destroy();
      return this.container.createComponent(componentType);

    } catch (error) {
      loading.destroy();
      const errorRef = this.container.createComponent(ErrorComponent);
      errorRef.setInput('error', error);
      throw error;
    }
  }

  clearCache() {
    this.cache.clear();
  }
}
```

### ルーティングベースの遅延ロード
```typescript
interface RouteConfig {
  path: string;
  component: () => Promise<Type<any>>;
}

export class DynamicRouter {
  private container = inject(ViewContainerRef);

  private routes: RouteConfig[] = [
    {
      path: 'dashboard',
      component: () =>
        import('./dashboard.component').then(m => m.DashboardComponent)
    },
    {
      path: 'settings',
      component: () =>
        import('./settings.component').then(m => m.SettingsComponent)
    }
  ];

  async navigateTo(path: string) {
    const route = this.routes.find(r => r.path === path);
    if (!route) {
      console.error(`Route ${path} not found`);
      return;
    }

    this.container.clear();
    const spinner = this.container.createComponent(RouteLoadingComponent);

    try {
      const componentType = await route.component();
      spinner.destroy();
      this.container.createComponent(componentType);
    } catch (error) {
      spinner.destroy();
      this.container.createComponent(RouteErrorComponent);
    }
  }
}
```

### 条件付き遅延ロード
```typescript
export class ConditionalLazyLoader {
  private container = inject(ViewContainerRef);

  async loadBasedOnPermission(userRole: string) {
    let component: Type<any>;

    switch (userRole) {
      case 'admin':
        const admin = await import('./admin-panel.component');
        component = admin.AdminPanelComponent;
        break;

      case 'user':
        const user = await import('./user-dashboard.component');
        component = user.UserDashboardComponent;
        break;

      default:
        const guest = await import('./guest-view.component');
        component = guest.GuestViewComponent;
    }

    this.container.createComponent(component);
  }

  async loadBasedOnFeatureFlag(flags: Record<string, boolean>) {
    if (flags.newUI) {
      const { NewUIComponent } = await import('./new-ui.component');
      this.container.createComponent(NewUIComponent);
    } else {
      const { LegacyUIComponent } = await import('./legacy-ui.component');
      this.container.createComponent(LegacyUIComponent);
    }
  }
}
```

### プリロード戦略
```typescript
export class PreloadService {
  private preloaded = new Map<string, Type<any>>();

  async preload(imports: Array<{ path: string; name: string }>) {
    const promises = imports.map(async ({ path, name }) => {
      try {
        const module = await import(/* @vite-ignore */ path);
        this.preloaded.set(path, module[name]);
      } catch (error) {
        console.error(`Preload failed for ${path}:`, error);
      }
    });

    await Promise.all(promises);
    console.log('Preload complete:', this.preloaded.size, 'components');
  }

  get(path: string): Type<any> | undefined {
    return this.preloaded.get(path);
  }

  has(path: string): boolean {
    return this.preloaded.has(path);
  }
}

// 使用例
export class AppComponent implements OnInit {
  private preload = inject(PreloadService);
  private container = inject(ViewContainerRef);

  ngOnInit() {
    // アイドル時にプリロード
    requestIdleCallback(() => {
      this.preload.preload([
        { path: './heavy-component', name: 'HeavyComponent' },
        { path: './chart-component', name: 'ChartComponent' }
      ]);
    });
  }

  async loadPreloaded(path: string) {
    const component = this.preload.get(path);
    if (component) {
      // プリロード済み: 即座に表示
      this.container.createComponent(component);
    } else {
      // 未ロード: 動的ロード
      const module = await import(/* @vite-ignore */ path);
      this.container.createComponent(module.default);
    }
  }
}
```

### チャンク分割戦略
```typescript
// webpack magic comments を使用
export class ChunkLoader {
  private container = inject(ViewContainerRef);

  async loadWithChunkName() {
    // 明示的なチャンク名を指定
    const { AnalyticsComponent } = await import(
      /* webpackChunkName: "analytics" */
      './analytics.component'
    );

    this.container.createComponent(AnalyticsComponent);
  }

  async loadWithPrefetch() {
    // プリフェッチを指定
    const { ReportComponent } = await import(
      /* webpackPrefetch: true */
      './report.component'
    );

    this.container.createComponent(ReportComponent);
  }

  async loadWithPreload() {
    // プリロードを指定
    const { DashboardComponent } = await import(
      /* webpackPreload: true */
      './dashboard.component'
    );

    this.container.createComponent(DashboardComponent);
  }
}
```

### タイムアウト付き遅延ロード
```typescript
export class TimeoutLazyLoader {
  private container = inject(ViewContainerRef);

  async loadWithTimeout(
    path: string,
    componentName: string,
    timeout = 10000
  ) {
    const timeoutPromise = new Promise<never>((_, reject) =>
      setTimeout(() => reject(new Error('Load timeout')), timeout)
    );

    const loadPromise = import(/* @vite-ignore */ path).then(
      module => module[componentName]
    );

    try {
      const component = await Promise.race([loadPromise, timeoutPromise]);
      this.container.createComponent(component);
    } catch (error) {
      if (error instanceof Error && error.message === 'Load timeout') {
        const errorRef = this.container.createComponent(TimeoutErrorComponent);
        errorRef.setInput('path', path);
      } else {
        throw error;
      }
    }
  }
}
```

### バージョン管理付き遅延ロード
```typescript
interface VersionedComponent {
  version: string;
  loader: () => Promise<Type<any>>;
}

export class VersionedLazyLoader {
  private container = inject(ViewContainerRef);

  private components = new Map<string, VersionedComponent>([
    ['feature-a', {
      version: '2.0.0',
      loader: () => import('./feature-a-v2').then(m => m.FeatureAComponent)
    }],
    ['feature-b', {
      version: '1.5.0',
      loader: () => import('./feature-b-v1.5').then(m => m.FeatureBComponent)
    }]
  ]);

  async load(featureName: string) {
    const config = this.components.get(featureName);
    if (!config) {
      throw new Error(`Feature ${featureName} not found`);
    }

    console.log(`Loading ${featureName} v${config.version}`);

    const component = await config.loader();
    const ref = this.container.createComponent(component);
    ref.setInput('version', config.version);
    return ref;
  }
}
```

## ベストプラクティス

### エラーハンドリング
```typescript
// ✅ エラーを適切に処理
async load() {
  try {
    const { Component } = await import('./component');
    this.container.createComponent(Component);
  } catch (error) {
    this.showFallback(error);
  }
}

// ❌ エラーを無視
async load() {
  const { Component } = await import('./component');
  this.container.createComponent(Component);
}
```

### キャッシュの活用
```typescript
// ✅ 一度ロードしたコンポーネントを再利用
if (this.cache.has(path)) {
  return this.cache.get(path);
}
const module = await import(path);
this.cache.set(path, module.Component);
```

### プリロードの最適化
```typescript
// ✅ アイドル時にプリロード
requestIdleCallback(() => {
  this.preloadComponents();
});

// ✅ Intersection Observer でプリロード
const observer = new IntersectionObserver(entries => {
  if (entries[0].isIntersecting) {
    this.loadComponent();
  }
});
```

## 注意点

### バンドラー設定
Dynamic Importを使用するには、ビルドツール（Webpack、Vite等）の設定が必要です。

### 型安全性
Dynamic Importでは型推論が制限されます。適切な型アサーションを使用してください。

### ネットワークエラー
遅延ロードはネットワークに依存します。オフライン対応やリトライ機構を検討してください。

### SEO への影響
遅延ロードされたコンテンツは初期HTMLに含まれないため、SEOに影響する可能性があります。

## 関連技術
- **Dynamic Import**: ES2020の動的インポート
- **Code Splitting**: バンドル分割
- **Webpack**: バンドラー設定
- **Vite**: 高速ビルドツール
- **lazy()**: Angular 19+の新API
