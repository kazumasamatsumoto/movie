# #276 「Component のディレクトリ構成」

## 概要
コンポーネントのディレクトリ構成は、Feature単位やShared層などの整理されたファイル配置を通じて可読性と開発効率を高める設計ガイドである。

## 学習目標
- Feature/Shared単位のディレクトリ構成を理解する
- index.tsで公開APIを制御する方法を学ぶ
- Storybookやテストファイルの配置戦略を把握する

## 技術ポイント
- FeatureフォルダとSharedフォルダの分離
- index.tsの再エクスポート
- co-locatedなテスト/ドキュメント配置

## 📺 画面表示用コード（動画用）
```text
feature/
  invoice/
    container/
    view/
    index.ts
```

```typescript
export * from './container/invoice-container.component';
export * from './view/invoice-view.component';
```

```text
shared/
  ui/
    badge/
      badge.component.ts
      badge.component.spec.ts
```

## 💻 詳細実装例（学習用）
```markdown
- `feature/<domain>/` : 機能単位のContainer・Facadeを配置
- `shared/ui/` : 再利用可能なPresentation Component
- `shared/util/` : 非UIのユーティリティ
- `index.ts` : 公開対象のみ再エクスポート
```

## ベストプラクティス
- コンポーネントとテストを同階層に置き、変更範囲を可視化する
- index.tsで公開APIを制御し、外部からの依存を最小限にする
- Storybookやドキュメントも同フォルダに配置して同期する

## 注意点
- フォルダ階層を深くしすぎない
- 公開不要なコンポーネントをindex.tsに再エクスポートしない
- FeatureとSharedの境界が崩れないようレビューする

## 関連技術
- Barrelファイル
- ストラクチャードモノレポ
- Storybook
