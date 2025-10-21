
# #542 「ng generate pipe コマンド」

## 概要
`ng generate pipe`コマンドでカスタムPipeの雛形を生成でき、Standalone指定でモジュールレスに利用可能なPipeを即座に作成できる。

## 学習目標
- CLIコマンドでPipeを生成する手順を理解する
- 生成されるファイル構成と内容を把握する
- StandalonePipeとして利用する設定を学ぶ

## 技術ポイント
- `ng g pipe shared/truncate --standalone`
- デフォルトでPipeクラスとspecファイルが生成
- `standalone: true`でNgModule登録不要

## 📺 画面表示用コード（動画用）
```bash
ng g pipe pipes/filter --standalone
```

## 💻 詳細実装例（学習用）
```bash
# CLI例
ng g pipe shared/truncate --standalone

# 生成ファイル
src/app/shared/truncate.pipe.ts
src/app/shared/truncate.pipe.spec.ts
```

## ベストプラクティス
- Standalone構成を基本にし、コンポーネント側のimportsへ追加するだけで利用
- 生成直後にnameやファイル名をプロジェクト規約に合わせる
- specファイルを活用してロジックをテスト

## 注意点
- CLIバージョンによってオプションが異なる場合がある
- Standaloneでない場合は使用するモジュールへ登録が必要
- 雛形はシンプルなtransformのみのため引数や型注釈を追加する

## 関連技術
- Angular CLI
- Standalone API
- PipeTransform
