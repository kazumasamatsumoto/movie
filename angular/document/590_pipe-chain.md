# #590 「Pipe チェーン - 複数パイプの連結」

## 概要
Pipeチェーンはテンプレートで複数のPipeを順番に適用して値を加工する手法で、`{{ value | pipeA | pipeB }}`のように連結して使う。

## 学習目標
- Pipeチェーンの構文と動作を理解する
- 変換順序が結果に与える影響を把握する
- 可読性とパフォーマンスを考慮したPipe連結を学ぶ

## 技術ポイント
- `value | pipeA | pipeB` → pipeAの出力がpipeBの入力
- 各Pipeは純粋関数として再利用
- 複雑なチェーンはカスタムPipeでまとめることも検討

## 📺 画面表示用コード（動画用）
```html
<p>{{ userName$ | async | titlecase }}</p>
<span>{{ order.date | date:'yyyy-MM-dd' | uppercase }}</span>
```

## 💻 詳細実装例（学習用）
```html
<p>
  {{ (user$ | async)?.email | lowercase }}
</p>
```

## ベストプラクティス
- 可読性を保つためチェーンは必要最小限に
- `async`→整形Pipe→文字列加工の順で組み合わせると自然
- 同じPipeの繰り返しよりカスタムPipeでまとめることも検討

## 注意点
- Pipeチェーンは順序に敏感（dateの後にuppercaseなど意味のある順に）
- null安全に注意し、`?.`や`*ngIf`を組み合わせる
- 重いPipeを連結するとパフォーマンスに影響

## 関連技術
- AsyncPipe
- Built-in Pipes
- カスタムPipe
