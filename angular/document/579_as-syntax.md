# #579 「as 構文での値取得」

## 概要
`*ngIf="observable$ | async as value"`の`as`構文を使えば、AsyncPipeの結果をテンプレート変数として保持し、同じテンプレート内で複数回利用できる。

## 学習目標
- `as`構文の用途と利点を理解する
- AsyncPipeの重複購読を避けるパターンを学ぶ
- テンプレート変数を使って値を再利用する方法を把握する

## 技術ポイント
- `*ngIf="observable$ | async as data"`
- `data`変数をテンプレート内で参照
- elseブロックでローディング表示も可能

## 📺 画面表示用コード（動画用）
```html
<ng-container *ngIf="profile$ | async as profile; else loading">
  <h2>{{ profile.name }}</h2>
  <p>{{ profile.email }}</p>
</ng-container>
<ng-template #loading>読み込み中...</ng-template>
```

## 💻 詳細実装例（学習用）
```html
<section *ngIf="weather$ | async as weather">
  <h3>{{ weather.city }}</h3>
  <p>{{ weather.temperature }} ℃</p>
</section>
```

## ベストプラクティス
- `as`構文で変数化し、AsyncPipeの複数回使用を避けパフォーマンス向上
- elseテンプレートでローディングやエラー表示を整備
- 変数名は役割が分かる名称にする

## 注意点
- `as`構文は`*ngIf`や`*ngSwitchCase`など構造ディレクティブでのみ使用可
- 変数スコープはテンプレート内に限定される
- Observableがnullの場合は変数が割り当てられないので代替処理を用意

## 関連技術
- AsyncPipe
- *ngIf/else
- テンプレート変数
