# Angular Directives & Pipes 学習ショート動画 全300本タイトル
## 300本のショート動画で学ぶ実践Angular Directives & Pipes開発

---

## 第1章：Directives基礎（#001-030）- ディレクティブの基本概念

#001 「Directive とは？DOM拡張の仕組み」
#002 「Directive の3つの種類」
#003 「Component Directive - コンポーネント」
#004 「Structural Directive - 構造ディレクティブ」
#005 「Attribute Directive - 属性ディレクティブ」
#006 「Directive の役割と責任」
#007 「Directive vs Component の違い」
#008 「Directive の作成方法」
#009 「@Directive デコレータ」
#010 「selector の指定方法」
#011 「属性セレクタ [appXxx]」
#012 「クラスセレクタ .xxx」
#013 「要素セレクタ xxx」
#014 「Directive のライフサイクル」
#015 「ngOnInit での初期化」
#016 「ngOnDestroy でのクリーンアップ」
#017 「ElementRef - 要素参照」
#018 「nativeElement の使用」
#019 「直接DOM操作の注意点」
#020 「Renderer2 - 安全なDOM操作」
#021 「Renderer2 のメソッド」
#022 「setStyle() でのスタイル設定」
#023 「addClass() / removeClass()」
#024 「setAttribute() / removeAttribute()」
#025 「listen() でのイベント監視」
#026 「プラットフォーム非依存の実装」
#027 「SSR対応のDOM操作」
#028 「Directive のベストプラクティス」
#029 「Directive の命名規則」
#030 「Directive のデバッグ方法」

---

## 第2章：Structural Directives基礎（#031-070）- 構造ディレクティブ

#031 「Structural Directive とは？」
#032 「* (アスタリスク) 構文の意味」
#033 「<ng-template> への展開」
#034 「構造の追加・削除」
#035 「*ngIf - 条件付き表示」
#036 「*ngIf の基本構文」
#037 「真偽値での表示制御」
#038 「*ngIf="condition; else template"」
#039 「else ブロックの使用」
#040 「*ngIf="condition; then/else"」
#041 「then/else 両方の指定」
#042 「*ngIf="value as alias" - エイリアス」
#043 「値の再代入と使用」
#044 「*ngIf での null チェック」
#045 「*ngFor - 繰り返し表示」
#046 「*ngFor の基本構文」
#047 「*ngFor="let item of items"」
#048 「配列の反復処理」
#049 「index - インデックス取得」
#050 「first / last - 最初/最後の判定」
#051 「even / odd - 偶数/奇数の判定」
#052 「trackBy - パフォーマンス最適化」
#053 「trackBy 関数の実装」
#054 「一意キーでの追跡」
#055 「再描画の最小化」
#056 「*ngFor のネスト」
#057 「多次元配列の表示」
#058 「*ngSwitch - 多分岐」
#059 「*ngSwitch の基本構文」
#060 「[ngSwitch] での値指定」
#061 「*ngSwitchCase - ケース分岐」
#062 「*ngSwitchDefault - デフォルト」
#063 「複数 case の処理」
#064 「Structural Directive の組み合わせ」
#065 「ng-container の活用」
#066 「ラッパー要素なしの構造化」
#067 「複数ディレクティブの適用」
#068 「Control Flow構文（v17+）」
#069 「@if / @for / @switch 新構文」
#070 「従来構文との違い」

---

## 第3章：Attribute Directives基礎（#071-100）- 属性ディレクティブ

#071 「Attribute Directive とは？」
#072 「要素の振る舞いや見た目の変更」
#073 「DOMの構造は変えない」
#074 「ngClass - クラス制御」
#075 「[ngClass] の基本構文」
#076 「文字列でのクラス指定」
#077 「配列でのクラス指定」
#078 「オブジェクトでのクラス指定」
#079 「条件付きクラス適用」
#080 「複数クラスの動的制御」
#081 「ngStyle - スタイル制御」
#082 「[ngStyle] の基本構文」
#083 「オブジェクトでのスタイル指定」
#084 「複数スタイルの動的制御」
#085 「条件付きスタイル適用」
#086 「単位付き値の指定」
#087 「ngModel - 双方向バインディング」
#088 「[(ngModel)] の使用」
#089 「フォーム要素との連携」
#090 「ngModelChange イベント」
#091 「その他の組み込み Directive」
#092 「ngNonBindable - バインディング無効化」
#093 「ngPlural - 複数形制御」
#094 「ngTemplateOutlet - テンプレート挿入」
#095 「ngComponentOutlet - 動的コンポーネント」
#096 「Attribute Directive の実用例」
#097 「フォーム制御との組み合わせ」
#098 「アニメーションとの組み合わせ」
#099 「Attribute Directive のベストプラクティス」
#100 「パフォーマンス考慮事項」

---

## 第4章：Custom Directives作成（#101-140）- カスタムディレクティブ実装

#101 「カスタム Directive の作成手順」
#102 「ng generate directive コマンド」
#103 「Directive クラスの基本構造」
#104 「selector の命名規則」
#105 「app- プレフィックス」
#106 「HostListener - イベント監視」
#107 「@HostListener デコレータ」
#108 「クリックイベントの監視」
#109 「マウスイベントの監視」
#110 「キーボードイベントの監視」
#111 「event オブジェクトの取得」
#112 「preventDefault() の使用」
#113 「HostBinding - プロパティバインド」
#114 「@HostBinding デコレータ」
#115 「class バインディング」
#116 「style バインディング」
#117 「attribute バインディング」
#118 「HostListener + HostBinding」
#119 「インタラクティブな実装」
#120 「Input での設定受け取り」
#121 「@Input() プロパティ」
#122 「Directive のカスタマイズ」
#123 「デフォルト値の設定」
#124 「Output でのイベント発火」
#125 「@Output() プロパティ」
#126 「EventEmitter の使用」
#127 「カスタムイベントの発行」
#128 「Directive の再利用性」
#129 「汎用的な設計」
#130 「設定可能な実装」
#131 「Directive のテスト」
#132 「TestBed での設定」
#133 「Directive の動作確認」
#134 「イベントのシミュレーション」
#135 「Directive のデバッグ」
#136 「Angular DevTools での確認」
#137 「Directive のドキュメント作成」
#138 「使用例の記載」
#139 「Directive のベストプラクティス」
#140 「カスタム Directive の設計原則」

---

## 第5章：実用的なDirectives（#141-180）- 実践的なディレクティブ実装

#141 「Highlight Directive - ハイライト」
#142 「マウスオーバーで色変更」
#143 「動的な色指定」
#144 「Tooltip Directive - ツールチップ」
#145 「ホバー時の表示」
#146 「位置の動的調整」
#147 「ClickOutside Directive - 外部クリック検知」
#148 「要素外クリックの監視」
#149 「モーダル・ドロップダウンの閉じる処理」
#150 「Debounce Directive - デバウンス」
#151 「入力イベントの遅延」
#152 「検索ボックスでの活用」
#153 「AutoFocus Directive - 自動フォーカス」
#154 「表示時の自動フォーカス」
#155 「条件付きフォーカス」
#156 「InfiniteScroll Directive - 無限スクロール」
#157 「スクロール位置の監視」
#158 「追加データの自動読み込み」
#159 「LazyLoad Directive - 遅延読み込み」
#160 「画像の遅延ロード」
#161 「Intersection Observer の活用」
#162 「Drag Directive - ドラッグ」
#163 「ドラッグ可能要素の実装」
#164 「ドラッグイベントの処理」
#165 「Drop Directive - ドロップ」
#166 「ドロップゾーンの実装」
#167 「ドラッグ&ドロップの連携」
#168 「Resizable Directive - リサイズ」
#169 「要素のサイズ変更」
#170 「リサイズハンドルの実装」
#171 「Permission Directive - 権限制御」
#172 「ロールベースの表示制御」
#173 「権限チェック」
#174 「CopyToClipboard Directive - クリップボード」
#175 「クリックでコピー」
#176 「コピー完了の通知」
#177 「ScrollSpy Directive - スクロール監視」
#178 「スクロール位置の追跡」
#179 「ナビゲーションのアクティブ化」
#180 「実用 Directive の設計パターン」

---

## 第6章：Structural Directives作成（#181-210）- カスタム構造ディレクティブ

#181 「カスタム Structural Directive の作成」
#182 「ng generate directive --structural」
#183 「TemplateRef の注入」
#184 「ViewContainerRef の注入」
#185 「テンプレートの参照」
#186 「ビューコンテナの操作」
#187 「createEmbeddedView() メソッド」
#188 「ビューの生成」
#189 「clear() メソッド」
#190 「ビューの削除」
#191 「Unless Directive - 反転条件」
#192 「*ngIf の逆の動作」
#193 「条件の反転実装」
#194 「Repeat Directive - 繰り返し」
#195 「指定回数の繰り返し表示」
#196 「インデックスの提供」
#197 「Range Directive - 範囲指定」
#198 「開始・終了の指定」
#199 「数値範囲の反復」
#200 「Defer Directive - 遅延表示」
#201 「条件が真になるまで待機」
#202 「非同期条件の処理」
#203 「LoadingIf Directive - ローディング制御」
#204 「読み込み中の表示切り替え」
#205 「スケルトン表示」
#206 「Context オブジェクトの提供」
#207 「テンプレート変数の渡し方」
#208 「$implicit プロパティ」
#209 「カスタム Structural Directive のテスト」
#210 「高度な構造制御の実装」

---

## 第7章：Pipes基礎（#211-240）- パイプの基本

#211 「Pipe とは？データ変換」
#212 「| (パイプ) 構文」
#213 「テンプレートでの使用」
#214 「組み込み Pipe の種類」
#215 「DatePipe - 日付フォーマット」
#216 「{{ date | date }}」
#217 「フォーマット文字列の指定」
#218 「'yyyy-MM-dd' 形式」
#219 「'short' / 'medium' / 'long' / 'full'」
#220 「タイムゾーンの指定」
#221 「ロケールの設定」
#222 「CurrencyPipe - 通貨フォーマット」
#223 「{{ value | currency }}」
#224 「通貨コードの指定」
#225 「'USD' / 'EUR' / 'JPY'」
#226 「表示形式の指定」
#227 「DecimalPipe - 数値フォーマット」
#228 「{{ value | number }}」
#229 「小数点以下の桁数指定」
#230 「PercentPipe - パーセント表示」
#231 「{{ value | percent }}」
#232 「百分率への変換」
#233 「UpperCasePipe - 大文字変換」
#234 「{{ text | uppercase }}」
#235 「LowerCasePipe - 小文字変換」
#236 「{{ text | lowercase }}」
#237 「TitleCasePipe - タイトルケース」
#238 「{{ text | titlecase }}」
#239 「単語の先頭を大文字に」
#240 「組み込み Pipe の実践活用」

---

## 第8章：カスタムPipes作成（#241-270）- カスタムパイプ実装

#241 「カスタム Pipe の作成」
#242 「ng generate pipe コマンド」
#243 「@Pipe デコレータ」
#244 「name プロパティ」
#245 「PipeTransform インターフェース」
#246 「transform() メソッド」
#247 「引数の受け取り」
#248 「戻り値の型定義」
#249 「Pipe のパラメータ」
#250 「追加引数の使用」
#251 「{{ value | myPipe:arg1:arg2 }}」
#252 「可変長引数の実装」
#253 「Pure Pipe - 純粋パイプ」
#254 「pure: true - デフォルト」
#255 「参照の変更のみで再実行」
#256 「パフォーマンスが高い」
#257 「Impure Pipe - 非純粋パイプ」
#258 「pure: false の設定」
#259 「毎回の変更検知で再実行」
#260 「パフォーマンスへの影響」
#261 「Pure vs Impure の使い分け」
#262 「配列・オブジェクトの処理」
#263 「実用的なカスタム Pipe」
#264 「Truncate Pipe - 文字列切り詰め」
#265 「指定文字数で省略」
#266 「Filter Pipe - フィルタリング」
#267 「配列のフィルター処理」
#268 「OrderBy Pipe - ソート」
#269 「配列の並び替え」
#270 「カスタム Pipe の設計原則」

---

## 第9章：AsyncPipe & 高度なPipes（#271-290）- 非同期処理とパイプの応用

#271 「AsyncPipe - 非同期パイプ」
#272 「{{ observable$ | async }}」
#273 「Observable の自動購読」
#274 「自動購読解除」
#275 「メモリリーク防止」
#276 「Promise の処理」
#277 「null 値の扱い」
#278 「AsyncPipe と *ngIf」
#279 「as 構文での値取得」
#280 「*ngIf="data$ | async as data"」
#281 「複数 AsyncPipe の最適化」
#282 「share() オペレーターの併用」
#283 「JsonPipe - JSON表示」
#284 「{{ object | json }}」
#285 「デバッグ用途」
#286 「SlicePipe - 配列・文字列の切り出し」
#287 「{{ array | slice:start:end }}」
#288 「KeyValuePipe - オブジェクト反復」
#289 「*ngFor="let item of object | keyvalue"」
#290 「Pipe チェーン - 複数パイプの連結」

---

## 第10章：実践パターン & Testing（#291-300）- 実用的なパターンとテスト

#291 「Highlight Pipe - テキストハイライト」
#292 「検索キーワードの強調表示」
#293 「SafeHtml Pipe - HTML サニタイズ」
#294 「DomSanitizer の使用」
#295 「TimeAgo Pipe - 相対時間表示」
#296 「"3分前" 形式の表示」
#297 「FileSize Pipe - ファイルサイズ表示」
#298 「KB/MB/GB 変換」
#299 「Pipe のユニットテスト」
#300 「Directives & Pipes 総まとめと実践プロジェクト」

---

## 補足情報

- 各動画：30秒（28-32秒）
- 対象：Angular開発者、TypeScript経験者
- Angular Version：v20対応
- キャラクター：四国めたん（講師）、ずんだもん（開発者）
- 成果物：台本（ゆっくりムービーメーカー用）+ レスポンシブHTML一枚絵

---

## 学習推奨順序

1. 第1章（#001-030）：Directives基礎 - 最優先、概念理解
2. 第2章（#031-070）：Structural Directives - 必須機能
3. 第3章（#071-100）：Attribute Directives - 必須機能
4. 第7章（#211-240）：Pipes基礎 - データ変換必須
5. 第4章（#101-140）：Custom Directives - 実装力向上
6. 第8章（#241-270）：Custom Pipes - 実装力向上
7. 第5章（#141-180）：実用的なDirectives - 実践パターン
8. 第9章（#271-290）：AsyncPipe & 高度なPipes - 重要
9. 第6章（#181-210）：Structural Directives作成 - 高度な実装
10. 第10章（#291-300）：実践 & Testing - 総仕上げ

---

## 関連シリーズ

- **Angular Signals 300本**（作成済み）
- **Angular Components 300本**（作成済み）
- **Angular Routing 300本**（作成済み）
- **Angular Forms 300本**（作成済み）
- **Angular HTTP & API 300本**（作成済み）
- **Angular Services & DI 300本**（作成済み）
- **Angular RxJS & Observables 300本**（作成済み）
- **Angular Directives & Pipes 300本**（今回作成）
- Angular Testing 300本（次回作成候補）
- Angular Performance 300本（次回作成候補）

---

## 実践的なトピック

このシリーズでは以下の実務スキルが習得できます：

✅ 組み込みディレクティブの完全理解
✅ カスタムディレクティブの作成
✅ 実用的なUIインタラクション実装
✅ 組み込みパイプの使いこなし
✅ カスタムパイプの作成
✅ AsyncPipeでのメモリリーク対策
✅ Pure/Impureパイプの使い分け
✅ ドラッグ&ドロップ実装
✅ 無限スクロール実装
✅ DOM操作のベストプラクティス

---

## Directives & Pipesの重要性

Angularの表現力を高める重要な機能：

🎨 **UIの拡張** - Directivesで再利用可能なUI機能
📊 **データ変換** - Pipesで読みやすい表示
♻️ **再利用性** - DRY原則の実現
⚡ **パフォーマンス** - Pure Pipeの最適化
🔧 **保守性** - ロジックの分離と整理

---

## よく使う組み込みDirectives TOP10

1. **ngIf** - 条件付き表示（最頻出）
2. **ngFor** - 繰り返し表示（最頻出）
3. **ngClass** - クラス動的制御（重要）
4. **ngStyle** - スタイル動的制御（重要）
5. **ngModel** - 双方向バインディング
6. **ngSwitch** - 多分岐表示
7. **ngTemplateOutlet** - テンプレート挿入
8. **@if** - Control Flow新構文（v17+）
9. **@for** - Control Flow新構文（v17+）
10. **@switch** - Control Flow新構文（v17+）

---

## よく使う組み込みPipes TOP10

1. **date** - 日付フォーマット（最頻出）
2. **async** - Observable購読（重要）
3. **currency** - 通貨表示
4. **number** - 数値フォーマット
5. **percent** - パーセント表示
6. **uppercase/lowercase** - 大文字小文字変換
7. **json** - デバッグ用JSON表示
8. **slice** - 配列・文字列切り出し
9. **keyvalue** - オブジェクト反復
10. **titlecase** - タイトルケース変換