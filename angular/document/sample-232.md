# #232 「ComponentRef の活用」

## 概要
ComponentRefは、動的に生成されたコンポーネントへの参照を提供するクラスです。コンポーネントのインスタンスへのアクセス、DOM要素の取得、ライフサイクルの管理など、動的コンポーネントのあらゆる操作が可能になります。

## 学習目標
- ComponentRefの主要プロパティとメソッドを理解する
- 実践的なComponentRefの活用方法を習得する
- コンポーネントの高度な制御テクニックを学ぶ

## 技術ポイント
- **instance**: コンポーネントインスタンスへのアクセス
- **location**: DOM要素（ElementRef）の取得
- **hostView**: ビュー参照の取得
- **destroy()**: コンポーネントの破棄

## 📺 画面表示用コード

### 基本的なプロパティアクセス
```typescript
const ref = this.container.createComponent(MyComponent);

// インスタンスにアクセス
ref.instance.title = 'Hello';

// DOM要素を取得
const element = ref.location.nativeElement;

// ビュー参照を取得
const view = ref.hostView;
```

### コンポーネントタイプの確認
```typescript
const ref = this.container.createComponent(MyComponent);

// コンポーネントのタイプを取得
const componentType = ref.componentType;
console.log(componentType.name); // 'MyComponent'
```

### 変更検知の制御
```typescript
const ref = this.container.createComponent(MyComponent);

// 手動で変更検知を実行
ref.changeDetectorRef.detectChanges();

// 変更検知を無効化
ref.changeDetectorRef.detach();
```

## 実践的な活用例

### DOM操作とスタイリング
```typescript
export class StyledComponentHost {
  private container = inject(ViewContainerRef);

  createStyledComponent() {
    const ref = this.container.createComponent(CardComponent);

    // DOM要素を取得してスタイルを適用
    const element = ref.location.nativeElement as HTMLElement;
    element.style.backgroundColor = '#f0f0f0';
    element.style.padding = '20px';
    element.style.borderRadius = '8px';
    element.classList.add('animated', 'fade-in');

    // データ属性を追加
    element.setAttribute('data-component-id', 'card-123');

    return ref;
  }
}
```

### アニメーション制御
```typescript
export class AnimatedComponentHost {
  private container = inject(ViewContainerRef);

  async createWithAnimation() {
    const ref = this.container.createComponent(PanelComponent);
    const element = ref.location.nativeElement as HTMLElement;

    // 初期状態を設定
    element.style.opacity = '0';
    element.style.transform = 'translateY(-20px)';
    element.style.transition = 'all 0.3s ease';

    // DOMに追加後、アニメーション実行
    requestAnimationFrame(() => {
      element.style.opacity = '1';
      element.style.transform = 'translateY(0)';
    });

    return ref;
  }

  async removeWithAnimation(ref: ComponentRef<any>) {
    const element = ref.location.nativeElement as HTMLElement;

    // フェードアウトアニメーション
    element.style.opacity = '0';
    element.style.transform = 'translateY(20px)';

    // アニメーション完了を待って破棄
    await new Promise(resolve => setTimeout(resolve, 300));
    ref.destroy();
  }
}
```

### 位置とサイズの制御
```typescript
export class PositionableComponentHost {
  private container = inject(ViewContainerRef);

  createAtPosition(x: number, y: number) {
    const ref = this.container.createComponent(TooltipComponent);
    const element = ref.location.nativeElement as HTMLElement;

    // 絶対配置
    element.style.position = 'absolute';
    element.style.left = `${x}px`;
    element.style.top = `${y}px`;
    element.style.zIndex = '1000';

    return ref;
  }

  setSize(ref: ComponentRef<any>, width: number, height: number) {
    const element = ref.location.nativeElement as HTMLElement;
    element.style.width = `${width}px`;
    element.style.height = `${height}px`;
  }

  centerOnScreen(ref: ComponentRef<any>) {
    const element = ref.location.nativeElement as HTMLElement;
    element.style.position = 'fixed';
    element.style.left = '50%';
    element.style.top = '50%';
    element.style.transform = 'translate(-50%, -50%)';
  }
}
```

### ChangeDetectorRefの活用
```typescript
export class OptimizedComponentHost {
  private container = inject(ViewContainerRef);

  createOptimized() {
    const ref = this.container.createComponent(HeavyComponent);

    // 変更検知を無効化（パフォーマンス最適化）
    ref.changeDetectorRef.detach();

    // 必要な時だけ手動で変更検知
    ref.instance.dataChanged.subscribe(() => {
      ref.changeDetectorRef.detectChanges();
    });

    return ref;
  }

  updateData(ref: ComponentRef<any>, data: any) {
    ref.instance.data = data;
    // 変更を反映
    ref.changeDetectorRef.markForCheck();
  }
}
```

### イベント監視とデバッグ
```typescript
export class MonitoredComponentHost {
  private container = inject(ViewContainerRef);

  createMonitored() {
    const ref = this.container.createComponent(DataComponent);

    // DOMイベントを監視
    const element = ref.location.nativeElement as HTMLElement;
    element.addEventListener('click', (e) => {
      console.log('Component clicked:', ref.componentType.name);
    });

    // コンポーネントの状態を監視
    const originalNgOnDestroy = ref.instance.ngOnDestroy;
    ref.instance.ngOnDestroy = () => {
      console.log('Component destroying:', ref.componentType.name);
      originalNgOnDestroy?.call(ref.instance);
    };

    // ビューの状態をチェック
    console.log('View destroyed?', ref.hostView.destroyed);

    return ref;
  }
}
```

### 動的プロパティアクセス
```typescript
export class DynamicPropertyHost {
  private container = inject(ViewContainerRef);

  createWithDynamicProps(componentType: Type<any>, props: Record<string, any>) {
    const ref = this.container.createComponent(componentType);

    // 動的にプロパティを設定
    Object.entries(props).forEach(([key, value]) => {
      if (key in ref.instance) {
        (ref.instance as any)[key] = value;
      } else {
        console.warn(`Property ${key} not found on component`);
      }
    });

    // 変更検知を実行
    ref.changeDetectorRef.detectChanges();

    return ref;
  }

  readProperty<T>(ref: ComponentRef<any>, propertyName: string): T | undefined {
    if (propertyName in ref.instance) {
      return (ref.instance as any)[propertyName] as T;
    }
    return undefined;
  }
}
```

### コンポーネント間通信
```typescript
interface MessageBus {
  send(message: any): void;
  receive(): Observable<any>;
}

export class CommunicatingComponentHost {
  private container = inject(ViewContainerRef);
  private messageBus = new Subject<any>();

  createConnected(componentType: Type<any>) {
    const ref = this.container.createComponent(componentType);

    // メッセージバスを注入
    if ('messageBus' in ref.instance) {
      (ref.instance as any).messageBus = {
        send: (msg: any) => this.messageBus.next(msg),
        receive: () => this.messageBus.asObservable()
      };
    }

    return ref;
  }

  broadcast(message: any) {
    this.messageBus.next(message);
  }
}
```

### ビュー操作
```typescript
export class ViewManipulationHost {
  private container = inject(ViewContainerRef);
  private appRef = inject(ApplicationRef);

  createDetached() {
    const ref = this.container.createComponent(PopupComponent);

    // ビューをデタッチ（変更検知から除外）
    this.appRef.detachView(ref.hostView);

    // 必要に応じて再アタッチ
    setTimeout(() => {
      this.appRef.attachView(ref.hostView);
    }, 1000);

    return ref;
  }

  moveToContainer(ref: ComponentRef<any>, newContainer: ViewContainerRef) {
    // 現在のコンテナから削除（ビューは維持）
    const currentIndex = this.container.indexOf(ref.hostView);
    if (currentIndex !== -1) {
      this.container.detach(currentIndex);
    }

    // 新しいコンテナに追加
    newContainer.insert(ref.hostView);
  }
}
```

### コンポーネントメタデータの取得
```typescript
export class MetadataInspector {
  inspectComponent(ref: ComponentRef<any>) {
    const metadata = {
      name: ref.componentType.name,
      destroyed: ref.hostView.destroyed,
      elementTag: ref.location.nativeElement.tagName,
      properties: Object.keys(ref.instance),
      methods: Object.getOwnPropertyNames(
        Object.getPrototypeOf(ref.instance)
      ).filter(name => name !== 'constructor')
    };

    console.log('Component Metadata:', metadata);
    return metadata;
  }

  isInstanceOf<T>(ref: ComponentRef<any>, type: Type<T>): boolean {
    return ref.componentType === type;
  }
}
```

## ベストプラクティス

### 型安全なインスタンスアクセス
```typescript
// ✅ 型を明示
const ref: ComponentRef<MyComponent> =
  this.container.createComponent(MyComponent);

ref.instance.myMethod(); // 型チェックが効く

// ❌ any型でのアクセス
const ref: ComponentRef<any> = this.container.createComponent(MyComponent);
ref.instance.unknownMethod(); // エラー検出できない
```

### DOM操作の安全な実装
```typescript
// ✅ 型チェックと存在確認
const element = ref.location.nativeElement;
if (element instanceof HTMLElement) {
  element.style.color = 'red';
}

// ❌ 直接キャスト（危険）
(ref.location.nativeElement as HTMLElement).style.color = 'red';
```

### リソースのクリーンアップ
```typescript
ngOnDestroy() {
  // イベントリスナーを削除
  const element = this.ref?.location.nativeElement;
  if (element) {
    element.removeEventListener('click', this.clickHandler);
  }

  // コンポーネントを破棄
  this.ref?.destroy();
}
```

## 注意点

### 破棄済みコンポーネントへのアクセス
`destroy()`後のComponentRefへのアクセスはエラーになります。`hostView.destroyed`で状態を確認してください。

### 変更検知のタイミング
`instance`経由でプロパティを変更しても、自動的に変更検知は実行されません。必要に応じて`detectChanges()`を呼び出してください。

### DOM操作のタイミング
コンポーネント生成直後、まだDOMに完全にレンダリングされていない可能性があります。`requestAnimationFrame()`を使うと安全です。

### メモリリーク
イベントリスナーを追加した場合、コンポーネント破棄時に必ず削除してください。

## 関連技術
- **ViewContainerRef**: コンテナ管理
- **ElementRef**: DOM要素参照
- **ChangeDetectorRef**: 変更検知制御
- **ViewRef**: ビュー参照
- **ApplicationRef**: アプリケーションレベルの管理
