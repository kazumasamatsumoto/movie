# #022 「Component のホットリロード」

## 概要
ng serveのホットリロード機能により、コード変更を即座にブラウザに反映できます。

## 学習目標
- ホットリロードの仕組みを理解する
- HMR（Hot Module Replacement）の使い方を学ぶ
- 開発効率を向上させる

## 技術ポイント
- **ホットリロード**: ファイル保存で自動更新
- **HMR**: 状態を保持したまま更新
- **ng serve**: 開発サーバーの起動

## 📺 画面表示用コード（動画用）

```bash
# 基本的なホットリロード
ng serve
# ファイル保存で自動リロード
```

```bash
# ポート指定
ng serve --port 4201
# 自動でブラウザを開く
ng serve --open
```

```bash
# HMRを有効化
ng serve --hmr
# 状態を保持したまま更新
```

## ベストプラクティス

1. **ng serveで開発**: 常時起動
2. **HMRの活用**: フォーム入力などの状態保持
3. **自動保存の設定**: エディタで自動保存を有効化

## 注意点

- ファイル監視の上限に注意（Linux）
- 大規模プロジェクトではビルド時間増加
- HMRはすべてのケースで動作するわけではない

## 関連技術
- Webpack Dev Server
- File Watching
- Live Reload
- Development Workflow
