# #071 「ngAfterViewChecked - ビューチェック後」

## 概要
テンプレート内のビューが変更検知を受けた直後に呼び出される`ngAfterViewChecked`を利用し、描画更新後の確認や軽量な同期処理を行う方法を学びます。

## 学習目標
- `ngAfterViewChecked`の頻度とタイミングを理解する
- ViewChildの状態が変わったか検出するパターンを習得する
- パフォーマンスを損なわない条件付き処理を設計する

## 技術ポイント
- **毎サイクル呼び出し**: 変更検知が走るたびに呼ばれるため負荷に注意
- **状態比較**: 前回の値を保持し、変化があった場合のみ処理
- **ログやメトリクス**: 描画更新タイミングを可視化する用途に適する

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```typescript
ngAfterViewChecked(): void {
  if (this.count !== this.prevCount) {
    this.prevCount = this.count;
  }
}
```

```typescript
private prevCount = 0;
```

```html
<p>件数: {{ count }}</p>
```

## 💻 詳細実装例（学習用）
```typescript
import { AfterViewChecked, AfterViewInit, Component, ElementRef, ViewChild } from '@angular/core';

@Component({
  selector: 'app-list-monitor',
  standalone: true,
  templateUrl: './list-monitor.component.html',
})
export class ListMonitorComponent implements AfterViewInit, AfterViewChecked {
  @ViewChild('list') listRef!: ElementRef<HTMLUListElement>;
  count = 0;
  private previousHeight = 0;

  ngAfterViewInit(): void {
    this.updateSnapshot();
  }

  ngAfterViewChecked(): void {
    this.updateSnapshot();
  }

  add(): void {
    this.count++;
  }

  private updateSnapshot(): void {
    const height = this.listRef?.nativeElement.offsetHeight ?? 0;
    if (height !== this.previousHeight) {
      console.log(`リスト高さ: ${height}`);
      this.previousHeight = height;
    }
  }
}
```

```html
<button type="button" (click)="add()">追加</button>
<ul #list>
  <li @for (i of [].constructor(count); track i)">Item {{ i }}</li>
</ul>
```

## ベストプラクティス
- 前回値との比較を行い、変化がない場合は処理をスキップする
- 重いDOM計測は`ResizeObserver`など専用APIに任せる
- `ngAfterViewChecked`内で状態を書き換える場合は条件を厳格にし、無限ループを避ける

## 注意点
- `console.log`の多用でパフォーマンスが劣化しやすい
- ChangeDetectionStrategy.OnPushでもコンポーネントがマークされれば呼ばれる
- SSRではDOM APIを使えないため、ブラウザ環境チェックが必要

## 関連技術
- `ChangeDetectorRef`と`markForCheck`
- ResizeObserverとの連携
- Signalsによる描画後処理の最適化
