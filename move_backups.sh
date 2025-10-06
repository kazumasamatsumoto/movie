#!/bin/bash

# typescript/daihon/backups ディレクトリが存在することを確認
mkdir -p typescript/daihon/backups

# *.bak ファイルを backups ディレクトリへ移動
mv typescript/daihon/*.bak typescript/daihon/backups/

echo "バックアップファイルを typescript/daihon/backups/ へ移動しました"
