# #234 「動的ローディング実装」

## 概要
ユーザー操作や設定に応じてコンポーネントを動的に形成し、必要なときにだけ読み込む「動的ローディング」を実装する手順を学びます。

## 学習目標
- Dynamic importでコンポーネントを遅延読み込みする方法を理解する
- 読み込み完了後に`createComponent`でビューを生成する手順を習得する
- ローディング中のプレースホルダやエラーハンドリングを組み合わせた実装を把握する

## 技術ポイント
- **Dynamic import**: `import('./lazy.component').then(...)`
- **createComponent**: 読み込み完了後にViewContainerRefで生成
- **プレースホルダ**: ローディング状態をUIで表示し、UXを向上させる

## 📺 画面表示用コード（動画用）

```typescript
const { LazyWidgetComponent } = await import('./lazy-widget.component');
this.host.createComponent(LazyWidgetComponent);
```

```html
<p *ngIf="loading">読み込み中...</p>
```

```typescript
try { ... } catch (e) { this.error = e; }
```

## 💻 詳細実装例（学習用）
```typescript
// lazy-loader.component.ts
import { Component, ViewChild, ViewContainerRef } from '@angular/core';

@Component({
  selector: 'app-lazy-loader',
  standalone: true,
  templateUrl: './lazy-loader.component.html',
})
export class LazyLoaderComponent {
  @ViewChild('host', { read: ViewContainerRef, static: true })
  host!: ViewContainerRef;

  loading = false;
  error: unknown = null;

  async load(): Promise<void> {
    this.host.clear();
    this.loading = true;
    this.error = null;
    try {
      const { LazyWidgetComponent } = await import('./lazy-widget.component');
      const ref = this.host.createComponent(LazyWidgetComponent);
      ref.instance.message = '遅延ロード済みコンポーネント';
    } catch (e) {
      this.error = e;
    } finally {
      this.loading = false;
    }
  }
}
```

```html
<!-- lazy-loader.component.html -->
<button (click)="load()">ウィジェット読込</button>
<p *ngIf="loading">読み込み中...</p>
<p *ngIf="error" class="error">読み込みに失敗しました</p>
<ng-container #host></ng-container>
```

## ベストプラクティス
- Dynamic importでコンポーネント（またはスタンドアロンコンポーネント）をロードし、バンドル分割を実現する
- ローディング中のスピナーやプレースホルダを用意し、体験を損なわない
- エラーハンドリングを行い、必要ならリトライや代替コンテンツを表示する

## 注意点
- importパスはビルド時に解析可能な文字列である必要がある
- Lazy loadしたコンポーネントが依存するモジュールも同時に読み込まれるので、バンドル構成に注意
- SSR環境で利用する場合は、Dynamic importのタイミングをクライアントサイドに限定する

## 関連技術
- 遅延ロードコンポーネント（#235）
- Angular RouterのLazy Loading
- Angular CDK Portalでの遅延表示（#246, #247）
