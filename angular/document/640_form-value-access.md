# #640 「form.value でデータ取得」

## 概要
NgForm.valueはフォーム内の全コントロール値をオブジェクトで提供し、ngModelGroupの階層も反映されるため送信データの基礎として利用できる。

## 学習目標
- NgForm.valueを取得するタイミングを理解する
- ネスト構造とvalueの関係を把握する
- DTO作成への応用を学ぶ

## 技術ポイント
- form.valueはフォーム登録済みのコントロールのみ含む
- ngModelGroupの構造がvalueに反映
- disabledコントロールはvalueから除外される

## 📺 画面表示用コード（動画用）
```typescript
protected submit(form: NgForm): void {
  console.log(form.value);
}
```

## 💻 詳細実装例（学習用）
```typescript
protected buildPayload(form: NgForm) {
    const { account, profile } = form.value;
    return {
        ...account,
        profile: { ...profile }
    };
}
```

## ベストプラクティス
- 送信直前にvalueをコピーして副作用を防ぐ
- 値の型をインターフェースで表現して可読性を維持
- valueChangesとの組み合わせでリアルタイム処理を実装

## 注意点
- valueを直接変更してもフォームには反映されない
- disabled項目が除外される点に注意
- 巨大なオブジェクトをそのままAPIに渡すと不要データが混ざる

## 関連技術
- NgForm.value
- DTO設計
- ngModelGroup
