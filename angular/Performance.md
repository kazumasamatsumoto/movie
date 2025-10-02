# Angular Performance 学習ショート動画 全300本タイトル
## 300本のショート動画で学ぶ実践Angular Performance最適化

---

## 第1章：Performance基礎（#001-030）- パフォーマンスの基本概念

#001 「Performance とは？速度最適化の重要性」
#002 「ユーザー体験への影響」
#003 「パフォーマンス指標の理解」
#004 「FCP - First Contentful Paint」
#005 「LCP - Largest Contentful Paint」
#006 「FID - First Input Delay」
#007 「CLS - Cumulative Layout Shift」
#008 「TTI - Time to Interactive」
#009 「Core Web Vitals」
#010 「Google の推奨値」
#011 「パフォーマンス計測の重要性」
#012 「計測なしの最適化は無意味」
#013 「Chrome DevTools - Performance タブ」
#014 「Recording の開始と停止」
#015 「タイムラインの読み方」
#016 「ボトルネックの特定」
#017 「Lighthouse の使用」
#018 「パフォーマンススコア」
#019 「改善提案の確認」
#020 「Angular DevTools」
#021 「Component Explorer」
#022 「Profiler の使用」
#023 「変更検知の可視化」
#024 「パフォーマンスバジェット」
#025 「目標値の設定」
#026 「継続的な監視」
#027 「本番環境でのパフォーマンス」
#028 「開発環境との違い」
#029 「プロダクションビルドの重要性」
#030 「パフォーマンス最適化の基本戦略」

---

## 第2章：Change Detection（#031-060）- 変更検知戦略

#031 「Change Detection とは？」
#032 「Angular の変更検知メカニズム」
#033 「Zone.js の役割」
#034 「変更検知のトリガー」
#035 「イベント発火時」
#036 「HTTP レスポンス時」
#037 「タイマー実行時」
#038 「Default 戦略」
#039 「全コンポーネントチェック」
#040 「パフォーマンスへの影響」
#041 「OnPush 戦略」
#042 「ChangeDetectionStrategy.OnPush」
#043 「限定的な変更検知」
#044 「OnPush のトリガー条件」
#045 「@Input() の参照変更」
#046 「イベントの発火」
#047 「AsyncPipe の使用」
#048 「手動トリガー」
#049 「OnPush 実装の基本」
#050 「changeDetection プロパティ」
#051 「OnPush での注意点」
#052 「イミュータブルデータの重要性」
#053 「オブジェクトの新規作成」
#054 「配列のスプレッド演算子」
#055 「ChangeDetectorRef」
#056 「markForCheck() メソッド」
#057 「手動での変更検知マーク」
#058 「detectChanges() メソッド」
#059 「即座の変更検知実行」
#060 「detach() / reattach() メソッド」

---

## 第3章：TrackBy & List Optimization（#061-090）- リスト最適化

#061 「*ngFor のパフォーマンス問題」
#062 「全要素の再描画」
#063 「DOM 操作のコスト」
#064 「trackBy とは？」
#065 「要素の追跡関数」
#066 「一意キーでの識別」
#067 「trackBy の実装」
#068 「trackBy: trackByFn 構文」
#069 「index での追跡」
#070 「id での追跡」
#071 「trackBy のパフォーマンス効果」
#072 「再描画の最小化」
#073 「DOM 操作の削減」
#074 「Virtual Scrolling」
#075 「CDK Virtual Scroll」
#076 「大量データの表示」
#077 「可視領域のみレンダリング」
#078 「cdk-virtual-scroll-viewport」
#079 「itemSize の指定」
#080 「動的な高さの扱い」
#081 「Pagination 実装」
#082 「データの分割表示」
#083 「ページング制御」
#084 「Infinite Scroll」
#085 「スクロール時の追加読み込み」
#086 「パフォーマンス考慮」
#087 「リストフィルタリングの最適化」
#088 「Pure Pipe の活用」
#089 「メモ化の実装」
#090 「リスト最適化のベストプラクティス」

---

## 第4章：Lazy Loading（#091-120）- 遅延読み込み戦略

#091 「Lazy Loading とは？」
#092 「初期バンドルサイズ削減」
#093 「必要時のモジュール読み込み」
#094 「Module-based Lazy Loading」
#095 「loadChildren の使用」
#096 「動的 import()」
#097 「Feature Module の分割」
#098 「Standalone Lazy Loading」
#099 「loadComponent() - v14+」
#100 「Component の直接遅延読み込み」
#101 「Route Level Lazy Loading」
#102 「ルート設定での遅延読み込み」
#103 「Child Routes の遅延読み込み」
#104 「Preloading Strategy」
#105 「PreloadAllModules」
#106 「全モジュールの事前読み込み」
#107 「NoPreloading」
#108 「事前読み込みなし」
#109 「Custom Preloading Strategy」
#110 「条件付き事前読み込み」
#111 「優先度ベースの読み込み」
#112 「ネットワーク状態での判断」
#113 「Component Level Lazy Loading」
#114 「動的コンポーネント読み込み」
#115 「@defer ブロック（v17+）」
#116 「テンプレート内遅延読み込み」
#117 「on viewport トリガー」
#118 「on interaction トリガー」
#119 「Lazy Loading のデバッグ」
#120 「Chunk ファイルの確認」

---

## 第5章：Bundle Optimization（#121-150）- バンドル最適化

#121 「Bundle Size とは？」
#122 「初期読み込み時間への影響」
#123 「バンドルサイズの計測」
#124 「ng build --stats-json」
#125 「webpack-bundle-analyzer」
#126 「可視化での分析」
#127 「Tree Shaking」
#128 「未使用コードの削除」
#129 「ES6 Module の重要性」
#130 「Dead Code Elimination」
#131 「Production Build」
#132 「ng build --configuration=production」
#133 「最適化の自動適用」
#134 「Minification - 圧縮」
#135 「コードの短縮化」
#136 「Uglification - 難読化」
#137 「変数名の短縮」
#138 「AOT Compilation」
#139 「Ahead-of-Time コンパイル」
#140 「JIT との違い」
#141 「AOT のメリット」
#142 「テンプレートの事前コンパイル」
#143 「Code Splitting」
#144 「コードの分割戦略」
#145 「Vendor Bundle 分離」
#146 「Common Chunks」
#147 「動的インポートの活用」
#148 「Dependencies の最適化」
#149 「不要な依存の削除」
#150 「軽量な代替ライブラリ」

---

## 第6章：SSR & Hydration（#151-180）- サーバーサイドレンダリング

#151 「SSR とは？」
#152 「Server-Side Rendering」
#153 「初期表示の高速化」
#154 「SEO の改善」
#155 「Angular Universal」
#156 「SSR の実装」
#157 「@angular/platform-server」
#158 「サーバー環境の設定」
#159 「ng add @nguniversal/express-engine」
#160 「SSR ビルド」
#161 「npm run build:ssr」
#162 「サーバーの起動」
#163 「npm run serve:ssr」
#164 「Hydration とは？」
#165 「クライアント側での再起動」
#166 「DOM の再利用」
#167 「Full Hydration（v16+）」
#168 「provideClientHydration()」
#169 「Incremental Hydration」
#170 「段階的な再起動」
#171 「Non-Destructive Hydration」
#172 「破壊的でない再起動」
#173 「SSR でのデータ取得」
#174 「TransferState」
#175 「サーバーデータの転送」
#176 「重複リクエストの防止」
#177 「SSR での注意点」
#178 「DOM API の使用制限」
#179 「isPlatformBrowser の活用」
#180 「SSR パフォーマンスのベストプラクティス」

---

## 第7章：Preloading & Prefetching（#181-210）- 事前読み込み戦略

#181 「Preloading とは？」
#182 「先読みでの最適化」
#183 「Router Preloading」
#184 「ルートの事前読み込み」
#185 「PreloadingStrategy の実装」
#186 「カスタム戦略の作成」
#187 「Data Preloading」
#188 「Resolver での事前取得」
#189 「API データの先読み」
#190 「Image Preloading」
#191 「画像の事前読み込み」
#192 「priority 属性」
#193 「loading="eager"」
#194 「NgOptimizedImage（v15+）」
#195 「画像最適化ディレクティブ」
#196 「自動最適化機能」
#197 「Link Prefetching」
#198 「<link rel="prefetch">」
#199 「次ページのリソース取得」
#200 「DNS Prefetching」
#201 「<link rel="dns-prefetch">」
#202 「DNS 解決の高速化」
#203 「Resource Hints」
#204 「preconnect / preload」
#205 「Critical Resources」
#206 「重要リソースの優先読み込み」
#207 「Predictive Prefetching」
#208 「予測的な先読み」
#209 「ユーザー行動の分析」
#210 「事前読み込み戦略の実践」

---

## 第8章：Memory Management（#211-240）- メモリ管理

#211 「Memory Leak とは？」
#212 「メモリリークの原因」
#213 「パフォーマンスへの影響」
#214 「Observable の購読解除」
#215 「unsubscribe() の重要性」
#216 「購読解除忘れの問題」
#217 「AsyncPipe の活用」
#218 「自動購読解除」
#219 「メモリリーク防止」
#220 「takeUntilDestroyed()」
#221 「コンポーネント破棄時の解除」
#222 「DestroyRef の活用」
#223 「Subscription 管理」
#224 「複数購読のまとめて解除」
#225 「add() メソッド」
#226 「EventListener の解放」
#227 「addEventListener の注意点」
#228 「removeEventListener の必須性」
#229 「Timer の解放」
#230 「setInterval / setTimeout」
#231 「clearInterval / clearTimeout」
#232 「DOM 参照の解放」
#233 「ElementRef の注意」
#234 「循環参照の回避」
#235 「メモリプロファイリング」
#236 「Chrome DevTools Memory」
#237 「Heap Snapshot」
#238 「メモリリークの検出」
#239 「Allocation Timeline」
#240 「メモリ管理のベストプラクティス」

---

## 第9章：Runtime Performance（#241-270）- 実行時パフォーマンス

#241 「Runtime Performance とは？」
#242 「実行時の最適化」
#243 「Component のライフサイクル最適化」
#244 「ngOnInit での重い処理回避」
#245 「非同期処理への移行」
#246 「Template の最適化」
#247 「複雑な式の回避」
#248 「Computed Property の活用」
#249 「メソッド呼び出しの削減」
#250 「Getter の最適化」
#251 「Pure Function の使用」
#252 「Web Workers」
#253 「バックグラウンド処理」
#254 「重い計算の分離」
#255 「@angular/pwa」
#256 「Service Worker の活用」
#257 「オフラインキャッシング」
#258 「Intersection Observer」
#259 「要素の可視判定」
#260 「遅延処理のトリガー」
#261 「Request Animation Frame」
#262 「スムーズなアニメーション」
#263 「CSS での最適化」
#264 「Transform / Opacity の活用」
#265 「Reflow / Repaint の削減」
#266 「will-change プロパティ」
#267 「JavaScript 実行の最適化」
#268 「Debounce / Throttle」
#269 「イベント頻度の制御」
#270 「実行時最適化のパターン」

---

## 第10章：Monitoring & Tools（#271-300）- 計測とツール

#271 「継続的なパフォーマンス監視」
#272 「Real User Monitoring (RUM)」
#273 「実ユーザーデータの収集」
#274 「Google Analytics」
#275 「パフォーマンスイベント送信」
#276 「Web Vitals API」
#277 「JavaScript での計測」
#278 「Performance API」
#279 「Navigation Timing」
#280 「Resource Timing」
#281 「Sentry Performance」
#282 「エラーとパフォーマンスの統合監視」
#283 「New Relic」
#284 「APM ツールの活用」
#285 「WebPageTest」
#286 「詳細なパフォーマンス分析」
#287 「CI/CD でのパフォーマンステスト」
#288 「自動化された計測」
#289 「パフォーマンスバジェットの強制」
#290 「閾値超過時のビルド失敗」
#291 「Angular CLI Builder」
#292 「カスタムビルダーでの最適化」
#293 「Source Map Explorer」
#294 「バンドル内容の詳細分析」
#295 「Bundle Buddy」
#296 「重複コードの検出」
#297 「パフォーマンスチェックリスト」
#298 「最適化項目の体系化」
#299 「継続的改善のプロセス」
#300 「Performance 総まとめと実践プロジェクト」

---

## 補足情報

- 各動画：30秒（28-32秒）
- 対象：Angular開発者、TypeScript経験者
- Angular Version：v20対応
- キャラクター：四国めたん（講師）、ずんだもん（開発者）
- 成果物：台本（ゆっくりムービーメーカー用）+ レスポンシブHTML一枚絵

---

## 学習推奨順序

1. 第1章（#001-030）：Performance基礎 - 最優先、概念理解
2. 第2章（#031-060）：Change Detection - 最重要最適化
3. 第3章（#061-090）：TrackBy & List - 実装頻度高
4. 第5章（#121-150）：Bundle Optimization - 初期表示改善
5. 第4章（#091-120）：Lazy Loading - バンドル削減
6. 第8章（#211-240）：Memory Management - 安定性確保
7. 第9章（#241-270）：Runtime Performance - 実行時改善
8. 第6章（#151-180）：SSR & Hydration - 高度な最適化
9. 第7章（#181-210）：Preloading - 先読み戦略
10. 第10章（#271-300）：Monitoring - 継続的改善

---

## 関連シリーズ

- **Angular Signals 300本**（作成済み）
- **Angular Components 300本**（作成済み）
- **Angular Routing 300本**（作成済み）
- **Angular Forms 300本**（作成済み）
- **Angular HTTP & API 300本**（作成済み）
- **Angular Services & DI 300本**（作成済み）
- **Angular RxJS & Observables 300本**（作成済み）
- **Angular Directives & Pipes 300本**（作成済み）
- **Angular Testing 300本**（作成済み）
- **Angular Performance 300本**（今回作成）

---

## 実践的なトピック

このシリーズでは以下の実務スキルが習得できます：

✅ OnPush戦略による変更検知最適化
✅ TrackByによるリストパフォーマンス改善
✅ Lazy Loadingでの初期表示高速化
✅ Bundle サイズの削減と分析
✅ SSR/Hydrationによる高速化
✅ メモリリークの検出と対策
✅ パフォーマンス計測と監視
✅ Core Web Vitals の改善
✅ 継続的なパフォーマンス改善プロセス
✅ プロダクション環境での最適化

---

## Performance の重要性

ユーザー体験と事業成果に直結：

⚡ **速度 = UX** - 1秒の遅延で離脱率大幅増加
📊 **SEO への影響** - Google ランキング要因
💰 **ビジネス影響** - Amazon: 100msで1%売上減
🎯 **ユーザー満足度** - 快適な操作体験
🏆 **競合優位性** - 高速なアプリは選ばれる

---

## パフォーマンス最適化の優先順位

### **HIGH Priority（即効性大）**
1. **OnPush戦略** - 変更検知の最適化
2. **TrackBy** - リスト表示の高速化
3. **Lazy Loading** - 初期バンドル削減
4. **AOT Compilation** - Production Build
5. **メモリリーク対策** - 購読解除

### **MEDIUM Priority（効果的）**
6. **Bundle Optimization** - Tree Shaking
7. **Virtual Scrolling** - 大量データ表示
8. **Image Optimization** - NgOptimizedImage
9. **Preloading Strategy** - 先読み最適化
10. **AsyncPipe** - 自動購読解除

### **LOW Priority（高度）**
11. **SSR/Hydration** - サーバーレンダリング
12. **Web Workers** - バックグラウンド処理
13. **Service Worker** - PWA/キャッシング

---

## Core Web Vitals 目標値

Google 推奨の指標：

### **LCP (Largest Contentful Paint)**
- ✅ Good: 2.5秒以下
- ⚠️ Needs Improvement: 2.5-4.0秒
- ❌ Poor: 4.0秒超

### **FID (First Input Delay)**
- ✅ Good: 100ms以下
- ⚠️ Needs Improvement: 100-300ms
- ❌ Poor: 300ms超

### **CLS (Cumulative Layout Shift)**
- ✅ Good: 0.1以下
- ⚠️ Needs Improvement: 0.1-0.25
- ❌ Poor: 0.25超

---

## パフォーマンスチェックリスト

### **開発段階**
- [ ] OnPush 戦略の適用
- [ ] TrackBy の実装
- [ ] Pure Pipe の使用
- [ ] AsyncPipe の活用
- [ ] 購読解除の実装

### **ビルド段階**
- [ ] Production Build
- [ ] AOT Compilation
- [ ] Tree Shaking 有効化
- [ ] Lazy Loading 設定
- [ ] Bundle Size 分析

### **デプロイ段階**
- [ ] Gzip/Brotli 圧縮
- [ ] CDN の活用
- [ ] キャッシング戦略
- [ ] HTTP/2 対応
- [ ] SSR の検討

### **監視段階**
- [ ] Lighthouse スコア計測
- [ ] Core Web Vitals 監視
- [ ] RUM 導入
- [ ] エラー監視
- [ ] 継続的改善