# #028 「Component のコメント規約」

## 概要
統一されたコメント規約により、コードの可読性と保守性が向上します。

## 学習目標
- JSDocスタイルのコメントを習得する
- 適切なコメント位置を理解する
- コメントタグの使い方を学ぶ

## 技術ポイント
- **JSDoc**: 標準的なコメント形式
- **タグ**: @param、@returns等
- **位置**: クラス・メソッドの直前

## 📺 画面表示用コード（動画用）

```typescript
/**
 * ユーザー管理Component
 * @description ユーザー一覧の表示と編集機能を提供
 */
@Component({
  selector: 'app-user-manager'
})
export class UserManagerComponent {
  /**
   * 表示するユーザー一覧
   * @type {User[]}
   */
  @Input() users: User[] = [];

  /**
   * ユーザーを削除する
   * @param id - ユーザーID
   * @returns 削除成功時true
   */
  deleteUser(id: number): boolean {
    // 実装
    return true;
  }
}
```

```typescript
/**
 * データを処理する
 * @param data - 入力データ
 * @returns 処理済みデータ
 * @example
 * const result = processData({ name: 'John' });
 */
processData(data: any): any {
  return data;
}
```

## コメントタグ一覧

- @param - パラメータ説明
- @returns - 戻り値説明
- @example - 使用例
- @description - 詳細説明
- @deprecated - 非推奨マーク

## 注意点

- 自明なコードにはコメント不要
- WHYを書く（WHATではなく）
- 定期的に更新

## 関連技術
- JSDoc
- TSDoc
- Code Documentation
- Best Practices
