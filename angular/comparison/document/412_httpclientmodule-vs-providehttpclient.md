# #412 「HttpClientModule vs provideHttpClient あなたはどっち派？」

## 概要
HttpClientModuleは古典的だが簡単。provideHttpClientは機能ベースでツリーシェイカブルな設定ができ、Standalone構成にフィットする。

## 学習目標
- HttpClientModuleの構成と得意なシナリオを整理する
- provideHttpClientの採用メリットを理解する
- プロジェクト条件に応じた使い分け基準を決める

## 技術ポイント
- HttpClientModuleを成り立たせる主要API/構成要素
- provideHttpClientで押さえる設定やコード記述
- 両者を共存・移行させるためのブリッジ手法

## 📺 画面表示用コード（動画用）
**HttpClientModule派：NgModuleにimport**
```typescript
@NgModule({
  imports: [BrowserModule, HttpClientModule],
  bootstrap: [AppComponent],
})
export class AppModule {}
```

**provideHttpClient派：機能を組み合わせる**
```typescript
bootstrapApplication(AppComponent, {
  providers: [
    provideHttpClient(
      withFetch(),
      withInterceptors([authInterceptor]),
    ),
  ],
});
```

## 💻 詳細実装例（学習用）
```typescript
export function authInterceptor(req: HttpRequest<unknown>, next: HttpHandlerFn) {
  return next(req.clone({ setHeaders: { Authorization: 'Bearer token' } }));
}
```

## ベストプラクティス
- NgModule運用時でも`HttpClientModule`をrootだけでimportし、子Moduleからは再度importしない
- `provideHttpClient`では関数オプションを分離してテストしやすいように保つ
- SSRやHydrationが必要な場合は`withFetch()`を利用し、環境別プロバイダで切り替える

## 注意点
- HttpClientModuleとprovideHttpClientを同時に登録すると二重DIになる可能性がある
- interceptorを`multi: true`で提供する場合、順序を把握して副作用を避ける
- `provideHttpClient`のオプションは関数呼び出し順に適用されるので意図どおり並べる

## 関連技術
- HttpClientModule
- provideHttpClient
- HTTP Interceptors
