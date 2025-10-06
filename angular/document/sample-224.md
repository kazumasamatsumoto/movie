# #224 「createComponent() - 新方式（v13+）」

## 概要
Angular v13以降では、ViewContainerRef.createComponent()を直接呼び出すだけで動的コンポーネントを生成できます。ComponentFactoryResolverが不要になり、よりシンプルで直感的なAPIになりました。型安全性も向上し、現代的なAngular開発の標準方式となっています。

## 学習目標
- v13以降のcreateComponent()の使い方を習得する
- オプションパラメータの活用方法を理解する
- 旧方式との違いを説明できる

## 技術ポイント
- **シンプルなAPI**: 直接コンポーネントタイプを指定
- **オプション指定**: index、injector、projectableNodesなど
- **型安全性向上**: ComponentRef<T>で型推論が効く

## 📺 画面表示用コード

### 基本的な使い方
```typescript
export class HostComponent {
  private container = inject(ViewContainerRef);

  create() {
    const ref = this.container.createComponent(AlertComponent);
  }
}
```

### オプション付きで生成
```typescript
create() {
  const ref = this.container.createComponent(AlertComponent, {
    index: 0,  // 挿入位置
    injector: this.customInjector  // カスタムインジェクター
  });
}
```

### 型安全な生成
```typescript
const componentRef: ComponentRef<AlertComponent> =
  this.container.createComponent(AlertComponent);

componentRef.instance.message = 'Hello';  // 型チェックが効く
```

## 実践的な活用例

### インデックス指定での挿入
```typescript
export class OrderedContainerComponent {
  private container = inject(ViewContainerRef);

  // 先頭に挿入
  insertAtTop() {
    return this.container.createComponent(ItemComponent, { index: 0 });
  }

  // 2番目に挿入
  insertAtSecond() {
    return this.container.createComponent(ItemComponent, { index: 1 });
  }

  // 末尾に挿入（デフォルト）
  insertAtEnd() {
    return this.container.createComponent(ItemComponent);
  }

  // 現在の要素数の真ん中に挿入
  insertAtMiddle() {
    const middleIndex = Math.floor(this.container.length / 2);
    return this.container.createComponent(ItemComponent, { index: middleIndex });
  }
}
```

### カスタムインジェクターの使用
```typescript
export class CustomInjectionComponent {
  private container = inject(ViewContainerRef);
  private parentInjector = inject(Injector);

  createWithCustomDependency() {
    // カスタムデータを提供
    const customInjector = Injector.create({
      providers: [
        { provide: 'CUSTOM_DATA', useValue: { id: 1, name: 'Test' } }
      ],
      parent: this.parentInjector
    });

    return this.container.createComponent(DataComponent, {
      injector: customInjector
    });
  }
}

// 動的コンポーネント側
@Component({
  selector: 'app-data',
  template: '<p>{{ data.name }}</p>'
})
export class DataComponent {
  data = inject('CUSTOM_DATA');
}
```

### projectableNodes（ng-content対応）
```typescript
export class ProjectionComponent {
  private container = inject(ViewContainerRef);

  createWithProjection() {
    // テンプレート要素を作成
    const textNode = document.createTextNode('投影されるコンテンツ');
    const pElement = document.createElement('p');
    pElement.appendChild(textNode);

    return this.container.createComponent(CardComponent, {
      projectableNodes: [[pElement]]  // ng-content に投影
    });
  }
}

// CardComponent のテンプレート
@Component({
  template: `
    <div class="card">
      <ng-content></ng-content>
    </div>
  `
})
export class CardComponent {}
```

### 環境インジェクター（Environment Injector）の活用
```typescript
export class EnvironmentInjectorComponent {
  private container = inject(ViewContainerRef);
  private envInjector = inject(EnvironmentInjector);

  createWithEnvironmentInjector() {
    return this.container.createComponent(MyComponent, {
      environmentInjector: this.envInjector
    });
  }
}
```

### 複数オプションの組み合わせ
```typescript
export class AdvancedCreationComponent {
  private container = inject(ViewContainerRef);
  private injector = inject(Injector);

  createAdvanced(position: number, customData: any) {
    const customInjector = Injector.create({
      providers: [{ provide: 'DATA', useValue: customData }],
      parent: this.injector
    });

    return this.container.createComponent(DynamicComponent, {
      index: position,
      injector: customInjector,
      projectableNodes: this.createProjectableContent()
    });
  }

  private createProjectableContent(): Node[][] {
    const div = document.createElement('div');
    div.textContent = '動的に投影されるコンテンツ';
    return [[div]];
  }
}
```

## ベストプラクティス

### 型安全な実装
```typescript
// ✅ 型を明示的に指定
const ref: ComponentRef<AlertComponent> =
  this.container.createComponent(AlertComponent);

ref.instance.message = 'Type-safe access';  // IDE補完が効く

// ❌ 型指定なし
const ref = this.container.createComponent(AlertComponent);
ref.instance.unknownProperty = 'error';  // エラー検出が遅れる
```

### オプションオブジェクトの活用
```typescript
// ✅ 読みやすいオプション指定
const options = {
  index: 0,
  injector: this.customInjector
};
this.container.createComponent(MyComponent, options);

// ✅ 必要なオプションのみ指定
this.container.createComponent(MyComponent, { index: 0 });

// ✅ オプションなしもOK
this.container.createComponent(MyComponent);
```

### エラーハンドリング
```typescript
export class SafeCreationComponent {
  private container = inject(ViewContainerRef);

  safeCreate(componentType: Type<any>) {
    try {
      return this.container.createComponent(componentType);
    } catch (error) {
      console.error('コンポーネント生成エラー:', error);
      // フォールバック処理
      return this.container.createComponent(ErrorComponent);
    }
  }
}
```

### 再利用可能なファクトリー関数
```typescript
export class ComponentFactoryService {
  private container = inject(ViewContainerRef);

  createAt(component: Type<any>, index: number) {
    return this.container.createComponent(component, { index });
  }

  createWithData<T>(component: Type<T>, data: Partial<T>) {
    const ref = this.container.createComponent(component);
    Object.assign(ref.instance, data);
    return ref;
  }
}
```

## 注意点

### インデックスの範囲
指定する`index`は0から`container.length`の範囲内でなければなりません。範囲外を指定するとエラーになります。

### インジェクターの継承
カスタムインジェクターを作成する際は、必ず`parent`に既存のインジェクターを指定して、依存関係の解決チェーンを維持してください。

### projectableNodes の制約
`projectableNodes`は複雑なDOM操作を伴うため、パフォーマンスへの影響を考慮してください。単純なデータ渡しには`setInput()`を優先します。

### ライフサイクルフックのタイミング
`createComponent()`直後は、まだコンポーネントの初期化が完了していない場合があります。`ngAfterViewInit()`などのフックを活用してください。

## 関連技術
- **ComponentRef**: 生成されたコンポーネントの参照
- **ViewContainerRef**: コンテナの管理
- **Injector**: 依存性注入の仕組み
- **EnvironmentInjector**: 環境レベルのインジェクター
- **setInput()**: 動的な入力値設定
