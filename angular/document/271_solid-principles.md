# #271 「Component 設計の SOLID 原則」

## 概要
SOLID原則をコンポーネント設計に適用することで、変更に強く保守しやすいUIアーキテクチャを構築できる。

## 学習目標
- SOLID原則をコンポーネントレベルで理解する
- Input/Outputやサービス分離で原則を実践する
- テストや拡張を意識した設計判断を行う

## 技術ポイント
- SRP: 単一責任を守るコンポーネント分割
- OCP: 拡張性をInput/Configで確保
- DIP: 抽象サービスの注入

## 📺 画面表示用コード（動画用）
```typescript
@Component({ selector: 'app-report-view', standalone: true, template: `<p>{{ vm.summary }}</p>` })
export class ReportViewComponent {
  @Input({ required: true }) vm!: Readonly<ReportVm>;
}
```

```typescript
export type ReportVm = {
  readonly summary: string;
};
```

```typescript
@Injectable({ providedIn: 'root' })
export abstract class ReportGateway {
  abstract fetch(): Observable<ReportVm>;
}
```

## 💻 詳細実装例（学習用）
```typescript
@Injectable()
export class HttpReportGateway implements ReportGateway {
  constructor(private readonly http: HttpClient) {}
  fetch(): Observable<ReportVm> {
    return this.http.get<ReportVm>('/api/report');
  }
}

@Component({
  selector: 'app-report-container',
  standalone: true,
  imports: [ReportViewComponent],
  providers: [{ provide: ReportGateway, useClass: HttpReportGateway }],
  template: `<app-report-view [vm]="vm()"></app-report-view>`
})
export class ReportContainerComponent implements OnInit {
  private readonly gateway = inject(ReportGateway);
  private readonly state = signal<ReportVm>({ summary: '' });
  readonly vm = this.state.asReadonly();

  ngOnInit(): void {
    this.gateway.fetch().subscribe(data => this.state.set(data));
  }
}
```

## ベストプラクティス
- SRPを守るためにコンポーネントの変更理由を明文化する
- OCPを意識してInput/Configを設計し拡張時の変更を局所化する
- DIPで抽象サービスを注入しテスト時はモックを差し替える

## 注意点
- 原則を守るための抽象化が過剰にならないようにする
- Providerのスコープを意識し、Component提供のサービス範囲を理解する
- 原則チェックをコードレビューに組み込む

## 関連技術
- SOLID原則
- Angular Dependency Injection
- ViewModel設計
