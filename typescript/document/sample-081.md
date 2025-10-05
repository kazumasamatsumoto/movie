# #081 「Angularコンポーネントのstring型」

## 概要
TypeScript v5.9のAngularコンポーネントstring型について学習します。コンポーネントのプロパティでstring型を使用する方法を理解します。

## 学習目標
- Angularコンポーネントでのstring型使用を理解する
- プロパティの定義方法を理解する
- テンプレートでの活用方法を理解する

## 画面表示用コード

```typescript
// Angularコンポーネントのstring型
import { Component } from '@angular/core';

@Component({
  selector: 'app-user',
  template: `
    <h1>{{title}}</h1>
    <p>{{message}}</p>
    <span>{{userName}}</span>
  `
})
export class UserComponent {
  title: string = "ユーザー管理";
  message: string = "ユーザー情報を表示中";
  userName: string = "Alice";
}
```

## 重要なポイント
1. **プロパティ定義**: コンポーネントクラスでstring型プロパティを定義
2. **テンプレートバインディング**: {{}}でプロパティを表示
3. **実用性**: タイトル、メッセージ、データの表示に活用

## 次のステップ
次回は、テンプレートバインディングについて学習します。