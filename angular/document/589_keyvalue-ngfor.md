# #589 「*ngFor=\"let item of object | keyvalue\"」

## 概要
KeyValuePipeを`*ngFor`と組み合わせることで、オブジェクトのプロパティを反復しキーと値を表示できる。テンプレートで動的な内容を扱う際に役立つ。

## 学習目標
- `*ngFor`でKeyValuePipeを使う構文を理解する
- `entry.key`/`entry.value`の扱い方を学ぶ
- ソート順やテンプレート表示のパターンを把握する

## 技術ポイント
- `<div *ngFor="let entry of object | keyvalue">`
- `entry.key`, `entry.value`でアクセス
- compareFnで並び順を制御可能

## 📺 画面表示用コード（動画用）
```html
<dl>
  <ng-container *ngFor="let entry of user | keyvalue">
    <dt>{{ entry.key }}</dt>
    <dd>{{ entry.value }}</dd>
  </ng-container>
</dl>
```

## 💻 詳細実装例（学習用）
```html
<ul>
  <li *ngFor="let entry of config | keyvalue">{{ entry.key }}: {{ entry.value }}</li>
</ul>
```

## ベストプラクティス
- 設定やステータス表示など動的なキーを扱う際に利用
- compareFnを渡して表示順序を制御
- 入力オブジェクトがnullの場合のガードを実装

## 注意点
- オブジェクトのプロパティ順は保証されないため必要に応じてcompareFn
- ループ中に編集や削除を行う場合は動的更新に注意
- 大きなオブジェクトを表示すると可読性が下がる

## 関連技術
- keyvalue compareFn
- JSON表示/デバッグ
- テンプレートループ構文
