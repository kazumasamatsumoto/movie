# #029 「Component のフォルダ構成戦略」

## 概要
大規模プロジェクトに適したフォルダ構成戦略を学びます。

## 学習目標
- Feature-based構成を理解する
- Layer-based構成を理解する
- プロジェクトに適した戦略を選択できる

## 技術ポイント
- **Feature-based**: 機能ごとに分割
- **Layer-based**: 役割ごとに分割
- **Hybrid**: 両方の組み合わせ

## 📺 画面表示用コード（動画用）

```bash
# Feature-based（推奨）
src/app/
├── features/
│   ├── user/
│   ├── product/
│   └── order/
└── shared/
```

```bash
# Layer-based
src/app/
├── components/
├── services/
├── pipes/
└── directives/
```

```bash
# Hybrid（大規模向け）
src/app/
├── features/
│   └── user/
│       ├── components/
│       ├── services/
│       └── models/
└── shared/
```

## 戦略の選択基準

- **小規模**: Feature-based
- **中規模**: Hybrid
- **大規模**: Feature-based + モジュール分割

## 注意点

- 一貫性を保つ
- チームで合意
- 柔軟に見直し

## 関連技術
- Project Structure
- Folder Organization
- Scalability
- Team Collaboration
