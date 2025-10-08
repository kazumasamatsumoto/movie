# #221 「Dynamic Components とは？」

## 概要
Angularで実行時にコンポーネントを生成・挿入する「Dynamic Components」の概念を整理し、静的テンプレートでは難しい柔軟なUI構成を実現する基本を学びます。

## 学習目標
- Dynamic Componentの目的とユースケースを理解する
- ViewContainerRefとComponentRefを使う流れを把握する
- 静的テンプレートとの違いを説明できるようにする

## 技術ポイント
- **ランタイム生成**: `ViewContainerRef.createComponent()`でコンポーネントを生成
- **ComponentRef**: 生成したコンポーネントのインスタンス・ライフサイクルを操作できる
- **ユースケース**: ダッシュボードウィジェット、動的フォーム、プラグインロードなど

## 📺 画面表示用コード（動画用）

```html
<ng-container #host></ng-container>
```

```typescript
@ViewChild('host', { read: ViewContainerRef, static: true })
host!: ViewContainerRef;
```

```typescript
this.host.createComponent(MyDynamicComponent);
```

## 💻 詳細実装例（学習用）
```typescript
// dynamic-host.component.ts
import { Component, ViewChild, ViewContainerRef } from '@angular/core';
import { MessageCardComponent } from './message-card.component';

@Component({
  selector: 'app-dynamic-host',
  standalone: true,
  imports: [MessageCardComponent],
  templateUrl: './dynamic-host.component.html',
})
export class DynamicHostComponent {
  @ViewChild('host', { read: ViewContainerRef, static: true })
  host!: ViewContainerRef;

  load(): void {
    this.host.clear();
    const ref = this.host.createComponent(MessageCardComponent);
    ref.instance.title = 'Dynamic Component';
    ref.instance.message = '実行時に生成されました。';
  }
}
```

```typescript
// message-card.component.ts
import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-message-card',
  standalone: true,
  template: `
    <article class="card">
      <h3>{{ title }}</h3>
      <p>{{ message }}</p>
    </article>
  `,
})
export class MessageCardComponent {
  @Input() title = '';
  @Input() message = '';
}
```

```html
<!-- dynamic-host.component.html -->
<button (click)="load()">コンポーネントを生成</button>
<ng-container #host></ng-container>
```

## ベストプラクティス
- 動的生成部分は専用サービスやファクトリにまとめ、責務を分離する
- 生成したComponentRefは配列で管理し、必要に応じてdestroyする
- 必要以上に動的生成せず、`*ngIf`など静的テンプレートで解決できない場合に限定する

## 注意点
- 生成後にInputを設定する場合、`detectChanges()`で更新を反映する
- イベント購読はdestroy時に解除し、メモリリークを防ぐ
- 依存するモジュールやスタンドアロンコンポーネントが正しくエクスポートされているか確認する

## 関連技術
- ViewContainerRef / ComponentRef（#222, #232）
- `createComponent()`の新API（#224）
- Angular CDK Portal（#246, #247）
