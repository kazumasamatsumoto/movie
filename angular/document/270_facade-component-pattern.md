# #270 「Facade Component パターン」

## 概要
Facade Componentパターンは、複数の子コンポーネントやサービスを統合し、上位コンポーネントに対して簡潔なAPIを提供する境界コンポーネントである。

## 学習目標
- Facade Componentの役割と境界設計を理解する
- 複数コンポーネントの連携を1つのAPIに集約する
- Signal Storeを内部に保持して状態を管理する

## 技術ポイント
- 複数のComponent/Serviceの統合
- readonly Signalの公開
- Input/Outputの一本化

## 📺 画面表示用コード（動画用）
```typescript
@Component({ selector: 'app-dashboard-facade', standalone: true, imports: [DashboardHeaderComponent, DashboardGridComponent], template: `<app-dashboard-header [vm]="vm()"></app-dashboard-header><app-dashboard-grid [vm]="vm()"></app-dashboard-grid>` })
export class DashboardFacadeComponent {
  private readonly store = inject(DashboardStore);
  readonly vm = this.store.vm;
}
```

```typescript
@Injectable({ providedIn: 'root' })
export class DashboardStore {
  private readonly state = signal<DashboardVm>({ stats: [], user: null });
  readonly vm = this.state.asReadonly();
}
```

```typescript
export type DashboardVm = {
  readonly stats: ReadonlyArray<DashboardStat>;
  readonly user: User | null;
};
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-dashboard-page',
  standalone: true,
  imports: [DashboardFacadeComponent],
  template: `
    <app-dashboard-facade></app-dashboard-facade>
  `
})
export class DashboardPageComponent implements OnInit {
  private readonly store = inject(DashboardStore);

  ngOnInit(): void {
    this.store.load();
  }
}
```

## ベストプラクティス
- Facadeは内部でSignal Storeやサービスをまとめ、外部にはreadonlyなAPIのみ公開する
- 子コンポーネントとのデータ契約をViewModelで統一する
- Facadeを境界としてチーム間の依存を整理する

## 注意点
- Facadeが機能過多になった場合はサブFacadeを追加する
- 内部実装を隠蔽するためにpublic APIを最小限に保つ
- Storeのメソッドは副作用と戻り値を明確にする

## 関連技術
- Smart Component
- Angular Signals
- CQRS
