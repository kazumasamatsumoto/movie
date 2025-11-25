# #420 「NoPreloading vs PreloadAllModules あなたはどっち派？」

## 概要
NoPreloadingは通信量と初回負荷を抑える。PreloadAllModulesは後続遷移の体感速度を上げる。ハイブリッドも可能。

## 学習目標
- NoPreloadingの構成と得意なシナリオを整理する
- PreloadAllModulesの採用メリットを理解する
- プロジェクト条件に応じた使い分け基準を決める

## 技術ポイント
- NoPreloadingを成り立たせる主要API/構成要素
- PreloadAllModulesで押さえる設定やコード記述
- 両者を共存・移行させるためのブリッジ手法

## 📺 画面表示用コード（動画用）
**NoPreloading：標準設定**
```typescript
provideRouter(routes);
```

**PreloadAllModules：全て先読み**
```typescript
provideRouter(routes, withPreloading(PreloadAllModules));
```

## 💻 詳細実装例（学習用）
```typescript
provideRouter(routes, withPreloading(PreloadAllModules));
```

## ベストプラクティス
- トラフィックに余裕がある管理画面などはPreloadAllModulesでUXを最適化する
- 大規模アプリはカスタムPreloadingStrategyを実装し、優先度の高いルートだけ先読みする
- ネットワーク状況に応じて戦略を切り替えたい場合は`NetworkInformation` API等と連携する

## 注意点
- PreloadAllModulesは大量のLazyモジュールがあると帯域を圧迫する
- NoPreloadingはユーザーが初めて訪れる画面で待ち時間が必ず発生する
- 戦略変更後はCore Web Vitalsを計測し、効果を確認する

## 関連技術
- Angular Router PreloadingStrategy
- withPreloading
- PreloadAllModules
