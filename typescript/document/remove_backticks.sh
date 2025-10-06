#!/bin/bash

input_file="extracted_codes.md"
output_file="cleaned_extracted_codes.md"

# 出力ファイルを空にして初期化
> "$output_file"

# 状態管理用フラグ
skip_next=false

while IFS= read -r line; do
  if [[ "$skip_next" == true ]]; then
    # 次の行が ``` の場合はスキップ
    if [[ "$line" == '```' ]]; then
      skip_next=false
      continue
    fi
    skip_next=false
  fi

  # タイトル行か判定 (# #数字 で始まる)
  if [[ "$line" =~ ^#\ #[0-9]+ ]]; then
    echo "$line" >> "$output_file"
    skip_next=true
  else
    echo "$line" >> "$output_file"
  fi
done < "$input_file"

echo "✅ 完了しました: $output_file に出力されました。"
