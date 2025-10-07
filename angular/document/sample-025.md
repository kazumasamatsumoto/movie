# #025 「Component の複製と再利用」

## 概要
既存Componentを複製して新しいComponentを効率的に作成する方法を学びます。

## 学習目標
- Component複製の手順を理解する
- 共通化のポイントを把握する
- 効率的な開発方法を習得する

## 技術ポイント
- **ファイル複製**: コピー&カスタマイズ
- **共通化**: 親Componentやサービスへの抽出
- **テンプレート化**: 汎用的な設計

## 📺 画面表示用コード（動画用）

```bash
# ファイルを複製
cp -r user-card/ product-card/
```

```typescript
// クラス名とselectorを変更
// Before: UserCardComponent
// After: ProductCardComponent
@Component({
  selector: 'app-product-card',  // 変更
  template: `...`
})
export class ProductCardComponent {}  // 変更
```

```typescript
// 共通ロジックを親に抽出
export abstract class BaseCardComponent {
  abstract getData(): any;
}

export class ProductCardComponent extends BaseCardComponent {
  getData() { /* ... */ }
}
```

## ベストプラクティス

1. **テンプレート化**: 汎用的な設計
2. **共通部分の抽出**: DRY原則
3. **適切な命名**: 明確な名前

## 注意点

- コピペではなく共通化を検討
- 独立性を保つ
- 過度な複製は避ける

## 関連技術
- Code Reuse
- Inheritance
- Composition
- Template Pattern
