# #026 「Component のバージョン管理」

## 概要
Gitを使用したComponentのバージョン管理手法を学びます。

## 学習目標
- Gitでの効果的な管理方法を理解する
- コミットメッセージの書き方を習得する
- CHANGELOGの作成方法を学ぶ

## 技術ポイント
- **Git**: バージョン管理システム
- **Commit**: 変更の記録
- **CHANGELOG**: 変更履歴の文書化

## 📺 画面表示用コード（動画用）

```bash
# 機能単位でコミット
git add user.component.ts
git commit -m "feat: add user profile component"
```

```bash
# Conventional Commits
git commit -m "fix: resolve input validation bug"
git commit -m "refactor: split large component"
```

```markdown
# CHANGELOG.md
## [2.0.0] - 2025-01-15
### Breaking Changes
- UserComponent APIを変更

### Added
- 新しいプロパティを追加
```

## コミットメッセージ規約

- feat: 新機能
- fix: バグ修正
- refactor: リファクタリング
- docs: ドキュメント
- test: テスト追加

## 注意点

- 小さく頻繁にコミット
- 明確なメッセージ
- 破壊的変更は明記

## 関連技術
- Git
- Semantic Versioning
- Conventional Commits
- CHANGELOG
