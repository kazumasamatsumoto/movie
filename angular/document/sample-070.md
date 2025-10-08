# #070 「ngAfterViewInit - ビュー初期化後」

## 概要
テンプレート内の要素参照や子コンポーネントが準備できた直後に実行される`ngAfterViewInit`の活用方法を学びます。

## 学習目標
- `ViewChild`/`ViewChildren`が利用可能になるタイミングを理解する
- 外部ライブラリ初期化やDOM計測を`ngAfterViewInit`で安全に行う
- 初回のみの処理と継続的な処理を区別する

## 技術ポイント
- **ビュー初期化後**: `ViewChild`で取得した要素が確定
- **初回のみ**: `ngAfterViewInit`は1回だけ呼ばれる（コンポーネント再作成時を除く）
- **テンプレート参照**: `static: false`がデフォルトで、ビュー初期化後に利用可能

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```typescript
@ViewChild('chart') chartRef!: ElementRef<HTMLCanvasElement>;
```

```typescript
ngAfterViewInit(): void {
  initChart(this.chartRef.nativeElement);
}
```

```html
<canvas #chart></canvas>
```

## 💻 詳細実装例（学習用）
```typescript
import { AfterViewInit, Component, ElementRef, ViewChild } from '@angular/core';

@Component({
  selector: 'app-chart',
  standalone: true,
  templateUrl: './chart.component.html',
  styleUrls: ['./chart.component.css'],
})
export class ChartComponent implements AfterViewInit {
  @ViewChild('canvas', { static: false }) canvas!: ElementRef<HTMLCanvasElement>;

  ngAfterViewInit(): void {
    const ctx = this.canvas.nativeElement.getContext('2d');
    if (!ctx) {
      return;
    }
    drawMockChart(ctx);
  }
}

function drawMockChart(ctx: CanvasRenderingContext2D): void {
  ctx.fillStyle = '#4caf50';
  ctx.fillRect(10, 10, 120, 40);
  ctx.fillStyle = '#2196f3';
  ctx.fillRect(10, 60, 80, 40);
}
```

```html
<canvas #canvas width="200" height="120"></canvas>
```

## ベストプラクティス
- DOM操作はRenderer2を通すとテストやSSRで扱いやすい
- 初期化処理が重い場合は`requestAnimationFrame`で1フレーム遅らせて描画をブロックしない
- ライブラリ初期化後はリファレンスを保持して、`ngOnDestroy`で終了処理を行う

## 注意点
- `ViewChild`がundefinedの場合はテンプレート側に要素が存在しない可能性があるため、安全なガードを入れる
- ChangeDetectionStrategy.OnPushでビューチェックがスキップされることはないが、後続更新の仕組みを理解しておく
- SSR時はDOM APIが利用できないので`isPlatformBrowser`ガードを検討する

## 関連技術
- `ViewChildren`と`QueryList`
- Renderer2によるDOM抽象化
- Angular CDK Overlayなどビュー依存のライブラリ
