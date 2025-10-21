# #727 「updateValueAndValidity() メソッド」

## 概要
updateValueAndValidityは値やバリデーション設定の変更後に状態を再評価し、emitEventやonlySelfオプションで通知方法を制御できる。

## 学習目標
- updateValueAndValidityの役割を理解する
- オプション引数の使い方を学ぶ
- バリデーション切り替え時の使用タイミングを把握する

## 技術ポイント
- 再評価してvalid/invalidやerrorsを更新
- emitEvent:falseでvalueChangesを抑制
- onlySelf:trueで親グループへの伝播を止める

## 📺 画面表示用コード（動画用）
```typescript
this.ageCtrl.setValidators([Validators.min(18)]);
this.ageCtrl.updateValueAndValidity({ emitEvent: false });
```

## 💻 詳細実装例（学習用）
```typescript
protected ageCtrl = new FormControl(0);
```

## ベストプラクティス
- バリデーション変更後は必ず呼ぶルールを設ける
- emitEventオプションで不要な処理を抑制する
- onlySelfは親グループとの整合性に注意しながら使う

## 注意点
- 多用するとパフォーマンスに影響するため必要なときだけ呼ぶ
- emitEvent:falseにするとUIが更新されない場合がある
- 非同期バリデーション実行中に呼び出すタイミングに注意

## 関連技術
- updateValueAndValidity
- emitEvent
- onlySelf
