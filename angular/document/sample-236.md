# #236 「条件付き Component 表示」

## 概要
条件付きコンポーネント表示は、実行時の条件に基づいて適切なコンポーネントを動的に生成・表示する技術です。ユーザー権限、フィーチャーフラグ、デバイスタイプなど、様々な条件に応じた柔軟なUI制御が可能になります。

## 学習目標
- 条件分岐とコンポーネント生成の組み合わせ方を習得する
- 実践的な条件パターンを理解する
- 保守性の高い条件制御の実装方法を学ぶ

## 技術ポイント
- **条件ベース生成**: if/switch文での分岐
- **戦略パターン**: Map/Objectでの管理
- **動的判定**: 実行時条件の評価

## 📺 画面表示用コード

### 基本的な条件分岐
```typescript
loadByCondition(type: string) {
  this.container.clear();

  if (type === 'admin') {
    this.container.createComponent(AdminComponent);
  } else {
    this.container.createComponent(UserComponent);
  }
}
```

### switch文での複数条件
```typescript
loadByRole(role: 'admin' | 'editor' | 'viewer') {
  let component: Type<any>;

  switch (role) {
    case 'admin': component = AdminPanelComponent; break;
    case 'editor': component = EditorPanelComponent; break;
    case 'viewer': component = ViewerPanelComponent; break;
  }

  this.container.createComponent(component);
}
```

### Mapを使った管理
```typescript
private componentMap = new Map([
  ['mobile', MobileViewComponent],
  ['tablet', TabletViewComponent],
  ['desktop', DesktopViewComponent]
]);

loadByDevice(deviceType: string) {
  const component = this.componentMap.get(deviceType);
  if (component) {
    this.container.createComponent(component);
  }
}
```

## 実践的な活用例(continued)

### 権限ベースのコンポーネント表示
```typescript
interface Permission {
  role: 'admin' | 'user' | 'guest';
  features: string[];
}

export class PermissionBasedLoader {
  private container = inject(ViewContainerRef);

  private roleComponents = new Map<string, Type<any>>([
    ['admin', AdminDashboardComponent],
    ['user', UserDashboardComponent],
    ['guest', GuestViewComponent]
  ]);

  loadByPermission(permission: Permission) {
    const component = this.roleComponents.get(permission.role);

    if (!component) {
      this.container.createComponent(UnauthorizedComponent);
      return;
    }

    const ref = this.container.createComponent(component);
    ref.setInput('features', permission.features);
    ref.setInput('role', permission.role);
  }

  loadByFeature(permission: Permission, feature: string) {
    if (!permission.features.includes(feature)) {
      this.container.createComponent(FeatureDisabledComponent);
      return;
    }

    const featureMap = new Map([
      ['analytics', AnalyticsComponent],
      ['reports', ReportsComponent],
      ['settings', SettingsComponent]
    ]);

    const component = featureMap.get(feature);
    if (component) {
      this.container.createComponent(component);
    }
  }
}
```

### フィーチャーフラグ対応
```typescript
interface FeatureFlags {
  newUI: boolean;
  experimentalFeatures: boolean;
  betaAccess: boolean;
}

export class FeatureFlagLoader {
  private container = inject(ViewContainerRef);

  loadWithFlags(flags: FeatureFlags) {
    // 新UIが有効な場合
    if (flags.newUI) {
      this.loadNewUI(flags);
    } else {
      this.loadLegacyUI();
    }
  }

  private loadNewUI(flags: FeatureFlags) {
    const ref = this.container.createComponent(NewUIComponent);

    // 実験的機能の有効化
    if (flags.experimentalFeatures) {
      ref.setInput('experimental', true);
    }

    // ベータ機能のアクセス
    if (flags.betaAccess) {
      ref.setInput('betaFeatures', ['feature-a', 'feature-b']);
    }
  }

  private loadLegacyUI() {
    this.container.createComponent(LegacyUIComponent);
  }
}
```

### デバイス・ブラウザ別表示
```typescript
export class DeviceAwareLoader {
  private container = inject(ViewContainerRef);

  loadByDevice() {
    const isMobile = /Mobile|Android|iPhone/i.test(navigator.userAgent);
    const isTablet = /iPad|Tablet/i.test(navigator.userAgent);

    if (isMobile) {
      this.loadMobileView();
    } else if (isTablet) {
      this.loadTabletView();
    } else {
      this.loadDesktopView();
    }
  }

  loadByScreenSize() {
    const width = window.innerWidth;
    let component: Type<any>;

    if (width < 768) {
      component = MobileComponent;
    } else if (width < 1024) {
      component = TabletComponent;
    } else {
      component = DesktopComponent;
    }

    this.container.createComponent(component);
  }

  loadByOrientation() {
    const isPortrait = window.innerHeight > window.innerWidth;

    const component = isPortrait
      ? PortraitComponent
      : LandscapeComponent;

    this.container.createComponent(component);
  }

  private loadMobileView() {
    this.container.createComponent(MobileComponent);
  }

  private loadTabletView() {
    this.container.createComponent(TabletComponent);
  }

  private loadDesktopView() {
    this.container.createComponent(DesktopComponent);
  }
}
```

### A/Bテスト実装
```typescript
export class ABTestLoader {
  private container = inject(ViewContainerRef);

  loadWithABTest(userId: string) {
    const variant = this.getVariant(userId);

    const componentMap = new Map([
      ['A', VariantAComponent],
      ['B', VariantBComponent]
    ]);

    const component = componentMap.get(variant) || VariantAComponent;
    const ref = this.container.createComponent(component);
    ref.setInput('variant', variant);

    // アナリティクスに送信
    this.trackVariant(userId, variant);
  }

  private getVariant(userId: string): 'A' | 'B' {
    // ハッシュベースの振り分け
    const hash = this.hashString(userId);
    return hash % 2 === 0 ? 'A' : 'B';
  }

  private hashString(str: string): number {
    let hash = 0;
    for (let i = 0; i < str.length; i++) {
      hash = ((hash << 5) - hash) + str.charCodeAt(i);
      hash |= 0;
    }
    return Math.abs(hash);
  }

  private trackVariant(userId: string, variant: string) {
    console.log(`User ${userId} assigned to variant ${variant}`);
  }
}
```

### 環境別コンポーネント
```typescript
type Environment = 'development' | 'staging' | 'production';

export class EnvironmentLoader {
  private container = inject(ViewContainerRef);
  private env: Environment = 'production'; // 実際は環境変数から取得

  loadByEnvironment() {
    const envComponents = new Map<Environment, Type<any>>([
      ['development', DevToolsComponent],
      ['staging', StagingBannerComponent],
      ['production', ProductionComponent]
    ]);

    const component = envComponents.get(this.env);
    if (component) {
      this.container.createComponent(component);
    }
  }

  loadDebugInfo() {
    if (this.env === 'development') {
      this.container.createComponent(DebugPanelComponent);
    }
  }
}
```

### 時間ベースの条件表示
```typescript
export class TimeBasedLoader {
  private container = inject(ViewContainerRef);

  loadByTimeOfDay() {
    const hour = new Date().getHours();
    let component: Type<any>;

    if (hour >= 6 && hour < 12) {
      component = MorningGreetingComponent;
    } else if (hour >= 12 && hour < 18) {
      component = AfternoonGreetingComponent;
    } else {
      component = EveningGreetingComponent;
    }

    this.container.createComponent(component);
  }

  loadByCampaignPeriod() {
    const now = new Date();
    const campaignStart = new Date('2024-12-01');
    const campaignEnd = new Date('2024-12-31');

    const component = (now >= campaignStart && now <= campaignEnd)
      ? CampaignComponent
      : RegularComponent;

    this.container.createComponent(component);
  }
}
```

### 複合条件での判定
```typescript
interface LoadCondition {
  userRole: string;
  deviceType: string;
  featureEnabled: boolean;
  isPremium: boolean;
}

export class ComplexConditionLoader {
  private container = inject(ViewContainerRef);

  load(condition: LoadCondition) {
    // 複合条件の評価
    if (condition.isPremium && condition.featureEnabled) {
      this.loadPremiumFeature(condition);
    } else if (condition.userRole === 'admin') {
      this.loadAdminView(condition);
    } else if (condition.deviceType === 'mobile') {
      this.loadMobileView();
    } else {
      this.loadStandardView();
    }
  }

  private loadPremiumFeature(condition: LoadCondition) {
    const ref = this.container.createComponent(PremiumComponent);
    ref.setInput('deviceType', condition.deviceType);
  }

  private loadAdminView(condition: LoadCondition) {
    this.container.createComponent(AdminComponent);
  }

  private loadMobileView() {
    this.container.createComponent(MobileComponent);
  }

  private loadStandardView() {
    this.container.createComponent(StandardComponent);
  }
}
```

## ベストプラクティス

### 戦略パターンの使用
```typescript
// ✅ Mapで管理
private strategies = new Map<string, Type<any>>([
  ['A', ComponentA],
  ['B', ComponentB]
]);

load(key: string) {
  const component = this.strategies.get(key);
  if (component) {
    this.container.createComponent(component);
  }
}

// ❌ 長いif-else
load(key: string) {
  if (key === 'A') {
    this.container.createComponent(ComponentA);
  } else if (key === 'B') {
    this.container.createComponent(ComponentB);
  }
  // ...
}
```

### フォールバック処理
```typescript
// ✅ デフォルトコンポーネントを用意
const component = this.componentMap.get(key) || DefaultComponent;
this.container.createComponent(component);

// ✅ エラーコンポーネントの表示
if (!component) {
  this.container.createComponent(ErrorComponent);
  return;
}
```

### 条件の集約
```typescript
// ✅ 判定ロジックを関数化
private shouldShowAdminPanel(user: User): boolean {
  return user.role === 'admin' && user.isActive && !user.isSuspended;
}

load(user: User) {
  if (this.shouldShowAdminPanel(user)) {
    this.container.createComponent(AdminPanelComponent);
  }
}
```

## 注意点

### 条件の複雑化
条件が複雑になりすぎる場合は、戦略パターンやファクトリーパターンの導入を検討してください。

### パフォーマンス
頻繁に条件評価が行われる場合、結果をキャッシュすることでパフォーマンスを改善できます。

### テスタビリティ
条件ロジックは別関数に切り出すことで、ユニットテストが容易になります。

### 保守性
条件分岐が増えた場合、設定ファイルやデータベースから条件を読み込む仕組みを検討してください。

## 関連技術
- **戦略パターン**: デザインパターン
- **フィーチャーフラグ**: 機能管理
- **A/Bテスト**: 実験的機能展開
- **権限管理**: アクセス制御
- **レスポンシブデザイン**: デバイス対応
