# #342 「*ngIf=\"value as alias\" - エイリアス」

## 概要
`*ngIf="expr as alias"`は条件を満たした際に評価結果をテンプレート変数として再利用できる構文で、冗長な式の再計算を避けられる。

## 学習目標
- `as`構文でエイリアスを定義する方法を理解する
- 非同期データを安全に扱うテンプレートパターンを学ぶ
- nullチェックと組み合わせた活用例を把握する

## 技術ポイント
- `*ngIf="user$ | async as user"`で非同期値を受け取る
- テンプレート内で`alias`を参照し、nullチェックを省略
- `else`と組み合わせてフォールバックを提供

## 📺 画面表示用コード（動画用）
```html
<section *ngIf="profile$ | async as profile">
  <h3>{{ profile.name }}</h3>
</section>
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-if-alias-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <article *ngIf="user$ | async as user; else loadingTpl">
      <h2>{{ user.name }}</h2>
      <p>{{ user.description }}</p>
    </article>
    <ng-template #loadingTpl>
      <p>ユーザーを読み込み中...</p>
    </ng-template>
  `
})
export class IfAliasDemoComponent {
  protected user$ = of({ name: 'Alias User', description: 'エイリアス構文の例' }).pipe(delay(400));
}
```

## ベストプラクティス
- `as`構文で得たエイリアスは読み取り専用なので、変更はコンポーネント側で行う
- 非同期データを扱うときは`AsyncPipe`と組み合わせて購読解除を自動化する
- エイリアス名は内容を表す短い単語にする（`user`, `result`など）

## 注意点
- `as`構文は条件が真のときのみエイリアスが存在するため、偽の場合の参照に注意
- エイリアスを再代入しようとするとテンプレートエラーになる
- Observableの結果が`undefined`でも`false`と同じ扱いになるためデフォルト値を検討する

## 関連技術
- AsyncPipe
- RxJS Observable
- Null Safety Patterns
