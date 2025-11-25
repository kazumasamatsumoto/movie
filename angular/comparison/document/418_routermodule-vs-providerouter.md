# #418 「RouterModule vs provideRouter あなたはどっち派？」

## 概要
RouterModuleはNgModuleベースの習熟を活かせる。provideRouterはStandaloneアプリのルーティングをシンプルに記述でき、付加機能も選べる。

## 学習目標
- RouterModuleの構成と得意なシナリオを整理する
- provideRouterの採用メリットを理解する
- プロジェクト条件に応じた使い分け基準を決める

## 技術ポイント
- RouterModuleを成り立たせる主要API/構成要素
- provideRouterで押さえる設定やコード記述
- 両者を共存・移行させるためのブリッジ手法

## 📺 画面表示用コード（動画用）
**RouterModule派：NgModuleで宣言**
```typescript
@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
```

**provideRouter派：関数で提供**
```typescript
const routes: Routes = [...];

bootstrapApplication(AppComponent, {
  providers: [
    provideRouter(routes, withComponentInputBinding()),
  ],
});
```

## 💻 詳細実装例（学習用）
```typescript
export const routes: Routes = [
  {
    path: 'heroes',
    loadComponent: () => import('./heroes/hero-page.component').then(m => m.HeroPageComponent),
  },
];
```

## ベストプラクティス
- RouterModule運用時もルート設定は単一ファイルにまとめ、Lazy Load境界を明示する
- provideRouterを使う際は`withViewTransitions`, `withPreloading`など機能オプションを積極的に活用する
- 両アプローチが混在する場合は`RouterModule.forChild`の中身もStandalone Componentにするなど徐々に移行する

## 注意点
- RouterModuleとprovideRouterを同時に提供しない、二重DIになる可能性がある
- Functional Guardなどv15以降のAPIを使う際はバージョンを確認
- ルート定義ファイルは循環参照が起きやすいのでimportパスを管理する

## 関連技術
- RouterModule.forRoot
- provideRouter
- withComponentInputBinding
