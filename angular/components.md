# Angular Components 学習ショート動画 全300本タイトル
## 300本のショート動画で学ぶ実践Angular Components開発



## 第1章：Component基礎（#001-030）- コンポーネントの作り方

#001 「Component とは？Angular の基本単位」
#002 「CLI で Component 作成 - ng generate component」
#003 「Component デコレータ - @Component の役割」
#004 「selector - コンポーネントの呼び出し方」
#005 「template - インラインテンプレート」
#006 「templateUrl - 外部テンプレートファイル」
#007 「styles - インラインスタイル」
#008 「styleUrls - 外部スタイルファイル」
#009 「Component クラスの基本構造」
#010 「TypeScript で Component を書く」
#011 「Component のファイル構成」
#012 「Component の命名規則」
#013 「Standalone Component - standalone: true」
#014 「Standalone vs Module-based 比較」
#015 「imports 配列 - 依存関係の宣言」
#016 「Component の export と再利用」
#017 「Component のディレクトリ構成」
#018 「Component のベストプラクティス」
#019 「Component 作成時のよくあるエラー」
#020 「Component のデバッグ方法」
#021 「Angular DevTools で Component 確認」
#022 「Component のホットリロード」
#023 「Component の削除方法」
#024 「Component のリファクタリング」
#025 「Component の複製と再利用」
#026 「Component のバージョン管理」
#027 「Component のドキュメント作成」
#028 「Component のコメント規約」
#029 「Component のフォルダ構成戦略」
#030 「Component 設計の基本原則」

---

## 第2章：Template構文基礎（#031-060）- データ表示とバインディング

#031 「{{ }} 補間バインディング - データ表示」
#032 「{{ }} 式の評価 - 計算とメソッド呼び出し」
#033 「{{ }} 安全な補間 - XSS対策」
#034 「[property] プロパティバインディング基礎」
#035 「[src] 画像バインディング」
#036 「[href] リンクバインディング」
#037 「[disabled] 属性バインディング」
#038 「[class] クラスバインディング」
#039 「[style] スタイルバインディング」
#040 「[attr.] 属性バインディング」
#041 「(event) イベントバインディング基礎」
#042 「(click) クリックイベント」
#043 「(input) 入力イベント」
#044 「(change) 変更イベント」
#045 「(submit) フォーム送信イベント」
#046 「(keyup) キーボードイベント」
#047 「(mouseenter) マウスイベント」
#048 「(focus) / (blur) フォーカスイベント」
#049 「$event オブジェクトの活用」
#050 「イベント修飾子 - .preventDefault()」
#051 「[(ngModel)] 双方向バインディング」
#052 「[(ngModel)] FormsModule のインポート」
#053 「バナナインボックス構文の仕組み」
#054 「複数のバインディングを組み合わせる」
#055 「テンプレート式のベストプラクティス」
#056 「テンプレート式の制約事項」
#057 「テンプレート式でのメソッド呼び出し注意点」
#058 「バインディングのパフォーマンス考慮」
#059 「テンプレート構文のデバッグ」
#060 「テンプレートのよくあるエラー」

---

## 第3章：Lifecycle Hooks（#061-090）- ライフサイクル管理

#061 「Lifecycle Hooks とは？コンポーネントの一生」
#062 「ngOnChanges - 入力プロパティ変更時」
#063 「ngOnChanges - SimpleChanges の活用」
#064 「ngOnInit - 初期化処理」
#065 「ngOnInit のベストプラクティス」
#066 「constructor vs ngOnInit の使い分け」
#067 「ngDoCheck - 変更検知のカスタマイズ」
#068 「ngAfterContentInit - コンテンツ投影後」
#069 「ngAfterContentChecked - コンテンツチェック後」
#070 「ngAfterViewInit - ビュー初期化後」
#071 「ngAfterViewChecked - ビューチェック後」
#072 「ngOnDestroy - クリーンアップ処理」
#073 「ngOnDestroy でのメモリリーク対策」
#074 「Lifecycle の実行順序」
#075 「親子コンポーネントの Lifecycle 順序」
#076 「Lifecycle Hooks の使い分け」
#077 「ngOnInit での API 呼び出し」
#078 「ngOnDestroy での購読解除」
#079 「Lifecycle でのタイマー処理」
#080 「Lifecycle での DOM 操作」
#081 「Lifecycle での状態初期化」
#082 「Lifecycle でのイベントリスナー登録」
#083 「Lifecycle でのリソース解放」
#084 「Lifecycle のデバッグ方法」
#085 「Lifecycle のよくあるエラー」
#086 「Lifecycle のパフォーマンス影響」
#087 「Lifecycle とSignals の組み合わせ」
#088 「Lifecycle のテスト方法」
#089 「Lifecycle のベストプラクティス」
#090 「Lifecycle のアンチパターン」

---

## 第4章：Component通信（#091-130）- 親子間のデータ受け渡し

#091 「@Input() - 親から子へデータを渡す」
#092 「@Input() の基本構文」
#093 「@Input() 必須プロパティ - required」
#094 「@Input() デフォルト値の設定」
#095 「@Input() エイリアス指定」
#096 「@Input() 型定義とバリデーション」
#097 「@Input() プリミティブ型の受け渡し」
#098 「@Input() オブジェクトの受け渡し」
#099 「@Input() 配列の受け渡し」
#100 「@Input() 関数の受け渡し」
#101 「@Input() での不変性の考慮」
#102 「@Input() の変更検知」
#103 「@Input() とngOnChanges の連携」
#104 「@Output() - 子から親へイベント通知」
#105 「@Output() の基本構文」
#106 「EventEmitter の使い方」
#107 「@Output() カスタムイベント発火」
#108 「@Output() データ付きイベント」
#109 「@Output() エイリアス指定」
#110 「@Output() 複数イベントの管理」
#111 「@Input() + @Output() の組み合わせ」
#112 「双方向バインディングのカスタム実装」
#113 「親子間通信のベストプラクティス」
#114 「深い階層の Component 通信」
#115 「祖先-子孫間の通信戦略」
#116 「兄弟 Component 間の通信」
#117 「Service を使った Component 間通信」
#118 「Input/Output のパフォーマンス考慮」
#119 「Input/Output のデバッグ方法」
#120 「Input/Output のよくあるエラー」
#121 「Input/Output のテスト方法」
#122 「SignalInput - signal() ベース入力」
#123 「SignalInput vs @Input() 比較」
#124 「SignalOutput - signal() ベース出力」
#125 「SignalOutput vs @Output() 比較」
#126 「Component 通信のデザインパターン」
#127 「プロパティドリリングの回避」
#128 「Component 境界の設計」
#129 「Component 通信のセキュリティ考慮」
#130 「Component 通信の実践例」

---

## 第5章：ViewChild & ContentChild（#131-160）- DOM参照とクエリ

#131 「ViewChild - 子要素への参照」
#132 「ViewChild の基本構文」
#133 「ViewChild テンプレート参照変数」
#134 「ViewChild 子コンポーネント参照」
#135 「ViewChild ディレクティブ参照」
#136 「ViewChild read オプション」
#137 「ViewChild static オプション」
#138 「ViewChild とライフサイクル」
#139 「ViewChild で DOM 操作」
#140 「ViewChild でメソッド呼び出し」
#141 「ViewChildren - 複数要素参照」
#142 「ViewChildren QueryList の活用」
#143 「ViewChildren での反復処理」
#144 「ViewChildren 変更監視」
#145 「ContentChild - 投影コンテンツ参照」
#146 「ContentChild の基本構文」
#147 「ContentChild と ng-content」
#148 「ContentChild 複数投影の参照」
#149 「ContentChildren - 複数投影参照」
#150 「ContentChildren QueryList 活用」
#151 「ViewChild vs ContentChild 使い分け」
#152 「テンプレート参照変数 # の活用」
#153 「テンプレート参照変数のスコープ」
#154 「ElementRef での直接 DOM アクセス」
#155 「ElementRef の注意点とリスク」
#156 「Renderer2 での安全な DOM 操作」
#157 「QueryList の変更検知」
#158 「QueryList のメソッド活用」
#159 「ViewChild/ContentChild のテスト」
#160 「DOM 参照のベストプラクティス」

---

## 第6章：Component Styling（#161-190）- スタイリングとテーマ

#161 「Component スタイルの基本」
#162 「ViewEncapsulation - カプセル化戦略」
#163 「ViewEncapsulation.Emulated - デフォルト」
#164 「ViewEncapsulation.None - グローバル」
#165 「ViewEncapsulation.ShadowDom - Shadow DOM」
#166 「:host セレクタ - ホスト要素」
#167 「:host-context セレクタ - 祖先条件」
#168 「::ng-deep - 子孫セレクタ（非推奨）」
#169 「Component 固有スタイルの適用」
#170 「グローバルスタイルとの使い分け」
#171 「CSS 変数の活用」
#172 「CSS カスタムプロパティ」
#173 「テーマの実装方法」
#174 「ダークモード対応」
#175 「動的スタイル変更」
#176 「[ngClass] 動的クラス制御」
#177 「[ngClass] オブジェクト構文」
#178 「[ngClass] 配列構文」
#179 「[ngClass] 条件付きクラス」
#180 「[ngStyle] 動的スタイル制御」
#181 「[ngStyle] オブジェクト構文」
#182 「[ngStyle] 複数スタイル指定」
#183 「CSS Modules の活用」
#184 「SCSS/SASS の使用」
#185 「レスポンシブデザイン実装」
#186 「メディアクエリの活用」
#187 「Flexbox レイアウト」
#188 「CSS Grid レイアウト」
#189 「スタイリングのパフォーマンス」
#190 「スタイリングのベストプラクティス」

---

## 第7章：Content Projection（#191-220）- コンテンツ投影とスロット

#191 「ng-content - 基本的なコンテンツ投影」
#192 「ng-content の仕組み」
#193 「Single Slot Projection - 単一スロット」
#194 「Multi Slot Projection - 複数スロット」
#195 「select 属性 - スロット選択」
#196 「select タグ名での選択」
#197 「select クラス名での選択」
#198 「select 属性での選択」
#199 「select ディレクティブでの選択」
#200 「デフォルトコンテンツの設定」
#201 「条件付きコンテンツ投影」
#202 「動的コンテンツ投影」
#203 「ng-container との組み合わせ」
#204 「ng-template での投影」
#205 「ngTemplateOutlet の活用」
#206 「コンテンツ投影とライフサイクル」
#207 「ContentChild での投影取得」
#208 「投影されたコンテンツの操作」
#209 「カード Component での活用例」
#210 「モーダル Component での活用例」
#211 「タブ Component での活用例」
#212 「アコーディオン での活用例」
#213 「レイアウト Component での活用例」
#214 「再利用可能な Component 設計」
#215 「コンテンツ投影のパフォーマンス」
#216 「コンテンツ投影のデバッグ」
#217 「コンテンツ投影のテスト」
#218 「コンテンツ投影のベストプラクティス」
#219 「コンテンツ投影の制約事項」
#220 「Web Components との比較」

---

## 第8章：Dynamic Components（#221-250）- 動的コンポーネント生成

#221 「Dynamic Components とは？」
#222 「ViewContainerRef の基本」
#223 「ComponentFactoryResolver（旧方式）」
#224 「createComponent() - 新方式（v13+）」
#225 「動的 Component の作成」
#226 「動的 Component への入力渡し」
#227 「動的 Component のイベント購読」
#228 「動的 Component の削除」
#229 「動的 Component の置き換え」
#230 「複数の動的 Component 管理」
#231 「ng-template + ViewContainerRef」
#232 「ComponentRef の活用」
#233 「動的 Component のライフサイクル」
#234 「動的ローディング実装」
#235 「遅延ロード Component」
#236 「条件付き Component 表示」
#237 「動的フォーム生成」
#238 「動的タブシステム」
#239 「動的ウィジェットシステム」
#240 「プラグインアーキテクチャ」
#241 「Component ファクトリーパターン」
#242 「動的 Component のメモリ管理」
#243 「動的 Component のテスト」
#244 「動的 Component のデバッグ」
#245 「動的 Component のパフォーマンス」
#246 「Angular Portal の活用」
#247 「CDK Portal の実装」
#248 「動的 Component のベストプラクティス」
#249 「動的 Component の実践例」
#250 「動的 Component の設計パターン」

---

## 第9章：Component設計パターン（#251-280）- 設計とアーキテクチャ

#251 「Smart Component - 賢いコンポーネント」
#252 「Dumb Component - 純粋なコンポーネント」
#253 「Smart/Dumb パターンの実践」
#254 「Presentation Component - 表示専用」
#255 「Container Component - ロジック層」
#256 「Presentation/Container 分離」
#257 「Stateful vs Stateless Component」
#258 「Pure Component の実装」
#259 「Component の責任分離」
#260 「Single Responsibility Principle」
#261 「Component の粒度設計」
#262 「Component の再利用性向上」
#263 「Component の拡張性設計」
#264 「Component のテスト容易性」
#265 「Composition over Inheritance」
#266 「Component Composition パターン」
#267 「Higher Order Component」
#268 「Wrapper Component パターン」
#269 「Adapter Component パターン」
#270 「Facade Component パターン」
#271 「Component 設計の SOLID 原則」
#272 「DRY 原則の適用」
#273 「KISS 原則の適用」
#274 「YAGNI 原則の適用」
#275 「Component の命名戦略」
#276 「Component のディレクトリ構成」
#277 「Feature Component の設計」
#278 「Shared Component の設計」
#279 「UI Component Library の構築」
#280 「Component 設計のベストプラクティス」

---

## 第10章：実践Component実装（#281-300）- 実用的なコンポーネント集

#281 「Button Component - ボタンの実装」
#282 「Input Component - 入力フィールド」
#283 「Textarea Component - テキストエリア」
#284 「Select Component - セレクトボックス」
#285 「Checkbox Component - チェックボックス」
#286 「Radio Component - ラジオボタン」
#287 「Toggle Component - トグルスイッチ」
#288 「Card Component - カードUI」
#289 「Modal Component - モーダルダイアログ」
#290 「Drawer Component - サイドドロワー」
#291 「Dropdown Component - ドロップダウン」
#292 「Tooltip Component - ツールチップ」
#293 「Toast Component - トースト通知」
#294 「Loading Component - ローディング表示」
#295 「Spinner Component - スピナー」
#296 「Progress Component - プログレスバー」
#297 「Avatar Component - アバター表示」
#298 「Badge Component - バッジ」
#299 「Tab Component - タブシステム」
#300 「Component 総まとめと実践プロジェクト」

---

## 補足情報

- 各動画：30秒（28-32秒）
- 対象：Angular開発者、TypeScript経験者
- Angular Version：v20対応
- キャラクター：四国めたん（講師）、ずんだもん（開発者）
- 成果物：台本（ゆっくりムービーメーカー用）+ レスポンシブHTML一枚絵

---

## 学習推奨順序

1. 第1章（#001-030）：Component基礎 - 最優先
2. 第2章（#031-060）：Template構文基礎 - 必須
3. 第3章（#061-090）：Lifecycle Hooks - 重要
4. 第4章（#091-130）：Component通信 - 実務必須
5. 第6章（#161-190）：Component Styling - UI実装
6. 第7章（#191-220）：Content Projection - 再利用性
7. 第5章（#131-160）：ViewChild & ContentChild - 深掘り
8. 第9章（#251-280）：設計パターン - アーキテクチャ
9. 第8章（#221-250）：Dynamic Components - 高度な実装
10. 第10章（#281-300）：実践実装 - 総仕上げ

---

## 関連シリーズ

- **Angular Signals 300本**（作成済み）
- Angular Routing 300本（次回作成候補）
- Angular Forms 300本（次回作成候補）
- Angular HTTP & API 300本（次回作成候補）