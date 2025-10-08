# #240 「プラグインアーキテクチャ」

## 概要
Angularでプラグインを動的に読み込み、対応するコンポーネントを表示する構造を設計する方法を学びます。Dynamic importとComponentFactoryを組み合わせ、機能拡張を容易にします。

## 学習目標
- プラグイン識別子とコンポーネントのマッピング方法を理解する
- プラグインをLazy loadし、Dynamic Componentとして生成する実装を習得する
- プラグインごとの依存関係や設定を注入する手順を把握する

## 技術ポイント
- **プラグイン登録**: `PluginRegistry`を用意し、識別子→Dynamic import関数を登録
- **ロード**: `await registry.load('analytics')`でコンポーネント定義を取得
- **生成**: `ViewContainerRef.createComponent(componentType)`で表示

## 📺 画面表示用コード（動画用）

```typescript
const component = await registry.load(pluginId);
this.host.createComponent(component);
```

```typescript
registry.register('chart', () => import('./plugins/chart.plugin').then(m => m.ChartPluginComponent));
```

```typescript
ref.instance.config = pluginConfig;
```

## 💻 詳細実装例（学習用）
```typescript
// plugin-registry.service.ts
import { Injectable, Type } from '@angular/core';

type Loader = () => Promise<Type<unknown>>;

@Injectable({ providedIn: 'root' })
export class PluginRegistry {
  private loaders = new Map<string, Loader>();

  register(id: string, loader: Loader): void {
    this.loaders.set(id, loader);
  }

  async load<T>(id: string): Promise<Type<T>> {
    const loader = this.loaders.get(id);
    if (!loader) throw new Error(`Plugin not found: ${id}`);
    return (await loader()) as Type<T>;
  }
}
```

```typescript
// plugin-host.component.ts
import { Component, Injector, ViewChild, ViewContainerRef } from '@angular/core';
import { PluginRegistry } from './plugin-registry.service';

@Component({
  selector: 'app-plugin-host',
  standalone: true,
  templateUrl: './plugin-host.component.html',
})
export class PluginHostComponent {
  @ViewChild('host', { read: ViewContainerRef, static: true })
  host!: ViewContainerRef;

  constructor(private readonly registry: PluginRegistry, private readonly injector: Injector) {}

  async load(id: string): Promise<void> {
    this.host.clear();
    const component = await this.registry.load(id);
    const ref = this.host.createComponent(component, { injector: this.injector });
    if ('config' in ref.instance) {
      (ref.instance as any).config = { pluginId: id };
    }
  }
}
```

## ベストプラクティス
- プラグイン登録を初期化処理でまとめて行い、設定ファイルやAPIから動的にロードする
- プラグインのインターフェース（Input/Output）を定義し、互換性を保つ
- 依存サービスはEnvironmentInjectorやInjectorを指定して注入し、プラグインごとに設定可能にする

## 注意点
- Dynamic importするパスはビルドで決定できるようにし、任意文字列連結は避ける
- プラグイン破棄時に関連する購読やリソースを確実に破棄する
- セキュリティの観点から、読み込むプラグインを信頼できるソースに限定する

## 関連技術
- 遅延ロードコンポーネント（#235）
- Component Factoryパターン（#241）
- Angular CDK Portal / Overlayによるプラグイン表示
