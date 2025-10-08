# #241 「Component ファクトリーパターン」

## 概要
動的コンポーネント生成を工場（ファクトリ）に集約し、識別子や設定からコンポーネントを生成する設計パターンを紹介します。ロジックをサービス化することでテスト・保守性を高めます。

## 学習目標
- ファクトリサービスにコンポーネント生成ロジックを集約する方法を理解する
- 識別子ベースのコンポーネント生成を実装する
- テストでファクトリをモックしやすくなる利点を把握する

## 技術ポイント
- **Factory Service**: `DynamicComponentFactory.create(id, viewContainerRef, config)`
- **マッピング**: コンポーネントクラスを辞書に登録し、識別子から取得
- **テスト**: Factoryをモックすることで生成タイミングを制御

## 📺 画面表示用コード（動画用）

```typescript
factory.register('alert', AlertComponent);
```

```typescript
factory.create('alert', host, { message: 'hi' });
```

```typescript
ref.destroy();
```

## 💻 詳細実装例（学習用）
```typescript
// dynamic-component-factory.service.ts
import { Injectable, Type, ViewContainerRef, ComponentRef } from '@angular/core';

type ComponentMap = Record<string, Type<any>>;

@Injectable({ providedIn: 'root' })
export class DynamicComponentFactory {
  private components: ComponentMap = {};

  register(id: string, component: Type<any>): void {
    this.components[id] = component;
  }

  create<T>(id: string, host: ViewContainerRef, config?: Partial<T>): ComponentRef<T> {
    const component = this.components[id];
    if (!component) throw new Error(`Component not registered: ${id}`);
    const ref = host.createComponent<T>(component);
    if (config) {
      Object.assign(ref.instance, config);
      ref.changeDetectorRef.detectChanges();
    }
    return ref;
  }
}
```

```typescript
// usage.component.ts
import { Component, ViewChild, ViewContainerRef } from '@angular/core';
import { DynamicComponentFactory } from './dynamic-component-factory.service';
import { AlertComponent } from './alert.component';

@Component({
  selector: 'app-usage',
  standalone: true,
  imports: [AlertComponent],
  template: `<ng-container #host></ng-container>`,
})
export class UsageComponent {
  @ViewChild('host', { read: ViewContainerRef, static: true })
  host!: ViewContainerRef;

  constructor(private readonly factory: DynamicComponentFactory) {
    this.factory.register('alert', AlertComponent);
  }

  showAlert() {
    this.factory.create('alert', this.host, { message: 'Factory pattern' });
  }
}
```

## ベストプラクティス
- ファクトリに登録するコンポーネントをモジュール起動時にまとめる
- Configオブジェクトに型を付けてInput設定を安全に行う
- テストではMockFactoryを注入し、生成呼び出しが行われたかをアサートする

## 注意点
- 登録忘れするとランタイムエラーになるため、サニティチェックを行う
- 依存サービスが必要なコンポーネントには`EnvironmentInjector`などの注入オプションを渡す必要がある
- 識別子の衝突や命名規則を統一し、ドキュメント化して利用者に周知する

## 関連技術
- プラグインアーキテクチャ（#240）
- ComponentRef活用（#232）
- 動的ローディング・遅延ロード（#234, #235）
