# #585 「デバッグ用途」

## 概要
JsonPipeは主にデバッグ用途で使われ、テンプレート内でオブジェクトの内容を確認したいときに活用する。ログやコンソール代わりになる。

## 学習目標
- JsonPipeをデバッグ支援として利用する方法を理解する
- プロダクションでの取り扱い注意点を学ぶ
- 開発フラグなどで表示を制御するベストプラクティスを把握する

## 技術ポイント
- `*ngIf="isDebug"`などで表示制御
- `json`Pipeは純粋Pipeで参照変更時のみ更新
- 巨大オブジェクトは過剰な表示負荷になる

## 📺 画面表示用コード（動画用）
```html
<pre *ngIf="isDebug">{{ state | json }}</pre>
```

## 💻 詳細実装例（学習用）
```html
<ng-container *ngIf="isDebug">
  <h3>Debug State</h3>
  <pre>{{ storeSnapshot | json }}</pre>
</ng-container>
```

## ベストプラクティス
- debugフラグや`environment.production`で制御し、開発時のみ表示
- 重要情報が含まれないようログレベルを分ける
- ログ用コンポーネントに包み、開発者ツールとして運用

## 注意点
- プロダクションに残すと情報漏洩やパフォーマンス低下の恐れ
- ネストが深いオブジェクトは可視性が悪い
- Pipeの評価が頻繁に走ると負荷が高くなるため`async``slice`等で制御

## 関連技術
- 環境設定（environment.ts）
- Loggerサービス
- Angular DevTools
