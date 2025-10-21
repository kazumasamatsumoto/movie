# #696 「Reactive Forms のデータフロー」

## 概要
Reactive FormsではFormControlがソースとなりテンプレートと双方向同期し、valueChangesやstatusChanges経由でデータフローを制御できる。

## 学習目標
- Reactive Formsのデータフロー概念を理解する
- valueChanges/statusChangesの役割を把握する
- Observable連携による反応的設計を学ぶ

## 技術ポイント
- フォーム値はFormControlからテンプレートへ伝播
- テンプレートからの入力はFormControlを更新
- Observableを介して副作用処理を組み込める

## 📺 画面表示用コード（動画用）
```text
FormControl ⇄ [formControl]
valueChanges → サービス → UI
```

## 💻 詳細実装例（学習用）
```typescript
protected searchCtrl = new FormControl('');

protected constructor(private readonly api: SearchService) {
  this.searchCtrl.valueChanges
    .pipe(debounceTime(300), distinctUntilChanged())
    .subscribe(term => this.api.search(term ?? ''));
}
```

## ベストプラクティス
- フォーム値の変化はObservableで処理を連鎖させる
- 副作用はサービスに閉じ込めてコンポーネントを薄く保つ
- UI更新ロジックはAsyncPipeやsignalで簡潔にする

## 注意点
- valueChangesは初期値でも発火する
- 複数の購読が重なるとパフォーマンスを圧迫する
- 副作用をsubscribe内に書きすぎるとテストが困難になる

## 関連技術
- valueChanges
- statusChanges
- RxJS
