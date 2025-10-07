# #034 「[property] プロパティバインディング基礎」

## 概要
プロパティバインディングは、角括弧`[ ]`を使用してDOM要素やコンポーネントのプロパティに値を設定する手法です。補間とは異なり、文字列以外の型（boolean、number、オブジェクトなど）も直接バインドできます。

## 学習目標
- プロパティバインディングの基本構文を理解する
- 補間との違いと使い分けを学ぶ
- 型安全なデータバインディングを実装できるようになる

## 技術ポイント
- `[property]="expression"`構文
- 補間との違い（型の扱い）
- DOM要素プロパティへの直接バインディング
- 一方向データフロー

## 📺 画面表示用コード（動画用）

```typescript
// component.ts
export class ButtonComponent {
  isDisabled = true;
  imageUrl = '/assets/logo.png';
}
```

```html
<!-- プロパティバインディング -->
<button [disabled]="isDisabled">送信</button>
<img [src]="imageUrl" alt="ロゴ">
```

```html
<!-- 補間との比較 -->
<img src="{{imageUrl}}"> <!-- 補間 -->
<img [src]="imageUrl">   <!-- プロパティバインディング -->
```

## 💻 詳細実装例（学習用）

```typescript
// property-binding.component.ts
import { Component } from '@angular/core';

@Component({
  selector: 'app-property-binding',
  standalone: true,
  template: `
    <div class="demo">
      <h2>プロパティバインディングの例</h2>

      <!-- boolean型 -->
      <button [disabled]="isDisabled">ボタン</button>
      <input [readonly]="isReadonly" value="読み取り専用">

      <!-- 文字列型 -->
      <img [src]="imageUrl" [alt]="imageAlt">
      <a [href]="linkUrl">リンク</a>

      <!-- number型 -->
      <input [value]="count" type="number">
      <progress [value]="progress" [max]="100"></progress>

      <!-- オブジェクト型 -->
      <app-user [user]="currentUser"></app-user>

      <!-- 配列型 -->
      <app-list [items]="items"></app-list>

      <!-- 式の評価 -->
      <button [disabled]="count >= maxCount">追加</button>
      <div [hidden]="!isVisible">表示/非表示</div>

      <!-- 制御ボタン -->
      <button (click)="toggleDisabled()">有効/無効切替</button>
      <button (click)="incrementProgress()">進捗+10%</button>
    </div>
  `,
  styles: [`
    .demo {
      padding: 20px;
    }
    button, input {
      margin: 5px;
      padding: 8px 16px;
    }
    progress {
      width: 200px;
      height: 20px;
    }
  `]
})
export class PropertyBindingComponent {
  // boolean型プロパティ
  isDisabled = false;
  isReadonly = true;
  isVisible = true;

  // 文字列型プロパティ
  imageUrl = '/assets/images/logo.png';
  imageAlt = 'アプリケーションロゴ';
  linkUrl = 'https://angular.dev';

  // number型プロパティ
  count = 5;
  maxCount = 10;
  progress = 30;

  // オブジェクト型プロパティ
  currentUser = {
    id: 1,
    name: '田中太郎',
    email: 'tanaka@example.com'
  };

  // 配列型プロパティ
  items = ['項目1', '項目2', '項目3'];

  toggleDisabled() {
    this.isDisabled = !this.isDisabled;
  }

  incrementProgress() {
    this.progress = Math.min(this.progress + 10, 100);
  }
}
```

### 補間 vs プロパティバインディング

```typescript
@Component({
  template: `
    <!-- ✅ 文字列コンテキスト: 両方可能 -->
    <img src="{{imageUrl}}">        <!-- 補間 -->
    <img [src]="imageUrl">          <!-- プロパティバインディング（推奨） -->

    <!-- ✅ boolean値: プロパティバインディングのみ -->
    <button [disabled]="isDisabled">ボタン</button>

    <!-- ❌ 補間では文字列になってしまう -->
    <button disabled="{{isDisabled}}">ボタン</button> <!-- "true"という文字列 -->

    <!-- ✅ オブジェクト: プロパティバインディングのみ -->
    <app-user [user]="userObject"></app-user>

    <!-- ❌ 補間は使えない -->
    <app-user user="{{userObject}}"></app-user> <!-- [object Object] -->
  `
})
export class ComparisonComponent {
  imageUrl = '/assets/logo.png';
  isDisabled = true;
  userObject = { name: 'Taro' };
}
```

## ベストプラクティス
- 文字列以外の型を渡す場合は必ずプロパティバインディングを使う
- 要素のプロパティには`[property]`、HTML属性には`[attr.attribute]`を使い分ける
- boolean型の属性は常にプロパティバインディングを使用する
- 複雑なオブジェクトや配列を子コンポーネントに渡すときに活用する

## 注意点
- プロパティバインディングは一方向（コンポーネント → テンプレート）
- `[property]`はDOMプロパティであり、HTML属性とは異なる
- `disabled="false"`（文字列）と`[disabled]="false"`（boolean）は動作が異なる
- null/undefinedの扱いに注意する

## 関連技術
- 属性バインディング `[attr.name]`
- イベントバインディング `(event)`
- 双方向バインディング `[(ngModel)]`
- Input デコレータ（子コンポーネント）
