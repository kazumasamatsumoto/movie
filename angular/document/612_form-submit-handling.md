# #612 「フォームの送信処理」

## 概要
フォーム送信処理はバリデーション確認、データ整形、サービス呼び出し、結果のフィードバックまでを一連のフローとして設計する。

## 学習目標
- フォーム送信フローのステップを整理する
- サービス層への委譲タイミングを理解する
- 成功・失敗時のUI更新方法を把握する

## 技術ポイント
- ngSubmitでフォーム有効性を確認
- 整形用ユーティリティでDTOを組み立て
- ObservableやPromiseで結果を待ちUIを更新

## 📺 画面表示用コード（動画用）
```typescript
protected async submit(): Promise<void> {
  if (this.form.invalid) {
    return;
  }
  await this.userService.save(this.form.value);
}
```

## 💻 詳細実装例（学習用）
```typescript
protected async submit(): Promise<void> {
  if (this.form.invalid) {
    this.form.markAllAsTouched();
    return;
  }
  this.isSubmitting = true;
  try {
    const payload = this.buildPayload(this.form.value);
    await this.userService.save(payload);
    this.notification.success('保存しました');
  } catch (error) {
    this.notification.error('送信に失敗しました');
  } finally {
    this.isSubmitting = false;
  }
}

private buildPayload(value: Record<string, unknown>) {
  return { ...value, updatedAt: new Date().toISOString() };
}
```

## ベストプラクティス
- 送信前にmarkAllAsTouchedでエラー表示を確実に出す
- DTO組み立てロジックを関数化してテスト可能にする
- サービス呼び出し結果に応じた通知処理を統一する

## 注意点
- 例外処理を忘れるとロード中のままUIが止まる
- フォーム値をそのままAPIに送ると不要データが混ざる
- 同期処理と非同期処理を混在させるとステートが破綻する

## 関連技術
- ngSubmit
- サービス層
- 通知コンポーネント
