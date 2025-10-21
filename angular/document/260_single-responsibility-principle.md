# #260 「Single Responsibility Principle」

## 概要
Single Responsibility Principle（単一責任の原則）は、コンポーネントが一つの理由でのみ変更されるよう役割を限定し、保守性を高める設計原則である。

## 学習目標
- SRPをコンポーネント設計に適用する方法を理解する
- 変更理由を列挙して責務を明確化する
- サービスとの協調でUIの責務を保つ

## 技術ポイント
- ViewModelを通じた情報の抽象化
- サービス層との責務分離
- OnPush戦略と入力データの整形

## 📺 画面表示用コード（動画用）
```typescript
@Component({
  selector: 'app-invoice-summary',
  standalone: true,
  template: `<p>請求額: {{ vm.total | currency:'JPY' }}</p>`,
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class InvoiceSummaryComponent {
  @Input({ required: true }) vm!: Readonly<InvoiceVm>;
}
```

```typescript
@Injectable({ providedIn: 'root' })
export class InvoiceService {
  getSummary(): Observable<InvoiceVm> {
    return this.http.get<InvoiceVm>('/api/invoice');
  }
  constructor(private readonly http: HttpClient) {}
}
```

```typescript
export type InvoiceVm = {
  readonly total: number;
};
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-invoice-container',
  standalone: true,
  imports: [InvoiceSummaryComponent],
  template: `<app-invoice-summary [vm]="vm()"></app-invoice-summary>`
})
export class InvoiceContainerComponent implements OnInit {
  private readonly invoiceService = inject(InvoiceService);
  private readonly summary = signal<InvoiceVm>({ total: 0 });
  readonly vm = this.summary.asReadonly();

  ngOnInit(): void {
    this.invoiceService.getSummary().subscribe(value => this.summary.set(value));
  }
}
```

## ベストプラクティス
- コンポーネントの責務を文書化し、SRPを満たすかレビューする
- データ取得はサービスに委譲し、UIはViewModel表示に集中させる
- SRPを守れない場合は分割して役割を再定義する

## 注意点
- コンポーネントに複数の変更理由が混ざっていないか定期的に検証する
- サービスが肥大化した場合はユースケース単位に再編成する
- SRPを形式的に守るだけでなく実際の変更履歴も確認する

## 関連技術
- SOLID原則
- Angular Services
- ViewModel設計
