# #416 「CSRオンリー vs SSR+Hydration あなたはどっち派？」

## 概要
CSRは構成がシンプルでコストを抑えられる。SSR+Hydrationは実装コストがかかるがUXとSEOが向上する。

## 学習目標
- CSRオンリーの構成と得意なシナリオを整理する
- SSR+Hydrationの採用メリットを理解する
- プロジェクト条件に応じた使い分け基準を決める

## 技術ポイント
- CSRオンリーを成り立たせる主要API/構成要素
- SSR+Hydrationで押さえる設定やコード記述
- 両者を共存・移行させるためのブリッジ手法

## 📺 画面表示用コード（動画用）
**CSR派：静的ホスティングに配置**
```typescript
ng build --configuration production
npx http-server dist/app
```

**SSR派：server.tsを用意**
```typescript
export function app(): Promise<Express> {
  const server = express();
  server.use(express.static(join(process.cwd(), 'dist/app/browser')));
  server.get('*', ngExpressEngine);
  return server;
}
```

## 💻 詳細実装例（学習用）
```typescript
bootstrapApplication(AppComponent, {
  providers: [
    provideClientHydration(),
  ],
});
```

## ベストプラクティス
- CSR構成でも`ngx-build-plus`や`esbuild`でバンドルサイズを管理し、初回表示を最適化する
- SSR導入時はAPIレスポンス時間も測定し、`TransferState`でデータ再取得を防ぐ
- Hydration対象のコンポーネントは副作用を`ngOnInit`以降に寄せて一致させる

## 注意点
- SSRはNode.jsランタイムが必要で、デプロイ先のコストが上がる
- ブラウザAPIを`ngOnInit`前に使うとSSRでクラッシュする
- CSRからSSRへ移行する際は環境判定コードを必ずテストする

## 関連技術
- Angular SSR
- Hydration
- TransferState
