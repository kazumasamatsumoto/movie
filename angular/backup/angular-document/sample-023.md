# #023 「Component の削除方法」

## 概要
不要なComponentを安全に削除する手順を学びます。

## 学習目標
- Componentの安全な削除手順を理解する
- 使用箇所の確認方法を習得する
- 削除後の確認ポイントを把握する

## 技術ポイント
- **検索**: 使用箇所の特定
- **imports削除**: 依存関係の解消
- **ビルド確認**: エラーチェック

## 📺 画面表示用コード（動画用）

```bash
# 1. 使用箇所を検索（VSCode）
Ctrl+Shift+F で "UserComponent" を検索
```

```typescript
// 2. importsから削除
@Component({
  imports: [
    // UserComponent,  // 削除
    OtherComponent
  ]
})
```

```bash
# 3. ファイル削除
rm -rf user-component/
# または手動でフォルダ削除
```

## 削除チェックリスト

1. ✅ Component名で全検索
2. ✅ importsから削除
3. ✅ ルーティング設定確認
4. ✅ テストファイル削除
5. ✅ ビルド確認（ng build）

## 注意点

- 必ず使用箇所を確認してから削除
- Gitでコミット前にバックアップ
- ビルドエラーが出ないか確認

## 関連技術
- File Management
- Dependency Management
- Code Search
- Version Control
