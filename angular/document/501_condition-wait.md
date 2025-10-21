# #501 「条件が真になるまで待機」

## 概要
条件が真になるまで待機するDeferディレクティブは、初期状態で表示せず、条件が満たされたらビューを生成する。非同期状態にも対応できるよう設計する。

## 学習目標
- 条件が真になるまで待つロジックを理解する
- boolean/Promise/Observableに対応する方法を学ぶ
- 条件変化時の再評価を把握する

## 技術ポイント
- booleanなら即判定、Promise/Observableなら非同期で完了を待つ
- 条件がfalseに戻る場合にどう処理するか設計
- `takeUntilDestroyed`で購読解除

## 📺 画面表示用コード（動画用）
```html
<section *appDefer="isLoaded">コンテンツ</section>
```

## 💻 詳細実装例（学習用）
```typescript
@Input('appDefer') condition!: boolean | Promise<unknown> | Observable<unknown>;
@Input('appDeferKeep') keepView = true;

// conditionがfalseに戻った際 clear するか keepView で制御
```

## ベストプラクティス
- keepViewなどのInputで条件がfalseに戻ったときの挙動を指定
- Promise/Observableのエラーハンドリングを実装
- 読み込み中の状態も一緒に扱えるようLoadingテンプレートを検討

## 注意点
- Promiseが複数回設定される場合の競合を防ぐ
- Observableを無限ストリームにすると表示タイミングが決まらないため注意
- SSRでは初期条件がfalseの場合にレンダーされない点に留意

## 関連技術
- DeferDirective
- Observable処理
- Loadingコンポーネント
