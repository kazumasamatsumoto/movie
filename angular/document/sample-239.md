# #239 「動的ウィジェットシステム」

## 概要
ダッシュボードのウィジェットなど、ユーザー設定に応じてコンポーネントを動的に配置・再構築するシステムを実装する方法を学びます。

## 学習目標
- ウィジェット定義（種類・位置・設定）をもとにコンポーネントを生成する手順を理解する
- ComponentRefとWidgetConfigを紐付けて状態を管理する方法を習得する
- 再配置や削除などインタラクティブな操作に対応するパターンを把握する

## 技術ポイント
- **定義**: `WidgetConfig { type, position, settings }`
- **生成**: `viewContainerRef.createComponent`でコンポーネント生成、設定をInputで渡す
- **管理**: `Map<string, ComponentRef>`などで参照を追跡し、ドラック&ドロップで位置変更も可能

## 📺 画面表示用コード（動画用）

```typescript
const ref = this.host.createComponent(widgetMap[config.type]);
ref.instance.settings = config.settings;
```

```typescript
this.widgets[config.id] = { config, ref };
```

```typescript
ref.destroy();
```

## 💻 詳細実装例（学習用）
```typescript
// dashboard.component.ts
import { Component, ComponentRef, ViewChild, ViewContainerRef } from '@angular/core';
import { WeatherWidgetComponent } from './widgets/weather-widget.component';
import { StockWidgetComponent } from './widgets/stock-widget.component';
import { WidgetConfig } from './widgets/widget-config';

const WIDGETS = {
  weather: WeatherWidgetComponent,
  stock: StockWidgetComponent,
} as const;

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [WeatherWidgetComponent, StockWidgetComponent],
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.scss'],
})
export class DashboardComponent {
  @ViewChild('host', { read: ViewContainerRef, static: true })
  host!: ViewContainerRef;

  widgetRefMap = new Map<string, ComponentRef<any>>();

  load(configs: WidgetConfig[]): void {
    this.host.clear();
    this.widgetRefMap.forEach((ref) => ref.destroy());
    this.widgetRefMap.clear();

    configs.forEach((config) => {
      const component = WIDGETS[config.type];
      if (!component) return;
      const ref = this.host.createComponent(component);
      ref.instance.settings = config.settings;
      ref.instance.position = config.position;
      this.widgetRefMap.set(config.id, ref);
    });
  }

  remove(id: string): void {
    const ref = this.widgetRefMap.get(id);
    if (ref) {
      ref.destroy();
      this.widgetRefMap.delete(id);
    }
  }
}
```

## ベストプラクティス
- Widgetの種類・設定・位置情報を明確に保持する型を定義し、コンポーネントに渡す
- リフレッシュや再配置（ドラッグ&ドロップ）時にdestroy→createするか、hostViewを移動するかを設計する
- ウィジェットが多い場合は仮想スクロールや遅延ロードを導入してパフォーマンスを最適化する

## 注意点
- 設定をサービスやStoreで管理し、ページ離脱後も構成を保持できるようにする
- ComponentRefをマップで管理する際、削除時に確実にdestroyする
- レンダリング順序やZ-indexを調整し、UIの整合性を保つ

## 関連技術
- 動的タブシステム（#238）
- プラグインアーキテクチャ（#240）
- Angular CDK Drag&Dropでのレイアウト操作
