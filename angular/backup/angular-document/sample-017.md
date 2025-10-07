# #017 「Component のディレクトリ構成」

## 概要
適切なディレクトリ構成により、Componentの管理と保守が容易になります。機能別、用途別に整理することが重要です。

## 学習目標
- 効果的なディレクトリ構成を理解する
- features、shared、layoutの使い分けを学ぶ
- スケーラブルな構造を設計する

## 技術ポイント
- **機能別分割**: features ディレクトリ
- **共通Component**: shared ディレクトリ
- **レイアウト**: layout ディレクトリ

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```bash
# 推奨ディレクトリ構成
src/app/
├── features/      # 機能別Component
├── shared/        # 共通Component
└── layout/        # レイアウトComponent
```

```bash
# features の詳細
features/
├── user/
│   ├── user-list/
│   ├── user-detail/
│   └── user-form/
└── product/
    ├── product-list/
    └── product-detail/
```

```bash
# shared の詳細
shared/
├── components/
│   ├── button/
│   ├── card/
│   └── modal/
├── pipes/
└── directives/
```

## 💻 詳細実装例（学習用）

### 完全なディレクトリ構造
```bash
src/app/
├── core/                    # シングルトンサービス
│   ├── services/
│   │   ├── auth.service.ts
│   │   └── api.service.ts
│   └── guards/
│       └── auth.guard.ts
│
├── features/                # 機能別Component
│   ├── user/
│   │   ├── user-list/
│   │   │   ├── user-list.component.ts
│   │   │   ├── user-list.component.html
│   │   │   └── user-list.component.css
│   │   ├── user-detail/
│   │   └── user-form/
│   ├── product/
│   └── order/
│
├── shared/                  # 共通Component
│   ├── components/
│   │   ├── button/
│   │   ├── card/
│   │   ├── modal/
│   │   └── table/
│   ├── pipes/
│   │   └── date-format.pipe.ts
│   └── directives/
│       └── highlight.directive.ts
│
└── layout/                  # レイアウトComponent
    ├── header/
    ├── footer/
    ├── sidebar/
    └── page-layout/
```

## ベストプラクティス

1. **機能ごとに分離**: features で独立管理
2. **共通化**: shared で再利用促進
3. **レイアウト分離**: layout で構造管理
4. **スケーラビリティ**: 拡張しやすい構造

## 注意点

- 深すぎるネストは避ける
- 命名規則の統一
- index.ts で export を整理
- 循環参照に注意

## 関連技術
- Project Structure
- Module Organization
- File Management
- Scalability
