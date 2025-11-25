# Angular比較シリーズ 引き継ぎメモ

## 目的
Signals導入前後など「A派 vs B派」を比較するショート動画（約1分）の台本とドキュメントを量産する仕組みを整えています。TypeScriptシリーズ同様にテンプレート＋スクリプトで一括生成する運用です。

## ディレクトリ構成
- `angular/comparison/generate_assets.py` … 台本/ドキュメントをまとめて生成
- `angular/comparison/daihon/` … 生成された会話台本（四国めたん×ずんだもん）
- `angular/comparison/document/` … 詳細ドキュメント（概要・学習目標・コード等）
- `angular/comparison/README.md` … この引き継ぎメモ

## 追加作業の流れ
1. `angular/comparison/generate_assets.py` の `ENTRIES` リストに `Entry` を追記する  
   - `number`: 3桁で連番（401-430を使用済み。次は431）  
   - `slug`: ファイル名に使う英小文字＋ハイフン  
   - 会話テキストやコード例、ベストプラクティス等を埋める  
2. 生成実行  
   ```bash
   cd /Users/kazu/coding/movie-zunda/angular/comparison
   python3 generate_assets.py
   ```  
   既存ファイルは `Entry` の内容で上書きされます。  
3. 必要なら `angular/index.md` 等にタイトルを追記し、管理表を更新する

## 編集時の注意
- 台本／ドキュメントはテンプレートで再生成されるため、手動修正を残す場合は `generate_assets.py` も同じ内容に更新してから生成してください。
- 画面表示用コードは **最大3個・各10行以内** のテンプレ規約を守ります。
- 1分尺を想定しているため、会話は導入→A案→B案→まとめの流れで約8行に収めます。
- `ENTRIES` に追加した後は `git status` で差分を確認し、必要なファイルのみコミットしてください。

## よくあるタスク
- 新テーマの比較ネタ作成 → `Entry` 追加、スクリプト実行
- 既存テーマの調整 → `Entry` 該当箇所を修正し再生成
- バッチ生成確認 → `python3 generate_assets.py` 実行後に `angular/comparison/daihon/*.txt` などをチェック

このREADMEを参照すればCodexセッションを再開せずとも作業を続けられます。***
