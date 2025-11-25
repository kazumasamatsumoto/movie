# #408 「Zone.js依存 vs Zoneless構成 あなたはどっち派？」

## 概要
Zone.jsは互換性とDXを担保するが、ZonelessはSignals＋明示的更新でパフォーマンスと理解を得られる。アプリの成熟度に合わせて選ぶ。

## 学習目標
- Zone.jsありの構成と得意なシナリオを整理する
- Zonelessの採用メリットを理解する
- プロジェクト条件に応じた使い分け基準を決める

## 技術ポイント
- Zone.jsありを成り立たせる主要API/構成要素
- Zonelessで押さえる設定やコード記述
- 両者を共存・移行させるためのブリッジ手法

## 📺 画面表示用コード（動画用）
**Zone.jsあり：既定の`bootstrapApplication`**
```typescript
bootstrapApplication(AppComponent, {
  providers: [
    provideRouter(routes),
  ],
});
```

**Zoneless：実験的プロバイダを適用**
```typescript
bootstrapApplication(AppComponent, {
  providers: [
    provideExperimentalZonelessChangeDetection(),
    provideRouter(routes),
  ],
});
```

## 💻 詳細実装例（学習用）
```typescript
import { provideExperimentalZonelessChangeDetection } from '@angular/core';

bootstrapApplication(AppComponent, {
  providers: [
    provideExperimentalZonelessChangeDetection(),
    provideRouter(routes),
  ],
});
```

## ベストプラクティス
- Zoneless化する場合はSignalsや`effect`でUI更新を記述し、`runOutsideAngular`に頼らない
- 外部ライブラリがZone依存の場合はAdapter層を設け、完全移行まではZoneを残す
- Zoneあり構成でも`bootstrapApplication`で必要なプロバイダだけを読み込んでコストを抑える

## 注意点
- Zonelessはまだexperimental扱いなのでサポート範囲を把握しておく
- Zoneを外すと`setTimeout`等で自動検知されないためSignals以外の更新をどう扱うか決める
- SSRやHydrationを使う場合はZonelessとの組み合わせを事前検証する

## 関連技術
- Zone.js
- provideExperimentalZonelessChangeDetection
- Signals/effect
