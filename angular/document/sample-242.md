# #242 「動的 Component のメモリ管理」

## 概要
動的に生成したコンポーネントを適切に破棄し、イベント購読やタイマーなどリソースを解放するメモリ管理のポイントを学びます。

## 学習目標
- ComponentRef.destroy()の役割とタイミングを理解する
- EventEmitterやObservable購読を解除してリークを防ぐ方法を習得する
- ViewContainerRefの`clear/remove`が内部でdestroyを呼ぶことを把握する

## 技術ポイント
- **destroy**: `ref.destroy()`でOnDestroy呼び出しおよびDOM除去
- **購読解除**: RxJSの`takeUntilDestroyed`や`Subscription.unsubscribe()`を活用
- **コレクション管理**: `ComponentRef`をSet/Mapで追跡し、破棄漏れを防ぐ

## 📺 画面表示用コード（動画用）

```typescript
const sub = ref.instance.change.subscribe(...);
sub.unsubscribe();
ref.destroy();
```

```typescript
this.refs.forEach(ref => ref.destroy());
this.refs.clear();
```

```typescript
this.viewContainer.clear(); // 全てdestroy
```

## 💻 詳細実装例（学習用）
```typescript
// dynamic-manager.service.ts
import { Injectable, ComponentRef } from '@angular/core';
import { takeUntilDestroyed } from '@angular/core/rxjs-interop';

@Injectable({ providedIn: 'root' })
export class DynamicManagerService {
  private refs = new Set<ComponentRef<any>>();

  register<T>(ref: ComponentRef<T>): void {
    this.refs.add(ref);
    ref.onDestroy(() => this.refs.delete(ref));
  }

  destroyAll(): void {
    this.refs.forEach((ref) => ref.destroy());
    this.refs.clear();
  }
}
```

```typescript
// usage snippet
const ref = this.host.createComponent(AlertComponent);
this.manager.register(ref);
ref.instance.closed.pipe(takeUntilDestroyed(this.destroyRef)).subscribe(() => ref.destroy());
```

## ベストプラクティス
- ComponentRefを集中管理し、コンポーネントが自身でdestroyするケースにも対応する
- RxJS購読は`takeUntilDestroyed`（v16+）や`takeUntil`を利用して自動解放する
- setTimeoutやsetIntervalを使用する場合はOnDestroyで解除するロジックを組み込む

## 注意点
- `clear()`でdestroyされるが、配列やマップに残った参照を忘れずに削除する
- Destroy後のComponentRefにアクセスしないよう、ガードや状態変更を行う
- `ViewContainerRef.detach()`でビューを外した場合、destroyは実行されないため明示的に呼ぶ必要がある

## 関連技術
- ComponentRefライフサイクル（#233）
- 動的イベント購読（#227）
- パフォーマンス最適化（#245）
