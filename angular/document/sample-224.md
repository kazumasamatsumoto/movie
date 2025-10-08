# #224 「createComponent() - 新方式（v13+）」

## 概要
Angular v13以降で推奨される`ViewContainerRef.createComponent()` APIを利用し、ComponentFactoryResolverを使わずに動的コンポーネントを生成する方法を学びます。

## 学習目標
- `createComponent`新APIの構文と引数を理解する
- DIやInjectorを自動解決する仕組みを把握する
- 旧方式からの移行手順を説明できるようにする

## 技術ポイント
- **基本呼び出し**: `viewContainerRef.createComponent(MyComponent)`
- **オプション**: `{ injector, projectableNodes }` などを指定可能
- **戻り値**: `ComponentRef`としてインスタンス・ChangeDetectorRefへアクセス

## 📺 画面表示用コード（動画用）

```typescript
const ref = this.host.createComponent(AlertComponent);
```

```typescript
ref.instance.message = 'Hello';
```

```typescript
ref.destroy();
```

## 💻 詳細実装例（学習用）
```typescript
// modern-host.component.ts
import { Component, ViewChild, ViewContainerRef } from '@angular/core';
import { AlertComponent } from './alert.component';

@Component({
  selector: 'app-modern-host',
  standalone: true,
  imports: [AlertComponent],
  templateUrl: './modern-host.component.html',
})
export class ModernHostComponent {
  @ViewChild('host', { read: ViewContainerRef, static: true })
  host!: ViewContainerRef;

  load(): void {
    this.host.clear();
    const ref = this.host.createComponent(AlertComponent);
    ref.instance.message = '新APIで生成されました';
  }
}
```

```html
<!-- modern-host.component.html -->
<button (click)="load()">createComponentで生成</button>
<ng-container #host></ng-container>
```

## ベストプラクティス
- `createComponent`は最小限のコードで済むため、新規実装はこのAPIを採用する
- InjectorやEnvironmentInjectorをオプションで渡すことで、依存関係を柔軟に解決できる
- `ComponentRef`を配列で保持し、destroyを適切に行ってメモリ管理を徹底する

## 注意点
- 同じ場所に複数のコンポーネントを生成する場合は明示的に`clear()`や`remove()`で整頓
- `detectChanges()`は通常不要だが、生成直後にInput設定を行った場合は念のため呼ぶ
- Angular v13未満では利用できないため、バージョンを確認してから利用する

## 関連技術
- ViewContainerRef基礎（#222）
- ComponentRef活用（#232）
- 動的コンポーネントの入力渡し（#226）
