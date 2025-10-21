# #344 「*ngIf での null チェック」

## 概要
`*ngIf`は`null`チェックと相性が良く、`as`構文で非nullを保証した変数をテンプレート内で安全に扱える。

## 学習目標
- `null`ガードとしての`*ngIf`の利用方法を理解する
- `as`構文で型を絞り込む手法を学ぶ
- nullとundefinedを区別した条件式を設計する

## 技術ポイント
- `*ngIf="value as v"`で`v`は非nullとして扱える
- `strictNullChecks`環境でテンプレート型チェックが有効に働く
- elseテンプレートを用意して未取得状態を扱う

## 📺 画面表示用コード（動画用）
```html
<div *ngIf="user; as u">
  <span>{{ u.name }}</span>
</div>
```

## 💻 詳細実装例（学習用）
```typescript
interface Detail {
  title: string;
  description: string;
}

@Component({
  selector: 'app-null-check-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <section *ngIf="detail(); as d; else placeholder">
      <h2>{{ d.title }}</h2>
      <p>{{ d.description }}</p>
    </section>
    <ng-template #placeholder>
      <p>データがまだありません。</p>
    </ng-template>
  `
})
export class NullCheckDemoComponent {
  private readonly detailSignal = signal<Detail | null>(null);
  protected detail = this.detailSignal.asReadonly();

  protected load(): void {
    this.detailSignal.set({ title: 'Angular Null Check', description: 'nullの安全な扱い方' });
  }
}
```

## ベストプラクティス
- `??`演算子よりも`*ngIf`で明示的に枝分かれさせた方がテンプレートの意図が明確
- 非同期処理の結果が`null`の場合は理由をログに残してデバッグしやすくする
- テンプレート参照名を`detail`など意味あるものにして可読性を高める

## 注意点
- `0`や空文字はnullではないため、別条件で扱う必要がある
- nullチェック漏れによるテンプレートエラーは`strictTemplates`で検出できる
- elseテンプレート側でもユーザーへの案内を充実させ、UXを損なわないようにする

## 関連技術
- strictNullChecks
- Angular Signals
- Template Type Checking
