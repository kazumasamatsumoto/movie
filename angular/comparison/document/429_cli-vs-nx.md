# #429 「Angular CLI単体 vs Nx Workspace あなたはどっち派？」

## 概要
Angular CLI単体は軽量で標準。Nxはモノレポ機能とタスク実行管理が強み。プロジェクト規模に応じて選定する。

## 学習目標
- Angular CLI単体の構成と得意なシナリオを整理する
- Nx Workspaceの採用メリットを理解する
- プロジェクト条件に応じた使い分け基準を決める

## 技術ポイント
- Angular CLI単体を成り立たせる主要API/構成要素
- Nx Workspaceで押さえる設定やコード記述
- 両者を共存・移行させるためのブリッジ手法

## 📺 画面表示用コード（動画用）
**CLI派：package.jsonで制御**
```typescript
{
  "scripts": {
    "start": "ng serve",
    "test": "ng test"
  }
}
```

**Nx派：project.jsonとタスクランナー**
```typescript
{
  "name": "app",
  "targets": {
    "serve": { "executor": "@nx/angular:dev-server" }
  }
}
```

## 💻 詳細実装例（学習用）
```typescript
npx create-nx-workspace@latest myorg --preset=angular-monorepo
nx graph
```

## ベストプラクティス
- CLI運用でも`ng generate library`でコード共有を進め、いつでもNxに移行できるようにする
- Nx導入時はタスクキャッシュの保存先をCIと共有し、効果を最大化する
- モノレポのコードオーナーやlintルールをNxの`project.json`で明示する

## 注意点
- Nxは設定ファイルが増えるため学習コストを見積もる
- CLIとNxのコマンドを混在させるとスクリプトが複雑になるのでラッパーを提供する
- モノレポでも依存境界が守られなければスケールしないのでタグベースlintを設定する

## 関連技術
- Angular CLI
- Nx Workspace
- Monorepo戦略
