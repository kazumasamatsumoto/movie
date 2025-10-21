# #521 「ロケールの設定」

## 概要
ロケールを設定するとPipeのフォーマットが地域に合わせて表示される。アプリ全体の`LOCALE_ID`を設定する方法と、Pipe呼び出し時にロケールを指定する方法がある。

## 学習目標
- Angularアプリでロケールを設定する手順を理解する
- `registerLocaleData`の利用方法を学ぶ
- Pipeごとにロケールを指定するケースを把握する

## 技術ポイント
- `import localeJa from '@angular/common/locales/ja'; registerLocaleData(localeJa);`
- `providers: [{ provide: LOCALE_ID, useValue: 'ja-JP' }]`
- DatePipeの第四引数にロケールを指定可能

## 📺 画面表示用コード（動画用）
```typescript
providers: [{ provide: LOCALE_ID, useValue: 'ja-JP' }]
```

## 💻 詳細実装例（学習用）
```typescript
import localeJa from '@angular/common/locales/ja';
registerLocaleData(localeJa);

@NgModule({
  providers: [{ provide: LOCALE_ID, useValue: 'ja-JP' }]
})
export class AppModule {}

// Pipeで直接指定
{{ price | currency:'EUR':'symbol':'1.2-2':'de-DE' }}
```

## ベストプラクティス
- 多言語対応ではユーザーの選択に応じてLOCALE_IDを切り替える
- 選択ロケールをサービスで管理し、Pipeやi18nと連携
- 単体でロケールを変えたい場合はPipe呼び出しの引数で指定

## 注意点
- `registerLocaleData`を呼ばないとロケールが読み込まれずエラーになる
- SSRではサーバー側のロケールも合わせる必要がある
- ロケール変更時にPipeの結果が変わるためテストで考慮

## 関連技術
- i18n
- CurrencyPipe/DatePipe
- LOCALE_ID, registerLocaleData
