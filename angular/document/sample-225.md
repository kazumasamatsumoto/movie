# #225 「動的 Component の作成」

## 概要
ViewContainerRefと`createComponent()`を用いて動的コンポーネントを生成・表示する具体的な手順をまとめます。

## 学習目標
- 動的生成の基本フロー（clear→create→設定→破棄）を理解する
- ComponentRefからインスタンスやViewを操作する手順を習得する
- 生成したコンポーネントの管理方法を把握する

## 技術ポイント
- **生成フロー**: `clear()`→`createComponent()`→`ref.instance`設定→`detectChanges()`
- **参照管理**: ComponentRefを配列で保持し、必要に応じてdestroy
- **DI解決**: createComponentはInjectorを自動解決するためResolver不要

## 📺 画面表示用コード（動画用）

```typescript
this.host.clear();
const ref = this.host.createComponent(AlertComponent);
ref.instance.message = '生成完了';
```

```typescript
this.refs.push(ref);
```

```typescript
ref.destroy();
```

## 💻 詳細実装例（学習用）
```typescript
// dynamic-manager.component.ts
import { Component, ViewChild, ViewContainerRef } from '@angular/core';
import { AlertComponent } from './alert.component';

@Component({
  selector: 'app-dynamic-manager',
  standalone: true,
  imports: [AlertComponent],
  templateUrl: './dynamic-manager.component.html',
})
export class DynamicManagerComponent {
  @ViewChild('host', { read: ViewContainerRef, static: true })
  host!: ViewContainerRef;

  refs = new Set<ComponentRef<AlertComponent>>();

  create(): void {
    const ref = this.host.createComponent(AlertComponent);
    ref.instance.message = `生成: ${new Date().toLocaleTimeString()}`;
    this.refs.add(ref);
  }

  clear(): void {
    this.refs.forEach((ref) => ref.destroy());
    this.refs.clear();
  }
}
```

```html
<!-- dynamic-manager.component.html -->
<button (click)="create()">追加</button>
<button (click)="clear()">全削除</button>
<ng-container #host></ng-container>
```

## ベストプラクティス
- ComponentRefをコレクションで管理し、destroy忘れを防ぐ
- 生成直後にInputやEventを設定する場合、ChangeDetectorRefを使って同期を取る
- 繰り返し生成する場合はプールや再利用を検討してパフォーマンスを最適化する

## 注意点
- `clear()`すると既存ComponentRefはdestroyされる。必要なら先に配列から削除する
- 生成完了後すぐにDOMを操作する場合は`AfterViewInit`的なフックがないため、`setTimeout`などで遅延させる場面もある
- SSRではViewContainerRefが利用できないため、ブラウザ限定処理であることを意識する

## 関連技術
- ComponentRef活用（#232）
- イベント購読（#227）
- メモリ管理とパフォーマンス（#242, #245）
