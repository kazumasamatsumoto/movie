# #227 「動的 Component のイベント購読」

## 概要
動的に生成したコンポーネントの`@Output`イベントを購読し、親コンポーネント側でハンドリングする方法を学びます。

## 学習目標
- ComponentRef.instance経由でEventEmitterを購読する手順を理解する
- 購読解除やdestroy時のクリーンアップを習得する
- 複数コンポーネントを動的追加した場合のイベント管理を把握する

## 技術ポイント
- **購読**: `componentRef.instance.submit.subscribe(...)`
- **購読解除**: `Subscription`を保持し、destroy時に`unsubscribe()`
- **クリーンアップ**: `componentRef.destroy()`でOnDestroyが呼ばれる

## 📺 画面表示用コード（動画用）

```typescript
const ref = this.host.createComponent(FormComponent);
const sub = ref.instance.submit.subscribe(data => ...);
```

```typescript
sub.unsubscribe();
```

```typescript
ref.destroy();
```

## 💻 詳細実装例（学習用）
```typescript
// dynamic-events.component.ts
import { Component, ComponentRef, ViewChild, ViewContainerRef } from '@angular/core';
import { FormCardComponent } from './form-card.component';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-dynamic-events',
  standalone: true,
  imports: [FormCardComponent],
  templateUrl: './dynamic-events.component.html',
})
export class DynamicEventsComponent {
  @ViewChild('host', { read: ViewContainerRef, static: true })
  host!: ViewContainerRef;

  ref?: ComponentRef<FormCardComponent>;
  sub?: Subscription;

  open() {
    this.close();
    this.ref = this.host.createComponent(FormCardComponent);
    this.sub = this.ref.instance.submit.subscribe((value) => console.log('submit:', value));
  }

  close() {
    this.sub?.unsubscribe();
    this.ref?.destroy();
    this.sub = undefined;
    this.ref = undefined;
  }
}
```

## ベストプラクティス
- `takeUntilDestroyed()`（v16+）などを使い、購読解除を自動化する
- ComponentRefとSubscriptionをセットで保持し、破棄時に両方クリアする
- イベント内容を型付けして、親側で安全に処理する

## 注意点
- destroyせずにSubscriptionだけ解除すると、ビューは残るので忘れずdestroyする
- イベントが頻繁に発火する場合はBackpressureやDebounceを検討
- Outputを`EventEmitter`以外で実装している場合（RxJS Subjectなど）は購読解除の仕方に注意

## 関連技術
- 動的コンポーネントの入力（#226）
- ComponentRefライフサイクル（#233）
- 動的コンポーネントのメモリ管理（#242）
