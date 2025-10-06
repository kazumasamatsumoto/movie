#!/bin/bash

# Usage: ./extract_codes.sh <start_number> <end_number> <output_file>
# Example: ./extract_codes.sh 1 100 extracted_codes.md

if [ $# -ne 3 ]; then
    echo "Usage: $0 <start_number> <end_number> <output_file>"
    echo "Example: $0 1 100 extracted_codes.md"
    exit 1
fi

START_NUM=$1
END_NUM=$2
OUTPUT_FILE=$3

# 出力ファイルを初期化
> "$OUTPUT_FILE"

for i in $(seq -f "%03g" $START_NUM $END_NUM); do
    INPUT_FILE="typescript/daihon/${i}.txt"

    if [ ! -f "$INPUT_FILE" ]; then
        echo "Warning: $INPUT_FILE not found, skipping..."
        continue
    fi

    # 1行目を取得
    FIRST_LINE=$(head -n 1 "$INPUT_FILE")

    # ---の行番号を取得
    SEPARATOR_LINE=$(grep -n "^---$" "$INPUT_FILE" | head -n 1 | cut -d: -f1)

    if [ -z "$SEPARATOR_LINE" ]; then
        echo "Warning: No '---' separator found in $INPUT_FILE, skipping..."
        continue
    fi

    # 出力ファイルに書き込み
    echo "## File: ${i}.txt" >> "$OUTPUT_FILE"
    echo "" >> "$OUTPUT_FILE"
    echo "$FIRST_LINE" >> "$OUTPUT_FILE"
    echo "" >> "$OUTPUT_FILE"
    echo '```' >> "$OUTPUT_FILE"
    tail -n +$((SEPARATOR_LINE + 1)) "$INPUT_FILE" >> "$OUTPUT_FILE"
    echo '```' >> "$OUTPUT_FILE"
    echo "" >> "$OUTPUT_FILE"

    # 元ファイルから抽出した部分を削除（1行目と---以下を削除）
    # 2行目から---の行の前まで残す
    sed -i.bak "1d;${SEPARATOR_LINE},\$d" "$INPUT_FILE"

    echo "Processed: $INPUT_FILE"
done

echo "Extraction complete. Output saved to $OUTPUT_FILE"
