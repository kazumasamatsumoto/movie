# #223 「ComponentFactoryResolver（旧方式）」

## 概要
ComponentFactoryResolverは、Angular v13以前に動的コンポーネントを生成するために使用されていたサービスです。ComponentFactoryを解決（resolve）して、それを使ってコンポーネントインスタンスを作成する仕組みでした。v13以降は非推奨となり、ViewContainerRef.createComponent()の直接使用が推奨されています。

## 学習目標
- ComponentFactoryResolverの役割を理解する（歴史的背景）
- 旧方式と新方式の違いを説明できる
- レガシーコードを新方式に移行できる

## 技術ポイント
- **v13以前の標準方式**: ComponentFactory経由での生成
- **v13以降deprecated**: 直接createComponent()を使用
- **移行の重要性**: 新規開発では新方式を採用

## 📺 画面表示用コード

### 旧方式（v13以前）
```typescript
export class OldWayComponent {
  constructor(
    private resolver: ComponentFactoryResolver,
    private viewContainer: ViewContainerRef
  ) {}

  loadComponent() {
    const factory = this.resolver.resolveComponentFactory(AlertComponent);
    this.viewContainer.createComponentFromFactory(factory);
  }
}
```

### 新方式（v13以降推奨）
```typescript
export class NewWayComponent {
  private viewContainer = inject(ViewContainerRef);

  loadComponent() {
    this.viewContainer.createComponent(AlertComponent);
  }
}
```

### entryComponents（v9以前は必須）
```typescript
// v9以前は entryComponents に登録が必要だった
@NgModule({
  declarations: [AlertComponent],
  entryComponents: [AlertComponent] // v9以降は不要
})
export class AppModule {}
```

## 実践的な活用例

### 旧方式の完全な実装例
```typescript
import { Component, ViewChild, ViewContainerRef, ComponentFactoryResolver } from '@angular/core';

@Component({
  selector: 'app-legacy-host',
  template: '<ng-container #container></ng-container>'
})
export class LegacyHostComponent {
  @ViewChild('container', { read: ViewContainerRef })
  container!: ViewContainerRef;

  constructor(private componentFactoryResolver: ComponentFactoryResolver) {}

  loadDynamicComponent() {
    // Step 1: ComponentFactory を解決
    const componentFactory = this.componentFactoryResolver
      .resolveComponentFactory(DynamicComponent);

    // Step 2: ViewContainerRef をクリア
    this.container.clear();

    // Step 3: ComponentFactory からコンポーネントを作成
    const componentRef = this.container.createComponent(componentFactory);

    // Step 4: 入力値を設定
    componentRef.instance.title = 'Dynamic Title';
  }
}
```

### 新方式への移行例
```typescript
// Before (v13以前)
export class OldComponent {
  constructor(
    private resolver: ComponentFactoryResolver,
    private viewContainer: ViewContainerRef
  ) {}

  load() {
    const factory = this.resolver.resolveComponentFactory(MyComponent);
    const ref = this.viewContainer.createComponent(factory);
    ref.instance.data = 'value';
  }
}

// After (v13以降)
export class NewComponent {
  private viewContainer = inject(ViewContainerRef);

  load() {
    const ref = this.viewContainer.createComponent(MyComponent);
    ref.setInput('data', 'value');
  }
}
```

### Module指定が必要だった場合の移行
```typescript
// Before: NgModuleRef を指定
export class OldModuleComponent {
  constructor(
    private resolver: ComponentFactoryResolver,
    private viewContainer: ViewContainerRef,
    private injector: Injector
  ) {}

  load() {
    const factory = this.resolver.resolveComponentFactory(MyComponent);
    this.viewContainer.createComponent(factory, 0, this.injector);
  }
}

// After: より簡潔に
export class NewModuleComponent {
  private viewContainer = inject(ViewContainerRef);

  load() {
    this.viewContainer.createComponent(MyComponent);
  }
}
```

## ベストプラクティス

### 新規プロジェクトでの対応
```typescript
// ✅ v13以降の新規プロジェクトでは直接 createComponent() を使用
export class ModernComponent {
  private container = inject(ViewContainerRef);

  create() {
    this.container.createComponent(DynamicComponent);
  }
}

// ❌ ComponentFactoryResolver は使用しない
export class AvoidComponent {
  constructor(private resolver: ComponentFactoryResolver) {} // 非推奨
}
```

### レガシーコードのリファクタリング
```typescript
// 段階的な移行アプローチ
export class MigrationComponent {
  private container = inject(ViewContainerRef);

  // Phase 1: ComponentFactoryResolver の削除
  load() {
    // const factory = this.resolver.resolveComponentFactory(C); // 削除
    const ref = this.container.createComponent(MyComponent);
    return ref;
  }

  // Phase 2: setInput() の使用
  loadWithInput() {
    const ref = this.container.createComponent(MyComponent);
    ref.setInput('title', 'New Title'); // instance 直接アクセスより推奨
  }
}
```

### エラーハンドリングの改善
```typescript
export class SafeMigrationComponent {
  private container = inject(ViewContainerRef);

  load(componentType: Type<any>) {
    try {
      const ref = this.container.createComponent(componentType);
      return ref;
    } catch (error) {
      console.error('コンポーネントの生成に失敗:', error);
      // フォールバック処理
      return null;
    }
  }
}
```

## 注意点

### entryComponents の削除
v9以降、Ivy レンダラーでは`entryComponents`の指定が不要になりました。古いコードを見つけたら削除できます。

### ComponentFactoryResolver の削除タイミング
既存プロジェクトでは、Angularバージョンをv13以上にアップグレードした後、段階的に新方式へ移行してください。

### 型安全性の向上
新方式では`setInput()`を使うことで、より型安全なコード記述が可能になっています。

### パフォーマンスの違い
新方式の方がシンプルで、内部的にも最適化されているため、わずかにパフォーマンスが向上しています。

## 関連技術
- **ViewContainerRef**: コンポーネント挿入先の管理
- **ComponentRef**: 生成されたコンポーネントの参照
- **Ivy レンダラー**: v9以降のレンダリングエンジン
- **createComponent()**: v13以降の推奨API
- **Angular バージョン移行ガイド**: 公式の移行手順
