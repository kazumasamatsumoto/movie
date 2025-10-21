# #255 「Container Component - ロジック層」

## 概要
Container Componentは機能単位のロジックを担当し、サービスからデータを取得してSignalで保持し、Presentation ComponentへViewModelとして渡す役割を持つ。

## 学習目標
- Container Componentの責務と境界を理解する
- Signal Storeを用いたViewModel生成を学ぶ
- Outputイベントを介したコマンド処理を設計する

## 技術ポイント
- Standalone構成による疎結合化
- Signalを利用したリアクティブな状態管理
- ViewModelの型定義

## 📺 画面表示用コード（動画用）
```typescript
@Component({
  selector: 'app-user-container',
  standalone: true,
  template: `<app-user-view [vm]="vm()" (refresh)="reload()" />`
})
export class UserContainerComponent {
  private readonly store = inject(UserStore);
  readonly vm = this.store.vm;
  reload(): void { this.store.load(); }
}
```

```typescript
@Injectable({ providedIn: 'root' })
export class UserStore {
  private readonly user = signal<User | null>(null);
  readonly vm = computed(() => ({ user: this.user() }));
  load(): void { /* APIでuserを更新 */ }
}
```

```typescript
export type UserVm = {
  readonly user: User | null;
};
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-user-feature',
  standalone: true,
  imports: [UserContainerComponent, UserViewComponent],
  template: `
    <app-user-view [vm]="vm()" (refresh)="reload()"></app-user-view>
  `,
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class UserFeatureComponent implements OnInit {
  private readonly store = inject(UserStore);
  readonly vm = this.store.vm;

  ngOnInit(): void {
    this.store.load();
  }

  reload(): void {
    this.store.load();
  }
}
```

## ベストプラクティス
- Container ComponentはHTTP・Routerなどの副作用を一手に引き受ける
- ViewModelをcomputedで生成し、子コンポーネントにはreadonlyなデータのみ渡す
- コマンド処理はメソッド化しテストしやすい形に保つ

## 注意点
- Containerが巨大化したら責務を分割する
- プレゼンテーションロジックを混在させない
- サービスの戻り値を直接渡さずViewModelで整形する

## 関連技術
- Smart Component
- Angular Signals
- Command/Query Responsibility Segregation
