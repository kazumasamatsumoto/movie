# #605 「どちらを選ぶべきか？使い分け」

## 概要
フォームアプローチの選択はフォーム規模、バリデーションの複雑さ、チームスキルなど複数要素を考慮して決める必要がある。

## 学習目標
- 選定基準となる観点を列挙できるようにする
- プロトタイプから本番への移行戦略を理解する
- チーム合意形成のポイントを押さえる

## 技術ポイント
- 小規模・簡易検証はテンプレート駆動が迅速
- 大規模・厳格なバリデーションはリアクティブが安定
- フォーム方針は設計ドキュメントで共有する

## 📺 画面表示用コード（動画用）
```text
項目数 <= 5 && 単純検証 -> Template
複雑ビジネスルール or 再利用 -> Reactive
```

## 💻 詳細実装例（学習用）
```typescript
interface FormDecisionInput {
  fieldCount: number;
  requiresAsyncValidation: boolean;
  teamPrefersTs: boolean;
}

function decideApproach(input: FormDecisionInput): 'template' | 'reactive' {
  if (input.fieldCount > 8 || input.requiresAsyncValidation || input.teamPrefersTs) {
    return 'reactive';
  }
  return 'template';
}
```

## ベストプラクティス
- 選定理由をチームで文書化し新メンバーに共有する
- 段階的な移行プランを準備してリスクを減らす
- UI/UX観点で必要な状態表示を洗い出す

## 注意点
- 判断材料を可視化しないと主観的な選択になりがち
- 一度決めた方針は安易に変えないよう合意形成する
- 実装途中で切り替える場合の工数を見積もっておく

## 関連技術
- アーキテクチャ設計
- デザインレビュー
- チームガイドライン
