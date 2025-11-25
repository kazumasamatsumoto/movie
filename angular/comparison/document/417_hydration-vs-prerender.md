# #417 「Hydration vs Prerenderオンリー あなたはどっち派？」

## 概要
Prerenderは配信コストを抑えられSEOも満たせるが、クライアントJSは別で走る。HydrationはSSR DOMを再利用し、初回のJS処理を削減する。

## 学習目標
- Prerenderオンリーの構成と得意なシナリオを整理する
- Hydrationの採用メリットを理解する
- プロジェクト条件に応じた使い分け基準を決める

## 技術ポイント
- Prerenderオンリーを成り立たせる主要API/構成要素
- Hydrationで押さえる設定やコード記述
- 両者を共存・移行させるためのブリッジ手法

## 📺 画面表示用コード（動画用）
**Prerender：`ng prerender`で静的出力**
```typescript
ng build && ng run app:prerender
// dist/app/browserに静的HTMLが展開
```

**Hydration：クライアントで再利用**
```typescript
bootstrapApplication(AppComponent, {
  providers: [
    provideClientHydration(),
  ],
});
```

## 💻 詳細実装例（学習用）
```typescript
import { provideClientHydration } from '@angular/platform-browser';

bootstrapApplication(AppComponent, {
  providers: [provideClientHydration()],
});
```

## ベストプラクティス
- Prerender対象は更新頻度の低いページに限定し、ISR（Incremental Static Regeneration）的なフローを整える
- Hydrationするページは副作用を`afterRender`等に逃し、サーバとクライアントのDOM差分を無くす
- 動的・静的ページを混在させる場合はルーティングで明示的に分離する

## 注意点
- Prerenderは大量ページでビルド時間が伸びるため監視が必要
- HydrationしないとクライアントJSが再描画するため一瞬チラつくことがある
- Hydration済みページに直接DOM操作を入れるとミスマッチになるので避ける

## 関連技術
- Angular prerender
- Client Hydration
- Server-side rendering
