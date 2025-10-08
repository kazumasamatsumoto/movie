# #236 「条件付き Component 表示」

## 概要
条件に応じて異なるコンポーネントを動的に表示する方法を学び、`ViewContainerRef`を使った柔軟なコンポーネント切り替えを実装します。

## 学習目標
- 条件によって異なるコンポーネントを生成・破棄する手順を理解する
- コンポーネントマッピングを利用して識別子からクラスを取り出す方法を習得する
- 置き換え時のクリーンアップと状態引き継ぎを把握する

## 技術ポイント
- **マッピング**: `{ info: InfoComponent, warning: WarningComponent }`のような辞書を用意
- **切り替え**: `clear()`→`createComponent()`で置き換え
- **状態保持**: 旧コンポーネントから必要な値を取り出して新コンポーネントへ反映

## 📺 画面表示用コード（動画用）

```typescript
const component = COMPONENT_MAP[type];
this.host.clear();
const ref = this.host.createComponent(component);
```

```typescript
ref.instance.config = config;
```

```typescript
ref.destroy();
```

## 💻 詳細実装例（学習用）
```typescript
// conditional-renderer.component.ts
import { Component, ViewChild, ViewContainerRef } from '@angular/core';
import { InfoAlertComponent } from './info-alert.component';
import { WarningAlertComponent } from './warning-alert.component';

const COMPONENTS = {
  info: InfoAlertComponent,
  warning: WarningAlertComponent,
} as const;

@Component({
  selector: 'app-conditional-renderer',
  standalone: true,
  imports: [InfoAlertComponent, WarningAlertComponent],
  templateUrl: './conditional-renderer.component.html',
})
export class ConditionalRendererComponent {
  @ViewChild('host', { read: ViewContainerRef, static: true })
  host!: ViewContainerRef;

  switch(type: keyof typeof COMPONENTS) {
    this.host.clear();
    const ref = this.host.createComponent(COMPONENTS[type]);
    ref.instance.message = `${type} alert`;
  }
}
```

```html
<!-- conditional-renderer.component.html -->
<button (click)="switch('info')">INFO</button>
<button (click)="switch('warning')">WARNING</button>
<ng-container #host></ng-container>
```

## ベストプラクティス
- 切り替えるコンポーネントをマップにまとめ、識別子でswitchできる設計にする
- 状態をサービスで共有することで、切り替え時にデータを保持できる
- 頻繁な切り替えでパフォーマンスが課題になる場合は、コンポーネントをプールして再利用する

## 注意点
- `clear()`で破棄した後もComponentRefへの参照が残るとメモリリークとなる
- Inputが必須のコンポーネントは、生成直後に確実に値を設定する
- 選択肢が多い場合はFactoryクラスやディレクティブで責務を分割する

## 関連技術
- 動的コンポーネントの置き換え（#229）
- プラグインアーキテクチャ（#240）
- Angular CDK Portalでの動的切り替え（#246, #247）
