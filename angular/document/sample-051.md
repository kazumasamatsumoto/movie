# #051 「[(ngModel)] 双方向バインディング」

## 概要
テンプレートの入力値とコンポーネントのプロパティを同期させる[(ngModel)]双方向バインディングを紹介し、値の往復がワンステップで完了する仕組みを理解します。

## 学習目標
- [(ngModel)]構文の基本的な書き方を理解する
- 双方向バインディングで入力値をコンポーネントに反映させる
- フォーム以外の簡易入力でも[(ngModel)]を活用する

## 技術ポイント
- **[(ngModel)]**: `[ngModel]`と`(ngModelChange)`を統合した構文糖衣
- **双方向同期**: 入力値変更がプロパティへ、プロパティ更新がビューへ反映
- **初期値設定**: プロパティの初期値がテンプレートにも自動反映される

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```html
<input [(ngModel)]="profile.name" placeholder="名前" />
```

```html
<textarea [(ngModel)]="profile.note" rows="3"></textarea>
```

```html
<select [(ngModel)]="profile.role">
  <option value="user">User</option>
  <option value="admin">Admin</option>
</select>
```

## 💻 詳細実装例（学習用）
```typescript
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';

type Role = 'user' | 'admin';

@Component({
  selector: 'app-ngmodel-demo',
  standalone: true,
  imports: [FormsModule],
  templateUrl: './ngmodel-demo.component.html',
})
export class NgModelDemoComponent {
  profile = {
    name: '四国めたん',
    role: 'user' as Role,
    note: 'Angular v20を学習中',
  };

  reset(): void {
    this.profile = {
      name: '',
      role: 'user',
      note: '',
    };
  }
}
```

```html
<section>
  <label>
    名前
    <input [(ngModel)]="profile.name" placeholder="名前を入力" />
  </label>
</section>

<section>
  <label>
    役割
    <select [(ngModel)]="profile.role">
      <option value="user">User</option>
      <option value="admin">Admin</option>
    </select>
  </label>
</section>

<section>
  <label>
    メモ
    <textarea [(ngModel)]="profile.note" rows="3"></textarea>
  </label>
</section>

<pre>{{ profile | json }}</pre>
<button type="button" (click)="reset()">リセット</button>
```

## ベストプラクティス
- 双方向バインディングは少数の入力に限定し、状態が増えたらReactive Formsを検討する
- モデルオブジェクトの型注釈を付けて、プロパティ名のタイポを防ぐ
- 初期値はコンポーネントで定義し、テンプレートではロジックを持たせない

## 注意点
- `ngModel`を利用するにはFormsModuleまたはProvideFormsが必要
- 双方向バインディングでも即座にAPI送信しないよう、送信トリガーを別途用意する
- ネストオブジェクトに直接バインドするとリファレンスが変わる点に注意する

## 関連技術
- Angular Template-driven Forms
- Reactive Formsと双方向バインディングの比較
- Angular Signalsとの連携パターン
