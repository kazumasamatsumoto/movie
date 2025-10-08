# #223 「ComponentFactoryResolver（旧方式）」

## 概要
Angular v13以前に利用されていた`ComponentFactoryResolver`による動的コンポーネント生成手法を振り返り、レガシーコードを理解・保守できるようにします。

## 学習目標
- `ComponentFactoryResolver`の役割とAPIを理解する
- 旧方式のコードを読み解き、新方式への移行ポイントを把握する
- 新旧APIの違いを説明できるようにする

## 技術ポイント
- **ファクトリ取得**: `resolver.resolveComponentFactory(MyComponent)`
- **生成**: `viewContainerRef.createComponent(factory)`
- **新方式**: v13以降は`ViewContainerRef.createComponent()`だけで済む

## 📺 画面表示用コード（動画用）

```typescript
constructor(private resolver: ComponentFactoryResolver) {}
```

```typescript
const factory = this.resolver.resolveComponentFactory(MyComponent);
```

```typescript
this.host.createComponent(factory);
```

## 💻 詳細実装例（学習用）
```typescript
// legacy-host.component.ts
import { Component, ComponentFactoryResolver, ViewChild, ViewContainerRef } from '@angular/core';
import { LegacyCardComponent } from './legacy-card.component';

@Component({
  selector: 'app-legacy-host',
  standalone: true,
  template: `<ng-container #host></ng-container>`,
})
export class LegacyHostComponent {
  @ViewChild('host', { read: ViewContainerRef, static: true })
  host!: ViewContainerRef;

  constructor(private readonly resolver: ComponentFactoryResolver) {}

  load(): void {
    const factory = this.resolver.resolveComponentFactory(LegacyCardComponent);
    this.host.createComponent(factory);
  }
}
```

## ベストプラクティス
- 旧コードを保守する際は、いずれ新方式へ移行できるよう抽象化レイヤー（サービス等）を挟む
- `ComponentFactoryResolver`をアプリ全体で共有するより、必要な場所でDIする
- 新方式（`createComponent(ComponentType)`）が利用可能ならそちらへリファクタリングする

## 注意点
- Ivy以前はComponentFactoryResolverが必須だったため、古い記事に沿っていると記述が古い可能性がある
- 将来的にResolver APIはメンテナンスモードであるため、新規開発には推奨されない
- Resolverを使う際もDestroyや入力設定など基本ロジックは新方式と同じ

## 関連技術
- `createComponent()`新API（#224）
- ViewContainerRefの基本（#222）
- Angular v13リリースノート（Component factories不要化）
