# #668 「FormControl.reset() メソッド」

## 概要
FormControl.resetは値と状態を初期状態に戻し、引数に初期値を渡すとその値で再初期化できる。状態フラグもリセットされるためUXを考慮する。

## 学習目標
- resetの基本動作を理解する
- 初期値を指定したリセット方法を学ぶ
- 状態フラグの変化を把握する

## 技術ポイント
- reset()は値をnull/undefinedに戻す
- reset(initialValue)で新しい初期値を設定できる
- pristine・touched・dirtyなどが初期状態へ戻る

## 📺 画面表示用コード（動画用）
```html
<input [formControl]="commentCtrl" />
<button type="button" (click)="clearComment()">クリア</button>
```

## 💻 詳細実装例（学習用）
```typescript
protected commentCtrl = new FormControl('');

protected clearComment(): void {
  this.commentCtrl.reset('');
}
```

## ベストプラクティス
- リセット後のフォーカス位置を考慮する
- 初期値は定数化して複数箇所で共有する
- 状態リセットでエラー表示が消える点をUIで補足する

## 注意点
- resetを乱用するとユーザー入力が失われる
- disabled状態は維持されるため必要ならenableする
- リセット後のvalueChanges発火を想定して制御する

## 関連技術
- reset
- 状態管理
- UX配慮
