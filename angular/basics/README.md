# Angular基礎知識シリーズ

## 目的
Angularでよくある開発課題に対して、「そもそもどうやるの？」という基礎知識を解説するショート動画シリーズです。比較シリーズ（comparison/）を見る前の前提知識として位置づけられます。

## ディレクトリ構成
- `angular/basics/daihon/` … 会話台本（四国めたん×ずんだもん）
- `angular/basics/basics-app/` … 実際に動くAngularアプリケーション
- `angular/basics/README.md` … この引き継ぎメモ

## 動画制作の流れ
1. **台本を作成** (`daihon/101_ngoninit-api.txt`)
2. **実際に動くコードを実装** (`basics-app/src/app/hero-list/`)
3. **台本を読みながら、VS Codeでコードを見せて、ブラウザで動作を確認**

## カテゴリ構成

### 1️⃣ データ取得・通信（101-106）
「サーバーからデータを取得して画面に表示したい」

- 101: ngOnInitでのAPI呼び出し基礎
- 102: Route Resolverの仕組み
- 103: HttpClientの設定方法
- 104: CSRとは？
- 105: SSRとは？
- 106: Hydrationとは？

### 2️⃣ フォーム処理（201-202）
「ユーザーの入力を受け付けてバリデーションしたい」

- 201: Template-driven Formsの基礎
- 202: Reactive Formsの基礎

### 3️⃣ 状態管理（301-306）
「複数コンポーネントで共有するデータを管理したい」

- 301: Signalsの基礎
- 302: RxJSの基礎
- 303: NgRx Storeの基礎
- 304: Signals Storeの基礎
- 305: ComponentStoreの基礎
- 306: toSignalとtoObservableの使い方

### 4️⃣ UI表示・レンダリング（401-406）
「リストを表示したら動作が重い」

- 401: *ngIfと*ngForの基礎
- 402: Control Flow構文の基礎
- 403: ChangeDetection戦略
- 404: Zone.jsの仕組み
- 405: trackByの役割
- 406: 画像最適化

### 5️⃣ コンポーネント間通信（501-504）
「親から子へデータを渡したい」

- 501: @Inputの基礎
- 502: SignalInputの基礎
- 503: @Outputの基礎
- 504: SignalOutputの基礎

### 6️⃣ スタイリング・アニメーション（601-606）
「見た目を整えたい」

- 601: Component Stylesの基礎
- 602: Global Stylesの使い方
- 603: Angular Materialの導入
- 604: Tailwind CSSの導入
- 605: CSSアニメーションの基礎
- 606: Angular Animationsの基礎

### 7️⃣ ルーティング・ナビゲーション（701-705）
「画面遷移を実装したい」

- 701: Routesの定義方法
- 702: RouterModuleとprovideRouter
- 703: Lazy Loadingの仕組み
- 704: Route Guardの基礎
- 705: Preloadingの仕組み

### 8️⃣ DOM操作・テンプレート（801-804）
「input要素にフォーカスを当てたい」

- 801: Template参照変数の使い方
- 802: ViewChildの使い方
- 803: ng-contentの基礎
- 804: TemplateRefとLayoutコンポーネント

### 9️⃣ アプリ構成・DI（901-904）
「プロジェクトをどう構成すればいい？」

- 901: NgModuleの基礎
- 902: Standalone Componentの基礎
- 903: Dependency Injectionの仕組み
- 904: constructorとinject()関数

### 🔟 開発環境・品質管理（1001-1008）
「ビルドが遅い。テストを速くしたい」

- 1001: Karmaテストランナーの基礎
- 1002: Jest/Vitestの導入
- 1003: Webpackビルダーの仕組み
- 1004: Esbuildビルダーの導入
- 1005: Angular CLI基礎
- 1006: Nx Workspaceの導入
- 1007: ESLintの設定
- 1008: Angular ESLintでTemplate Linting

## 制作時の注意
- 台本は自然な会話を心がける（テンプレ感を出さない）
- コード全体を見せてから、部分的に説明する
- 実際に動く様子をブラウザで確認できるようにする

## 比較シリーズ（comparison/）との関係
基礎シリーズで個別技術を学んだ後、比較シリーズで使い分けを学ぶ流れです。

例：
- 基礎101（ngOnInit） + 基礎102（Resolver） → 比較409（ngOnInit vs Resolver）
- 基礎301（Signals） + 基礎302（RxJS） → 比較401（Signals vs RxJS）
