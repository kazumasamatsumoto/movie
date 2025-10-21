# #663 「FormControl の初期値設定」

## 概要
FormControlの初期値はコンストラクタで与え、必要に応じてsetValueやresetで再設定する。参照型はコピーして渡すと安全。

## 学習目標
- 初期値設定のパターンを学ぶ
- setValueとresetの違いを理解する
- 参照型初期値の扱いを把握する

## 技術ポイント
- constructorで初期値を定義
- reset(initialValue)で初期状態へ戻せる
- オブジェクトはディープコピーして渡すのが安全

## 📺 画面表示用コード（動画用）
```html
<input [formControl]="profileCtrl" placeholder="ユーザー名" />
```

## 💻 詳細実装例（学習用）
```typescript
protected readonly defaultProfile = { name: 'ゲスト' } as const;
protected profileCtrl = new FormControl({ ...this.defaultProfile });

protected resetProfile(): void {
  this.profileCtrl.reset({ ...this.defaultProfile });
}
```

## ベストプラクティス
- 初期値は定数化して一箇所で管理する
- リセット時はreset(initial)で状態も含めて戻す
- 参照型はスプレッドやstructuredCloneでコピーする

## 注意点
- reset()だけだとnullになる可能性がある
- 非同期取得後に初期値を設定する場合は遅延初期化を考慮
- setValueは同期的に実行されるため例外処理を備える

## 関連技術
- FormControl
- reset
- 初期値管理
