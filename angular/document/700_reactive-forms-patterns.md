# #700 「Reactive Forms の基本パターン」

## 概要
Reactive Formsの基本パターンはFormBuilderでフォームを生成し、valueChanges/statusChangesで副作用を処理し、DTO変換やAPI呼び出しをサービスに委譲することでテスト性を高める。

## 学習目標
- Reactive Formsにおける典型パターンを理解する
- 責務分離によるテスト性向上を学ぶ
- フォーム生成・バリデーション・副作用の整理を把握する

## 技術ポイント
- FormBuilderでフォーム生成を統一する
- valueChanges/statusChangesでリアクティブ処理を組み込む
- DTO整形はサービスやユーティリティに委譲する

## 📺 画面表示用コード（動画用）
```typescript
protected readonly fb = inject(FormBuilder);
protected profileForm = this.fb.group({
  name: ['', Validators.required],
  email: ['', Validators.email],
  phones: this.fb.array([this.fb.control('')])
});
```

## 💻 詳細実装例（学習用）
```markdown
- フォーム生成: FormBuilderファクトリでまとめる
- 副作用: valueChanges/statusChangesでObservable連鎖
- 送信: DTO整形 → APIサービス → 成功時 reset
```

## ベストプラクティス
- フォーム生成ロジックをfactory関数として切り出す
- 副作用処理はサービスに委譲してテスト性を高める
- DTO整形とAPI呼び出しを分離して責務を明確化する

## 注意点
- フォームが巨大化したら機能ごとに分割する
- 購読解除を怠ると副作用が蓄積する
- サービス層との依存関係を整理して循環参照を避ける

## 関連技術
- FormBuilder
- valueChanges
- ベストプラクティス
