# #402 「Standalone Components vs NgModule設計 あなたはどっち派？」

## 概要
Standalone ComponentとNgModuleベース構成は依存の明示度とスケーラビリティの考え方が違う。共有ライブラリの提供方法、DI構成、ルーティング記述の差を理解して適材適所で組み合わせる。

## 学習目標
- NgModuleベースの構成と得意なシナリオを整理する
- Standaloneの採用メリットを理解する
- プロジェクト条件に応じた使い分け基準を決める

## 技術ポイント
- NgModuleベースを成り立たせる主要API/構成要素
- Standaloneで押さえる設定やコード記述
- 両者を共存・移行させるためのブリッジ手法

## 📺 画面表示用コード（動画用）
**NgModule派：共有リソースを束ねる**
```typescript
@NgModule({
  declarations: [HeroListComponent],
  imports: [CommonModule, HeroesRoutingModule],
  exports: [HeroListComponent]
})
export class HeroesModule {}
```

**Standalone派：コンポーネント内で完結**
```typescript
@Component({
  selector: 'app-hero-list',
  standalone: true,
  imports: [CommonModule, HeroCardComponent],
  templateUrl: './hero-list.component.html'
})
export class HeroListComponent {}
```

## 💻 詳細実装例（学習用）
```typescript
// Standaloneブートストラップ
bootstrapApplication(AppComponent, {
  providers: [
    provideRouter(routes),
    provideHttpClient(withFetch()),
  ],
});

// NgModuleブートストラップ
@NgModule({
  declarations: [AppComponent],
  imports: [BrowserModule, HeroesModule],
  bootstrap: [AppComponent],
})
export class AppModule {}

platformBrowserDynamic().bootstrapModule(AppModule);
```

## ベストプラクティス
- 共有Pipe/DirectiveはModule化してまとめ、画面単位はStandaloneで小さく切る
- Standalone遷移時は`provideRouter`や`provideHttpClient`など機能ベースAPIを活用してDIを整理する
- ライブラリがNgModule依存の場合はFacade Moduleを残しつつ徐々にStandaloneへ移行する

## 注意点
- StandaloneとNgModuleを混在させる際は同じ依存を二重登録しないように注意する
- Lazy RouteでStandaloneを使う場合も`canMatch`等のガード設定を忘れない
- Module前提のスキーマを利用するライブラリを無理にStandaloneに置き換えない

## 関連技術
- Standalone Component
- NgModule
- bootstrapApplication/provideRouter
