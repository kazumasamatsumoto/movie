# #520 「タイムゾーンの指定」

## 概要
DatePipeの第三引数にタイムゾーンを指定すると、表示を特定のタイムゾーンへ変換できる。UTCやオフセット、IANAタイムゾーンを利用可能。

## 学習目標
- タイムゾーン指定の書式を理解する
- `UTC`、`'GMT+0900'`などの指定方法を学ぶ
- ユーザーのローカルタイムとの違いを理解する

## 技術ポイント
- `date:'yyyy/MM/dd HH:mm':'UTC'`
- `date:'short':'Asia/Tokyo'`
- タイムゾーン指定がない場合はローカルタイムゾーン

## 📺 画面表示用コード（動画用）
```html
<p>{{ today | date:'yyyy/MM/dd HH:mm':'UTC' }}</p>
```

## 💻 詳細実装例（学習用）
```html
<p>ローカル: {{ meeting | date:'yyyy/MM/dd HH:mm' }}</p>
<p>東京: {{ meeting | date:'yyyy/MM/dd HH:mm':'Asia/Tokyo' }}</p>
<p>UTC: {{ meeting | date:'yyyy/MM/dd HH:mm':'UTC' }}</p>
```

## ベストプラクティス
- サーバー時間とクライアント表示の差を吸収するためタイムゾーンを明示
- 国際ユーザー向けにユーザー選択のタイムゾーンを適用
- ログや監査用途ではUTC表記を標準にすることが多い

## 注意点
- タイムゾーン指定に対応していないブラウザが存在する可能性
- IANAタイムゾーン名を使う場合はブラウザのIntl実装に依存
- SSRではサーバー側のタイムゾーン設定を確認

## 関連技術
- Intl API
- Moment/Day.jsのtzサポート
- Angular LOCALE設定
