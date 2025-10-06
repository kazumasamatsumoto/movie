# #229 「動的 Component の置き換え」

## 概要
動的コンポーネントの置き換えは、既存のコンポーネントを削除してから新しいコンポーネントを作成する方法が基本です。clear()やdestroy()で削除した後、createComponent()で新規作成するパターンや、データを保持しながら置き換えるパターンなど、用途に応じた実装方法があります。

## 学習目標
- コンポーネント置き換えの基本パターンを習得する
- 状態を保持しながら置き換える方法を理解する
- 効率的な置き換え実装のベストプラクティスを学ぶ

## 技術ポイント
- **clear() + createComponent()**: 全削除してから作成
- **destroy() + createComponent()**: 個別削除してから作成
- **データ保持**: 置き換え前に状態を退避

## 📺 画面表示用コード

### 基本的な置き換え
```typescript
// 既存を削除して新規作成
this.container.clear();
const newRef = this.container.createComponent(NewComponent);
```

### 個別の置き換え
```typescript
// 既存の参照を破棄
this.currentRef?.destroy();
// 新しいコンポーネントを作成
this.currentRef = this.container.createComponent(NewComponent);
```

### 状態を保持した置き換え
```typescript
// データを退避
const data = this.currentRef?.instance.data;
// 置き換え
this.currentRef?.destroy();
this.currentRef = this.container.createComponent(NewComponent);
this.currentRef.setInput('data', data);
```

## 実践的な活用例

### ビュー切り替えシステム
```typescript
export class ViewSwitcherComponent {
  private container = inject(ViewContainerRef);
  private currentView?: ComponentRef<any>;

  switchTo(viewType: Type<any>, data?: any) {
    // 既存ビューを削除
    this.currentView?.destroy();

    // 新しいビューを作成
    this.currentView = this.container.createComponent(viewType);

    // データがあれば設定
    if (data) {
      Object.entries(data).forEach(([key, value]) => {
        this.currentView?.setInput(key, value);
      });
    }
  }

  getCurrentViewType(): Type<any> | undefined {
    return this.currentView?.componentType;
  }
}

// 使用例
this.viewSwitcher.switchTo(GridViewComponent, { items: this.items });
this.viewSwitcher.switchTo(ListViewComponent, { items: this.items });
```

### タブコンテンツの切り替え
```typescript
interface Tab {
  id: string;
  title: string;
  component: Type<any>;
  data?: any;
}

export class TabComponent {
  private contentContainer = inject(ViewContainerRef);
  private currentTabRef?: ComponentRef<any>;

  tabs: Tab[] = [
    { id: 'overview', title: '概要', component: OverviewComponent },
    { id: 'details', title: '詳細', component: DetailsComponent },
    { id: 'settings', title: '設定', component: SettingsComponent }
  ];

  selectTab(tab: Tab) {
    // 既存のタブコンテンツを削除
    this.currentTabRef?.destroy();

    // 新しいタブコンテンツを表示
    this.currentTabRef = this.contentContainer.createComponent(tab.component);

    // タブ固有のデータを設定
    if (tab.data) {
      Object.entries(tab.data).forEach(([key, value]) => {
        this.currentTabRef?.setInput(key, value);
      });
    }
  }
}
```

### アニメーション付き置き換え
```typescript
export class AnimatedReplacementComponent {
  private container = inject(ViewContainerRef);
  private currentRef?: ComponentRef<any>;

  async replaceWithAnimation(
    newComponent: Type<any>,
    animationDuration = 300
  ) {
    // フェードアウト（オプション: アニメーションクラスを追加）
    if (this.currentRef) {
      const element = this.currentRef.location.nativeElement;
      element.classList.add('fade-out');

      // アニメーション完了を待つ
      await new Promise(resolve => setTimeout(resolve, animationDuration));

      this.currentRef.destroy();
    }

    // 新しいコンポーネントを作成
    this.currentRef = this.container.createComponent(newComponent);

    // フェードイン
    const newElement = this.currentRef.location.nativeElement;
    newElement.classList.add('fade-in');
  }
}
```

### 条件付き置き換え
```typescript
export class ConditionalReplacementComponent {
  private container = inject(ViewContainerRef);
  private currentRef?: ComponentRef<any>;

  replaceIfDifferent(newComponentType: Type<any>, data?: any) {
    // 同じコンポーネントタイプなら置き換えない
    if (this.currentRef?.componentType === newComponentType) {
      // データだけ更新
      if (data) {
        Object.entries(data).forEach(([key, value]) => {
          this.currentRef?.setInput(key, value);
        });
      }
      return this.currentRef;
    }

    // 異なるコンポーネントなら置き換え
    this.currentRef?.destroy();
    this.currentRef = this.container.createComponent(newComponentType);

    if (data) {
      Object.entries(data).forEach(([key, value]) => {
        this.currentRef?.setInput(key, value);
      });
    }

    return this.currentRef;
  }
}
```

### 状態を完全に保持した置き換え
```typescript
export class StatefulReplacementComponent {
  private container = inject(ViewContainerRef);
  private currentRef?: ComponentRef<any>;

  replaceWithState(newComponent: Type<any>) {
    // 現在の状態を全て取得
    const state = this.getCurrentState();

    // コンポーネントを置き換え
    this.currentRef?.destroy();
    this.currentRef = this.container.createComponent(newComponent);

    // 状態を復元
    this.restoreState(state);

    return this.currentRef;
  }

  private getCurrentState(): Record<string, any> {
    if (!this.currentRef) return {};

    const instance = this.currentRef.instance;
    const state: Record<string, any> = {};

    // インスタンスのプロパティを全て取得
    Object.keys(instance).forEach(key => {
      if (!key.startsWith('_')) {  // プライベートプロパティは除外
        state[key] = instance[key];
      }
    });

    return state;
  }

  private restoreState(state: Record<string, any>) {
    if (!this.currentRef) return;

    Object.entries(state).forEach(([key, value]) => {
      try {
        this.currentRef?.setInput(key, value);
      } catch (error) {
        console.warn(`状態の復元に失敗: ${key}`, error);
      }
    });
  }
}
```

### 複数位置での置き換え
```typescript
export class MultiPositionReplacementComponent {
  private container = inject(ViewContainerRef);
  private components = new Map<number, ComponentRef<any>>();

  replaceAt(index: number, component: Type<any>, data?: any) {
    // 指定位置の既存コンポーネントを削除
    const existing = this.components.get(index);
    if (existing) {
      existing.destroy();
    }

    // 新しいコンポーネントを同じ位置に作成
    const newRef = this.container.createComponent(component, { index });

    if (data) {
      Object.entries(data).forEach(([key, value]) => {
        newRef.setInput(key, value);
      });
    }

    this.components.set(index, newRef);
    return newRef;
  }

  replaceAll(component: Type<any>) {
    // 全てのコンポーネントを同じタイプに置き換え
    this.components.forEach((ref, index) => {
      ref.destroy();
      const newRef = this.container.createComponent(component, { index });
      this.components.set(index, newRef);
    });
  }
}
```

### ファクトリーパターンでの置き換え
```typescript
type ComponentFactory = () => Type<any>;

export class FactoryReplacementComponent {
  private container = inject(ViewContainerRef);
  private currentRef?: ComponentRef<any>;

  private factories = new Map<string, ComponentFactory>([
    ['view-a', () => ViewAComponent],
    ['view-b', () => ViewBComponent],
    ['view-c', () => ViewCComponent]
  ]);

  switchToView(viewId: string, data?: any) {
    const factory = this.factories.get(viewId);
    if (!factory) {
      console.error(`Unknown view: ${viewId}`);
      return;
    }

    this.currentRef?.destroy();

    const componentType = factory();
    this.currentRef = this.container.createComponent(componentType);

    if (data) {
      Object.entries(data).forEach(([key, value]) => {
        this.currentRef?.setInput(key, value);
      });
    }
  }

  registerFactory(id: string, factory: ComponentFactory) {
    this.factories.set(id, factory);
  }
}
```

## ベストプラクティス

### 置き換え前のクリーンアップ
```typescript
// ✅ 既存コンポーネントを確実に削除
replace(newComponent: Type<any>) {
  if (this.currentRef) {
    this.currentRef.destroy();
    this.currentRef = undefined;
  }
  this.currentRef = this.container.createComponent(newComponent);
}

// ❌ 削除を忘れるとメモリリーク
replace(newComponent: Type<any>) {
  this.currentRef = this.container.createComponent(newComponent); // 古い参照が残る
}
```

### 型安全な置き換え
```typescript
replaceTyped<T>(component: Type<T>, inputs?: Partial<T>): ComponentRef<T> {
  this.currentRef?.destroy();
  this.currentRef = this.container.createComponent(component);

  if (inputs) {
    Object.entries(inputs).forEach(([key, value]) => {
      this.currentRef?.setInput(key, value);
    });
  }

  return this.currentRef;
}
```

### 置き換えのトランザクション
```typescript
// ✅ エラーが起きても安全
safeReplace(newComponent: Type<any>) {
  const oldRef = this.currentRef;
  try {
    this.currentRef = this.container.createComponent(newComponent);
    oldRef?.destroy();
  } catch (error) {
    console.error('置き換えエラー:', error);
    this.currentRef = oldRef; // ロールバック
  }
}
```

## 注意点

### 参照の更新
置き換え後は、必ず新しいComponentRefを保持してください。古い参照は無効になります。

### イベント購読の再設定
コンポーネントを置き換えると、以前のイベント購読は失われます。必要なら再設定してください。

### アニメーションのタイミング
アニメーション付きで置き換える場合、アニメーション完了を待ってから削除することで、スムーズな遷移を実現できます。

### インデックスの考慮
特定の位置に置き換える場合、`index`オプションを正しく指定しないと、意図しない位置に挿入される可能性があります。

## 関連技術
- **ComponentRef**: コンポーネント参照
- **ViewContainerRef**: コンテナ管理
- **destroy()**: コンポーネント削除
- **createComponent()**: コンポーネント生成
- **アニメーション**: スムーズな遷移効果
