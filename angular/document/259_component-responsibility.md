# #259 「Component の責任分離」

## 概要
コンポーネントの責任分離は、UI表示・状態管理・データ取得などの役割を明確に分け、保守性とテスト性を高めるための設計指針である。

## 学習目標
- コンポーネントの責任を可視化する手法を理解する
- Input/Outputを用いた責任境界の定義を学ぶ
- フォームやダイアログでも適用できる分割パターンを把握する

## 技術ポイント
- ViewModelによるデータ整形
- Outputイベントで責任を分離
- Feature単位でのコンポーネント群構成

## 📺 画面表示用コード（動画用）
```typescript
@Component({
  selector: 'app-report-shell',
  standalone: true,
  template: `<app-report-container></app-report-container>`
})
export class ReportShellComponent {}
```

```typescript
@Component({
  selector: 'app-report-container',
  standalone: true,
  template: `<app-report-view [vm]="vm()" (export)="export()" />`
})
export class ReportContainerComponent {
  private readonly store = inject(ReportStore);
  readonly vm = this.store.vm;
  export(): void { this.store.export(); }
}
```

```typescript
@Component({
  selector: 'app-report-view',
  standalone: true,
  template: `<button (click)="export.emit()">エクスポート</button>`
})
export class ReportViewComponent {
  @Input({ required: true }) vm!: Readonly<ReportVm>;
  @Output() export = new EventEmitter<void>();
}
```

## 💻 詳細実装例（学習用）
```typescript
@Injectable({ providedIn: 'root' })
export class ReportStore {
  private readonly summary = signal<ReportVm>({ total: 0 });
  readonly vm = this.summary.asReadonly();

  load(): void {
    // API呼び出しでsummaryを更新
  }

  export(): void {
    // エクスポート用のサービス呼び出し
  }
}
```

## ベストプラクティス
- 表示・調停・データアクセスをレイヤーで分け、責務図を残す
- Outputイベント名はアクションを表現し親側で処理を完結させる
- ViewModelを型定義し、表示側で必要な情報に限定する

## 注意点
- ContainerにUIロジックを混在させない
- Viewがサービスへ直接アクセスしないようにする
- 役割が曖昧なコンポーネントは責任表を作り分割を検討する

## 関連技術
- Smart/Dumbパターン
- CQRS的な責務分割
- Angular Signals
