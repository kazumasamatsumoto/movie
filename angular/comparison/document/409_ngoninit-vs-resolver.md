# #409 「ngOnInit API呼び出し vs Route Resolver あなたはどっち派？」

## 概要
コンポーネント内でAPIを呼ぶと実装が楽だが表示が遅れる。一方Resolverはルート遷移と統合されUXは良いが、再利用には工夫が必要。

## 学習目標
- ngOnInit fetchの構成と得意なシナリオを整理する
- Route Resolverの採用メリットを理解する
- プロジェクト条件に応じた使い分け基準を決める

## 技術ポイント
- ngOnInit fetchを成り立たせる主要API/構成要素
- Route Resolverで押さえる設定やコード記述
- 両者を共存・移行させるためのブリッジ手法

## 📺 画面表示用コード（動画用）
**ngOnInit派：コンポーネント内で取得**
```typescript
ngOnInit(): void {
  this.repo.list().subscribe((items) => {
    this.items = items;
  });
}
```

**Resolver派：ルートで事前取得**
```typescript
export const routes: Routes = [
  {
    path: 'heroes',
    loadComponent: () => import('./heroes.component'),
    resolve: { heroes: heroesResolver },
  },
];
```

## 💻 詳細実装例（学習用）
```typescript
export const heroesResolver: ResolveFn<Hero[]> = () => {
  const repo = inject(HeroRepository);
  return repo.list();
};

@Component({
  selector: 'app-heroes',
  standalone: true,
  template: `
    <ng-container *ngIf="heroes$ | async as heroes">
      <app-hero-card *ngFor="let hero of heroes" [hero]="hero" />
    </ng-container>
  `,
})
export class HeroesComponent {
  readonly heroes$ = inject(ActivatedRoute).data.pipe(map(data => data['heroes'] as Hero[]));
}
```

## ベストプラクティス
- API呼び出しが軽い一覧はResolverで先読みし、重い処理はコンポーネント内に分割する
- Resolverはpure functionとして定義し、DIでサービスを注入してテストしやすくする
- ngOnInit派でも`takeUntilDestroyed`で購読解除を忘れない

## 注意点
- Resolverで失敗した場合の遷移制御（リトライ・リダイレクト）を必ず設計する
- Resolverに元々重い複数APIを詰め込むと初回遷移が遅くなる
- ngOnInitで取得する場合はSkeleton UIなどでUX低下を補う

## 関連技術
- Route Resolver
- ActivatedRoute.data
- ngOnInitとRxJS
