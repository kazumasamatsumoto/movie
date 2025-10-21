# #671 「FormGroup の構造定義」

## 概要
FormGroupの構造定義は取得したいオブジェクト形状を先に設計し、ドメインやAPIのDTOと合わせることで変換を最小化する。

## 学習目標
- FormGroup構造設計の考え方を理解する
- DTOとの整合性を意識する
- ネスト設計のベストプラクティスを学ぶ

## 技術ポイント
- フォーム値を先に設計してからコントロールを割り当てる
- 小さなサブFormGroupに分割すると責務が明確になる
- DTOとの差分はマッピング関数で吸収する

## 📺 画面表示用コード（動画用）
```text
FormGroup => { credentials: { email, password }, profile: { displayName } }
```

## 💻 詳細実装例（学習用）
```typescript
interface AccountForm {
  credentials: {
    email: string;
    password: string;
  };
  profile: {
    displayName: string;
  };
}

protected accountGroup = new FormGroup<AccountForm>({
  credentials: new FormGroup({
    email: new FormControl('', { nonNullable: true }),
    password: new FormControl('', { nonNullable: true })
  }),
  profile: new FormGroup({
    displayName: new FormControl('', { nonNullable: true })
  })
});
```

## ベストプラクティス
- フォームの型定義をinterfaceで用意する
- サブグループは別ファイルでファクトリ化する
- データ変換用のmapper関数を整備する

## 注意点
- ネストしすぎるとテンプレートが複雑化する
- DTOと完全一致させるとUI専用フィールドが追加しづらい
- 型定義を更新したらフォーム構造も忘れず更新する

## 関連技術
- フォーム設計
- DTO
- 型定義
