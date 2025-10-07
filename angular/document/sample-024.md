# #024 「Component のリファクタリング」

## 概要
Componentが大きくなった時のリファクタリング手法を学びます。

## 学習目標
- リファクタリングのタイミングを理解する
- Component分割の手法を習得する
- 安全なリファクタリング手順を学ぶ

## 技術ポイント
- **Extract Component**: 部品の抽出
- **責任の分離**: 単一責任の原則
- **テスト駆動**: テストを書いてからリファクタリング

## 📺 画面表示用コード（動画用）

```typescript
// Before: 大きなComponent
@Component({
  template: `
    <header>...</header>
    <form>...</form>
    <table>...</table>
  `
})
export class LargeComponent {
  // 100行以上のロジック...
}
```

```typescript
// After: 分割
@Component({
  imports: [HeaderComponent, FormComponent, TableComponent],
  template: `
    <app-header />
    <app-form />
    <app-table />
  `
})
export class SmallComponent {}
```

```typescript
// 共通ロジックをサービスに抽出
@Injectable()
export class DataService {
  processData() { /* ... */ }
}
```

## リファクタリング手順

1. テストを書く
2. 小さく分割
3. 共通化
4. テスト実行
5. コミット

## 注意点

- 一度に大きく変更しない
- テストで安全性を確保
- コミットは小さく頻繁に

## 関連技術
- Code Refactoring
- Design Patterns
- Test-Driven Development
- SOLID Principles
