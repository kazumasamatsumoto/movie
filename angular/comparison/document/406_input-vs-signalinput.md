# #406 「@Input setter vs SignalInput あなたはどっち派？」

## 概要
@Input setterは柔軟だが副作用を抱え込みやすい。SignalInputは入力値をSignal化し、派生状態やSignalOutputと合わせてスッキリ書ける。

## 学習目標
- @Input setterの構成と得意なシナリオを整理する
- SignalInputの採用メリットを理解する
- プロジェクト条件に応じた使い分け基準を決める

## 技術ポイント
- @Input setterを成り立たせる主要API/構成要素
- SignalInputで押さえる設定やコード記述
- 両者を共存・移行させるためのブリッジ手法

## 📺 画面表示用コード（動画用）
**setter派：入力で副作用を実行**
```typescript
private _userId = '';

@Input()
set userId(value: string) {
  this._userId = value;
  this.fetchProfile();
}
```

**SignalInput派：Signalとして受け取る**
```typescript
userId = input.required<string>();
profile = computed(() => this.repo.load(this.userId()));

refresh() {
  this.repo.refresh(this.userId());
}
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-user-card',
  standalone: true,
  template: `
    <ng-container *ngIf="profile() as p">
      <h3>{{ p.name }}</h3>
    </ng-container>
  `,
})
export class UserCardComponent {
  private readonly repo = inject(UserRepository);

  readonly userId = input.required<string>();
  readonly profile = toSignal(
    this.repo.profile$(this.userId()),
    { initialValue: null },
  );
}
```

## ベストプラクティス
- SignalInputと`computed`を組み合わせて派生状態を作り、副作用は`effect`へ切り出す
- レガシーsetterは薄く保ち、SignalInputへ徐々に移行できるようFacadeを用意する
- 入力が任意なら`input<string | undefined>`を使い、undefinedハンドリングを型で表現する

## 注意点
- SignalInputはAngular v17+限定なのでバージョン互換を確認する
- setterとSignalInputを同じプロパティ名で併用しない
- SignalInputで受けた値を直接ミューテートしない（不変データを前提にする）

## 関連技術
- SignalInput API
- @Input setter
- toSignal/toObservable
