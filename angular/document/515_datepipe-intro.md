# #515 「DatePipe - 日付フォーマット」

## 概要
DatePipeは日付をロケールに応じた形式で文字列へ変換するPipeで、テンプレート内で簡単にフォーマットを切り替えられる。

## 学習目標
- DatePipeの基本的な使い方を理解する
- フォーマット文字列やプリセットの活用方法を学ぶ
- タイムゾーンとロケール指定による表示制御を把握する

## 技術ポイント
- `{{ dateValue | date:'yyyy/MM/dd' }}`
- プリセット `'short'`, `'medium'`, `'long'`, `'full'`
- 第三引数でタイムゾーン、第四引数でロケール指定

## 📺 画面表示用コード（動画用）
```html
<p>{{ birthday | date:'yyyy/MM/dd' }}</p>
```

## 💻 詳細実装例（学習用）
```html
<p>標準: {{ today | date }}</p>
<p>ISO風: {{ today | date:'yyyy-MM-dd HH:mm' }}</p>
<p>プリセット: {{ today | date:'full' }}</p>
<p>UTC: {{ today | date:'yyyy/MM/dd HH:mm':'UTC' }}</p>
<p>ロケール指定: {{ today | date:'longDate':'':'fr-FR' }}</p>
```

## ベストプラクティス
- 表示形式はプリセットから選び、必要な場合のみカスタムフォーマットを使用
- タイムゾーンやロケールを明示的に指定し、国際化へ対応
- 事前に`registerLocaleData`を呼んで対象ロケールを登録

## 注意点
- Angularでは`Date`やISO文字列のみを正しく扱えるよう注意
- Timezone指定がない場合はブラウザのローカルタイムゾーン
- 旧ブラウザではIntl APIが必要な場合がある

## 関連技術
- LOCALE_ID
- registerLocaleData
- Moment.js/Day.jsとの比較
