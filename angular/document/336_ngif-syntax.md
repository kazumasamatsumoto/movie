# #336 「*ngIf の基本構文」

## 概要
`*ngIf="condition"`は条件が真の時にテンプレートを描画し、偽の時はビューを生成しない基本構文である。

## 学習目標
- `*ngIf`の書式と評価タイミングを理解する
- 可読性の高い条件式の書き方を学ぶ
- 複雑な式を避ける設計指針を得る

## 技術ポイント
- Angularはtruthy/falsy評価で条件判定
- コンポーネントのプロパティやメソッドを式内で参照可能
- 余分な再評価を避けるため、条件式は軽量に保つ

## 📺 画面表示用コード（動画用）
```html
<section *ngIf="userLoaded">ユーザーが読み込まれました。</section>
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-ngif-syntax-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <button (click)="fetch()">ユーザー読み込み</button>
    <p *ngIf="isLoading">読み込み中...</p>
    <article *ngIf="user">
      <h3>{{ user.name }}</h3>
      <p>{{ user.email }}</p>
    </article>
  `
})
export class NgIfSyntaxDemoComponent {
  protected isLoading = false;
  protected user: { name: string; email: string } | null = null;

  protected fetch(): void {
    this.isLoading = true;
    setTimeout(() => {
      this.user = { name: 'Angular User', email: 'user@example.com' };
      this.isLoading = false;
    }, 800);
  }
}
```

## ベストプラクティス
- メソッド呼び出しを条件式に書くと毎回実行されるため避ける
- 変数名は状態を表す命名にし、テンプレートの意図が伝わるようにする
- 複雑な条件はgetterやSignalで事前に計算する

## 注意点
- `*ngIf`と`[hidden]`の違いを理解し、DOM破棄が必要なケースでのみ利用する
- 条件式で非同期処理を直接行わない
- strictTemplatesでは型安全が保証されるが、any型を使うとエラーが検出されにくい

## 関連技術
- Angular Signals
- Change Detection
- TypeScript strictTemplates
