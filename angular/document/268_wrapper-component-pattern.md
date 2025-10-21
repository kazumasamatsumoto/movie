# #268 「Wrapper Component パターン」

## 概要
Wrapper Componentパターンは、外部ライブラリや複雑なUIをAngularのInput/OutputやDIに適合させるためにラッピングする手法である。

## 学習目標
- Wrapper Componentの構造と責務を理解する
- 外部ライブラリのAPIをAngularの契約に変換する
- 初期化と破棄をライフサイクルで管理する

## 技術ポイント
- `ngOnInit`/`ngOnDestroy`でのライフサイクル制御
- Input設定のマッピング
- Outputイベントのブリッジ

## 📺 画面表示用コード（動画用）
```typescript
@Component({
  selector: 'app-chart-wrapper',
  standalone: true,
  template: `<canvas #chart></canvas>`
})
export class ChartWrapperComponent implements OnInit, OnDestroy {
  @Input({ required: true }) config!: ChartConfig;
  @Output() ready = new EventEmitter<void>();
  private instance?: Chart;
}
```

```typescript
export type ChartConfig = {
  readonly type: string;
  readonly data: unknown;
  readonly options?: unknown;
};
```

```typescript
interface Chart {
  destroy(): void;
}
```

## 💻 詳細実装例（学習用）
```typescript
export class ChartWrapperComponent implements OnInit, OnDestroy {
  @ViewChild('chart', { static: true }) canvas!: ElementRef<HTMLCanvasElement>;
  @Input({ required: true }) config!: ChartConfig;
  @Output() ready = new EventEmitter<void>();
  private instance?: Chart;

  ngOnInit(): void {
    this.instance = new ChartJs(this.canvas.nativeElement, this.config);
    this.ready.emit();
  }

  ngOnDestroy(): void {
    this.instance?.destroy();
  }
}
```

## ベストプラクティス
- 外部ライブラリの設定をTypeScript型で表現して契約を明確にする
- 初期化と破棄をライフサイクルフックで管理しメモリリークを防ぐ
- Outputで準備完了やイベントを通知し親側で制御を可能にする

## 注意点
- Wrapperが肥大化したらサービスやFacadeに再分割する
- バージョンアップ時の破壊的変更に備えて型を更新する
- テストではライブラリをモックし副作用を排除する

## 関連技術
- ライフサイクルフック
- 外部ライブラリ統合
- Facadeパターン
