# #233 「動的 Component のライフサイクル」

## 概要
動的に生成したコンポーネントがAngularライフサイクルをどのように実行するかを理解し、生成・破棄のタイミングで行うべき処理を整理します。

## 学習目標
- createComponent直後にライフサイクルが開始される仕組みを理解する
- destroy呼び出し時にOnDestroyが実行されることを把握する
- Change Detectionの挙動と手動制御方法を習得する

## 技術ポイント
- **OnInit**: `createComponent()`後すぐに呼び出される
- **OnDestroy**: `ComponentRef.destroy()`／`ViewContainerRef.remove()`／`clear()`時に呼ばれる
- **Change Detection**: コンポーネントはホストビューにアタッチされている限り通常のCDサイクルに参加する

## 📺 画面表示用コード（動画用）

```typescript
const ref = this.host.createComponent(DynamicChildComponent);
```

```typescript
ref.destroy(); // OnDestroyが呼ばれる
```

```typescript
ref.changeDetectorRef.detach(); // 手動制御
```

## 💻 詳細実装例（学習用）
```typescript
// lifecycle-child.component.ts
import { Component, OnDestroy, OnInit } from '@angular/core';

@Component({
  selector: 'app-lifecycle-child',
  standalone: true,
  template: `<p>Dynamic Child</p>`,
})
export class LifecycleChildComponent implements OnInit, OnDestroy {
  ngOnInit(): void {
    console.log('Dynamic component OnInit');
  }

  ngOnDestroy(): void {
    console.log('Dynamic component OnDestroy');
  }
}
```

```typescript
// lifecycle-host.component.ts
import { Component, ComponentRef, ViewChild, ViewContainerRef } from '@angular/core';
import { LifecycleChildComponent } from './lifecycle-child.component';

@Component({
  selector: 'app-lifecycle-host',
  standalone: true,
  imports: [LifecycleChildComponent],
  templateUrl: './lifecycle-host.component.html',
})
export class LifecycleHostComponent {
  @ViewChild('host', { read: ViewContainerRef, static: true })
  host!: ViewContainerRef;

  ref?: ComponentRef<LifecycleChildComponent>;

  create(): void {
    this.destroy();
    this.ref = this.host.createComponent(LifecycleChildComponent);
  }

  destroy(): void {
    this.ref?.destroy();
    this.ref = undefined;
  }
}
```

```html
<!-- lifecycle-host.component.html -->
<button (click)="create()">生成</button>
<button (click)="destroy()">破棄</button>
<ng-container #host></ng-container>
```

## ベストプラクティス
- 動的コンポーネントでも`ngOnInit`/`ngOnDestroy`を活用し、初期化やクリーンアップを各コンポーネントが担う
- Change Detectionの負荷が高い場合は`ChangeDetectionStrategy.OnPush`を設定する
- 必要に応じて`changeDetectorRef.detach() / detectChanges()`で手動制御し、パフォーマンスを最適化する

## 注意点
- `createComponent`後にInputを設定する場合、`detectChanges()`でViewを更新する
- destroyを呼ばずにViewContainerRefを破棄してもビューは除かれるが、ComponentRef参照が残っているとリークする
- Detached状態のコンポーネントは自動更新されないため、再アタッチや手動更新を忘れない

## 関連技術
- ComponentRef活用（#232）
- メモリ管理（#242）
- 動的コンポーネントのテスト（#243）
