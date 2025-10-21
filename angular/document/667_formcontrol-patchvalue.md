# #667 「FormControl.patchValue() メソッド」

## 概要
FormControlでもpatchValueが利用でき、setValueと同様に値と状態を更新する。将来的にFormGroupへ拡張する場合にAPI整合性を保てる。

## 学習目標
- patchValueの挙動を理解する
- setValueとの違いと共通点を押さえる
- FormGroup移行を見据えた設計を考える

## 技術ポイント
- FormControlではsetValueと挙動は同じ
- emitEvent/onlySelfなどのオプションが利用可能
- FormGroupでは存在しないキーを無視して部分更新できる

## 📺 画面表示用コード（動画用）
```html
<input [formControl]="memoCtrl" />
```

## 💻 詳細実装例（学習用）
```typescript
protected memoCtrl = new FormControl('作業メモ');

                protected appendFooter(): void {
                  this.memoCtrl.patchValue('作業メモ
-- updated', { emitEvent: false });
                }
```

## ベストプラクティス
- FormGroupへ拡張可能な設計ならpatchValueを使う
- オプションのデフォルト値を共有化する
- 更新メソッドはサービスにまとめ再利用性を高める

## 注意点
- FormControl単体ではsetValueと違いが無い
- patchValueで存在しないキーを渡してもエラーにならないため検知しにくい
- emitEvent:falseを多用すると状態同期が難しくなる

## 関連技術
- patchValue
- API整合性
- メソッド設計
