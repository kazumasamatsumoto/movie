# #604 「Template-driven vs Reactive 比較」

## 概要
テンプレート駆動フォームとリアクティブフォームは構築方法やテスト性が異なり、プロジェクトの性質に応じた選択が必要になる。

## 学習目標
- 2つのアプローチの比較ポイントを整理する
- チーム構成とフォーム規模による選択基準を知る
- 移行時の考慮事項を把握する

## 技術ポイント
- テンプレート駆動は双方向バインディング主体
- リアクティブは明示的なFormGroupとObservableベース
- テスト・再利用・型安全性でリアクティブが優位

## 📺 画面表示用コード（動画用）
```text
Template-driven: HTML中心 / 小規模向け
Reactive: TypeScript中心 / 大規模向け
```

## 💻 詳細実装例（学習用）
```typescript
type FormStrategy = 'template' | 'reactive';

function chooseStrategy(options: { teamPrefersTs: boolean; fields: number }): FormStrategy {
  if (options.teamPrefersTs || options.fields > 10) {
    return 'reactive';
  }
  return 'template';
}
```

## ベストプラクティス
- プロジェクト開始時にフォーム方針を決定し共有する
- 移行計画を立てて段階的にリアクティブへ移す
- 必要に応じてハイブリッド構成も検討する

## 注意点
- 途中でアプローチを混在させるとメンテナンスが難しい
- チームメンバーがメリットを理解していないと反発が起こる
- 既存テンプレートをそのままリアクティブ化すると工数が膨らむ

## 関連技術
- 設計ガイドライン
- チーム開発プロセス
- フォームモジュール選定
