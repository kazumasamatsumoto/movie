# Angular Services & DI 学習ショート動画 全300本タイトル
## 300本のショート動画で学ぶ実践Angular Services & DI開発

---

## 第1章：DI基礎（#001-030）- 依存性注入の基本概念

#001 「Dependency Injection とは？DI の基本」
#002 「なぜ DI が必要なのか？メリット」
#003 「DI Container の役割」
#004 「Injector の仕組み」
#005 「Service とは？サービスの定義」
#006 「@Injectable デコレータ」
#007 「@Injectable() の基本構文」
#008 「providedIn オプション」
#009 「providedIn: 'root' - ルートレベル」
#010 「Singleton パターン」
#011 「アプリ全体での共有」
#012 「Service の作成方法」
#013 「ng generate service コマンド」
#014 「Service クラスの基本構造」
#015 「Service の命名規則」
#016 「Service のファイル構成」
#017 「Service の責任範囲」
#018 「Single Responsibility Principle」
#019 「ビジネスロジックの分離」
#020 「データ管理の責務」
#021 「Service の注入方法」
#022 「constructor での注入（旧方式）」
#023 「private/public 修飾子」
#024 「inject() 関数（新方式 v14+）」
#025 「inject() の基本構文」
#026 「inject() のメリット」
#027 「constructor vs inject() 比較」
#028 「Service の使用例」
#029 「Component から Service を呼び出す」
#030 「DI のベストプラクティス」

---

## 第2章：Service作成パターン（#031-060）- 実践的なサービス設計

#031 「Data Service の作成」
#032 「CRUD 操作の実装」
#033 「API 呼び出しの集約」
#034 「HttpClient の注入」
#035 「Observable の返却」
#036 「State Management Service」
#037 「状態管理の実装」
#038 「BehaviorSubject の活用」
#039 「Subject の使い分け」
#040 「状態の購読と更新」
#041 「Utility Service の作成」
#042 「共通ユーティリティ関数」
#043 「日付フォーマット処理」
#044 「文字列操作処理」
#045 「数値計算処理」
#046 「Validation Service」
#047 「共通バリデーションロジック」
#048 「カスタム検証ルール」
#049 「Logger Service の作成」
#050 「ログ出力の一元管理」
#051 「ログレベルの制御」
#052 「環境別ログ設定」
#053 「Storage Service の作成」
#054 「localStorage ラッパー」
#055 「sessionStorage ラッパー」
#056 「データの永続化」
#057 「Notification Service」
#058 「Toast 通知の実装」
#059 「Alert ダイアログ管理」
#060 「通知キューの管理」

---

## 第3章：Scope管理（#061-090）- スコープとライフサイクル

#061 「DI のスコープとは？」
#062 「Root Level Injector」
#063 「Module Level Injector」
#064 「Component Level Injector」
#065 「Injector の階層構造」
#066 「親子関係の理解」
#067 「providedIn: 'root' の詳細」
#068 「グローバルシングルトン」
#069 「遅延インスタンス化」
#070 「Tree-shakable Providers」
#071 「providedIn: 'any' の使い方」
#072 「複数インスタンスの作成」
#073 「Lazy Loaded Module での挙動」
#074 「providedIn: 'platform' の使い方」
#075 「プラットフォームレベルの共有」
#076 「Component Level の Provider」
#077 「providers 配列での登録」
#078 「Component 固有のインスタンス」
#079 「Component ツリーでの共有」
#080 「Module Level の Provider」
#081 「NgModule の providers」
#082 「Feature Module での提供」
#083 「Module スコープの Service」
#084 「Service のライフサイクル」
#085 「インスタンス生成タイミング」
#086 「破棄タイミング」
#087 「ngOnDestroy での解放」
#088 「メモリリーク対策」
#089 「スコープの使い分け」
#090 「スコープ設計のベストプラクティス」

---

## 第4章：inject()関数（#091-120）- 新しいDI API

#091 「inject() 関数の詳細」
#092 「inject() が使える場所」
#093 「Injection Context」
#094 「コンストラクタ内での使用」
#095 「フィールド初期化での使用」
#096 「関数内での使用制限」
#097 「Lifecycle Hook での使用」
#098 「ngOnInit での inject()」
#099 「inject() の型推論」
#100 「型安全な注入」
#101 「ジェネリクスの活用」
#102 「オプショナル注入」
#103 「inject() の options」
#104 「optional: true オプション」
#105 「null 許容の注入」
#106 「self: true オプション」
#107 「自身の Injector のみ検索」
#108 「skipSelf: true オプション」
#109 「親 Injector のみ検索」
#110 「host: true オプション」
#111 「ホストコンポーネントまで検索」
#112 「複数オプションの組み合わせ」
#113 「inject() でのデバッグ」
#114 「注入エラーのトラブルシューティング」
#115 「inject() のパフォーマンス」
#116 「Functional Guard での活用」
#117 「Functional Interceptor での活用」
#118 「Functional Resolver での活用」
#119 「inject() のベストプラクティス」
#120 「inject() の実践例」

---

## 第5章：InjectionToken（#121-150）- カスタムトークン

#121 「InjectionToken とは？」
#122 「InjectionToken の作成」
#123 「new InjectionToken() 構文」
#124 「トークンの型定義」
#125 「ジェネリクスでの型指定」
#126 「トークンの説明文」
#127 「デバッグ用の識別子」
#128 「InjectionToken の提供」
#129 「providers での設定」
#130 「useValue での値提供」
#131 「プリミティブ値の提供」
#132 「オブジェクトの提供」
#133 「設定オブジェクトの注入」
#134 「InjectionToken の注入」
#135 「@Inject() デコレータ」
#136 「inject() での注入」
#137 「トークンの型安全性」
#138 「環境変数の管理」
#139 「API_URL トークンの実装」
#140 「環境別設定の切り替え」
#141 「Feature Flag の実装」
#142 「機能フラグの管理」
#143 「設定の階層化」
#144 「親子での設定上書き」
#145 「Multi Provider Token」
#146 「multi: true オプション」
#147 「複数値の配列提供」
#148 「プラグインシステムの実装」
#149 「InjectionToken のテスト」
#150 「InjectionToken のベストプラクティス」

---

## 第6章：Provider設定（#151-190）- 様々なプロバイダー

#151 「Provider の種類」
#152 「Class Provider」
#153 「provide + useClass」
#154 「クラスでの提供」
#155 「インターフェースベースの DI」
#156 「抽象クラスの活用」
#157 「実装の切り替え」
#158 「モック実装への切り替え」
#159 「Value Provider」
#160 「provide + useValue」
#161 「定数値の提供」
#162 「設定オブジェクトの提供」
#163 「イミュータブルな値」
#164 「Factory Provider」
#165 「provide + useFactory」
#166 「ファクトリー関数の定義」
#167 「動的なインスタンス生成」
#168 「deps 配列での依存定義」
#169 「他の Service への依存」
#170 「条件付きインスタンス生成」
#171 「環境に応じた実装切り替え」
#172 「Existing Provider」
#173 「provide + useExisting」
#174 「エイリアスの作成」
#175 「既存インスタンスの共有」
#176 「後方互換性の維持」
#177 「Provider の優先順位」
#178 「複数 Provider の解決順序」
#179 「オーバーライドの仕組み」
#180 「Provider のテスト」
#181 「TestBed での Provider 設定」
#182 「モックプロバイダーの作成」
#183 「スパイの使用」
#184 「Provider の動的変更」
#185 「Runtime での Provider 追加」
#186 「Injector.create() の活用」
#187 「カスタム Injector の作成」
#188 「Provider 設定のベストプラクティス」
#189 「Provider 設計パターン」
#190 「Provider の実践例」

---

## 第7章：階層的DI（#191-220）- 親子関係とマルチプロバイダー

#191 「階層的 DI の仕組み」
#192 「Injector ツリーの構造」
#193 「親 Injector への委譲」
#194 「検索アルゴリズム」
#195 「上方向への探索」
#196 「Component Injector」
#197 「Element Injector」
#198 「Component 階層での DI」
#199 「親コンポーネントからの継承」
#200 「子コンポーネントでの上書き」
#201 「viewProviders の使用」
#202 「ビュープロバイダーの範囲」
#203 「Content vs View の違い」
#204 「投影コンテンツへの影響」
#205 「Resolution Modifier」
#206 「@Self() デコレータ」
#207 「自身のみから解決」
#208 「@SkipSelf() デコレータ」
#209 「親からのみ解決」
#210 「@Host() デコレータ」
#211 「ホストまでの解決」
#212 「@Optional() デコレータ」
#213 「オプショナルな依存」
#214 「Modifier の組み合わせ」
#215 「Multi Providers」
#216 「複数プロバイダーの登録」
#217 「配列としての注入」
#218 「プラグインアーキテクチャ」
#219 「拡張ポイントの提供」
#220 「階層的 DI の実践例」

---

## 第8章：Service設計パターン（#221-260）- アーキテクチャパターン

#221 「Repository パターン」
#222 「データアクセス層の抽象化」
#223 「Repository の実装」
#224 「CRUD メソッドの定義」
#225 「Entity の管理」
#226 「Facade パターン」
#227 「複雑なサブシステムの隠蔽」
#228 「Facade Service の実装」
#229 「統一されたインターフェース」
#230 「Store パターン」
#231 「状態管理ストアの実装」
#232 「Redux ライクな設計」
#233 「Action の定義」
#234 「Reducer の実装」
#235 「State の immutability」
#236 「Selector の実装」
#237 「Strategy パターン」
#238 「アルゴリズムの切り替え」
#239 「Strategy の実装」
#240 「実行時の戦略選択」
#241 「Factory パターン」
#242 「オブジェクト生成の抽象化」
#243 「Factory Service の実装」
#244 「型に応じたインスタンス生成」
#245 「Observer パターン」
#246 「Subject/Observer の実装」
#247 「イベント駆動アーキテクチャ」
#248 「Command パターン」
#249 「コマンドオブジェクトの実装」
#250 「Undo/Redo の実装」
#251 「Adapter パターン」
#252 「外部 API の適合」
#253 「Adapter Service の実装」
#254 「Decorator パターン」
#255 「機能の動的追加」
#256 「Service のラッピング」
#257 「Composite パターン」
#258 「階層構造の Service」
#259 「パターンの組み合わせ」
#260 「設計パターンのベストプラクティス」

---

## 第9章：実践的なService（#261-290）- 業務で使うサービス実装

#261 「Authentication Service」
#262 「ログイン処理の実装」
#263 「トークン管理」
#264 「認証状態の保持」
#265 「自動ログアウト」
#266 「セッション管理」
#267 「Authorization Service」
#268 「権限チェックの実装」
#269 「ロールベースアクセス制御」
#270 「パーミッション管理」
#271 「User Service」
#272 「ユーザー情報管理」
#273 「プロフィール更新」
#274 「ユーザー設定の保持」
#275 「Theme Service」
#276 「テーマ切り替え機能」
#277 「ダークモード実装」
#278 「テーマの永続化」
#279 「i18n Service」
#280 「言語切り替え機能」
#281 「翻訳データの管理」
#282 「動的言語ロード」
#283 「Analytics Service」
#284 「イベントトラッキング」
#285 「ページビュー計測」
#286 「Google Analytics 連携」
#287 「Error Tracking Service」
#288 「エラーログの収集」
#289 「Sentry 連携」
#290 「エラー通知の実装」

---

## 第10章：Testing & Best Practices（#291-300）- テストとベストプラクティス

#291 「Service のユニットテスト」
#292 「TestBed の設定」
#293 「Service のインスタンス取得」
#294 「inject() でのテスト」
#295 「依存関係のモック」
#296 「HttpClient のモック」
#297 「HttpTestingController の使用」
#298 「Observable のテスト」
#299 「非同期テストの実装」
#300 「Services & DI 総まとめと実践プロジェクト」

---

## 補足情報

- 各動画：30秒（28-32秒）
- 対象：Angular開発者、TypeScript経験者
- Angular Version：v20対応
- キャラクター：四国めたん（講師）、ずんだもん（開発者）
- 成果物：台本（ゆっくりムービーメーカー用）+ レスポンシブHTML一枚絵

---

## 学習推奨順序

1. 第1章（#001-030）：DI基礎 - 最優先、概念理解
2. 第2章（#031-060）：Service作成パターン - 実装必須
3. 第3章（#061-090）：Scope管理 - アーキテクチャ理解
4. 第4章（#091-120）：inject()関数 - 最新API習得
5. 第5章（#121-150）：InjectionToken - 設定管理
6. 第6章（#151-190）：Provider設定 - 柔軟な設計
7. 第7章（#191-220）：階層的DI - 高度な制御
8. 第8章（#221-260）：設計パターン - プロレベル
9. 第9章（#261-290）：実践Service - 業務実装
10. 第10章（#291-300）：Testing - 品質保証

---

## 関連シリーズ

- **Angular Signals 300本**（作成済み）
- **Angular Components 300本**（作成済み）
- **Angular Routing 300本**（作成済み）
- **Angular Forms 300本**（作成済み）
- **Angular HTTP & API 300本**（作成済み）
- **Angular Services & DI 300本**（今回作成）
- Angular RxJS & Observables 300本（次回作成候補）
- Angular Directives & Pipes 300本（次回作成候補）

---

## 実践的なトピック

このシリーズでは以下の実務スキルが習得できます：

✅ 依存性注入の完全理解
✅ スケーラブルなサービス層設計
✅ 認証・認可システムの実装
✅ 状態管理サービスの構築
✅ テスト可能な設計
✅ デザインパターンの適用
✅ 階層的DIの活用
✅ inject()関数の実践的使用
✅ InjectionTokenでの設定管理
✅ エンタープライズレベルのアーキテクチャ

---

## Angularアーキテクチャの中核

Services & DIはAngularアーキテクチャの根幹を成す最重要テーマです：

🏗️ **疎結合な設計** - テスト可能で保守性の高いコード
🔄 **再利用性** - ビジネスロジックの共通化
🎯 **責任分離** - Component はUIのみに集中
⚡ **パフォーマンス** - Singletonによる効率的なメモリ使用
🧪 **テスタビリティ** - モックによる単体テスト容易化