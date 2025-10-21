# #636 「フォームの階層構造」

## 概要
テンプレート駆動フォームでもngModelGroupを使って階層構造を構築でき、親子関係を意識した設計が状態管理とバリデーション設計を助ける。

## 学習目標
- フォーム階層の設計ポイントを理解する
- 親子グループの状態伝播を把握する
- 設計段階でのデータ構造とUIの整合性を確認する

## 技術ポイント
- 親FormGroupのvalidは子グループの状態に依存
- ngModelGroupをネストして複雑なフォームを分割
- 階層構造はform.valueにもそのまま反映される

## 📺 画面表示用コード（動画用）
```html
<form #profileForm="ngForm">
  <section ngModelGroup="account">
    <input name="email" ngModel />
    <input name="password" ngModel />
  </section>
</form>
```

## 💻 詳細実装例（学習用）
```typescript
protected logHierarchy(form: NgForm): void {
    console.log(form.value.account?.email);
    console.log(form.controls['account']?.valid);
}
```

## ベストプラクティス
- UIセクションとフォーム階層を一致させて迷わないようにする
- 親子のvalid/invalidを確認できるようテンプレート参照を用意する
- データモデルと階層を一致させて変換コストを減らす

## 注意点
- 過度なネストはパフォーマンスを悪化させる
- 階層変更時はform.valueの扱いも更新する
- CSSとDOM構造だけでなくフォーム階層も同期する必要がある

## 関連技術
- ngModelGroup
- テンプレート駆動フォーム
- フォーム設計
