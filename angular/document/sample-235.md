# #235 「遅延ロード Component」

## 概要
大きなコンポーネントや頻繁に使われない機能を遅延ロードし、初期バンドルを軽量化する方法を学びます。動的インポートと`createComponent`を組み合わせたパターンを実践します。

## 学習目標
- 遅延ロードコンポーネントのベーシックな実装手順を理解する
- ローディング状態・エラー状態のハンドリングを習得する
- 遅延ロードしたコンポーネントへのInput/Outputを設定する方法を学ぶ

## 技術ポイント
- **Dynamic import**: `await import('./lazy-component.component')`
- **ComponentRef操作**: 生成後にInputを設定し、Change Detectionを走らせる
- **UX向上**: プレースホルダやSkeletonを表示し、読み込み完了後に差し替える

## 📺 画面表示用コード（動画用）

```typescript
const { LazyComponent } = await import('./lazy.component');
const ref = this.host.createComponent(LazyComponent);
```

```typescript
ref.instance.config = config;
ref.changeDetectorRef.detectChanges();
```

```html
<p *ngIf="loading">読み込み中...</p>
```

## 💻 詳細実装例（学習用）
```typescript
// lazy-container.component.ts
import { Component, ViewChild, ViewContainerRef } from '@angular/core';
import { LazyConfig } from './lazy-component.types';

@Component({
  selector: 'app-lazy-container',
  standalone: true,
  templateUrl: './lazy-container.component.html',
})
export class LazyContainerComponent {
  @ViewChild('host', { read: ViewContainerRef, static: true })
  host!: ViewContainerRef;

  loading = false;
  async load(config: LazyConfig): Promise<void> {
    this.host.clear();
    this.loading = true;
    try {
      const { LazyCardComponent } = await import('./lazy-card.component');
      const ref = this.host.createComponent(LazyCardComponent);
      ref.instance.config = config;
      ref.changeDetectorRef.detectChanges();
    } finally {
      this.loading = false;
    }
  }
}
```

```html
<!-- lazy-container.component.html -->
<button (click)="load({ title: '遅延カード', description: '動的読込です' })">
  遅延ロード
</button>
<p *ngIf="loading">読み込み中...</p>
<ng-container #host></ng-container>
```

## ベストプラクティス
- 遅延ロードするコンポーネントはスタンドアロン化するか、専用モジュールにまとめて依存を明確にする
- 読み込み中/失敗時のUIを準備し、ユーザー体験を損なわない
- 生成後すぐにInputを設定し、`detectChanges()`で確実に反映させる
- 遅延ロード対象が増えすぎた場合はプリフェッチやprefetchリンクで改善検討

## 注意点
- Dynamic importはブラウザ環境でのみ動作するため、SSRではガードが必要
- スタンドアロンコンポーネント以外を読み込む場合、モジュールのNgModuleRefを作成する必要がある
- 依存コンポーネントがさらにLazy loadを必要とする場合、包摂関係に注意

## 関連技術
- 動的ローディング（#234）
- Angular Routerの`loadComponent`
- Angular CDK Portal / Overlayでの遅延表示
