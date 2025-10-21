# #519 「'short' / 'medium' / 'long' / 'full'」

## 概要
DatePipeには`'short'`, `'medium'`, `'long'`, `'full'`といったプリセットがあり、ロケールに合わせた一般的な日付・時刻形式を簡単に利用できる。

## 学習目標
- プリセットフォーマットの内容を理解する
- プリセットとカスタムフォーマットの使い分けを学ぶ
- ロケール依存で表示が変わることを把握する

## 技術ポイント
- `date:'short'` → 短い日付と時間（例: 1/1/24, 5:00 PM）
- `date:'medium'` → 中程度の情報
- `date:'long'`, `date:'full'` → 詳細で長い表記、曜日やタイムゾーン含む

## 📺 画面表示用コード（動画用）
```html
<p>{{ today | date:'short' }}</p>
<p>{{ today | date:'full' }}</p>
```

## 💻 詳細実装例（学習用）
```html
<ul>
  <li>Short: {{ today | date:'short' }}</li>
  <li>Medium: {{ today | date:'medium' }}</li>
  <li>Long: {{ today | date:'long' }}</li>
  <li>Full: {{ today | date:'full' }}</li>
```

## ベストプラクティス
- プリセットはロケール対応しているため多言語アプリで便利
- 詳細な形式が不要な場合はプリセットで十分
- カスタム形式が必要な場合のみフォーマット文字列を指定

## 注意点
- プリセットの表示はロケールによって異なるためテスト環境と本番が異なる可能性
- タイムゾーンを指定しない場合はローカルタイム
- プリセットを基に微調整したい場合はカスタムフォーマットへ切り替える

## 関連技術
- LOCALE_ID
- DatePipeフォーマット文字列
- Internationalization
