# #138 「ViewChild とライフサイクル」

## 概要
`@ViewChild`で取得した参照をライフサイクルフックと組み合わせて安全に扱う手順を解説します。

## 学習目標
- ViewChild参照が使用可能になるタイミングを理解する
- ライフサイクルフック（`ngAfterViewInit`, `ngAfterViewChecked`）の使い分けを学ぶ
- 参照が変化するケースに対する防御的な実装を身につける

## 技術ポイント
- **ngAfterViewInit**: ViewChildを使う基本タイミング
- **ngAfterViewChecked**: ビュー更新後に再評価したい場合に利用
- **setterパターン**: ViewChildのプロパティをsetterにして変化を感知

```typescript
ngAfterViewInit() {
  this.chart?.render();
}
```

```typescript
ngAfterViewChecked() {
  if (this.chartChanged) { this.chart?.update(); }
}
```

```typescript
@ViewChild('chart') set chartRef(ref: ChartComponent | undefined) { ... }
```

## 💻 詳細実装例（学習用）
```typescript
// chart-container.component.ts
import { AfterViewChecked, AfterViewInit, Component, ViewChild } from '@angular/core';
import { ChartComponent } from './chart.component';

@Component({
  selector: 'app-chart-container',
  standalone: true,
  imports: [ChartComponent],
  templateUrl: './chart-container.component.html',
})
export class ChartContainerComponent implements AfterViewInit, AfterViewChecked {
  @ViewChild(ChartComponent)
  chart?: ChartComponent;

  private pendingUpdate = false;

  ngAfterViewInit(): void {
    this.chart?.render();
  }

  requestUpdate(): void {
    this.pendingUpdate = true;
  }

  ngAfterViewChecked(): void {
    if (!this.pendingUpdate) {
      return;
    }
    this.chart?.update();
    this.pendingUpdate = false;
  }
}
```

```html
<!-- chart-container.component.html -->
<app-chart></app-chart>
<button type="button" (click)="requestUpdate()">データ更新</button>
```

## ベストプラクティス
- 初期描画後に参照が必要なら`ngAfterViewInit`で実行、再描画後にチェックしたい処理は`ngAfterViewChecked`へ
- setterパターン（`@ViewChild('ref') set ...`）を使うと参照変化時に自動的に処理できる
- 参照がnullになり得ることを想定し、nullチェックを徹底する

## 注意点
- `ngAfterViewChecked`は頻繁に呼ばれるため、重い処理を置かない
- 子コンポーネントが*ngIfで切り替わる場合、ViewChildはnullになるのでイベントで監視する必要がある
- 非同期で参照を使う場合は`setTimeout`でマクロタスクに遅らせるなど工夫する

## 関連技術
- ViewChildrenのchanges Observable
- `ChangeDetectorRef.detectChanges()`の使いどころ
- Signalベースの参照更新（ViewChild Setterとeffectの併用）
