# #238 「動的タブシステム」

## 概要
動的に追加・削除できるタブUIを実装し、`ViewContainerRef`でタブコンテンツを管理するパターンを学びます。

## 学習目標
- タブごとにコンポーネントを生成・破棄する方法を理解する
- タブリストとComponentRefを同期し、閉じる操作に対応する
- 選択タブの状態を管理し、UIを更新する手順を習得する

## 技術ポイント
- **タブデータ**: `{ id, title, component, ref }` のようにメタ情報を保持
- **ViewContainerRef**: タブごとのアンカー、または1つのコンテナを利用しhostViewを差し替える
- **イベント**: タブ切り替え時にChange Detectionを手動で走らせることも可能

## 📺 画面表示用コード（動画用）

```typescript
const ref = this.host.createComponent(TAB_MAP[type]);
this.tabs.push({ id, title, ref });
```

```typescript
select(tab) { this.active = tab; this.show(tab.ref); }
```

```typescript
close(tab) { tab.ref.destroy(); this.tabs = this.tabs.filter(t => t !== tab); }
```

## 💻 詳細実装例（学習用）
```typescript
// dynamic-tabs.component.ts
import { Component, ComponentRef, ViewChild, ViewContainerRef } from '@angular/core';
import { ChartWidgetComponent } from './widgets/chart-widget.component';
import { LogWidgetComponent } from './widgets/log-widget.component';

const TAB_COMPONENTS = {
  chart: ChartWidgetComponent,
  log: LogWidgetComponent,
} as const;

type TabType = keyof typeof TAB_COMPONENTS;

interface DynamicTab {
  id: number;
  type: TabType;
  title: string;
  ref: ComponentRef<any>;
}

@Component({
  selector: 'app-dynamic-tabs',
  standalone: true,
  imports: [ChartWidgetComponent, LogWidgetComponent],
  templateUrl: './dynamic-tabs.component.html',
  styleUrls: ['./dynamic-tabs.component.scss'],
})
export class DynamicTabsComponent {
  @ViewChild('host', { read: ViewContainerRef, static: true })
  host!: ViewContainerRef;

  tabs: DynamicTab[] = [];
  active?: DynamicTab;
  counter = 0;

  open(type: TabType) {
    const ref = this.host.createComponent(TAB_COMPONENTS[type]);
    const tab: DynamicTab = {
      id: ++this.counter,
      type,
      title: `${type.toUpperCase()} #${this.counter}`,
      ref,
    };
    this.tabs.push(tab);
    this.select(tab);
  }

  select(tab: DynamicTab) {
    this.active = tab;
    this.tabs.forEach((t) => (t.ref.location.nativeElement.hidden = t !== tab));
  }

  close(tab: DynamicTab) {
    const index = this.tabs.indexOf(tab);
    if (index !== -1) {
      tab.ref.destroy();
      this.tabs.splice(index, 1);
      if (this.active === tab) {
        this.active = this.tabs[index] ?? this.tabs[index - 1] ?? undefined;
        if (this.active) this.select(this.active);
      }
    }
  }
}
```

```html
<!-- dynamic-tabs.component.html -->
<div class="tabs">
  <nav class="tabs__header">
    <button *ngFor="let tab of tabs" (click)="select(tab)" [class.active]="tab === active">
      {{ tab.title }}
      <span class="tabs__close" (click)="close(tab); $event.stopPropagation()">×</span>
    </button>
    <button (click)="open('chart')">+ Chart</button>
    <button (click)="open('log')">+ Log</button>
  </nav>
  <section class="tabs__body">
    <ng-container #host></ng-container>
  </section>
</div>
```

## ベストプラクティス
- タブ情報を配列で管理し、ComponentRefと表示用ステータスを同期させる
- タブ閉鎖時に確実にdestroyし、選択状態を更新する
- 多数のタブを扱う場合は、スクロールや遅延ロードを導入してパフォーマンスを保つ

## 注意点
- `hidden`プロパティで切り替えるとDOMに残るため、必要なら`remove/insert`でビューそのものを切り替える
- イベントバブリングでタブ切り替えと閉じる操作が同時に走らないよう`stopPropagation()`を利用する
- 動的コンポーネントへの入力値やサービス依存を正しく設定し、タブごとに独立した状態を持たせる

## 関連技術
- 動的ウィジェットシステム（#239）
- ComponentRef管理（#232, #230）
- Angular CDK Portalでのタブ実装
