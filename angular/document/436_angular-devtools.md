# #436 「Angular DevTools での確認」

## 概要
Angular DevToolsはブラウザ拡張で、コンポーネント・ディレクティブ階層や状態を可視化でき、ディレクティブが正しく適用されているか確認できる。

## 学習目標
- Angular DevToolsの基本操作を理解する
- Directiveの状態やHostBindingの値を確認する方法を学ぶ
- パフォーマンスプロファイルを利用する手順を把握する

## 技術ポイント
- Elementsタブでディレクティブ一覧とInput/Outputを確認
- ProfilerタブでChange Detectionコストを可視化
- Signals対応で状態変化を追跡

## 📺 画面表示用コード（動画用）
```text
Angular DevTools → Elements → Directives
```

## 💻 詳細実装例（学習用）
```text
1. Chrome拡張 Angular DevTools をインストール
2. アプリを開き DevTools → Angular → Elements
3. 要素を選択し、適用されたDirectiveとHostBindingを確認
```

## ベストプラクティス
- デバッグ時はDevToolsでInput/Outputの現在値を確認し、想定外の変化を早期発見
- Profilerでレンダリング頻度をチェックし、パフォーマンス課題を可視化
- Signals利用時はSignalsタブで依存関係を追跡

## 注意点
- 本番ビルドではソースマップがないと追跡が困難
- SSRではブラウザ拡張が利用できないため別手段を用意
- 大規模アプリでは要素数が多く見失いやすいため命名を工夫

## 関連技術
- Chrome DevTools
- Angular Profiler
- Signalsデバッグ
