# #340 「*ngIf=\"condition; then/else\"」

## 概要
`*ngIf="condition; then tplA; else tplB"`は真偽双方のテンプレートを一度に指定し、条件分岐の見通しを良くする構文である。

## 学習目標
- then/else構文の記法を理解する
- テンプレート参照のネーミングと配置を学ぶ
- 条件分岐を整理する設計パターンを身につける

## 技術ポイント
- `then`テンプレートは条件が真のとき、`else`は偽のときに表示
- テンプレートは`<ng-template #name>`で定義し、同スコープで参照
- `as`構文と組み合わせて値を渡すと表現力が増す

## 📺 画面表示用コード（動画用）
```html
<section *ngIf="ready; then success; else loading"></section>
<ng-template #success><p>完了！</p></ng-template>
<ng-template #loading><p>処理中...</p></ng-template>
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-then-else-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <ng-container *ngIf="state(); then doneTpl; else pendingTpl"></ng-container>
    <ng-template #doneTpl>
      <h2>完了しました</h2>
      <p>{{ detail }}</p>
    </ng-template>
    <ng-template #pendingTpl>
      <p>処理を実行中です。しばらくお待ちください。</p>
    </ng-template>
    <button type="button" (click)="toggle()">状態を切り替える</button>
  `
})
export class ThenElseDemoComponent {
  private readonly status = signal(false);
  protected state = this.status.asReadonly();
  protected detail = '最終更新: just now';

  protected toggle(): void {
    this.status.update(v => !v);
  }
}
```

## ベストプラクティス
- テンプレート参照名は`successTpl`など役割が分かる名前にする
- 同じテンプレートを複数箇所で使う場合は共通コンポーネントにまとめる
- then/else構文で条件ロジックを集約し、ネストを減らす

## 注意点
- then/elseのテンプレートは同じコンポーネントスコープ内で定義する必要がある
- 表示内容が大きい場合はファイルが長くなるため、別コンポーネントへ分割する
- Hydration時に条件が変わらないようサーバーとクライアントの初期値を揃える

## 関連技術
- Angular Signals
- Template Reference Variables
- Component Composition
