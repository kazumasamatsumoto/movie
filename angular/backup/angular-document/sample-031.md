# #031 「{{ }} 補間バインディング - データ表示」

## 概要
補間バインディング（Interpolation）は、コンポーネントのプロパティ値をテンプレート内に表示するための最も基本的なデータバインディング手法です。二重中括弧`{{ }}`を使用してコンポーネントのデータをHTMLに埋め込みます。

## 学習目標
- 補間バインディングの基本構文を理解する
- コンポーネントプロパティをテンプレートに表示できるようになる
- リアクティブなデータ更新の仕組みを理解する

## 技術ポイント
- `{{ }}`構文によるプロパティの埋め込み
- 自動的なデータの変更検知と表示更新
- 文字列コンテキストでの利用

## 📺 画面表示用コード（動画用）

```typescript
// component.ts
export class UserComponent {
  userName = '田中太郎';
  age = 25;
}
```

```html
<!-- template.html -->
<h1>{{userName}}</h1>
<p>年齢: {{age}}</p>
```

## 💻 詳細実装例（学習用）

```typescript
// user-profile.component.ts
import { Component } from '@angular/core';

@Component({
  selector: 'app-user-profile',
  standalone: true,
  template: `
    <div class="profile">
      <h1>ユーザー名: {{userName}}</h1>
      <p>メール: {{email}}</p>
      <p>年齢: {{age}}歳</p>
      <p>役職: {{position}}</p>
      <button (click)="updateAge()">年齢を更新</button>
    </div>
  `,
  styles: [`
    .profile {
      padding: 20px;
      border: 1px solid #ddd;
      border-radius: 8px;
    }
  `]
})
export class UserProfileComponent {
  userName = '田中太郎';
  email = 'tanaka@example.com';
  age = 25;
  position = 'エンジニア';

  updateAge() {
    this.age++; // 補間バインディングが自動で更新される
  }
}
```

## ベストプラクティス
- プロパティ名は分かりやすく命名する
- 補間内での複雑な式は避け、コンポーネント側で処理する
- プリミティブ型やシンプルなオブジェクトプロパティの表示に使用する

## 注意点
- `{{ }}`内では基本的な式の評価が可能だが、複雑なロジックは避ける
- null/undefinedの場合は空文字として表示される
- HTMLタグはエスケープされる（XSS対策）

## 関連技術
- プロパティバインディング `[property]`
- 式の評価 `{{ expression }}`
- 変更検知メカニズム
